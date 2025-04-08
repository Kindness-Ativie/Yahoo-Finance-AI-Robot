
# I want cases for each possibility. Then we will run those cases through function.
# possible options: they drop link, they say hi, they request stock ticker, wiki search, web scraper

from english_to_bot import *
from bot_replies import call_bot_reply
from yfinance_actions import asked_bot_term_company

# start series
start_statement: str = "I conduct website analysis and financial analysis. Begin."
call_bot_reply()
print(start_statement)

while True:
    call_user_reply()
    user_input: str = str(input())
    u = user_input

    if not check_existence_of_url(u):
        u = lower_remove_special_char(u)
        # print("Test:", u)

    greeted_bot(u)
    question_greeted_bot(u)
    find_url(u)
    thanked_bot(u)
    said_nothing(u)
    said_goodbye(u)
    asked_bot_term_company(u)

    print("")
