import random
x = int(input("Guess a number between 0 to 100:"))
# y = random.randint(0,101)
y = 56
count = 1
finish = False
while not finish :
    if x==y: 
        print(f"You Win, and you gussed this number in {count} times")
        finish = True
    else:
        if x > y :
            count += 1
            print("Too High")
            x=int(input("Guess again : "))
        else :
            print("Too Low")
            count += 1
            x=int(input("Guess again : "))