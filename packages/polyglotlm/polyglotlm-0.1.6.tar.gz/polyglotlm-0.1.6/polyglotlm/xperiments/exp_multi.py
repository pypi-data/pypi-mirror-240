
from polyglotlm.streamed_completion import StreamedCompletionInterface

if __name__ == '__main__':

  models = ['gpt-3.5-turbo-1106', 'text-bison-32k', 'anthropic.claude-instant-v1']

  params = {
    'temperature': 0.0,
    'max_tokens': 10,
    'messages': [{'role': 'user', 'content': 'what is Ebitda?'}],
  }

  outputs = StreamedCompletionInterface.create_multi_models(models, **params)
