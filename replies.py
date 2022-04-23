import tweepy
import csv
import datetime
import json
import os
#import pandas as pd
####input your credentials here

consumer_key = 'pRw4PPuHLWje40Hqqe2Z53pRT'
consumer_secret = 'kLc35kiCf5rV2xK40Or3FkyXa5G388IrHRMPm9KWhgdL0xX9Yo'
access_token = '16479615-1QhMcQjHz5bwqiJGEWTEu08LitnPotme2RWVfpZ2S'
access_token_secret = '8oBpfnGUywzgSBdSYvvdQG7dTJ4QlUQcXFrQI72nSESRr'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)

#CDC screen name
screen_name = "CDCgov"

"YYYYMMDDHHMM"
orig_date = "202001010001"
until_date = "202006242359"

#CHANGE TO GET FULL TEXT WITH TWEET_MODE=EXTENDED

#replies = tweepy.Cursor(api.search_tweets, q='to:{}'.format(screen_name), since_id=tweet_id, max_id=last_id,tweet_mode='extended').items()
replies = tweepy.Cursor(api.search_full_archive, label="FullArchiveGandy",query='to:{}'.format(screen_name), fromDate=orig_date,toDate=until_date,maxResults=500).items()
lsFiles = [fStr.split('.json')[0] for fStr in os.listdir(r'A:\Project\New_data')]

#tweet IDs from CDCgov which talks about children vaccinations and having atleast 500 replies.
tweet_IDs = ["1232431332220784640",
             "1237129805310701569",
             "1246243351503962113",
             "1359536382180544517",
             "1392911350058320000",
             "1408462933793853443",
             "1408518303614648326",
             "1414623345291714567",
             "1420104200957038594",
             "1420105925440983040",
             "1443313161487196171",
             "1475607165981405193",
             "1485300545413783554",
             "1488618916616314880",
             "1489675180242870278",
             "1493982257790570501",
             "1504910584709582862"]



while True:
    try:
        reply = replies.next()
        print(reply._json)
        if reply.in_reply_to_status_id_str in tweet_IDs:
          tweet_id = reply.id
          if str(tweet_id) in lsFiles: assert(0)
          print(tweet_id)
          f = open(r'A:\Project\New_data' + str(reply.id) + '.json','w')
          json_out = json.dumps(reply._json)
          f.write(json_out)
          f.close()
          #print(reply)
          #assert(0)
    except StopIteration:
        print("Cursor is done")
        break

print(api)


################################################################################

