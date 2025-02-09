from EmotionDetection.emotion_detection import emotion_detector
import unittest

class TestSentimentAnalyzer(unittest.TestCase):
    def test_emotion_detecter(self):   
        # test case for joy emotion 
        resp1 = emotion_detector("I am glad this happened")
        self.assertEqual(resp1['dominant_emotion'], 'joy')

        # test case for anger emotion 
        resp1 = emotion_detector("I am really mad about this")
        self.assertEqual(resp1['dominant_emotion'], 'anger')

        # test case for disgust emotion 
        resp1 = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(resp1['dominant_emotion'], 'disgust')

        # test case for sadness emotion 
        resp1 = emotion_detector("I am so sad about this")
        self.assertEqual(resp1['dominant_emotion'], 'sadness')

        # test case for fear emotion 
        resp1 = emotion_detector("I am really afraid that this will happen")
        self.assertEqual(resp1['dominant_emotion'], 'fear')


unittest.main()
