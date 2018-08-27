from DataClean import DataCleaner
from Sentiment import SentimentCalculator
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

class DataPlotter():
    def __init__(self, df):
        self.df = df
        self.fig, self.ax = plt.subplots()
    
    def bar(self, col, ax=None, trendline=False):
        if ax is None:
            ax = self.ax
        ax.bar(self.df.index, self.df[col])

        if trendline:
            x = range(0, len(self.df.index))
            z = np.polyfit(x, self.df[col], 1)
            p = np.poly1d(z)

            # Plot trendline
            ax.plot(x, p(x), "g--")

    def scatter(self, col, ax=None, trendline=False):
        if ax is None:
            ax = self.ax
        ax.plot(self.df.index, self.df[col], color="red")

        if trendline:
            x = range(0, len(self.df.index))
            z = np.polyfit(x, self.df[col], 1)
            p = np.poly1d(z)

            ax.plot(x, p(x), "y--")

    def set_xticks(self, num_ticks, rot=20):
        idx_len = len(self.df.index)
        ticks = self.df.index[::idx_len / num_ticks]
        plt.xticks(ticks, rotation=rot)
        
    def get_axis_clone(self):
         return self.ax.twinx()

    def show(self):
        plt.show()


def main():
    data_cleaner = DataCleaner()
    df = data_cleaner.create_dataframe("data.csv")

    df = SentimentCalculator().add_sentiment_to_df(df)

    plot = DataPlotter(df)
    plot.bar("numTweets", trendline=True)
    ax2 = plot.get_axis_clone()
    plot.scatter("avg_wordcount", ax = ax2, trendline=True)
    plot.set_xticks(5)
    plot.show()
    
if __name__ == "__main__":
    main()
