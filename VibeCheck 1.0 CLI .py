import colorama
from textblob import TextBlob
from colorama import Fore

colorama.init(autoreset=True)

banner = ("\n"
          " __      ___ _           _____ _               _    \n"
          " \ \    / (_) |         / ____| |             | |   \n"
          "  \ \  / / _| |__   ___| |    | |__   ___  ___| | __\n"
          "   \ \/ / | | '_ \ / _ \ |    | '_ \ / _ \/ __| |/ /\n"
          "    \  /  | | |_) |  __/ |____| | | |  __/ (__|   < \n"
          "     \/   |_|_.__/ \___|\_____|_| |_|\___|\___|_|\_\n"
          "                                                    \n"
          "                                                    ")

print(Fore.CYAN + banner)

def analyze_sentiment(text):
    blob = TextBlob(text)
    sentiment_score = blob.sentiment.polarity

    if sentiment_score <= -0.6:
        sentiment_score = "Very Negative"
    elif sentiment_score < 0:
        sentiment_category = "Negative"
    elif sentiment_score > 0:
        sentiment_category = "Positive"
    elif sentiment_score > 0.6:
        sentiment_category = "Very Positive"
    else:
        sentiment_category = "Neutral"
    return sentiment_category, sentiment_score

text = input("Enter The Text For Sentiment Analysis: ")

result, score = analyze_sentiment(text)

print(f"Sentiment:  {result}")
print(f"Sentiment Score: {score}")
