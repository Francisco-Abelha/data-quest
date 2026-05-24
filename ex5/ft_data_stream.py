import typing
import random


def gen_event() -> typing.Generator[tuple, None, None]:
	player = [
		"Alice",
		"Bob",
		"Charlie",
		"Dylan"
	]
	actions = [
		"Move",
		"Jump",
		"Crouch",
		"Vault",
		"Attack",
		"Defend",
		"Shield",
		"Heal"
	]
	while True:
		pair = (random.choice(player), random.choice(actions))
		yield pair


def consume_event(events_list: list) -> typing.Generator[tuple, None, None]:
	while events_list:
		element = random.choice(events_list)
		events_list.remove(element)
		yield element


def main() -> None:
	print("=== Game Data Stream Processor ===")
	event = gen_event()
	count = 0
	while count < 1000:
		name, action = next(event)
		print(f"Event {count}: Player {name} did action {action}")
		count += 1
	events_list = [next(event) for _ in range(10)]
	print(f"Built list of 10 events: {events_list}")
	for item in consume_event(events_list):
		print(f"Got event from list: {item}")
		print(f"Remains in list: {events_list}")


if __name__ == "__main__":
	main()