from flask import Flask, request, jsonify
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route('/emotionDetector')
def emotion_detector_endpoint():
    """
    Endpoint for emotion detection based on user input.
    
    Returns:
        str: A message with the emotion analysis result.
    """
    text_to_analyze = request.args.get('textToAnalyze')
    
    if text_to_analyze:
        result = emotion_detector(text_to_analyze)

        if result['dominant_emotion'] is None:  # Handle invalid text
            return "Invalid text! Please try again!", 400

        # Constructing the response as per the customer request
        response_text = (
            f"For the given statement, the system response is "
            f"'anger': {result['anger']}, "
            f"'disgust': {result['disgust']}, "
            f"'fear': {result['fear']}, "
            f"'joy': {result['joy']} and "
            f"'sadness': {result['sadness']}. "
            f"The dominant emotion is {result['dominant_emotion']}."
        )
        return response_text
    else:
        return "No text provided for analysis", 400

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
