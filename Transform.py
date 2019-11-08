import pandas as pd
from textblob import TextBlob
import json as JSON

def processTransform(dataDFList):
    for df in dataDFList:
        if (df[0] == 'iris'):
            df[1] = processTable1(df[1])
        elif (df[0] == 'tweets'):
            df[1] = processTweets(df[1])
    return dataDFList

def processTable1(df):
    df['sepallengthcm'] = df['sepallengthcm'].astype('float32')
    df['sepalwidthcm']  = df['sepalwidthcm'].astype('float32')
    df['petallengthcm'] = df['petallengthcm'].astype('float32')
    df['petalwidthcm']  = df['petalwidthcm'].astype('float32')
    df = df.dropna()
    return df

def processTweets(df):
    tweetsData = []
    columns = ['time', 'location', 'lang', 'text', 'source','hashtag','htcount','rtcount','fvcount','polarity','subjectivity']
    for tweet in df.values.tolist():
        i = JSON.loads(tweet[0])
        tweetD = []
        hashtagT = ''
        count = 0
        tweetD.append(i['created_at'])
        tweetD.append(i['user']['location'])
        tweetD.append(i['lang'])
        tweetD.append(i['text'])
        sourceraw = i['source']
        source = sourceraw[sourceraw.find('rel="nofollow">') + 15:-4]
        tweetD.append(source)
        for hashtag in i['entities']['hashtags']:
            count = count + 1
            hashtagT = hashtagT + '-->' + hashtag['text']
        tweetD.append(hashtagT)
        tweetD.append(count)
        tweetD.append(i['retweet_count'])
        tweetD.append(i['favorite_count'])
        tweetD.append(TextBlob(i['text']).polarity)
        tweetD.append(TextBlob(i['text']).subjectivity)
        tweetsData.append(tweetD)

    df = pd.DataFrame(tweetsData, columns=columns)
    return df