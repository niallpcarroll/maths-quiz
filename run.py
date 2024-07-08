name = input(f"Enter your name here: ")
print("Welcome,", name)
game = input(f"Choose which maths game you would like to play: Addition (+), Subtraction (-), Multiplication (x), Division (/):")
if game == "+":
    print("Let's play an addition game!")
elif game == "-":
    print("Let's play a subtraction game!")
elif game == "x":
    print("Let's play a multiplication game!")
elif game == "/":
    print("Let's play a division game!")
else: print("Please choose a valid game type (+,-,x,/)")            