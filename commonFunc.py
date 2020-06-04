import oauthInfo
import praw

def getRedditInstance():
    return praw.Reddit(client_id = oauthInfo.client_id,
                    client_secret = oauthInfo.client_secret,
                    user_agent = oauthInfo.user_agent)

def getSubredditInstance():
    reddit = getRedditInstance()
    subredditToWatch = input("What subreddit posts links would you like to monitor? (press ENTER for buildapcsales): ") or "buildapcsales"
    print("\nSelected subreddit: " + subredditToWatch)
    return reddit.subreddit(subredditToWatch).stream

def getFlairWhitelist():
    printBAPCSalesFlairs()
    flairs = input("What flairs would you like to whitelist? Seperate with comments. (press ENTER for all): ") or None
    return [x.strip().lower() for x in flairs.split(',')] if flairs != None else None

def printBAPCSalesFlairs(): 
    print( '''
        Buildapcsales common flairs:
        Cables, Keyboard, PSU, Case, Memory, RAM
        Router, Controller, MOBO, Cooler, Sound, CPU 	
        Monitor, Speakers, Motherboard, SSD, Fan, Mouse
        GPU, Newegg, Webcam, Hard Drive, Networking, Bundle
        HDD, OS, Flash Drive, Headphones, Other, Optical Drive
        Power Supply, Mic, Processor\n''')