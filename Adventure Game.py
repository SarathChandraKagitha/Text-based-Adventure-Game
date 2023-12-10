import time
import random

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []

    def display_stats(self):
        print(f"\n{name}'s Health: {self.health}")
        print("Inventory:", ', '.join(self.inventory))

def introduction():
    print("Welcome to the Adventure Game!")
    time.sleep(1)
    print("You are a brave hero on a quest to rescue the kidnapped princess.")
    time.sleep(1)
    print("Your journey begins in the small village of Rivertown.")
    time.sleep(1)

def make_choice(options):
    print("\nChoose your action:")
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")
    choice = int(input("Enter the number of your choice: "))
    return choice

def explore_village(player):
    print("\nYou start exploring the village of Rivertown.")
    time.sleep(1)
    print("You come across a market, a blacksmith, and an old tavern.")

    choices = ["Visit the market", "Go to the blacksmith", "Enter the tavern"]
    choice = make_choice(choices)

    if choice == 1:
        print("\nYou visit the market and buy some supplies.")
        player.inventory.append("Health Potion")
    elif choice == 2:
        print("\nThe blacksmith gives you a sword to aid in your quest.")
        player.inventory.append("Sword")
    else:
        print("\nIn the tavern, you hear rumors about the princess's location.")
        time.sleep(1)
        print("What do you do?")
        choices = ["Listen to rumors", "Challenge someone to a duel"]
        choice = make_choice(choices)

        if choice == 1:
            print("\nThe rumors hint at a dark cave to the north.")
            return True
        else:
            print("\nA brawl ensues, and you lose some health.")
            player.health -= 10

    return False

def enter_cave(player):
    print("\nYou decide to follow the rumors and head towards the dark cave.")
    time.sleep(1)
    print("Inside the cave, you encounter a fork in the path.")

    choices = ["Take the left path", "Take the right path"]
    choice = make_choice(choices)

    if choice == 1:
        print("\nYou take the left path and encounter a group of bandits.")
        time.sleep(1)
        print("What do you do?")
        choices = ["Fight the bandits", "Try to sneak past them"]
        choice = make_choice(choices)

        if choice == 1:
            print("\nYou engage in a fierce battle with the bandits.")
            if "Sword" in player.inventory:
                print("Having a sword, you manage to defeat them.")
            else:
                print("Without a proper weapon, the bandits overpower you.")
                player.health -= 30
        else:
            print("\nYou attempt to sneak past the bandits.")
            success = random.choice([True, False])
            if success:
                print("You successfully sneak past them.")
            else:
                print("The bandits spot you and demand a toll.")
                player.inventory.append("Gold Coin")

    else:
        print("\nYou take the right path and encounter a mystical creature.")
        time.sleep(1)
        print("What do you do?")
        choices = ["Attempt to communicate", "Attack"]
        choice = make_choice(choices)

        if choice == 1:
            print("\nThe creature seems friendly and guides you deeper into the cave.")
        else:
            print("\nThe creature retaliates, and you lose some health.")
            player.health -= 20

    return player.health > 0

def rescue_princess(player):
    print("\nAs you venture deeper into the cave, you discover the kidnapped princess!")
    time.sleep(1)
    print("Congratulations! You have successfully rescued the princess.")

def main():
    introduction()

    player_name = input("Enter your hero's name: ")
    player = Player(player_name)

    if explore_village(player):
        if enter_cave(player):
            rescue_princess(player)
            print("You have completed your quest and saved the day!")
        else:
            print("\nYour journey ends in defeat.")
    else:
        print("\nYour adventure in Rivertown concludes.")

if __name__ == "__main__":
    main()
