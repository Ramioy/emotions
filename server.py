"""
Final Project: Emotion Detector
BY: Yoimar Moreno
"""

from flask import Flask, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector")
def predit_emotion():
    """
    This funtion handles the prediction request
    If user send no data, It returns an status code 400
    and a message to the user
    """
    text_to_analyse = str(request.args.get("textToAnalyze"))
    response = emotion_detector(text_to_analyse)
    if text_to_analyse == "" or (response['dominant_emotion'] is None):
        return "Invalid text! Please try again!", 400

    return (
        f"For the given statement, the system response is<br>" 
        f"'anger': {response['anger']}<br>"
        f"'disgust': {response['disgust']} <br>"
        f"'fear': {response['fear']}<br>"
        f"'joy': {response['joy']} and<br>" 
        f"'sadness': {response['sadness']}<br>"
        f"The dominant emotion is {response['dominant_emotion']}."
    )

if __name__ == "__main__":
    app.run()
