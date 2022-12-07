import random
x = int(input("Guess a number between 0 to 100:"))
# y = random.randint(0,101)
y = 56
count = 1
while True :
    if x==y: 
        print(f"You Win, and you gussed this number in {count} times")
        break
    else:
        if x > y :
            print("Too High")
        else :
            print("Too Low")
        count += 1
        x=int(input("Guess again : "))