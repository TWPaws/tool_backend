from flask import Flask, request, Blueprint
import hmac
import hashlib
import logging

channel = Blueprint('channel', __name__)
SECRET = 'your_secret'

logging.basicConfig(level=logging.DEBUG)

@channel.route('/webhook', methods=['POST'])
def webhook():
    return 'Hello World'
    logging.debug('Webhook received')
    message_type = request.headers.get('Twitch-Eventsub-Message-Type')
    
    if not message_type:
        logging.error('Missing Twitch-Eventsub-Message-Type header')
        return 'Bad Request', 400
    
    event_data = request.json
    logging.debug(f'Message type: {message_type}')
    logging.debug(f'Event data: {event_data}')
    
    if message_type == 'webhook_callback_verification':
        challenge = event_data.get('challenge')
        if challenge:
            logging.debug(f'Challenge: {challenge}')
            return challenge, 200, {'Content-Type': 'text/plain'}
        else:
            logging.error('Challenge not found in event data')
            return 'Bad Request', 400
    
    return 'OK', 200

