import random
from book_bot.lexicon.lexicon import LEXICON


def get_bot_choice() -> str:
    return random.choice(['rock', 'paper', 'scissors'])


def normalize_user_answer(user_answer: str) -> str:
    for key in LEXICON:
        if LEXICON[key] == user_answer:
            break
    return key


def get_winner(user_choice: str, bot_choice: str) -> str:
    user_choice = normalize_user_answer(user_choice)
    rules = {'rock': 'scissors',
             'scissors': 'paper',
             'paper': 'rock'}
    if user_choice == bot_choice:
        return 'nobody_won'
    elif rules[user_choice] == bot_choice:
        return 'user_won'
    return 'bot_won'
