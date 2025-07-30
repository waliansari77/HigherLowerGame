from random import choice
from game_data import data
from art import logo, vs

print(logo)

def random_item():
    item = choice(data)
    return item

def format_data(account):
    account_name = account['name']
    account_description = account['description']
    account_country = account['country']
    return f"{account_name}, a {account_description}, from {account_country}"

score = 0
optionA = random_item()

should_continue = True
while should_continue:
    optionB = random_item()
    if optionA == optionB:
        optionB = random_item()

    print(f"CompareA: {format_data(optionA)}")
    print(vs)
    print(f"AgainstB: {format_data(optionB)}")
    user_guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    #Clear the screen
    print("\n" *20)
    print(logo)

    if user_guess == "a" and optionA['followers_count'] > optionB['followers_count']:
        score += 1
        print("you are right! your current score is", score)
    elif user_guess == "b" and optionB['followers_count'] > optionA['followers_count']:
        score += 1
        print("you are right! your current score is", score)
        optionA = optionB
    elif optionA['followers_count'] == optionB['followers_count']:
        score = score
        print("you are right! your current score is", score)
    else:
        print("sorry, that's wrong your final score is", score)
        should_continue = False


