import os
import requests
from bs4 import BeautifulSoup
import requests
import tweepy as twitter
import time as time
import datetime

def API ():

    key = "ce7bJ9AzHejethSyQjyb7TjFW"
    secretKey = "vtBwo6hKGW7fJVoMGOaA0B3MTRfYQq5z6BFdqsB4SdpOL0HkQr"
    acessToken = "1206697140732465152-oSZMYjBuIBYTJa01lsXTEx96pwvnNe"
    secretToken = "AnhwBNF8pfThcTZ2523c2JPgi6cPKtMx3nOCPWLQ6duy5"

    auth = twitter.OAuthHandler(key,secretKey)
    authToke = auth.set_access_token(acessToken, secretToken)
    api = twitter.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

    return api

def TweetImage(connect, url, message):

    api = connect
    filename = 'temp.jpg'
    request = requests.get(url, stream=True)

    if request.status_code == 200:
        with open(filename, 'wb') as image:
            for chunk in request:
                image.write(chunk)

        api.update_with_media(filename, status=message)
        os.remove(filename)
    else:
        print("Unable to download image")

def ExtractImage(url):

    api = API()

    def getdata(url):
        r = requests.get(url)
        return r.text

    data = getdata(url)

    soup = BeautifulSoup(data, 'html.parser')

    for item in soup.find_all('img'):
        print(item['src'])

api = API()
searchThing = "#DOGE+#DOGECOIN+DOGE+DOGECOIN"

while True:

    try:



        for tweet in twitter.Cursor(api.search, searchThing).items():

            postUrl = f"https://twitter.com/i/web/status/{tweet.id}"
            ExtractImage(postUrl)


            f = open("IDStorage.txt", "a")
            f.write(f'{postUrl}\n')
            f.close()

            if tweet.favorited == False:

                api.create_favorite(tweet.id)
                print(f"Liked {datetime.datetime.now()}")
                time.sleep(2)

            else:

                print(f"Liked Already {datetime.datetime.now()}")

    except twitter.TweepError as e:
        print(f"{e.reason} {datetime.datetime.now()}")

    continue

url = "https://i.ytimg.com/vi/s3NWyh8a5t0/maxresdefault.jpg"
message = "Nice one"
TweetImage(api,url, message)

















