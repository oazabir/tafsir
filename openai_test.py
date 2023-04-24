import os
import time
import openai
import openai_config

openai.api_key = openai_config.openai_api_key
#prompt = input('> ');
with open("prompt.txt", "r") as f:
  prompt = f.read();


# record the time before the request is sent
start_time = time.time()

response = openai.ChatCompletion.create(
  model="gpt-4",
  messages=[
    {"role": "user", "content": prompt}
  ],
  temperature=0.2, # more than this results in incorrect verse selection
  #top_p=0.2,  # try higher number to see if it selects verses incorrectly
  stream=True
)

# create variables to collect the stream of chunks
collected_chunks = []
collected_messages = []
# iterate through the stream of events
with open("openai_output.txt","w") as f:

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
                f.write(chunk_message)
                f.flush()

# print the time delay and text received
print(f"\n\n==========\nFull response received {chunk_time:.2f} seconds after request")
