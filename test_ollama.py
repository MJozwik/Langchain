from openai import OpenAI

client = OpenAI(
    base_url = 'http://localhost:11434/v1',
    api_key='ollama', # required, but unused
)

if (client):
    print("OK")

question = input("Please provide a name for a superhero: ")
    
response = client.chat.completions.create(
  model="llama3.2:3b",
  messages=[
    {"role": "system", "content": "Please provide name of author of that fictional hero, also the date of first release of a story in which that hero appeared"},
    {"role": "user", "content": question},
  ]
)
print(response.choices[0].message.content)

#curl http://localhost:11434/v1/chat/completions \
#    -H "Content-Type: application/json" \
#    -d '{
#        "model": "llama3.2:3b",
#        "messages": [
#            {
#                "role": "system",
#                "content": "You are a helpful assistant."
#            },
#            {
#                "role": "user",
#                "content": "Hello!"
#            }
#        ]
#    }'


#{"id":"chatcmpl-951","object":"chat.completion","created":1737664553,"model":"llama3.2:3b","system_fingerprint":"fp_ollama","choices":[{"index":0,"message":{"role":"assistant","content":"How can I help you today? Do you have a question, need information on a particular topic, or just want to chat? I'm here to assist you."},"finish_reason":"stop"}],"usage":{"prompt_tokens":33,"completion_tokens":34,"total_tokens":67}}