import os
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
    combined_status = tweet + " " + hashtags

    if len(combined_status) >= TWEET_LENGTH_LIMIT:
        print(
            Fore.RED + "Error! Tweet too long! " + str(len(combined_status))
        ) + " characters"
        return response

    if response_id is None:
        status_response = api.update_status(status=combined_status)
    else:
        status_response = api.update_status(
            status=combined_status, in_reply_to_status_id=response["id"]
        )
    return {
        "status_id": status_response.id,
        "status_text": status_response.text,
        "responded_to": status_response.in_reply_to_status_id,
    }


print("Welcome to " + Back.GREEN + Fore.BLACK + " Lyrebird! ")

print(
    "Live-tweeting engaged for account "
    + Back.MAGENTA
    + Fore.BLACK
    + "@"
    + api.me().screen_name
)


hashtags = input(
    Back.BLUE
    + Fore.BLACK
    + " What hashtags should be appended to each tweet? "
    + Style.RESET_ALL
    + " "
)

while True:
    tweet = input("What do you want to tweet? ")
    response = sendTweet(tweet, hashtags, response)
    response_id = response["status_id"]
    print(
        "\nReply to: " + Back.BLUE + Fore.BLACK + " " + str(response["status_id"]) + " "
    )
    print("ID: " + Back.YELLOW + Fore.BLACK + " " + str(response["status_id"]) + " ")
    print("Tweet: " + str(response["status_text"]) + "\n")
