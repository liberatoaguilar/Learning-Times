import random
lst = ["Bacon", "Bread", "Mac 'n Cheese", "Gummy Worms", "Yellow Pear", "Ricotta Cheese", "Mayo", "Ketchup", "Milk Chocolate", "Chocolate Almonds", "Yogurt", "Bannanas", "Tomatoes", "100 year old eggs", "Cottage Cheese", "Fruit Loops"]
lunch = [lst[0], lst[12], lst[2], lst[5], "Zucchini", "Carrots", "Baby Tomatoes", "Sausage", "Olives", "Coliflour", "Pepperoni", "Pepper"]
app = [lst[1], lst[6], lst[7], lst[14], "Soy Sauce", "Lemon Zest", "Orange Zest", "Saltines", "Tuna", "Tilapia", "Salmon", "Blue Cheese"]
des = [lst[3], lst[4], lst[8], lst[9], lst[10], lst[11], lst[15], "Sour Patch", "Cookie Dough", "Ice Cream", "Mint Leaves", "Gum", "Cinammon Candy"]
spec = ["Stale Bread", "Aggave Syrup", "Warheads", "Cayenne Pepper", "Sardines", "California Reaper", "Cheese Balls", "Ramen Noodles", "Popcorn", "Octopus"]
def choose():
    cho = 1,2,3
    chnum = random.choice(cho)
    specchoice = random.choice(spec)
    if chnum == 1:
        print("LUNCH")
        for i in range(3):
            lunchoice = random.choice(lunch)
            print(lunchoice)
        print(specchoice)
    elif chnum == 2:
        print("APPETIZER")
        for i in range(3):
            appchoice = random.choice(app)
            print(appchoice)
        print(specchoice)
    elif chnum == 3:
        print("DESSERT")
        for i in range(3):
            deschoice = random.choice(des)
            print(deschoice)
        print(specchoice)
choose()
ask = input("So what will you do? ")
numbers = 1,2,3
num = random.choice(numbers)
if num == 1:
    print("Nice!")
elif num == 2:
    print("Sounds Good!")
elif num == 3:
    print("Awesome!")
if ask == "Barf" or ask == "barf":
    print("Ewww, That's gross.")
