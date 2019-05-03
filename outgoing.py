import os
from flask import Flask, request
from twilio.rest import Client
from twilio.twiml.voice_response import VoiceResponse, Gather, Hangup

TWILIO_PHONE_NUMBER = os.environ.get('TWILIO_PHONE_NUMBER')
TWILIO_API = os.environ.get('TWILIO_API')
TWILIO_AUTH_TOKEN = os.environ.get('TWILIO_AUTH_TOKEN')

# initialize ngrok URL
ngrok_url = "[insert at runtime]"  # INSERT NGROK URL...include /

app = Flask(__name__)

client = Client(TWILIO_API, TWILIO_AUTH_TOKEN)


# Make outgoing voice call
client.calls.create(
    to='18009666546',
    from_=TWILIO_PHONE_NUMBER,
    url=ngrok_url + 'parse'
)

# Handle outgoing voice call
@app.route('/parse', methods=['GET', 'POST'])
def voice():
    twiml = VoiceResponse()
    gather = Gather(action='store',
                    input='dtmf speech',
                    timeout="3")
    gather.say('hello')
    gather.pause(length="3")
    twiml.append(gather)
    twiml.hangup()  # hang up call after gathering speech
    return str(twiml)


# Handle POST from <Gather> action reach out final result
@app.route('/store', methods=['GET', 'POST'])
def callback():
    twiml = VoiceResponse()
    speech_result = request.values.get('SpeechResult', None)
    print('Speech Result: ' + speech_result)

    # print('Speech Result: ' + speech_result)
    twiml.hangup()  # hang up call after gathering speech
    return str(twiml)


if __name__ == "__main__":
    # input phone number
    app.run(port=5000, debug=True)

