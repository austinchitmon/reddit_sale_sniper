import praw
import webbrowser
import commonFunc


def main():

    subredditStream = commonFunc.getSubredditInstance()

    flairs = commonFunc.getFlairWhitelist()

    print("Monitoring...")
    for submission in subredditStream.submissions(skip_existing=True):
        print("Submission found: " + submission.title)
        if flairs is None or submission.link_flair_text.lower() in flairs:
            webbrowser.open_new_tab(submission.url)
    

if __name__ == "__main__":
    main()
