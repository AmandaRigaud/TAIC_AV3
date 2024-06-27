from os import environ
from openai import OpenAI
from dotenv import load_dotenv

# Carregando as variáveis de ambiente do arquivo .env
load_dotenv()

# Define API key
client = OpenAI(
  api_key=environ["API_KEY"],
)

def Chat(texto_usuario):
    completion = client.chat.completions.create(
      model="gpt-3.5-turbo",
      messages=[
        {"role": "system", "content": "Você é um contador de histórias infantis. Suas histórias não podem possuir linguagem impropria para crianças. A história deve ser contada em, no máximo, seis paragrafos. Cada história deve possuir uma finalização amistosa e algum aprendizado para as crianças"},
        {"role": "user", "content": texto_usuario}
      ]
    )

    return completion.choices[0].message.content

def Image(texto_entrada):
    response = client.images.generate(
    model="dall-e-3",
    prompt=texto_entrada,
    size="1024x1024",
    quality="standard",
    n=1,
    )

    return response.data[0].url

def Audio(texto_entrada, file_name):
    response = client.audio.speech.create(
    model="tts-1",
    voice="echo",
    input=texto_entrada,
    )

    response.stream_to_file(file_name)