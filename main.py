from flask import Flask, request
import requests

app = Flask(__name__)

BOT_TOKEN = "7960898905:AAF78UoHr0IefNjyvLGildRqIhJqhJv5jkI"
API_URL = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

@app.route("/", methods=["GET"])
def home():
    return "✅ Бот запущен и готов к работе."

@app.route("/webhook", methods=["POST"])
def webhook():
    try:
        data = request.get_json()
        print("📩 Получен POST от Telegram")
        print(data)

        # Обработка текстовых сообщений
        if "message" in data:
            chat_id = data["message"]["chat"]["id"]
            text = data["message"].get("text", "")
            reply = f"🤖 Бот работает! Ты написал: {text}"
            send_message(chat_id, reply)
        return "ok"
    except Exception as e:
        print("❌ Ошибка:", e)
        return "error"

def send_message(chat_id, text):
    payload = {
        "chat_id": chat_id,
        "text": text
    }
    response = requests.post(API_URL, json=payload)
    print(f"📤 Ответ отправлен. Статус: {response.status_code}")

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
