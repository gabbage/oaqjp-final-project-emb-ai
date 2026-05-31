import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetection(unittest.TestCase):
    def test_emotion_detector(self):
        res_pos = emotion_detector("I am glad this happened")
        self.assertEqual(res_pos['dominant_emotion'], "joy")

        res_pos = emotion_detector("I am really mad about this")
        self.assertEqual(res_pos['dominant_emotion'], "anger")

        res_pos = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(res_pos['dominant_emotion'], "disgust")

        res_pos = emotion_detector("I am so sad about this")
        self.assertEqual(res_pos['dominant_emotion'], "sadness")

        res_pos = emotion_detector("I am really afraid that this will happen")
        self.assertEqual(res_pos['dominant_emotion'], "fear")
        
if __name__ == '__main__':
    unittest.main()    

