from flask import Flask, request
import requests
import datetime

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return "💡 Бот запущен и работает."

@app.route("/webhook", methods=["POST"])
def webhook():
    try:
        data = request.get_json()
        print("📩 Получен POST от Telegram")
        print(data)

        chat_id = data["message"]["chat"]["id"]
        text = data["message"].get("text", "")

        # Ответное сообщение
        reply = f"Привет, ты написал: {text}"

        send_message(chat_id, reply)
        return "ok"

    except Exception as e:
        print(f"❌ Ошибка обработки запроса: {e}")
        return "error"

def send_message(chat_id, text):
    TOKEN = "7960898905:AAF78UoHr0IefNjyvLGildRqIhJqhJv5jkI"
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": text
    }
    r = requests.post(url, json=payload)
    print(f"📤 Ответ отправлен: {r.status_code}")

if __name__ == "__main__":
  import os
port = int(os.environ.get("PORT", 5000))
app.run(host="0.0.0.0", port=port)
