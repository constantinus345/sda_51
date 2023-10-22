#pip install openai
from super_secret import cod_openai
import os
import openai

def text_imbracaminte(temperatura):
    openai.api_key = cod_openai

    response = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=[
            {"role": "system", "content": "Da instructiuni de imbracaminte"},
            {"role": "user", "content": f"Afara sunt {temperatura} grade Celsius, cum trebuie sa ma imbrac?"},
        ]
    )

    rezultat = response["choices"][0]["message"]["content"]

    return rezultat


# response = openai.Completion.create(
#   model="babbage-002",
#   prompt="Afara sunt 30 grade Celsius. Cum trebuie sa ma imbrac?"
# )

# print(response["choices"][0]["text"])
# print(type(response))