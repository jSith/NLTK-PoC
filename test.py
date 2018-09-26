import unittest
from sentiment_analysis import analyze_sentiment


class TestAnalysis(unittest.TestCase):
    # This class inherits from the unittest.TestCase class

    def setUp(self):
        # setUp and tearDown are functions used by subclasses of TestCase
        # setUp will run before every method in the class, tearDown will run after
        # I don't actually need to do anything to set up or tear down here, so they're just for demonstration
        # However, you'll get an error if you try to leave a class or function blank. So use pass instead
        # NotImplementedError is also a thing, but it's for abstract methods
        pass

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
