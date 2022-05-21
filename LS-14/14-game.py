from game_data import data
from random import randint
from art import logo, vs

score = 0

def who_is_the_person(data):
    person_a = randint(0, len(data)-1)
    person_b = randint(0, len(data)-1)
    while person_a == person_b:
        person_b = randint(0, len(data)-1)
    print(logo)
    print(f"Compare A: {readable_format(person_a)}.")
    print(vs)
    print(f"Against B: {readable_format(person_b)}.")
    return person_a, person_b

def readable_format(person):
    return f"{data[person]['name']}, a {data[person]['description']}, from {data[person]['country']}"


def user_choice(person_a, person_b):
    user_choice = input("Who has more followers? Type 'A' or 'B': ")
    if user_choice == 'A':
        user_choice = person_a
    else:
        user_choice = person_b
    return user_choice


def subscribers_compare(data, person_a, person_b, user_choice, score):
    sub_a = data[person_a]["follower_count"]
    sub_b = data[person_b]["follower_count"]
    if (sub_a > sub_b and user_choice == person_a) or (sub_a < sub_b and user_choice == person_b):
        score += 1
        print(f"You are right! Your score is {score}")
        return score
    else:
        print(f"You are wrong! Your final score is {score}")
        exit()


while True:
    person_a, person_b = who_is_the_person(data)
    choice = user_choice(person_a, person_b)
    score = subscribers_compare(data, person_a, person_b, choice, score)