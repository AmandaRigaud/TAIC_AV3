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
    prompt="Era uma vez uma coruja muito inteligente e sábia, mas ela se sentia triste por não ter amigos para brincar e conversar. Certo dia, ela decidiu sair voando pela floresta em busca de companhia. No caminho, encontrou um coelho fofinho que estava perdido e com medo. A coruja prontamente se ofereceu para ajudá-lo a encontrar o caminho de volta para casa. Juntos, eles se tornaram grandes amigos, aprendendo que a amizade pode surgir quando menos esperamos, bastando estarmos dispostos a ajudar e ser gentis com o próximo.",
    size="1024x1024",
    quality="standard",
    n=1,
    )

    return response.data[0].url

def Audio(texto_entrada):
    response = client.audio.speech.create(
    model="tts-1",
    voice="echo",
    input="Era uma vez uma coruja muito inteligente e sábia, mas ela se sentia triste por não ter amigos para brincar e conversar. Certo dia, ela decidiu sair voando pela floresta em busca de companhia. No caminho, encontrou um coelho fofinho que estava perdido e com medo. A coruja prontamente se ofereceu para ajudá-lo a encontrar o caminho de volta para casa. Juntos, eles se tornaram grandes amigos, aprendendo que a amizade pode surgir quando menos esperamos, bastando estarmos dispostos a ajudar e ser gentis com o próximo.",
    )

    response.stream_to_file("output.mp3")