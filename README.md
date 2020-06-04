# reddit_sale_sniper
Automatically opens new links posted to a given subreddit.

## Oauth Config
Message me for the `client_id` and `client_secret` in `oauthInfoBase.py`

Rename `oauthInfoBase.py` file to `oauthInfo.py` after adding `client_id` and `client_secret`. 

## Compiling and running

Make sure you have Python 3+ and pip installed.

Download required reddit API package using the following command:

`pip install praw`

Run the script with the following command:

`python salesSelector.py`

Enter the subreddit you would like to monitor and whitelisted filter tags. Once 'Monitoring...' is printed, the script is reading the provided subreddit and will open new links posted in the default browser. 

