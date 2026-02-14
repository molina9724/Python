import random


def rock_paper_scissors():

    rounds = 3
    round_counter = 0
    score = {"user": 0, "machine": 0, "ties": 0}

    while round_counter < rounds:
        user = play()
        machine = play()
        print(f"You: {user}")
        print(f"Machine: {machine}")

        my_results = results(user, machine)

        winner(my_results)
        print(f"-----------------")

        history(my_results, score)
        round_counter += 1
    print(history(results, score))


def play():
    rock_paper_scissors = ("rock", "paper", "scissors")
    return rock_paper_scissors[random.randint(0, 2)]


def results(user, machine):
    results = 0

    if user == machine:
        results = 0
    elif user == "rock" and machine == "paper":
        results = -1
    elif user == "rock" and machine == "scissors":
        results = 1
    elif user == "paper" and machine == "rock":
        results = 1
    elif user == "paper" and machine == "scissors":
        results = -1
    elif user == "scissors" and machine == "rock":
        results = -1
    elif user == "scissors" and machine == "paper":
        results = 1
    return results


def history(result, score):
    if result == 1:
        score["user"] += 1
    elif result == 0:
        score["ties"] += 1
    else:
        score["machine"] += 1
    return score


def winner(result):
    if result == 1:
        print("You win!")
    elif result == 0:
        print("Tie")
    else:
        print("Machine wins!")


rock_paper_scissors()
