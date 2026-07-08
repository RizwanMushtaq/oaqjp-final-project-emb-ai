import requests
import json

def emotion_detector(text_to_analyze: str):
    if not text_to_analyze.strip():
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyze } }

    response = requests.post(url, json = input_json, headers=headers)
    
    formatted_response = json.loads(response.text)
    emotion_predictions = formatted_response['emotionPredictions']
    emotions = emotion_predictions[0]['emotion']

    highest_emotion = max(emotions, key=emotions.get)
    emotions['dominant_emotion'] = highest_emotion

    return emotions

if __name__ == "__main__":
    emotion_detector("I love this new technology.")