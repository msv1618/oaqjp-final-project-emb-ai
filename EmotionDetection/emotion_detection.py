import requests
import json


def emotion_detector(text_to_analyze):
    """Analyzes emotion of text_to_analyze"""
    # url, headers and  data
    URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyze } }

    # fetch response from watsonx
    resp = requests.post(url=URL, headers=headers, data=json.dumps(input_json))

    # Get status code
    print(resp.status_code)
    if resp.status_code == 200:
        response = json.loads(resp.text)['emotionPredictions'][0]['emotion']
        dominant = sorted(response.items(), key=lambda x: x[1], reverse=True)
        response['dominant_emotion'] = dominant[0][0]
    
    # Status code 500
    elif resp.status_code == 400:
        response = {
            "anger": None,
            "disgust": None, 
            "fear": None, 
            "joy": None, 
            "sadness": None, 
            "dominant_emotion": None
            }
   
    return response