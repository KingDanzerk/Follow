import tweepy as twitter
import time as time
import datetime

auth = twitter.OAuthHandler("Cft5LpN6IxNBm7WmyQaNchEP2","87lWt7a4DwnI1G9cFZrd2UvEBkK4DmnwofNzFoxIUDitLc6RhB")
authToke = auth.set_access_token("1029182465099882496-bRKTtvFxr9UDrO6c0d4V1AOCabQDOq", "MBNloVAouG5aJTcFkyn4U0FSZoCdCpPtTSfCgWJwX8NwR")
api = twitter.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

searchThing = "#DOGE+#DOGECOIN+DOGE+DOGECOIN"

while True:

    try:
        for tweet in twitter.Cursor(api.search, searchThing).items():

            status = api.get_status(tweet.id)

            if status.favorited == False:

                api.create_favorite(tweet.id)
                print(f"Liked {datetime.datetime.now()}")
                time.sleep(2)

            else:

                print(f"Liked Already {datetime.datetime.now()}")

    except twitter.TweepError as e:
        print(f"{e.reason} {datetime.datetime.now()}")

    continue


















