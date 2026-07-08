"""Flask server application for emotion detection."""

from flask import Flask, request, render_template

from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)


@app.route("/")
def get_app():
    """Render the application home page."""
    return render_template("index.html", result="")


@app.route("/emotionDetector")
def get_emotion_detector():
    """Analyze the input text and return detected emotions."""
    text = request.args.get("textToAnalyze")

    emotions = emotion_detector(text)

    if emotions["dominant_emotion"] is None:
        return "Invalid text! Please try again!"

    result = (
        f"For the given statement, the system response is "
        f"'anger': {emotions['anger']}, "
        f"'disgust': {emotions['disgust']}, "
        f"'fear': {emotions['fear']}, "
        f"'joy': {emotions['joy']} and "
        f"'sadness': {emotions['sadness']}. "
        f"The dominant emotion is {emotions['dominant_emotion']}."
    )

    return result


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
