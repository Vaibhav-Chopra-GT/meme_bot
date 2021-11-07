import tweepy
import time
import os
from postimage import downloadmeme

CONSUMER_KEY = os.environ.get('c_key')
CONSUMER_SECRET = os.environ.get('c_secret')
ACCESS_KEY = os.environ.get('acc_key')
ACCESS_SECRET = os.environ.get("acc_secret")

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)


filename = "lastid.txt"


def getlastid(file):
    fread = open(file, "r")
    lastid = int(fread.read().strip())
    fread.close()
    return lastid


def putid(id, file):
    fwrite = open(file, "w")
    fwrite.write(str(id))
    fwrite.close()
    return


def reply():
    lstseenid = getlastid(filename)
    mentions = api.mentions_timeline(
        since_id=lstseenid,
    )
    for mention in reversed(mentions):
        print(str(mention.id) + "  " + mention.text)
        downloadmeme()

        lstseenid = mention.id
        putid(lstseenid, filename)
        media = api.media_upload("meme.jpg")
        
        try:
            api.update_status(
            "@" + mention.user.screen_name,
            in_reply_to_status_id=mention.id,
            media_ids=[media.media_id],
                )
        except:
            api.update_status("@" + mention.user.screen_name + "Something wrong happened, pls try again",in_reply_to_status_id=mention.id)

if __name__ == "__main__":
    while True:
      
        reply()
        time.sleep(15)
           
