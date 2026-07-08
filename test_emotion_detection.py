from EmotionDetection.emotion_detection import emotion_detector
import unittest

class TestEmotionDetection(unittest.TestCase):
    def test_emotion_detector_joy(self):
        #Test case for 'I am glad this happened'
        result_1 = emotion_detector('I am glad this happened')
        self.assertEqual(result_1['dominant_emotion'], 'joy')

    def test_emotion_detector_anger(self):
        #Test case for 'I am really mad about this'
        result_1 = emotion_detector('I am really mad about this')
        self.assertEqual(result_1['dominant_emotion'], 'anger')
    
    def test_emotion_detector_disgust(self):
        #Test case for 'I feel disgusted just hearing about this'
        result_1 = emotion_detector('I feel disgusted just hearing about this')
        self.assertEqual(result_1['dominant_emotion'], 'disgust')
    
    def test_emotion_detector_sadness(self):
        #Test case for 'I am so sad about this'
        result_1 = emotion_detector('I am so sad about this')
        self.assertEqual(result_1['dominant_emotion'], 'sadness')
    
    def test_emotion_detector_fear(self):
        #Test case for 'I am really afraid that this will happen'
        result_1 = emotion_detector('I am really afraid that this will happen')
        self.assertEqual(result_1['dominant_emotion'], 'fear')


unittest.main()