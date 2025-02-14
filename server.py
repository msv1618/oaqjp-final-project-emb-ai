"""server.py file"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection")


@app.route("/")
def render_index_page():
    """Generates the template using index.html"""
    return render_template('index.html')


@app.route("/emotionDetector")
def emotion_analyzer():
    """Detects emotion of input text using emotion_detector function"""

    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the emotion_deteector function and store the response
    response = emotion_detector(text_to_analyze)

    # Case where dominant_emotion is None
    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!."

    # Return a formatted string with the emotion score and dominant emotion.
    return "For the given statement, the system response is " + \
    f"'anger': {response['anger']}, 'disgust': {response['disgust']}, " + \
    f"'fear': {response['fear']}, 'joy': {response['joy']} and " + \
    f"'sadness': {response['sadness']}. The dominant emotion is " + \
    f"{response['dominant_emotion']}"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
