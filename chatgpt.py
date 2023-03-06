import openai

#define openai key
openai.api_key = "//YOUR TOKEN//"

#set up the model and prompt
model_engine = "text-davinci-003"
prompt = input('Enter new prompt: ')

#Generate a response
completion = openai.Completion.create(
    engine=model_engine,
    prompt=prompt,
    max_tokens=1024,
    n=1,
    stop=None
)

response = completion.choices[0].text
print(response)