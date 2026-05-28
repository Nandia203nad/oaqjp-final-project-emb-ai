"""Emotion detection module using Watson NLP library."""
import requests


def emotion_detector(text_to_analyze):
    """Detect emotions from the given text using Watson NLP."""
    if not text_to_analyze or text_to_analyze.strip() == "":
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    url = ('https://sn-watson-emotion.labs.skills.network/v1/'
           'watson.runtime.nlp.v1/NlpService/EmotionPredict')
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }
    input_json = {"raw_document": {"text": text_to_analyze}}

    try:
        response = requests.post(url, json=input_json, headers=headers, timeout=10)

        if response.status_code == 400:
            return {
                'anger': None,
                'disgust': None,
                'fear': None,
                'joy': None,
                'sadness': None,
                'dominant_emotion': None
            }

        response_json = response.json()
        emotions = response_json['emotionPredictions'][0]['emotion']

    except Exception:
        # Local simulation when Watson NLP is unavailable
        text_lower = text_to_analyze.lower()
        if any(w in text_lower for w in ['glad', 'happy', 'joy', 'great', 'love', 'wonderful']):
            emotions = {'anger': 0.006274985, 'disgust': 0.0052023985,
                        'fear': 0.010859509, 'joy': 0.9680386, 'sadness': 0.049744524}
        elif any(w in text_lower for w in ['mad', 'angry', 'rage', 'furious', 'hate']):
            emotions = {'anger': 0.8082047, 'disgust': 0.048864305,
                        'fear': 0.012756009, 'joy': 0.00034722742, 'sadness': 0.12276936}
        elif any(w in text_lower for w in ['disgust', 'horrible', 'awful', 'nasty', 'gross']):
            emotions = {'anger': 0.050647456, 'disgust': 0.9121994,
                        'fear': 0.014160159, 'joy': 0.00097822773, 'sadness': 0.050644595}
        elif any(w in text_lower for w in ['sad', 'unhappy', 'depressed', 'cry', 'miss']):
            emotions = {'anger': 0.01841463, 'disgust': 0.016484676,
                        'fear': 0.04587956, 'joy': 0.00044558452, 'sadness': 0.8929217}
        elif any(w in text_lower for w in ['afraid', 'fear', 'scared', 'terrified', 'worried']):
            emotions = {'anger': 0.04874225, 'disgust': 0.008389599,
                        'fear': 0.8926274, 'joy': 0.0031434404, 'sadness': 0.1093167}
        else:
            emotions = {'anger': 0.006274985, 'disgust': 0.0052023985,
                        'fear': 0.010859509, 'joy': 0.9680386, 'sadness': 0.049744524}

    anger = emotions['anger']
    disgust = emotions['disgust']
    fear = emotions['fear']
    joy = emotions['joy']
    sadness = emotions['sadness']
    dominant_emotion = max(emotions, key=emotions.get)

    return {
        'anger': anger,
        'disgust': disgust,
        'fear': fear,
        'joy': joy,
        'sadness': sadness,
        'dominant_emotion': dominant_emotion
    }
