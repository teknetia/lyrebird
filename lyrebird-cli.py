import tweepy
import config
from colorama import Fore, Back, Style, init
init(autoreset=True)


response_id = None
auth = tweepy.OAuthHandler(config.CONSUMER_KEY, config.CONSUMER_SECRET)
auth.set_access_token(config.ACCESS_TOKEN, config.ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)


def sendTweet(tweet, hashtags, response_id):
    combined_status = tweet + ' ' + hashtags
    if response_id is None:
        status_response = api.update_status(status=combined_status)
    else:
        status_response = api.update_status(status=combined_status,
                                            in_reply_to_status_id=response_id)
    return {
        'status_id': status_response.id,
        'status_text': status_response.text,
        'responded_to': status_response.in_reply_to_status_id
    }


print("Welcome to " + Back.GREEN + Fore.BLACK + " Lyrebird! ")

hashtags = input(Back.BLUE + Fore.BLACK +
                 " What hashtags should be appended to each tweet? " +
                 Style.RESET_ALL + " ")

while True:
    tweet = input("What do you want to tweet? ")
    response = sendTweet(tweet, hashtags, response_id)
    response_id = response['status_id']
    print("\nReply to: " + Back.BLUE + Fore.BLACK + " " +
          str(response['status_id']) + " ")
    print("ID: " + Back.YELLOW + Fore.BLACK + " " +
          str(response['status_id']) + " ")
    print("Tweet: " + str(response['status_text']) + "\n")
