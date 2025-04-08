import re
import random
import requests
from bs4 import BeautifulSoup
from difflib import SequenceMatcher


def random_text() -> str:
    text: str = "this is random text"
    return text


def bot_reply_structure(reply: str) -> str:
    bot_line = f"Bot: {reply}"

    return bot_line


user_content_file: str = "user_text.txt"  # sets the file that we will be analyzing


# don't forget to add "json" type file where we can store questions asked previously
# when you make the code proprietary and unique you are easily absorbed into another company
# returns ratio for similarity of strings
def similar(a, b) -> float:
    return SequenceMatcher(None, a, b).ratio()


# returns replies when the user submits an empty string
def empty_string() -> str:
    empty_string_replies: list[str] = ["Please give me something to work with :(.",
                                       "But-but, you gave me nothing. @_A",
                                       "Text makes my robot veins tingle",
                                       "I can't analyze the air. -_-"]
    return random.choice(empty_string_replies)


# returns replies when the user submits more than one valid string
def valid_string(num_entries: int) -> str:
    valid_string_replies: list[str] = ["Yummy in my robot tummy.",
                                       "Give me more. @_@ If you'd like.",
                                       f"{num_entries}? Wow, you're really doing something. :/",
                                       f"Geez, {num_entries}? Don't go too crazy.",
                                       "The more text you add the better I feel. *_*",
                                       "Thank you, human. :)",
                                       "Ah...I'm excited to analyze this for you."]
    return random.choice(valid_string_replies)


def start_message() -> str:
    say_done_reply: str = 'Say "done" when ready'
    start_message_replies: list[str] = [
        f"I am here to analyze your human content. {say_done_reply} and I'll get to work. :0",
        f"I have been summoned. Please paste some text for me to view. {say_done_reply}, and I'll be a happy goose. I mean robot. @_@ ",
        f"*Beep boop* Paste some text for me to convert to 0s and 1s and then reconvert to human speak. {say_done_reply} -_-",
        f"Give me your text to analyze please. ~-~ {say_done_reply}, and my bot brain will get to work."]
    return random.choice(start_message_replies)


def detect_greeting(user_text) -> str:
    unrelated_greetings: list[str] = ["how are you", "how's it going", "what's up", "how's the weather"]
    hello_greetings: list[str] = ["hi", "hello", "hey", "hey there"]

    if user_text in unrelated_greetings or hello_greetings:
        pass  # return to this


def detect_web_link(user_text):
    # code to find url in statement
    def find(string):
        # findall() has been used
        # with valid conditions for urls in string
        regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
        url = re.findall(regex, string)

        urls = [x[0] for x in url]
        # check if urls empty for validation
        for link in urls:
            r = requests.get(link)
            soup = BeautifulSoup(r.content, 'html.parser')
            print(soup.title.string)
        return [x[0] for x in url]



    # Driver Code
    string = 'My Profile: https://auth.geeksforgeeks.org/user/Chinmoy%20Lenka/articles in the portal of https://www.geeksforgeeks.org/'
    print("Urls: ", find(string))


# writes content to file
def write_to_file(file_name: str, new_content: str) -> None:
    f = open(file_name, "a")
    f.write(new_content)
    f.close()


def retrieve_user_content_2():
    detect_web_link("hey")
    source_counter: int = 0

    print(call_bot_reply(), end="")
    print(start_message())
    user_text = input(str(f"{call_user_reply()}"))

    while True:
        # case if user gives empty string or says done with 0 text sent
        if user_text == "" or ((similar(user_text.lower(), "done") == 0.8) and source_counter == 0):
            print(call_bot_reply(), end="")
            print(empty_string())
            user_text = input(str(f"{call_user_reply()}"))

        # user is done and successfully added at least 1 text
        elif (similar(user_text.lower(), "done") >= 0.8) & source_counter > 0:
            break

        # displays message and prompts user to continue adding text
        elif source_counter >= 0 and user_text:
            print(call_bot_reply(), end="")
            print(valid_string(source_counter))
            user_text = input(str(f"{call_user_reply()}"))
            write_to_file(user_content_file, user_text)
            source_counter += 1

        # displays error if all other conditions fail
        else:
            print("Something unexpected occurred.")
            break


def call_user_reply() -> str:
    return "You: "


def call_bot_reply() -> str:
    return "Bot: "


retrieve_user_content_2()


# retrieve_user_content_2()
