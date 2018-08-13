import sys
import tweepy
import json
import yaml

def load_config(filename):
    with open("config.yml", 'r') as stream:
        try:
            config = yaml.load(stream)
        except yaml.YAMLError as exc:
            print(exc)
            
        return config

def scrape():
    config = load_config("config.yml")
    auth = tweepy.OAuthHandler(config['API_CONSUMER_KEY'], config['API_CONSUMER_SECRET'])
    auth.set_access_token(config['API_ACCESS_KEY'], config['API_ACCESS_SECRET'])

    api = tweepy.API(auth)

    tweets, dates = [], []
    for idx, tweet in enumerate(tweepy.Cursor(api.user_timeline,id='realdonaldtrump', tweet_mode='extended').items()):
        tweets.append(tweet.full_text.replace("\n", ""))
        dates.append(tweet.created_at)
        print(tweet.created_at)
        print("Processed tweet #{}".format(idx))
        
    with open("data.csv", 'w') as f:
        for tweet, date, in zip(tweets,dates):
            f.write("{0},{1}\n".format(str(date), tweet.encode("utf-8")))
                    
if __name__ == "__main__":
    scrape()
