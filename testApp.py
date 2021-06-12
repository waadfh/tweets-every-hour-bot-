import tweepy
from datetime import datetime
from pytz import timezone
import os
from dotenv import load_dotenv
load_dotenv()

API_KEY = os.getenv('API_KEY')
API_SECRET = os.getenv('API_SECRET')
ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
ACCESS_SECRET = os.getenv('ACCESS_SECRET')

auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)

format = "%Y-%m-%d %H:%M:%S %Z%z"

# current time in US
now_utc = datetime.now(timezone('US/Eastern'))
Eastren_time = now_utc.strftime(format)

# time in Asia/Qatar. My bot is based in Asia, so the following code converts US time to Asia/Qatar time.
now_asia = now_utc.astimezone(timezone('Asia/Qatar'))
qatar_time = now_asia.strftime(format)

# qatar_time returns a full string of date and time.
# The following code seperates them and stores each one in a new variable.
date_alone = qatar_time[0:10]
time_alone = qatar_time[11:16]


final_tweet = "On " + str(date_alone) + " At " + str(time_alone) + "\n" + "I love (Name)"


tweet = final_tweet
api.update_status(status = (tweet))