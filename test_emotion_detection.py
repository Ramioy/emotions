import unittest

from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetection(unittest.TestCase):

    def test_emotion_statement_1(self):
        result = emotion_detector("I am glad this happened")
        emotion = result["dominant_emotion"].split()[0]
        self.assertEqual(emotion, 'joy')

    def test_emotion_statement_1(self):
        result = emotion_detector("I am really mad about this")
        emotion = result["dominant_emotion"].split()[0]
        self.assertEqual(emotion, 'anger')

    def test_emotion_statement_1(self):
        result = emotion_detector("I feel disgusted just hearing about this")
        emotion = result["dominant_emotion"].split()[0]
        self.assertEqual(emotion, 'disgust')

    def test_emotion_statement_1(self):
        result = emotion_detector("I am so sad about this")
        emotion = result["dominant_emotion"].split()[0]
        self.assertEqual(emotion, 'sadness')
    
    def test_emotion_statement_1(self):
        result = emotion_detector("I am really afraid that this will happen")
        emotion = result["dominant_emotion"].split()[0]
        self.assertEqual(emotion, 'fear')

unittest.main()