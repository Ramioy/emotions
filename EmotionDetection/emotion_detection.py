import requests
import json

def emotion_detector(payload):
    text_to_analyse  = payload
    URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyse  } }
    response = requests.post(URL, json = input_json, headers=headers, verify=False)
    json_loaded = json.loads(response.text)
    emotions_list = list(json_loaded['emotionPredictions'][0]['emotion'].items())
    dominant_emotion = get_dominant_emotion(emotions_list)
    formated_output = {
        "anger": f"{emotions_list[0][1]}",
        "disgust": f"{emotions_list[1][1]}",
        "fear": f"{emotions_list[2][1]}",
        "joy": f"{emotions_list[3][1]}",
        "sadness": f"{emotions_list[4][1]}",
        "dominant_emotion": f"{dominant_emotion}"
    }
    pretty = json.dumps(formated_output, indent=2)
    print(pretty) #Had to do this because when it is returned directly it is not formated.
    return

def sort_emotions(payload):
    return payload[1]

def get_dominant_emotion(payload):
    dominant = payload.copy()
    dominant.sort(key = sort_emotions, reverse = True)
    return f"{dominant[0][0]}"