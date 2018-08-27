import sys
import io
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from datetime import date, timedelta
from collections import OrderedDict

class DataCleaner():
    def __init__(self):
        pass

    def load_data(self, filename):
        dates, tweets = [], []

        with open(filename, 'r') as f:
            for line in f:
                cleaned_line = self.clean_line(line)
                split_line = cleaned_line.split("|")
                dates.append(split_line[0])
                tweets.append(split_line[1])

        return (tweets, dates)

    def clean_line(self, line):
        replacements = {
            "&amp;": "and"
        }
        ret_str = line

        for replacement in replacements:
            ret_str = line.replace(replacement, replacements[replacement])

        return ret_str

    def construct_full_date_dict(self, dates):
        start_date = dates[-1].split(" ")[0]
        end_date = dates[0].split(" ")[0]

        split_start = start_date.split("-")
        split_end = end_date.split("-")
        
        # Create two date objects and then construct a list of the dates between them
        d1 = date(int(split_start[0]), int(split_start[1]), int(split_start[2]))
        d2 = date(int(split_end[0]), int(split_end[1]), int(split_end[2]))
        full_date_list = [d1 + timedelta(days=x) for x in range((d2 - d1).days + 1)]

        ret_dict = OrderedDict()
        for day in full_date_list:
            ret_dict[str(day)] = 0

        for day in dates:
            ret_dict[day.split(" ")[0]] += 1

        return ret_dict
    
    def construct_tweet_lists(self, tweets, occurances):
        column = []
        current_pos = 0
        for row in occurances:
            tweet_list = tweets[current_pos:current_pos+row]
            column.append(tweet_list)
            current_pos += row
            
        return column

    def add_wordcount_to_df(self, df):
        wordcounts = []
        avg_wc = []
        for row in df['tweets']:
            if len(row) == 0:
                wordcounts.append([])
                avg_wc.append(0)
            else:
                wc_list = [len(x.split(" ")) for x in row]
                wordcounts.append(wc_list)
                avg_wc.append(sum(wc_list)/len(wc_list))

        df['wordcounts'] = wordcounts
        df['avg_wordcount'] = avg_wc
        return df

    def create_dataframe(self, data_file):
        tweets, dates = self.load_data(data_file)
        dates_df = pd.DataFrame.from_dict(self.construct_full_date_dict(dates), orient="index")
        dates_df.index.name = "date"
        dates_df.columns = ["numTweets"]
        
        dates_df['tweets'] = self.construct_tweet_lists(tweets[::-1], dates_df['numTweets'])
        df = self.add_wordcount_to_df(dates_df)
        
        return dates_df



def main():
    pass


if __name__ == '__main__':
    main()
