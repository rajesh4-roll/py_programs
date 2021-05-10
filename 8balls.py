"""
Simulates a magic eight ball.
Prompts the user to type a yes or no question and gives
a random answer from a set of prefabricated responses.
"""

import random

def ret(num):
    if num == 1:
        print("As I see it,yes.")
    if num == 2:
        print("As I again later.")
    if num == 3:
        print("Better not to tell you now.")
    if num == 4:
        print("Cannot predict now.")
    if num == 5:
        print("Concentrate and ask again.")
    if num == 6:
        print("Don't count on it. ")
    if num == 7:
        print("It is certain.")
    if num == 8:
        print("It is decidedly so.")
    if num == 9:
        print("Most likely.")
    if num == 10:
        print("My reply is no. ")
    if num == 11:
        print("My sources say no.")
    if num == 12:
        print("Outlook not so good.")
    if num == 13:
        print("Outlook good. ")
    if num == 14:
        print("Reply hazy, try again.")
    if num == 15:
        print("Signs point to yes.")
    if num == 16:
        print("Very doubtful.")
    if num == 17:
        print("Without a doubt.")
    if num == 18:
        print("Yes.")
    if num == 19:
        print("Yes - definitely. ")
    if num == 20:
        print("You may rely on it.")
    


def main():
    # Fill this function out!
    aks = input("Ask a yes or no question: ")
    ret(random.randint(1,20))



if __name__ == "__main__":
    main()