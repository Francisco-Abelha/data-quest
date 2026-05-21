import sys


def main() -> None:
    print("=== Command Quest ===")
    print(f"Program name: {sys.argv[0]}")
    num_args = len(sys.argv) - 1
    if (num_args == 0):
        print("No arguments provided!")
    else:
        print(f"Arguments received: {num_args}")
        i = 1
        while (i <= num_args):
            print(f"Argument {i}: {sys.argv[i]}")
            i += 1
    print(f"Total arguments: {num_args + 1}")


if __name__ == "__main__":
    main()
