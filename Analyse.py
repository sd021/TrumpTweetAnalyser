import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from datetime import date, timedelta
from collections import OrderedDict

def load_data(filename):
    dates, tweets = [], []

    with open(filename) as f:
        for line in f:
            split_line = line.split(",")
            dates.append(split_line[0])
            tweets.append(split_line[1])

    return (tweets, dates)

def construct_full_date_dict(dates):
    start_date = dates[-1].split(" ")[0]
    end_date = dates[0].split(" ")[0]

    split_start = start_date.split("-")
    split_end = end_date.split("-")
    d1 = date(int(split_start[0]), int(split_start[1]), int(split_start[2]))
    d2 = date(int(split_end[0]), int(split_end[1]), int(split_end[2]))
    full_date_list = [d1 + timedelta(days=x) for x in range((d2 - d1).days + 1)]

    ret_dict = OrderedDict()
    for d in full_date_list:
        ret_dict[str(d)] = 0
        
    for d in dates:
        ret_dict[d.split(" ")[0]] += 1
        
    return ret_dict


def main():
    tweets, dates = load_data("data.csv")
    dates_df = pd.DataFrame.from_dict(construct_full_date_dict(dates), orient="index")
    dates_df.index.name = "date"
    dates_df.columns = ["numTweets"]
    print dates_df.head
    ticks = dates_df.index[::30]
    plt.bar(dates_df.index, dates_df['numTweets'])
    plt.xticks(ticks, rotation=60)
    plt.show()


if __name__ == '__main__':
    main()
