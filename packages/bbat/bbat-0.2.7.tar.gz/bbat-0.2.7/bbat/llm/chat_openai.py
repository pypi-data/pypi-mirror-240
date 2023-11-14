import openai

class ChatOpenaiAPI:
    '''openai version is openai==0.27.8'''

    def __init__(self, model_name=None, api_url="https://api.openai.com/v1", api_key="", proxy=None, history=[]):
        self.model_name = "gpt-3.5-turbo"
        if model_name:
            self.model_name = model_name

        self.api_url = api_url
        self.api_key = api_key
        self.proxy = proxy
        self.tokenizer = None
        self.history = history

    def generate(self, messages, system_prompt=None, stream=True, **kwargs):
        # 避免传入的messages内容过大，保持最新的5条数据
        params = dict(
            model=self.model_name,
            temperature=0.3,
            top_p=0.9,
            max_tokens=4096,
            frequency_penalty=1,
            presence_penalty=1,
            timeout=1,
        )
        params.update(kwargs)

        completion = openai.ChatCompletion.create(messages=messages, stream=stream, **params)
        # content = {'role': '', 'content': ''}
        for event in completion:
            if event["choices"][0]["finish_reason"] == "stop":
                StopAsyncIteration
            for delta_v in event["choices"][0]["delta"].get("content", ""):
                yield delta_v

    def chat(self, query, system_prompt=None, history=[], **kwargs):
        history = self.get_history()
        openai.api_key = self.api_key
        openai.api_base = self.api_url
        openai.proxy = {
            "http": self.proxy,
            "https": self.proxy,
        }

        kwargs["model"] = self.model_name
        messages = history + [{"role": "user", "content": query}]
        return self.generate(messages, system_prompt, stream=True, **kwargs)

    def get_history(self):
        history = self.history
        type_map = {
            1: "user",
            0: "assistant",
        }
        history = [{"role": type_map[h.get("status", 0)], "content": h.get("content", "")} for h in history]

        return history


if __name__ == "__main__":
    # model = ChatLLM(api_key="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", proxy="http://127.0.0.1:15777")
    # llama2 chinese: http://192.168.110.192:30000/v1
    # baichuan2_vllm:  http://192.168.110.180:31113/v1
    # qwen 14b: http://192.168.110.180:31114/v1
    llm = ChatOpenaiAPI(api_url="http://192.168.110.180:31113/v1", api_key="empty")
    response = llm.chat("解释CNN")
    for item in response:
        print(item, end='')
