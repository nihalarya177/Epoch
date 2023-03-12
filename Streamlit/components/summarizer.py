import openai

openai.api_key = "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"
model_engine = "text-davinci-003"


def get_openai_response(query: str):
    response = openai.Completion.create(
        engine=model_engine,
        prompt=query,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    return response
