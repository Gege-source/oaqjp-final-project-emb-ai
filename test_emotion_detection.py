# Import the EmotionDetection package and unittest librar
from EmotionDetection.emotion_detection import emotion_detector
import unittest

# Create a class to perform the test.
class TestEmotionDectector(unittest.TestCase):
    def test_emotion_detector(self):
        # Test the first statement and its expected emotion.
        output1 = emotion_detector('I am glad this happened')
        self.assertEqual(output1['dominant_emotion'], 'joy')

        # Test the second statement and its expected emotion.
        output2 = emotion_detector('I am really mad about this')
        self.assertEqual(output2['dominant_emotion'], 'anger')

        # Test the third statement and its expected emotion.
        output3 = emotion_detector('I feel disgusted jsut hearing about this')
        self.assertEqual(output3['dominant_emotion'], 'disgust')

        # Test the fourth statement and its expected emotion.
        output4 = emotion_detector('I am so sad about this')
        self.assertEqual(output4['dominant_emotion'], 'sadness')

        # Test the fifth statement and its expected emotion.
        output5 = emotion_detector('I am really afraid that this will happen')
        self.assertEqual(output5['dominant_emotion'], 'fear')

# Call the unit tests.
unittest.main()
