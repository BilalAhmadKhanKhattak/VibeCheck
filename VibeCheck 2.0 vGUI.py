import tkinter as tk

import colorama
from textblob import TextBlob
from tkinter import PhotoImage
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
          "                                                    "
          " A Simple Project To Check Your Vibe Through Your Text"
          "Created With Love By Bilal Ahmad Khan AKA Mr BILRED ")

print(Fore.CYAN + banner)
def analyze_sentiment():

    text = text_input.get("1.0", tk.END)
    blob = TextBlob(text)

    sentiment_score = blob.sentiment.polarity
    # if sentiment_score > 0.6:
    #     sentiment = "You have a very Positive Vibe\nYour Vibe Matches With Mine, We Have The Same Energy"
    #     emoji = "😊"
    # elif sentiment_score > 0:
    #     sentiment = "I guess you look good"
    #     emoji = "🙂"
    # elif sentiment_score <= -0.6:
    #     sentiment = "Naah, Dont be that VERY NEGATIVE guy"
    #     emoji = "😡"
    # elif sentiment_score < 0:
    #     sentiment = "Negative"
    #     emoji = "☹️"
    # else:
    #     sentiment = "Neutral"
    #     emoji = "😐"
    if sentiment_score > 0.4:
        sentiment = "Wow, you're really radiating positive energy!\nWe totally vibe together! Our energies align perfectly! 😊"
        emoji = "😊"
    elif sentiment_score > 0:
        sentiment = "You’re looking good today!\nThere's a great energy about you. Keep it up! 🙂"
        emoji = "🙂"
    elif sentiment_score <= -0.4:
        sentiment = "Hey, don’t be too hard on yourself!\nI know things can be tough, but let’s turn that frown upside down! 😡"
        emoji = "😡"
    elif sentiment_score < 0:
        sentiment = "I see you're feeling a little down.\nHang in there, things will get better. You’ve got this! ☹️"
        emoji = "☹️"
    else:
        sentiment = "You're feeling kind of neutral, huh?\nNo worries, let’s find that spark and get you back to feeling great! 😐"
        emoji = "😐"

    result_label.config(text= f"Vibe: {sentiment}")
    score_label.config(text=f"Sentiment Score: {sentiment_score:.2f}")
    emoji_label.config(text=f"{emoji}")


root = tk.Tk()
root.title("VibeCheck By BILRED")
root.geometry("1600x700")
root.configure(bg="lightYELLOW")

bg_image = PhotoImage(file="vibecheck16002.png")
bg_label = tk.Label(root, image=bg_image)
bg_label.place(relwidth=1, relheight=1)

# frame = tk.Frame(root, bg="grey", bd=5)
# frame.place(relwidth=1, relheight=1)

instruction_label = tk.Label(root, text="Enter text for Check Your Vibe", bg="Pink")
instruction_label.pack(padx=3, pady=10)

text_input = tk.Text(root, height=10, width=60)
text_input.pack(pady=10)

analyze_button = tk.Button(root, text="Analyze Vibe", command=analyze_sentiment, bg="LightGreen", font=("Arial", 15)) #  This calls the analyze_sentiment function
analyze_button.pack(pady=10)

result_label = tk.Label(root, text="Vibe: ", font=("Helvetica", 20))
result_label.pack(pady=5)

emoji_label = tk.Label(root, font=("Arial", 60))
emoji_label.pack(pady=5)

score_label = tk.Label(root, text="Sentiment Score: ")
score_label.pack(pady=5)

root.mainloop()
