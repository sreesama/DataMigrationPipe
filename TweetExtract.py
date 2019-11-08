import tweepy as tw
import pandas as pd
import json as JSON

def getAccess():
    consumer_key = "**************************"
    consumer_secret = "*****************************************"

    auth = tw.AppAuthHandler(consumer_key, consumer_secret)
    api = tw.API(auth, wait_on_rate_limit=True)

    return api

def extractTweets(search_words,date_since):
    api = getAccess();
    tweets = tw.Cursor(api.search,
                   q=search_words,
                   since=date_since).pages(5)

    lst=[]

    print('---> Reading tweets')
    for pages in tweets:
        for status in pages:
            lst.append(JSON.dumps(status._json))

    df = pd.DataFrame(lst)
    return df



