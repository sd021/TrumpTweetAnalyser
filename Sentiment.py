import sys
from DataClean import DataCleaner
from textblob import TextBlob

class SentimentCalculator():
    def __init__(self):
        pass

    def add_sentiment_to_df(self, df):
        days_sentiments = []
        avg_days_sentiments = []

        for item in df['tweets']:
            sentiments = []
            if len(item) == 0:
                avg_days_sentiments.append(0)
                days_sentiments.append([])
            else:
                for tweet in item:
                    blob = TextBlob(tweet)
                    sentiment = 0
                    for sentence in blob.sentences:
                        sentiment += sentence.sentiment.polarity
                    avg_sentiment = sentiment / len(blob.sentences)
                    sentiments.append(avg_sentiment)
                days_sentiments.append(sentiments)
                avg_days_sentiments.append(sum(sentiments)/len(sentiments))
        df['sentiments'] = days_sentiments
        df['avg_sentiment'] = avg_days_sentiments

        return df


def main():
    data_cleaner = DataCleaner()
    df = data_cleaner.create_dataframe("data.csv")

    df = SentimentCalculator().add_sentiment_to_df(df)
    print df['avg_sentiment']


if __name__ == '__main__':
    main()
