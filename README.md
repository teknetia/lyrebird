# Lyrebird

Lyrebird helps you tweet faster and eaier from events by automatically appending the hashtags for you.

## Installation

Setup a virtual environment, and install these requirements: 

```
pip install -r requirements.txt
```

Get a set of Twitter API keys for your account: https://apps.twitter.com/
  
Sign in, create a new app, and get your *Consumer Key*, *Consumer Secret*; then create a set of Tokens: *Access Token*, and *Secret Access Token*

Save these four values as environment variables: `CONSUMER_KEY`, `CONSUMER_SECRET`, `ACCESS_TOKEN`, `ACCESS_TOKEN_SECRET`

## Use

Start up Lyrebird

```
python lyrebird-cli.py
```

Specify your hashtags: 

```
Welcome to 🦉 Lyrebird!
What hashtags should be appended to each tweet?
```

(psst. It doesn't have to be a hashtag. It can be any string. It will be appended to any tweet you make)

Then, tweet away!

```
What do you want to tweet?
```

Press enter, and you'll see the resulting Tweet ID from your tweet. 

Then, just keep typing!

## System functions

Lyrebird has some built in features that will allow you to perform actions without needing to exit and re-launch the app. Enter any of the following commands at the tweet prompt and the function will activate.

|Command    |Function   |
|-----------|-----------|
|`[[reset]]`|Resets the current thread and requests replacement hashtags|
|`[[quit]]` |Quits Lyrebird|
