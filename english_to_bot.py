# this contains the methodologies for converting english to bot.
# all of these should return bools
from difflib import SequenceMatcher
from bot_replies import *
import re
from bs4 import BeautifulSoup
import requests

# have a general function that contains the code for the comment below def greeted_bot you will also pass the list
# is the above use of a decorator? We shall see.
# reply structure should be in ifs because user can also greet and then ask for knowledge of some variety
# remember to lower usertext and remove special characters (function) then you can start calling bot replies over
# maybe as last default append all possible variation lists into one list, have robot figure out what it's saying
# and deliver all

# TEST mimics user input for testing purposes
test_user_text = "hi!!"


# removes special characters and lowers user input (cleans)
def lower_remove_special_char(user_string) -> str:
    no_special_char = re.sub('[^A-Za-z0-9 ]+', '', user_string)
    no_special_char = no_special_char.lower()
    return no_special_char


def lower_remove_special_char_and_spaces(user_string) -> str:
    no_special_char_spaces = re.sub('[^A-Za-z0-9]+', '', user_string)
    no_special_char_spaces = no_special_char_spaces.lower()
    return no_special_char_spaces


def check_existence_of_url(string) -> list[str]:
    regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
    url = re.findall(regex, string)

    urls = [x[0] for x in url]
    return urls


# clean version of user input
# if not check_existence_of_url(test_user_text):
    # test_user_text = lower_remove_special_char(test_user_text)


# shows ratio of similarity between strings
def similar(a, b) -> float:
    return SequenceMatcher(None, a, b).ratio()


# translates what user is saying into bot form
def validate_user_input(user_string: str, possible_variations: list[str]):
    for variation in possible_variations:
        if similar(user_string, variation) >= 0.4 and variation in user_string:
            # print("I found this through option 1") -TEST
            return True
        elif similar(user_string, variation) >= 0.85:
            # print("I found this through option 2") - TEST
            return True


# below are translators for different scenarios. The _variations may be altered to simulate what a human would say
# *Note: Words with apostrophes may have them omitted because special characters are removed upon user input

# checks if user says something like "hello"
def greeted_bot(user_string: str):
    hello_variations: list[str] = ['hi', 'hello', 'hey', 'hey there', 'hi there', 'hello there']  # make list
    if validate_user_input(user_string, hello_variations):  # validate list
        call_bot_reply()  # print "Bot: "
        greeted_replies()  # grab relevant reply


# checks if user says something like "how are you"
def question_greeted_bot(user_string: str):
    question_greeting_variations: list[str] = ['how are you', 'how are you doing', 'are you well',
                                               'how are you feeling', 'howre you robot',
                                               'howre you doing', 'hows it going', 'hows the weather', 'whats up']
    if validate_user_input(user_string, question_greeting_variations):
        call_bot_reply()
        question_greeted_replies()


# code to find url in statement
def find_url(string):
    urls = check_existence_of_url(string)
    # check if urls empty for validation
    if len(urls):
        call_bot_reply()
        url_replies(len(urls))

    for link in urls:
        r = requests.get(link)
        soup = BeautifulSoup(r.content, 'html.parser')
        try:
            print(soup.title.string, end="; ")
        except AttributeError:
            failed_title()
        # out = ','.join(list) - to try and make the list output cleaner
        # if url returns none what shall you do. Catch that exception.


# user says something like "thank you"
def thanked_bot(user_string: str):
    thanks_variations: list[str] = ['thank you', 'thanks', 'cool', 'nice', 'awesome', 'great', 'nice job',
                                    'thank you so much', 'thank you robot', 'thanks robot']
    if validate_user_input(user_string, thanks_variations):
        call_bot_reply()
        thanked_replies()


def said_nothing(user_string: str):
    if not user_string:
        call_bot_reply()
        said_nothing_replies()


def said_goodbye(user_string: str):
    bye_variations: list[str] = ['done', 'im done', 'goodbye', 'bye', 'goodbye, robot', 'see you later', 'see you',
                                 'later', 'later, robot', 'farewell', 'take care', 'im finished', 'finished',
                                 'exit', 'complete']
    if validate_user_input(user_string, bye_variations):
        call_bot_reply()
        said_goodbye_replies()
        exit(0)
# greeted_bot(test_user_text)
# question_greeted_bot(test_user_text)
# find_url(test_user_text)

# things to do put print. random into function, and make salt for bot replies, create function to clean lower text
# fwi web parser may be in a whole different file as well as yf api and other tools.
# retrieve the tags from the page and then teach the program to find the classes...
# lower, similar, retrieve (maybe find Excel file of fortune 500 list with tickers and do work with that)
# do bot to english for empty string
# algorithm for companies is if above 0.9 match first, then if not "I'm not too sure" and pull max instead (time)
# you've pulled several items for this analysis: wiki summary, web page, and stock info if validated append
# code to list to see what user did for that set of queries, that way we keep track while program is running
# kind of like did they ask this already
