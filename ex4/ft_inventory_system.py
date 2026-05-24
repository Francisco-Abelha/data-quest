import sys


def parse_args() -> dict:
	inventory = {}
	for arg in sys.argv[1:]:
		try:
			parts = arg.split(":")
			if len(parts) != 2:
				print(f"Error - invalid parameter '{arg}'")
				continue
			item = parts[0]
			if item in inventory:
				print(f"Redundant item '{item}' - discarding")
				continue
			quantity = int(parts[1])
			if quantity < 0:
				print(f"Quantity for {item} can't be negative: {quantity}")
				continue
			inventory.update({item: quantity})
		except ValueError as e:
			print(f"Quantity error for '{item}': {e}")
	return inventory


def main() -> None:
	print("=== Inventory System Analysis ===")
	inventory = parse_args()
	if len(inventory) == 0:
		print("No valid items provided.")
		return
	print(f"Got inventory: {inventory}")
	item_list = list(inventory.keys())
	print(f"Item list: {item_list}")
	total_quantity = sum(inventory.values())
	print(f"Total quantity of the {len(item_list)} items: {total_quantity}")
	most_item, most_qty = None, 0
	least_item, least_qty = None, float('inf')
	for item, quantity in inventory.items():
		percentage = quantity / total_quantity * 100
		print(f"Item {item} represents {percentage:.1f}%")
		if quantity > most_qty:
			most_item = item
			most_qty = quantity
		if quantity < least_qty:
			least_item = item
			least_qty = quantity
	print(f"Item most abundant: {most_item} with quantity {most_qty}")
	print(f"Item least abundant: {least_item} with quantity {least_qty}")
	inventory.update({"magic_item": 1})
	print(f"Updated inventory: {inventory}")


if __name__ == "__main__":
	main()