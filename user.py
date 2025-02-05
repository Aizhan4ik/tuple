#Aizhan Mamatkalykova
import os
os.system('clear' if os.name != 'nt' else 'cls')

user = {
    "What is the user’s name? ": "",
    "What is the user’s age? ": "",
    "What is the user’s country of birth? ": "",
    "What is the user known for? ": ""
}

for question in user:
    user[question] = input(question)

os.system('clear' if os.name != 'nt' else 'cls')

for question, answer in user.items():
    print(f"{question}{answer}")
