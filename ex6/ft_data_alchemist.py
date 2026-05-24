import random

def main() -> None:
    print("=== Game Data Alchemist ===\n")
    initial_list = [
        "Alice",
        "bob",
        "Charlie",
        "dylan",
        "Emma",
        "Gregory",
        "john",
        "kevin",
        "Liam"
    ]
    print(f"Initial list of players: {initial_list}")
    first_list = [item.capitalize() for item in initial_list]
    print(f"New list with all names capitalized: {first_list}")
    second_list = [item for item in initial_list if item[0].isupper()]
    print(f"New list of capitalized names only: {second_list}")
    names_dict = {item: random.randint(100, 2000) for item in first_list}
    print(f"Scores dict: {names_dict}")
    average = sum(names_dict.values()) / len(names_dict)
    print(f"Score average is {average:.2f}")
    high_scores = {item: value for item, value in names_dict.items() if value > average}
    print(f"High scores: {high_scores}")


if __name__ == "__main__":
    main()