import requests

# 1. COLOQUE O TOKEN QUE VOCÊ COPIOU DO BOTFATHER AQUI
TOKEN = "8588052322:AAEraKnzeDWUvgGKSzYgX3SwEpYsf1Kteqo"

# 2. COLOQUE O SEU ID DO @userinfobot AQUI
CHAT_ID = "7974959962"

def enviar_teste():
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID, 
        "text": "🐂 ✅ CONSEGUIMOS! O robô do gado está ativo!"
    }
    
    # Isso vai forçar o erro a aparecer na tela da foto
    r = requests.post(url, data=payload)
    print(f"RESPOSTA_DO_TELEGRAM: {r.text}")

if __name__ == "__main__":
    enviar_teste()
