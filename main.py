import requests

# 1. Cole aqui o Token que você copiou do BotFather (aquela barra cinza)
TOKEN = "8588052322:AAEraKnzeDWUvgGKSzYgX3SwEpYsf1Kteqo" 

# 2. Cole aqui o número que o @userinfobot te deu (apenas os números)
CHAT_ID = 7974959962 

def enviar_teste():
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID, 
        "text": "🐂 *TESTE DO ROBÔ NESPRO*\nSe você recebeu isso, o robô está funcionando!",
        "parse_mode": "Markdown"
    }
    
    response = requests.post(url, data=payload)
    print(f"Resposta do Telegram: {response.text}")

if __name__ == "__main__":
    enviar_teste()
