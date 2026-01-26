import random


def rock_paper_scissors():
    rock_paper_scissors = ("rock", "paper", "scissors")

    user = rock_paper_scissors[random.randint(0, 2)]
    machine = rock_paper_scissors[random.randint(0, 2)]

    print(f"You: {user}")
    print(f"Machine: {machine}")

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

    if results == 1:
        print("You win!")
    elif results == -1:
        print("Machine wins!")
    else:
        print("Tied")


rock_paper_scissors()
