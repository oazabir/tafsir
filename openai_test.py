import os
import time
import openai
import openai_config

openai.api_key = openai_config.openai_api_key
#prompt = input('> ');
prompt = """generate a yaml formatted content.
For each surah in Juz 30 of the Quran
 - first level output name of the surah
 - second level generate a collection of theme names based on thematic breakdown of the  surah.
 - third level, generate a summary, verse range, list of tags based on topics found in the verses belonging to the theme
 """


# record the time before the request is sent
start_time = time.time()

response = openai.ChatCompletion.create(
  model="gpt-4",
  messages=[
    {"role": "user", "content": prompt}
  ],
  stream=True
)

# create variables to collect the stream of chunks
collected_chunks = []
collected_messages = []
# iterate through the stream of events
for chunk in response:
    chunk_time = time.time() - start_time  # calculate the time delay of the chunk
    collected_chunks.append(chunk)  # save the event response
    finish_reason = chunk['choices'][0]['finish_reason']
    if finish_reason != "stop":
        delta = chunk['choices'][0]['delta']
        if "content" in delta:
            chunk_message = delta['content']  # extract the message
            collected_messages.append(chunk_message)  # save the message
            print(chunk_message, end='')

# print the time delay and text received
print(f"Full response received {chunk_time:.2f} seconds after request")
full_reply_content = ''.join([m.get('content', '') for m in collected_messages])
print(f"Full conversation received: {full_reply_content}")

with open("openai_output.txt","w") as f:
    f.write(full_reply_content)
print('Finished.')
