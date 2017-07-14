from flask import Flask, jsonify
app = Flask(__name__)
app.config.from_pyfile('.env')

import sms
import voice
import number_insight

@app.route("/sms/send")
def sms_send():
    return jsonify(sms.send(app.config))

@app.route("/voice/call")
def call():
    return jsonify(voice.call(app.config))

@app.route('/number-insight/basic/<phone_number>')
def number_insight_basic(phone_number):
    return jsonify(number_insight.basic(app.config, phone_number))    

if __name__ == "__main__":
    app.run()
