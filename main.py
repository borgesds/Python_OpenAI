from openai import OpenAI
from dotenv import load_dotenv
import os


load_dotenv()
cliente = OpenAI(api_key=os.getenv("OPEN_API_KEY"))

resposta = cliente.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": "Listar apenas os nomes dos produtos, sem considerar descrição."
        },
        {
            "role": "user",
            "content": "Liste 3 produtos sustentáveis"
        }
    ],
    model="gpt-3.5-turbo"
)

print(resposta.choices[0].message.content)
