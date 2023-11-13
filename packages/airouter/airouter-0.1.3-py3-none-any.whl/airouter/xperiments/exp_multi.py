import airouter

if __name__ == '__main__':
  # outputs = airouter.StreamedCompletion.create(
  #   models=['gpt-3.5-turbo-1106', 'gpt-3.5-turbo-1106'],
  #   temperature=0.0,
  #   max_tokens=100,
  #   messages=[{'role': 'user', 'content': 'write a story about the big Large Language Models convention'}],
  #   return_instance=True
  # )


  outputs = airouter.StreamedCompletion.create_parallel(
    lst_kwargs=[
      dict(
        model='gpt-3.5-turbo-1106',
        temperature=0.0,
        max_tokens=100,
        messages=[{'role': 'user', 'content': 'write a story about the big Large Language Models convention'}],
        return_instance=True
      ),
      dict(
        model='text-bison-32k',
        temperature=0.0,
        max_tokens=100,
        messages=[{'role': 'user', 'content': 'Hi there'}],
        return_instance=True
      ),
    ]
  )

  s1 = outputs[0][0]
  s2 = outputs[1][0]
  print(len(s1.provider.timings['next_events_times']))
  print(len(s2.provider.timings['next_events_times']))