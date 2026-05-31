"""
Backend Server Module for Emotion Detection
"""

from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector")
def emotion_analyzer():
    """
    Run emotion detector with given string
    """
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)

    if response['dominant_emotion'] is None:
        return_text = "Invalid text! Please try again!"
    else:
        return_text = f"""For the given statement, the system response is
        'anger': {response['anger']},
        'disgust': {response['disgust']}, 'fear': {response['fear']},
        'joy': {response['joy']} and 'sadness': {response['sadness']}.
        The dominant emotion is <b>{response['dominant_emotion']}</b>"""
    return return_text

@app.route("/")
def render_index_page():
    """
    Render index.html
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="localhost", port=5000)
