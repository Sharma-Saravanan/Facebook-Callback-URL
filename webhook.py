from flask import Flask, request

app = Flask(__name__)

VERIFY_TOKEN = "my_verify_token_123"  # Use this in your Meta app settings

@app.route('/webhook', methods=['GET'])
def verify_webhook():
    mode = request.args.get('hub.mode')
    token = request.args.get('hub.verify_token')
    challenge = request.args.get('hub.challenge')

    if mode == 'subscribe' and token == VERIFY_TOKEN:
        return challenge, 200
    else:
        return 'Invalid verification token', 403

if __name__ == '__main__':
    app.run()
