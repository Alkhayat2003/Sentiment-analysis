from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection")

@app.route('/emotionDetector')
def sent_analyzer():
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again."
    result = (
        "For the given text, the system response is:\n"
        f"anger: {response['anger']}\n"
        f"disgust: {response['disgust']}\n"
        f"fear: {response['fear']}\n"
        f"joy: {response['joy']}\n"
        f"sadness: {response['sadness']}\n"
        f"dominant emotion: {response['dominant_emotion']}."
    )
    return result

@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
