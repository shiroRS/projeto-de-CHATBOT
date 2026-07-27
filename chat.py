from dotenv import load_dotenv
from google import genai

load_dotenv()

print("chat bot iniciado...(digite 'sair' para encerrar o chat)")

while True:

    pergunta = input("Digite sua pergunta: ")


    if pergunta.lower()=="sair":

        print("Encerrando o chat...")
        break


    try:
        cliente=genai.Client()

        resposta=cliente.models.generate_content(
            model="gemini-3.5-flash-lite",
            contents=[pergunta]   
        )

        print(resposta.text)
    except Exception as e:
        print(f"Ocorreu um erro: {e}")