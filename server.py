from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/')
def getApp():
    return render_template('index.html', result='')

@app.route('/emotionDetector')
def getEmotionDetector():
    text = request.args.get("textToAnalyze")

    emotions = emotion_detector(text)
    if emotions['dominant_emotion'] == None:
        return 'Invalid text! Please try again!'

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



if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)