import unittest
from sentiment_analysis import analyze_sentiment


class TestAnalysis(unittest.TestCase):
    def test_positive_analysis_one(self):
        text = 'This place was awesome! I loved everything about it, I especially liked the great service'
        result = analyze_sentiment(text)
        self.assertTrue(result.is_positive)

    def test_positive_analysis_two(self):
        text = 'Awesome ambience, excellent performances from the leads, wonderful ideas being conveyed.'
        result = analyze_sentiment(text)
        self.assertTrue(result.is_positive)

    def test_neutral_analysis_one(self):
        text = 'This was okay. I had a decent time, I guess?'
        result = analyze_sentiment(text)
        self.assertTrue(result.is_neutral)

    def test_neutral_analysis_two(self):
        text = 'There were some things I liked about this, but also some things I did not like. Passable.'
        result = analyze_sentiment(text)
        self.assertTrue(result.is_neutral)

    def test_negative_analysis_one(self):
        text = 'I had a terrible time, it sucked, this was horrible. I would never go again. Sad!'
        result = analyze_sentiment(text)
        self.assertTrue(result.is_negative)

    def test_negative_analysis_two(self):
        text = 'This was bad and you should feel bad. It was horrifyingly frustrating to use.'
        result = analyze_sentiment(text)
        self.assertTrue(result.is_negative)

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
