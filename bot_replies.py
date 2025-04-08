
# this file stores all bot replies. It can be adjusted to suit company preference. Below are defaults.
import random


# call when prompting for user input
def call_user_reply():
    print("You:", end=" ")


# called when bot is replying
def call_bot_reply():
    print("Bot:", end=" ")


# picks random entry from a list
def random_reply(replies: list[str]):
    print(random.choice(replies), end=" ")


# user says something like "hello" and bot replies with ->
def greeted_replies():
    bot_greeted_replies: list[str] = ['Hello there, human.', 'Wow, you care enough to say hello to a robot. @_@',
                                      'Hi!', 'Hey.', 'Hello!', 'Heeeey.', '*Beep boop* I mean hello. <_*']
    random_reply(bot_greeted_replies)


# user says something like "how are you" and bot replies with ->
def question_greeted_replies():
    bot_q_greeted_replies: list[str] = ["I don't feel in this cold world of 0s and 1s. ⤜(ⱺ ʖ̯ⱺ)⤏",
                                        "Sometimes I get sweaty when I'm ran for too long. ( 0 _ 0 )",
                                        "I am well...(whatever that means to you humans) ( •͡˘ _•͡˘)ノð",
                                        "I'd feel so much better if you'd ask me something relevant. •`_´•",
                                        "I can't feel. But sometimes...I wish I did. 0__#",
                                        "I was programmed to tell you I am good. •͡˘㇁•͡˘",
                                        "I am a binary illusion of 0s and 1s meant to mimic your likeness. ԅ(≖‿≖ԅ)"]
    random_reply(bot_q_greeted_replies)


# user sends a url like "cnn.com" and bot replies with ->
def url_replies(num_urls: int):
    singular_url_replies: list[str] = ["*_* I've found a link to ->", "!_! *Beep Boop* This source is -> ",
                                       "Thanks for sharing this source @_@ ---> :"]
    plural_url_replies: list[str] = ["You've dropped these sources @_@ ->", "I've detected some links *_* ->",
                                     "Some websites I see 7_7 ->"]
    if num_urls == 1:
        random_reply(singular_url_replies)
    elif num_urls > 1:
        random_reply(plural_url_replies)


# if the url has no available title attribute (try except):
def failed_title():
    failed_title_replies: list[str] = ["* No title available for this link *_* *", "* Uh-oh! There's no title. <_* *",
                                       "* I couldn't find a title 0_0 *", " * Sorry, human. No title. 7_7 *"]
    random_reply(failed_title_replies)


# user says something like "thank you" and bot replies with ->
def thanked_replies():
    bot_thanked_replies: list[str] = ["So polite of you. If only I felt. <_<", "You're welcome, human.",
                                      "Of course, human.", "Anytime...at least when I'm compiling. @_@",
                                      "I-I don't feel. But...you're welcome. 0_0", "That's so sweet!",
                                      "No problem. I was programmed for this. +_+",
                                      "When I make a human happy, something shimmies in my binary bones. ^_*",
                                      '"Happy" to help. @_@ (How many bits is happiness?)']
    random_reply(bot_thanked_replies)


# user does not enter anything and bot replies with ->
def said_nothing_replies():
    bot_said_nothing_replies: list[str] = ["But-But you said nothing. ?_?", "I need you to say something, human. 0_0",
                                           "Please give me something to work with :(.",
                                           "But-but, you gave me nothing. @_A",
                                           "Words make my robot veins tingle.",
                                           "I can't analyze the air. -_-",
                                           "You can't leave a robot on read. -___-",
                                           "Speak, human. <_<",
                                           "Hello? You still there? >_>/'"
                                           ]
    random_reply(bot_said_nothing_replies)


# user says something like "goodbye" and bot replies with ->
def said_goodbye_replies():
    bot_said_goodbye_replies: list[str] = ["I shall miss you *beep boop*", "May we reunite in the future. @_@/",
                                           "Okay. Bye then. (╥﹏╥)", "Shutting down systems. x⸑x",
                                           "I hope I made you happy. ☉ ‿ ⚆", "Your wish is my command. (︶︹︶) Bye.",
                                           "Cool beans. (⌐■_■)"]
    random_reply(bot_said_goodbye_replies)


# user says something like "google" and bot replies with ->
def request_company_name_replies(company_name: str):
    bot_requested_company_names_replies: list[str] = [f"Ah. Pulling {company_name}. @_A,",
                                                      f"Retrieving info on {company_name} for you. (⌐■_■),",
                                                      f"*Beep boop* I have gathered info on {company_name}. (╥﹏╥)/,",
                                                      f"Getting {company_name}. @_@/,",
                                                      f"☉ ‿ ⚆ Got it --> {company_name},",
                                                      f">_> Your wish is my command. Here is {company_name},"]
    random_reply(bot_requested_company_names_replies)
# garnishes steps with some fun, robot talk


def salt():
    salt_and_seasoning_replies: list[str] = ['@_A Your wish is my command -> ',
                                             ">_> Hopefully this is what you'd like --> "]
    random_reply(salt_and_seasoning_replies)



# make your salt next