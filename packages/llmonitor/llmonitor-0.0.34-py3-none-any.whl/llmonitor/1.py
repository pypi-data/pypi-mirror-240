from openai import OpenAI
import os, sys

sys.path.append(os.path.dirname(os.path.realpath(__file__)))

from . import monitor

client = OpenAI()

monitor(client)

stream = client.chat.completions.create(
    model="gpt-4",
    messages=[{"role": "user", "content": "Say this is a test"}],
    # functions=[
    #     {
    #         "name": "get_answer_for_user_query",
    #         "description": "Get user answer in series of steps",
    #         "parameters": {
    #             "title": "StepByStepAIResponse",
    #             "type": "object",
    #             "properties": {
    #                 "title": {"title": "Title", "type": "string"},
    #                 "steps": {
    #                     "title": "Steps",
    #                     "type": "array",
    #                     "items": {"type": "string"},
    #                 },
    #             },
    #             "required": ["title", "steps"],
    #         },
    #     }
    # ],
    # function_call={"name": "get_answer_for_user_query"},
    stream=True,
)


for a in stream:
    pass
