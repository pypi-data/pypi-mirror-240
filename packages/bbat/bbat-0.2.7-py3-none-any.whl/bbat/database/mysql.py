import pymysql
import aiomysql


class Mysql:
    def __init__(
        self,
        host=None,
        port=None,
        database=None,
        user=None,
        password=None,
        connect_timeout=20,
        read_timeout=20,
        write_timeout=20,
    ):
        self.conn = pymysql.connect(
            host=host,
            port=int(port),
            database=database,
            user=user,
            passwd=str(password),
            connect_timeout=connect_timeout,
            read_timeout=read_timeout,
            write_timeout=write_timeout,
            cursorclass=pymysql.cursors.DictCursor,
        )

    def count(self, table, where=""):
        cur = self.conn.cursor()
        sql = f"select count(1) cnt from {table}"
        if where:
            sql += f" WHERE {where}"
        cur.execute(sql)
        data = cur.fetchone()
        return data["cnt"]

    def execute(self, sql):
        cur = self.conn.cursor()
        cur.execute(sql)
        self.conn.commit()

    def query(self, sql):
        cur = self.conn.cursor()

        cur.execute(sql)
        data = cur.fetchall()
        return list(data)

    def fetch(self, sql, *args, **kwargs):
        cur = self.conn.cursor()
        cur.execute(sql, *args, **kwargs)
        data = cur.fetchone()
        return data

    def update(self, table=None, data=None, where=None):
        cur = self.conn.cursor()
        set_list = [f'`{k}`="{v}"' for k, v in data.items()]
        sql = f"update {table} set {','.join(set_list)}"
        if where:
            sql += f"where {where}"
        cur.execute(sql)
        self.conn.commit()

    def insert(self, table=None, data_list: list = []):
        cur = self.conn.cursor()
        for data in data_list:
            field = ",".join([f"`{key}`" for key in data.keys()])
            value = ",".join([f'"{val}"' for val in data.values()])
            sql = f"insert into {table}({field}) values({value})"
            cur.execute(sql)
        self.conn.commit()

    def quit(self):
        self.conn.close()


class AsyncMysql:
    """A lightweight wrapper around aiomysql.Pool for easy to use
    """
    def __init__(self, host, port, database, user, password,
                 loop=None, sanic=None,
                 minsize=3, maxsize=5,
                 return_dict=True,
                 pool_recycle=7*3600,
                 autocommit=True,
                 charset = "utf8mb4", **kwargs):
        '''
        kwargs: all args that aiomysql.connect() accept.
        '''
        self.db_args = {
            'host': host,
            'port': port,
            'db': database,
            'user': user,
            'password': password,
            'minsize': minsize,
            'maxsize': maxsize,
            'charset': charset,
            'loop': loop,
            'autocommit': autocommit,
            'pool_recycle': pool_recycle,
        }
        self.sanic = sanic
        if sanic:
            sanic.db = self
        if return_dict:
            self.db_args['cursorclass']=aiomysql.cursors.DictCursor
        if kwargs:
            self.db_args.update(kwargs)
        self.pool = None

    async def init_pool(self):
        if self.sanic:
            self.db_args['loop'] = self.sanic.loop
        self.pool = await aiomysql.create_pool(**self.db_args)

    async def query(self, query, parse=False, *args, **kwargs):
        """Returns a row list for the given query and args."""
        if not self.pool:
            await self.init_pool()
        async with self.pool.acquire() as conn:
            async with conn.cursor() as cur:
                try:
                    if parse:
                        await cur.execute(query, kwargs or args)
                    else:
                        await cur.execute(query)
                    ret = await cur.fetchall()
                except pymysql.err.InternalError:
                    await conn.ping()
                    await cur.execute(query)
                    ret = await cur.fetchall()
                return ret

    async def fetch(self, query, *args, **kwargs):
        """Returns the (singular) row returned by the given query.
        """
        if not self.pool:
            await self.init_pool()
        async with self.pool.acquire() as conn:
            async with conn.cursor() as cur:
                try:
                    await cur.execute(query)
                    ret = await cur.fetchone()
                except pymysql.err.InternalError:
                    await conn.ping()
                    await cur.execute(query)
                    ret = await cur.fetchone()
                return ret

    async def execute(self, query, *args, **kwargs):
        """Executes the given query, returning the lastrowid from the query."""
        if not self.pool:
            await self.init_pool()
        async with self.pool.acquire() as conn:
            async with conn.cursor() as cur:
                try:
                    await cur.execute(query)
                except Exception:
                    # https://github.com/aio-libs/aiomysql/issues/340
                    await conn.ping()
                    await cur.execute(query)
                return cur.lastrowid
            
    async def insert(self, table, data):
        keys = []
        values = []
        for k, v in data.items():
            if v is None: continue
            keys.append(f'`{k}`')
            if isinstance(v, str):
                v = v.replace("'", "\'")
            values.append(f"'{v}'")
            
        keys = ','.join(keys)
        values = ','.join(values)
        sql = f'INSERT INTO {table} ({keys}) VALUES ({values})'
        res = await self.execute(sql)
        return res

    async def update(self, table, data, where=None):
        set_list = [f'`{k}`="{v}"' for k, v in data.items()]
        sql = f"update {table} set {','.join(set_list)}"
        if where:
            sql += f"where {where}"
        return await self.execute(sql)


    # high level interface
    # 创建表
    async def create_table(self, table):
        sql = f'''CREATE TABLE `{table}`( 
            `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
            `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
            PRIMARY KEY (`id`)
        ) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4'''
        print(">>>", sql)
        res = await self.execute(sql)
        return res
    # 所有表
    async def tables(self, database):
        sql = f"SELECT table_name FROM information_schema.tables WHERE table_schema='{database}'"
        print(">>>", sql)
        tables = await self.query(sql)
        table_list = list(map(lambda x: x['table_name'], tables))
        return table_list
    
    # 表结构
    async def table_fields(self, name):
        sql = f"SELECT column_name name,data_type type,column_comment comment,column_default value FROM information_schema.columns WHERE table_name='{name}'"
        print(">>>", sql)
        table_info = await self.query(sql)
        return table_info

    # 添加字段
    async def add_field(self, table, field, type):
        sql = f"ALTER TABLE {table} ADD {field} {type}"
        print(">>>", sql)
        res = await self.execute(sql)
        return res
    
    async def drop_field(self, table, field):
        sql = f"ALTER TABLE {table} DROP {field}"
        print(">>>", sql)
        res = await self.execute(sql)
        return res