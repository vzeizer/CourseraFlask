import requests
import json

def emotion_detector(text_to_analyze):
    """
    Detects emotions in the given text using Watson NLP Library
    
    Args:
        text_to_analyze (str): The text to analyze for emotions
        
    Returns:
        dict: Dictionary containing emotion scores and dominant emotion
    """
    
    # Check for blank or empty input
    if not text_to_analyze or text_to_analyze.strip() == "":
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
    
    # Watson NLP API endpoint
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    
    # Required headers
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock",
        'Content-Type': 'application/json'
    }
    
    # Prepare the input data
    input_json = {
        "raw_document": {
            "text": text_to_analyze
        }
    }

    try:
        # Make the POST request to the Watson NLP API
        response = requests.post(url, json=input_json, headers=headers, timeout=15)
        
        # Check for bad request status
        if response.status_code == 400:
            return {
                'anger': None,
                'disgust': None,
                'fear': None,
                'joy': None,
                'sadness': None,
                'dominant_emotion': None
            }
        
        # Check if the request was successful
        response.raise_for_status()
        
        # Convert response text to dictionary
        response_dict = json.loads(response.text)
        
        # Extract emotion scores
        emotions = response_dict['emotionPredictions'][0]['emotion']
        
        # Create the formatted output dictionary
        output = {
            'anger': emotions['anger'],
            'disgust': emotions['disgust'],
            'fear': emotions['fear'],
            'joy': emotions['joy'],
            'sadness': emotions['sadness']
        }
        
        # Find the dominant emotion (emotion with highest score)
        dominant_emotion = max(output.items(), key=lambda x: x[1])[0]
        output['dominant_emotion'] = dominant_emotion
        
        return output
        
    except requests.exceptions.RequestException as e:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
    except (json.JSONDecodeError, KeyError) as e:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }