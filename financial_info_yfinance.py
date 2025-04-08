import warnings
import yfinance as yf
from company_ticker import ticker_company_pairs
from english_to_bot import lower_remove_special_char, lower_remove_special_char_and_spaces, similar
from bot_replies import call_bot_reply, request_company_name_replies
import re
from datetime import datetime

warnings.simplefilter(action="ignore", category=FutureWarning)  # used to remove future warning when importing yf API

test_string = "coke"
test_string_2 = "Mastercardincorporated show me the day high and day low for visa, discover, and mastercard"
test_string_3 = "pull website and state for apple, microsoft, and alphabet"


# removes endings like "inc." and "company" to match likely user inputs
def remove_ending(full_company_name: str) -> str:
    endings: list[str] = ['incorporated', 'corporation', 'inc', 'company', 'limited', 'incorporated', 'plc', 'holdings', 'holding',
                          'group', 'beverage', 'ltd', 'financial services']

    for ending in endings:
        full_company_name: str = full_company_name.replace(f'{ending}', '')

    return full_company_name


# WE ARE WORKING ON THIS
def check_existence_of_financial_term(user_string) -> list[str]:
    no_special_user_string: str = lower_remove_special_char_and_spaces(user_string)
    # note default ticker is used to generate a list of many financial terms from yfinance API - can be changed
    # when fetch info is called:
    # default ticker will not return error because probability term always returns max probability even if unlikely
    default_ticker: str = 'MSFT'
    yfinance_keys: list[str] = list(yf.Ticker(f'{default_ticker}').info.keys())
    yfinance_objects: list[str] = list(yfinance_properties_dict(f'{default_ticker}').keys())
    financial_term_variations: list[str] = yfinance_keys + yfinance_objects

    user_requested_terms: list[str] = []
    for term in financial_term_variations:
        clean_term = lower_remove_special_char_and_spaces(term)
        if clean_term in no_special_user_string:
            user_requested_terms.append(term)

    return user_requested_terms
    # you want to append this to list, and then later do for term and produce
    # if check for financial term and ______ company name


# grabs time when user requests stock info
def fetch_time() -> str:
    # datetime object containing current date and time
    now = datetime.now()
    # dd/mm/YY H:M:S
    dt_string: str = now.strftime("%m/%d/%Y %H:%M:%S")
    return dt_string


# displays full company name
def full_company_name(ticker: str) -> str:  # pass get_ticker to retrieve full company name
    message: str = f"{yf.Ticker(ticker).info['longName']} - Trading on {yf.Ticker(ticker).info['exchange']} " \
              f"as {yf.Ticker(ticker).info['symbol']} for today {fetch_time()}"

    return message


# you're going to what to put all keys into a list. If user string does not contain key prompt user to ask for analysis
# WE CAN TRY PARSING THE WEBSITE USING WEBSITE LINK

# converts from pascal to normal english
def convert_from_pascal(user_string: str) -> str:
    pattern = re.compile(r'(?<!^)(?=[A-Z])')
    user_string: str = pattern.sub(' ', user_string).lower()
    return user_string


def fetch_finance_term_per_company(user_string: str, user_terms):
    # remember, validate_company_name returns ticker and prints string
    user_words: list[str] = user_string.split()

    companies_in_user_string: list[str] = []

    for word in user_words:
        name_exists = validate_company_name(word, ticker_company_pairs.values(), ticker_company_pairs, ticker_company_pairs.keys())
        if name_exists:
            companies_in_user_string.append(word)
            print(full_company_name(ticker=name_exists))
            for term in user_terms:
                fetch_info(name_exists, term)

        if len(companies_in_user_string) > 0:
            return True



# may produce error with type of return set
# checks for match between user input and company name
def validate_company_name(user_string: str, companies: list[str], whole_dict: dict[str], tickers: list[str]) -> str:
    clean_user: str = lower_remove_special_char(user_string)

    for company in companies:
        clean_company: str = remove_ending(lower_remove_special_char(company))

        # run the same no spaces to check if company name and catch that first.
        if similar(clean_user, clean_company) >= 0.85:
            call_bot_reply()
            request_company_name_replies(company)
            return list(whole_dict.keys())[list(whole_dict.values()).index(company)]

        elif similar(clean_user, clean_company) >= 0.8:
            call_bot_reply()
            request_company_name_replies(company)
            return list(whole_dict.keys())[list(whole_dict.values()).index(company)]

    # REMOVING THIS FOR NOW TO SEE SEARCH - you can check if string is all upper and run that for tickeer instead
    # for ticker in tickers:
    #     if similar(clean_user, lower_remove_special_char(ticker)) >= 0.9:
    #         call_bot_reply()
    #         request_company_name_replies(company_name=whole_dict[ticker])
    #         print(f"TEST: I matched through option 3 using user {clean_user}")
    #         return ticker


# fwi try and find the attribute error for objects that don't work
# stores the yfinance objects - accessed when can't be taken from the dictionary
def yfinance_properties_dict(ticker: str):
    yfinance_properties: dict = {
        'dividends': yf.Ticker(ticker).dividends,
        'cash_flow': yf.Ticker(ticker).cash_flow,
        'balance_sheet': yf.Ticker(ticker).balance_sheet,
        # 'earnings': yf.Ticker(ticker).earnings,
        'actions': yf.Ticker(ticker).actions,
        # 'analyst_price_target': yf.Ticker(ticker).analyst_price_target,
        'balanceSheet': yf.Ticker(ticker).balancesheet,
        'basic_info': yf.Ticker(ticker).basic_info,
        'capital_gains': yf.Ticker(ticker).capital_gains,
        'cashflow': yf.Ticker(ticker).cashflow,
        # 'earnings_forecast': yf.Ticker(ticker).earnings_forecasts,
    }

    return yfinance_properties


# grabs financial term info for requested company name
def fetch_info(ticker: str, financial_term: str):
    threshold = 0.7  # sets match strength

    # checking yf dictionary for the term
    yfinance_keys: list[str] = list(yf.Ticker(ticker).info.keys())  # fetches keys from yf API
    probability_of_match: list[float] = []  # holds match strength for each term based on user input
    for _ in yfinance_keys:
        probability_of_match.append(similar(financial_term, _))
    highest_probability: float = max(probability_of_match)

    if highest_probability >= threshold:
        idx: int = probability_of_match.index(highest_probability)
        requested_financial_info: str = yfinance_keys[idx]
        # watch out for this in the future
        try:
            print(f"{convert_from_pascal(requested_financial_info)}: {yf.Ticker(ticker).info[f'{requested_financial_info}']}")
        except Exception as e:
            print("Can't grab this")
            print(e)

    # checking ticker object attributes for the term
    else:
        probability_of_match.clear()  # rest probability of match for manual dictionary
        yfinance_keys: list[str] = list(yfinance_properties_dict(ticker).keys())  # fetches keys from manual dictionary
        for _ in yfinance_keys:
            probability_of_match.append(similar(financial_term, _))
        highest_probability: float = max(probability_of_match)
        idx: int = probability_of_match.index(highest_probability)
        requested_financial_info: str = yfinance_keys[idx]
        print(f"{convert_from_pascal(requested_financial_info)}: {yfinance_properties_dict(ticker).get(requested_financial_info)}", end=" ")





print("TEST 1")
# company_term_find_2(test_string_2)
# check_existence_of_financial_term(test_string_2)
fetch_finance_term_per_company(test_string_2, check_existence_of_financial_term(test_string_2))


# fetch_info(company_term_find_2(test_string_2), "equity")
# remember that sometimes a term may be similar to a company, what will you do in this scenario?


# remove spaces from user string, remove spaces from terms and names to see if term or name is there
# if user input contains similar to company and financial term
# if user input not similar to company but contains financial term
# if user input contains datetime financial temrm



