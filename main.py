from flask import Flask, request
import requests

app = Flask(__name__)

# Токен бота Telegram
TOKEN = "7853699104:AAGKCXqpgdSfFagz5M6zdfDSiEVAOYNmsN4"
API_URL = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

@app.route("/", methods=["GET"])
def index():
    return "✅ Бот запущен и готов к работе."

@app.route("/webhook", methods=["POST"])
def webhook():
    try:
        data = request.get_json()
        print("📨 Получен POST от Telegram:", data)

        if "message" in data:
            chat_id = data["message"]["chat"]["id"]
            text = data["message"].get("text", "")
            reply = f"Привет, ты написал: {text}"
            send_message(chat_id, reply)

        return "ok"

    except Exception as e:
        print(f"❌ Ошибка при обработке запроса: {e}")
        return "error"

def send_message(chat_id, text):
    payload = {
        "chat_id": chat_id,
        "text": text
    }
    r = requests.post(API_URL, json=payload)
    print(f"📤 Ответ отправлен. Статус: {r.status_code}")

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
