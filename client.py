from openai import OpenAI
client = OpenAI(

    api_key="sk-ijklmnopqrstuvwxijklmnopqrstuvwxijklmnop", #Api keys was deleted so that not working
)

response = client.responses.create(
    model="gpt-4.1",
    messages=[ 
            {"role": "system", "content": "You are a persone name MEET GOTI who speake hindi as well as english . he is indian and my friend  "}, 
{"role": "user", "content": "text"}
    ]
)

print(response.output_text)

 