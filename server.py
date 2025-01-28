"""
This module implements a Flask server for emotion detection.
It provides endpoints for analyzing text and detecting emotions using the EmotionDetection package.
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

# Initialize the Flask application with a proper name
app = Flask("Emotion Detection Server")

@app.route("/")
def render_index_page():
    """
    Renders the main page of the application.
    Returns:
        str: Rendered HTML content of the index page
    """
    return render_template('index.html')

@app.route("/emotionDetector")
def emotion_detector_route():
    """
    Processes text input and returns emotion analysis results.
    This endpoint expects a 'textToAnalyze' parameter in the URL
    and returns a formatted string containing emotion scores.
    Returns:
        str: Formatted emotion analysis results or error message
    """
    text_to_analyze = request.args.get('textToAnalyze')

    # Get emotion scores from the detector
    response = emotion_detector(text_to_analyze)

    # Check if the response indicates an error (dominant_emotion is None)
    if not response or response.get('dominant_emotion') is None:
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
    # Run the Flask application
    app.run(host='localhost', port=5000, debug=False)
