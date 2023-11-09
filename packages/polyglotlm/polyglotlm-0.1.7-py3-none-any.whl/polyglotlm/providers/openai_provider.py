import os
import time
import openai
from decouple import config
from polyglotlm.providers.base_provider import BaseProvider, GenerationOutput
os.environ['OPENAI_API_KEY'] = config("OPENAI_API_KEY")

class OpenAIProvider(BaseProvider):

  def get_response(self):
    client = openai.OpenAI()
    if isinstance(self.last_exception, openai.RateLimitError):
      sleep_before = 20.0
      print(f"Sleeping {sleep_before}s before making the LLM call")
      time.sleep(sleep_before)
    response = client.chat.completions.create(**self.cleaned_parameters)
    return response

  def get_generation_output(self, event) -> GenerationOutput:
    choice = event.choices[0]
    crt_content = choice.delta.content
    crt_function_call = choice.delta.function_call

    kwargs = {
      'finish_reason': choice.finish_reason,
      'content': crt_content,
      'function_call': crt_function_call,
    }

    return GenerationOutput(**kwargs)

  def get_timeout_params(self):
    return {
      'start': 5.0,
      'maximum': 20.0,
      'increment': 5.0,
    }
