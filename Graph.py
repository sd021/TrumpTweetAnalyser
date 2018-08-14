from DataClean import DataCleaner
import matplotlib.pyplot as plt
import seaborn as sns



def main():
    data_cleaner = DataCleaner()
    df = data_cleaner.create_dataframe("data.csv")
    
    print df.head
    ticks = df.index[::30]
    plt.bar(df.index, df['numTweets'])
    plt.xticks(ticks, rotation=60)
    plt.show()
    
if __name__ == "__main__":
    main()