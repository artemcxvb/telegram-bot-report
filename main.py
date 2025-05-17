from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET"])
def hello():
    return "🟢 Бот працює!"

@app.route("/webhook", methods=["POST"])
def webhook():
    print("📨 Получен POST от Telegram")
    data = request.get_json()
    print(data)
    return "ok"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
