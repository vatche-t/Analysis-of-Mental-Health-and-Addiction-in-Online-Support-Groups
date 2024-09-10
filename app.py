from flask import Flask, render_template, request, jsonify
import os
import json
import re

app = Flask(__name__)

# Load intents and entities
intents_path = 'intents/'
entities_path = 'entities/'

def load_json_files(directory):
    data = {}
    for filename in os.listdir(directory):
        if filename.endswith('.json'):
            file_path = os.path.join(directory, filename)
            with open(file_path, 'r') as file:
                data[filename[:-5]] = json.load(file)
    return data

intents_data = load_json_files(intents_path)
entities_data = load_json_files(entities_path)

def find_entities(message):
    detected_entities = {}
    message_lower = message.lower()
    for entity_name, entity_info in entities_data.items():
        if entity_name.endswith('_entries_en'):
            for entry in entity_info:
                value = entry['value'].lower()
                synonyms = [syn.lower() for syn in entry['synonyms']]
                if value in message_lower or any(syn in message_lower for syn in synonyms):
                    detected_entities[entity_name.replace('_entries_en', '')] = value
                    break  # assuming one value per entity type for simplicity
    return detected_entities
def find_intent_by_training_phrase(message, entities):
    message_lower = message.lower()
    for intent_name, user_says in intents_data.items():
        if intent_name.endswith('_usersays_en'):
            for user_say_data in user_says:
                phrases = [d['text'].lower() for d in user_say_data['data']]
                for phrase in phrases:
                    if re.search(r'\b' + re.escape(phrase) + r'\b', message_lower):
                        return intent_name.replace('_usersays_en', '')
    return "Default Fallback Intent"


# Route to handle sending of messages
@app.route('/send_message', methods=['POST'])
def send_message():
    message = request.form['message']
    entities = find_entities(message)
    matched_intent = find_intent_by_training_phrase(message, entities)
    matched_intent_name = matched_intent if not matched_intent.endswith('_usersays_en') else matched_intent[:-12]

    # Get the response for the matched intent
    intent_responses = intents_data.get(matched_intent_name, {}).get('responses', [])
    response_text = "Sorry, I'm not sure what to say."
    
    if intent_responses:
        for resp in intent_responses:
            response_text = resp['messages'][0]['speech'][0]  # Use the first speech response
            break  # We use the first response for simplicity

    # Format the response with the detected entity
    for entity, value in entities.items():
        response_text = response_text.replace('$' + entity, value)
    
    return jsonify({'message': response_text})

# Serve the chatroom interface
@app.route('/')
def chatroom():
    return render_template('chatroom.html')

if __name__ == '__main__':
    app.run(debug=True)