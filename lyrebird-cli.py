import os
import sys
import tweepy
from colorama import Fore, Back, Style, init

init(autoreset=True)

TWEET_LENGTH_LIMIT = 280

CONSUMER_KEY = os.environ.get("CONSUMER_KEY")
CONSUMER_SECRET = os.environ.get("CONSUMER_SECRET")
ACCESS_TOKEN = os.environ.get("ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.environ.get("ACCESS_TOKEN_SECRET")

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

response = {"status_id": None, "status_text": None, "responded_to": None}


def sendTweet(tweet, hashtags, response):
    if not tweet:
        print(
            Fore.RED
            + "\nError! Your tweet has no content! "
        )

        return response

    combined_status = tweet + " " + hashtags

    if len(combined_status) >= TWEET_LENGTH_LIMIT:
        print(
            Fore.RED
            + "\nError! Tweet too long! "
            + str(len(combined_status))
            + " characters"
        )
        good = combined_status[:TWEET_LENGTH_LIMIT]
        bad = combined_status[TWEET_LENGTH_LIMIT:]
        print(good + Back.RED + Fore.BLACK + bad)

        return response

    if response["status_id"] is None:
        status_response = api.update_status(status=combined_status)
    else:
        status_response = api.update_status(
            status=combined_status, in_reply_to_status_id=response["status_id"]
        )

    return {
        "status_id": status_response.id,
        "status_text": status_response.text,
        "responded_to": status_response.in_reply_to_status_id,
    }


print("Welcome to " + Back.GREEN + Fore.BLACK + " 🐦 Lyrebird! ")

print(
    "Live-tweeting engaged for account "
    + Back.MAGENTA
    + Fore.BLACK
    + " @"
    + api.me().screen_name
    + " "
)


hashtags = input(
    Back.BLUE
    + Fore.BLACK
    + " What hashtags should be appended to each tweet? "
    + Style.RESET_ALL
    + " "
)

while True:
    tweet = input(
                  Back.GREEN
                  + Fore.BLACK
                  + " What do you want to tweet? "
                  + Style.RESET_ALL
                  + " "
            )

    if tweet == "[[reset]]":
        print()
        print(
            Back.RED
            + Fore.BLACK
            + " LYREBIRD RESET: "
            + Style.RESET_ALL
            + " Your hashtags and thread have been reset, please add your new tags."
        )
        print()
        response["status_id"] = None
        hashtags = input(
            Back.BLUE
            + Fore.BLACK
            + " What hashtags should be appended to each tweet? "
            + Style.RESET_ALL
            + " "
        )
    elif tweet == "[[quit]]":
        sys.exit()
    else:
        response = sendTweet(tweet, hashtags, response)
        print()
        print(
            Back.BLUE
            + Fore.BLACK
            + " Reply to: "
            + Style.RESET_ALL
            + " "
            + str(response["responded_to"])
        )
        print(
              Back.MAGENTA
              + Fore.BLACK
              + " ID:       "
              + Style.RESET_ALL
              + " "
              + str(response["status_id"])
        )
        print(
              Back.YELLOW
              + Fore.BLACK
              + " Tweet:    "
              + Style.RESET_ALL
              + " "
              + str(response["status_text"])
        )
        print()
