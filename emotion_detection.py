import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    json_obj = { "raw_document": { "text": text_to_analyze } }
    output = requests.post(url, json=json_obj, headers=header)
    
    # converting the response text into a json dictionary
    new_output = json.loads(output.text)
    # Extract the emotions alon with their scores.
    emotion = new_output['emotionPredictions']
    first_item = emotion[0]
    emotionss = first_item['emotion']
    my_dict = {'anger': emotionss['anger'], 'disgust': emotionss['disgust'], 'fear': emotionss['fear'], 'joy': emotionss['joy'], 'sadness': emotionss['sadness']}

    # Find the dominant emotion.
    # find the max value in the dictionary
    max_value = max(my_dict.values())
    # find the key corresponding to the max value.
    max_key = [key for key, value in my_dict.items() if value == max_value]
    # Add the first max key corresponding to the max value to the dictionary.
    my_dict['dominant_emotion'] = max_key[0]
    return my_dict

            

            
    

    