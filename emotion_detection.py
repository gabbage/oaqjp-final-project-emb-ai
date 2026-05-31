import requests
import json

URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

emotions = ['anger', 'disgust', 'fear', 'joy', 'sadness'] 
dominant = 'dominant_emotion'

def emotion_detector(text_to_analyze):
    if not isinstance(text_to_analyze, str):
        raise TypeError("Function 'emotion_detector' expected a string!")

    input_json = { "raw_document": { "text": text_to_analyze } }

    response = requests.post(URL, json=input_json, headers=header)
    response_json = json.loads(response.text)
    return_data = {}

    if response.status_code == 200:
        highest_score = 0.0
        highest_name = ''

        for e in emotions:
            return_data[e] = response_json["emotionPredictions"][0]["emotion"][e]
            if return_data[e] > highest_score:
                highest_score = return_data[e]
                highest_name = e

        return_data[dominant] = highest_name
        
        return return_data

    else:
        for e in emotions:
            return_data[e] = None

        return_data[dominant] = None

        return return_data

"""
{"emotionPredictions":[{"emotion":
                        {"anger":0.01364663, "disgust":0.0017160787, "fear":0.008986978, "joy":0.9719017, "sadness":0.055187024},
                        "target":"", "emotionMentions":[{"span":{"begin":0, "end":27, "text":"I love this new technology."}, "emotion":{"anger":0.01364663, "disgust":0.0017160787, "fear":0.008986978, "joy":0.9719017, "sadness":0.055187024}}]}], "producerId":{"name":"Ensemble Aggregated Emotion Workflow", "version":"0.0.1"}}
"""
