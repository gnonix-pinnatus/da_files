# No juvenile batfishes allowed.

try:
    age = int(input("Hello, little batfish. How old are you ? "))
    if 0 < age < 1:
        print("You're a little young for these crevices...")
    elif age >= 8:
        print("I'll get your usual sir.")
    elif age <= 0:
        print("You ate too much fugu uh ?")
    else: print("Okay, what can I get you ?")
except ValueError:
    print("Just need a number")
