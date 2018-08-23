from DataClean import DataCleaner
from Sentiment import SentimentCalculator
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns



def main():
    data_cleaner = DataCleaner()
    df = data_cleaner.create_dataframe("data.csv")

    df = SentimentCalculator().add_sentiment_to_df(df)

    fig, ax1 = plt.subplots()

    # Bar chart of number of tweets per day
    ax1.bar(df.index, df['numTweets'])

    # Trendline for the number of tweets per day
    x = range(0, len(df.index))
    z = np.polyfit(x, df['numTweets'], 1)
    p = np.poly1d(z)
    print p.coef
    # Plot trendline
    ax1.plot(x, p(x), "g--")

    # Create 2nd axis on rhs
    ax2 = ax1.twinx()

    # Plot average sentiment per day
    ax2.plot(df.index, df['avg_sentiment'], color="red")

    # Trenline for avergae sentiment per day
    z = np.polyfit(x, df['avg_sentiment'], 1)
    p = np.poly1d(z)
    print p.coef
    ax2.plot(x, p(x), "y--")

    # Only label x axis with one day per month
    ticks = df.index[::30]
    plt.xticks(ticks, rotation=60)
    plt.show()
    
if __name__ == "__main__":
    main()
