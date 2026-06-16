import flask 
from flask import request, jsonify
app = flask.Flask(__name__)

@app.route('chatbot/webhook', methods=['POST'])
def webhook():
    data = request.get_json()
    # Process the incoming webhook data
    return jsonify({"status": "success"})

if __name__ == '__main__':
    app.run(debug=True)