answer = input("What do you think about 4Chan?")
if len(answer) > 200:
    print("wow, you had a lot to saY about that")
if len(answer) >125:
    print("I didn't know you thought about it that much")
if len(answer) > 50:
    print("I guess that is about right")
if len(answer) >1:
    print("fairly laconic huh?")
else:
    print("Don't want to talk about it huh?")