from flask import Flask, request

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    # TODO: Get JSON data from the request and print it
    data = request.get_json()
    message = f"Received alert: {data}"
    print(message)
    return message

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
