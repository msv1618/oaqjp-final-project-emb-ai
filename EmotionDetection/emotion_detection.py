import requests
import json


def emotion_detector(text_to_analyze):
    URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyze } }
    resp = requests.post(url=URL, headers=headers, data=json.dumps(input_json))
    resp = json.loads(resp.text)['emotionPredictions'][0]['emotion']
    dominant = sorted(resp.items(), key=lambda x: x[1], reverse=True)
    resp['dominant_emotion'] = dominant[0][0]
    return resp