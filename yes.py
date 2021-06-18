import os
import tqdm
import bs4
import requests
from bs4 import BeautifulSoup
import requests
import tweepy as twitter
import time as time
import datetime
from selenium import webdriver
import urllib.parse
import Randoword

def API ():

    key = "ce7bJ9AzHejethSyQjyb7TjFW"
    secretKey = "vtBwo6hKGW7fJVoMGOaA0B3MTRfYQq5z6BFdqsB4SdpOL0HkQr"
    acessToken = "1206697140732465152-oSZMYjBuIBYTJa01lsXTEx96pwvnNe"
    secretToken = "AnhwBNF8pfThcTZ2523c2JPgi6cPKtMx3nOCPWLQ6duy5"

    # key = "MJScIMEqctzckk8TChjZ7SuZH"
    # secretKey = "WXtySv0OiNlTKjERxqXzE8LcxrkT79695zXZ72BgE5curTaQAV"
    # acessToken = "1029182465099882496-V6AvB5t4xXAP5oPLcci6Wsoufvfx7U"
    # secretToken = "R104PXiuoGfCgqYVeh2ha3xNWMO8j3V9lSEaPwyqobL4T"

    auth = twitter.OAuthHandler(key,secretKey)
    authToke = auth.set_access_token(acessToken, secretToken)
    api = twitter.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

    return api

api = API()

def TweetImage(connect, imageURL, message):

    api = connect
    filename = 'temp.jpg'
    request = requests.get(imageURL, stream=True)

    if request.status_code == 200:
        with open(filename, 'wb') as image:
            for chunk in request:
                image.write(chunk)

        api.update_with_media(filename, status=message)
        os.remove(filename)
    else:
        print("Unable to download image")

def ExtractPhoto(pageURL):

    url = pageURL
    driver = webdriver.Chrome(r"C:\Users\danny\PycharmProjects\pythonProject2\chromedriver.exe")

    driver.get(url)
    time.sleep(2)
    images = driver.find_elements_by_tag_name('img')

    for image in images:

        link = image.get_attribute("src")

        if "/media" in link:
            driver.close()
            return link

    driver.close()
    return None

searchThing = "(#doge) since:2021-06-17"

while True:

    try:

        data = twitter.Cursor(api.search, searchThing).items()

        for tweet in data:

            postUrl = f"https://twitter.com/i/web/status/{tweet.id}"

            if tweet.favorited == False:

                photoURL = ExtractPhoto(postUrl)

                if photoURL != None:

                    randoWord = Randoword.RandomWord()
                    TweetImage(api, photoURL, randoWord.SentenceGenerator())

                api.create_favorite(tweet.id)
                print(f"Liked {datetime.datetime.now()}")
                time.sleep(2)

            else:

                print(f"Liked Already {datetime.datetime.now()}")


            # f = open("IDStorage.txt", "a")
            # f.write(f'{postUrl}\n')
            # f.close()


    except twitter.TweepError as e:
        print(f"{e.reason} {datetime.datetime.now()}")

    continue


















