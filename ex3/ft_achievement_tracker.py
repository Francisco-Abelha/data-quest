import random


def gen_player_achievements() -> set:
    advancements = [
        "Minecraft", "Stone Age", "Getting an Upgrade",
        "Acquire Hardware", "Suit Up", "Hot Stuff",
        "Isn't It Iron Pick", "Not Today, Thank You", "Ice Bucket Challenge",
        "Diamonds!", "We Need to Go Deeper", "Cover Me With Diamonds",
        "Enchanter", "Zombie Doctor", "Eye Spy",
        "The End?", "Return to Sender", "Those Were the Days",
        "Hidden in the Depths", "Subspace Bubble", "A Terrible Fortress",
        "Who is Cutting Onions?", "Oh Shiny", "This Boat Has Legs",
        "Uneasy Alliance", "War Pigs", "Country Lode, Take Me Home",
        "Cover Me in Debris", "Spooky Scary Skeleton", "Into Fire",
        "Not Quite 'Nine' Lives", "Feels Like Home", "Withering Heights",
        "Local Brewery", "Bring Home the Beacon", "A Furious Cocktail",
        "Beaconator", "How Did We Get Here?", "Free the End",
        "The Next Generation", "Remote Getaway", "The End... Again...",
        "You Need a Mint", "Monsters Hunted",
        "The City at the End of the Game",
        "Sky's the Limit", "Great View From Up Here"
    ]
    achievements_list = random.sample(advancements, random.randint(5, 15))
    achievements_set = set(achievements_list)
    return achievements_set


def main():
    print("=== Achievement Tracker System ===")

    alice = gen_player_achievements()
    bob = gen_player_achievements()
    charlie = gen_player_achievements()
    dylan = gen_player_achievements()
    all_achievements = alice.union(bob, dylan, charlie)
    common = alice.intersection(bob, charlie, dylan)

    print(f"Player Alice: {alice}")
    print(f"Player Bob: {bob}")
    print(f"Player Charlie: {charlie}")
    print(f"Player Dylan: {dylan}\n")

    print(f"All distinct Achievements: {all_achievements}\n")

    print(f"Common achievements: {common}\n")

    print(f"Only Alice has: {alice.difference(bob, dylan, charlie)}")
    print(f"Only Bob has: {bob.difference(alice, charlie, dylan)}")
    print(f"Only Charlie has: {charlie.difference(alice, bob, dylan)}")
    print(f"Only Dylan has: {dylan.difference(charlie, alice, bob)}\n")

    print(f"Alice is missing: {all_achievements.difference(alice)}")
    print(f"Bob is missing: {all_achievements.difference(bob)}")
    print(f"Charlie is missing: {all_achievements.difference(charlie)}")
    print(f"Dylan is missing: {all_achievements.difference(dylan)}\n")


if __name__ == "__main__":
    main()
