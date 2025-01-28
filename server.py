from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection")

@app.route("/")
def render_index_page():
    """Renders the index.html template."""
    return render_template('index.html')

@app.route("/emotionDetector")
def emotion_detector_route():
    """
    Processes the text and returns formatted emotion analysis.
    Expected URL parameter: textToAnalyze
    """
    text_to_analyze = request.args.get('textToAnalyze')
    
    # Get emotion scores from the detector
    response = emotion_detector(text_to_analyze)
    
    # Check if the response indicates an error (dominant_emotion is None)
    if not response or response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"
    
    # Format the response string according to the specification
    formatted_response = (
        f"For the given statement, the system response is "
        f"'anger': {response['anger']}, "
        f"'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, "
        f"'joy': {response['joy']} and "
        f"'sadness': {response['sadness']}. "
        f"The dominant emotion is {response['dominant_emotion']}."
    )
    
    return formatted_response

if __name__ == "__main__":
    app.run(host='localhost', port=5000)