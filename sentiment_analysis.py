# import nltk
# nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from analysis import Analysis


def analyze_sentiment(text, threshold=0.3):
    sentiment_analyzer = SentimentIntensityAnalyzer()
    scores = sentiment_analyzer.polarity_scores(text)

    # The sentiment analyzer returns scores in a dictionary like so:
    # {'neg': 0.461, 'neu': 0.42, 'pos': 0.119, 'compound': -0.8094}

    try:
        # We could use dict.get(key) or dict[key] to retrieve the value in a dictionary
        # The difference is that if the key doesn't exist in the dictionary, dict.get(key) will silently return None
        # Whereas dict[key] will throw a KeyError
        compound_score = scores['compound']
    except KeyError:
        raise RuntimeError(f'Oops, compound doesn\'t exist as a key in {scores}')

    is_positive = compound_score > threshold
    is_negative = compound_score < -threshold
    is_neutral = not is_positive and not is_negative
    return Analysis(is_positive=is_positive, is_neutral=is_neutral, is_negative=is_negative)
