import sys


class ParameterError(Exception):
    def __init__(self, parameter: str):
        super().__init__(f"Error - invalid parameter '{parameter}'")


class RedundancyError(Exception):
    def __init__(self, item: str):
        super().__init__(f"Redundant item '{item}' - discarding")


def valid_input(inventory: dict[str, int], arg: str) -> None:
    if ":" not in arg:
        raise ParameterError(arg)
        return
    item, quantity = arg.split(":")
    if item in inventory:
        raise RedundancyError(item)
        return
    try:
        int(quantity)
    except ValueError as error:
        raise ValueError(f"Quantity error for '{item}': {error}")


def fill_inventory(argc: int, argv: list[str]) -> dict[str, int]:
    inventory: dict[str, int] = {}
    for i in range(1, argc):
        try:
            valid_input(inventory, argv[i])
        except ParameterError as error:
            print(error)
        except RedundancyError as error:
            print(error)
        except ValueError as error:
            print(error)
        else:
            item, quantity = argv[i].split(":")
            inventory.update({item: int(quantity)})
        finally:
            i += 1
    return inventory


def get_items(inventory: dict[str, int]) -> list[str]:
    return list(inventory.keys())


def get_num_items(inventory: dict[str, int]) -> int:
    return len(inventory)


def get_quantity(inventory: dict[str, int]) -> int:
    return sum(inventory.values())


def get_percent(inventory: dict[str, int], item: str) -> float:
    return round(100 / get_quantity(inventory) * inventory[item], 1)


def get_most_abundant(inventory: dict[str, int]) -> None:
    max_quant = max(inventory.values())
    most_items = []
    for item, quantity in inventory.items():
        if quantity == max_quant:
            most_items.append(item)
    for item in most_items:
        print(f"Item most abundant: {item} with quantity of {max_quant}")


def get_least_abundant(inventory: dict[str, int]) -> None:
    min_quant = min(inventory.values())
    least_items = []
    for item, quantity in inventory.items():
        if quantity == min_quant:
            least_items.append(item)
    for item in least_items:
        print(f"Item least abundant: {item} with quantity of {min_quant}")


def main() -> None:
    argv = sys.argv
    argc = len(argv)
    print("=== Inventory System Analysis ===")
    inventory = fill_inventory(argc, argv)
    items = get_items(inventory)
    print(f"Got inventory: {inventory}")
    print(f"Item list: {items}")
    print(
          f"Total quantity of the {get_num_items(inventory)} "
          f"items: {get_quantity(inventory)}"
         )
    for item in items:
        print(f"Item {item} represents {get_percent(inventory, item)}%")
    get_most_abundant(inventory)
    get_least_abundant(inventory)
    inventory.update({"magic_item": 1})
    print(f"Updated inventory: {inventory}")


if __name__ == "__main__":
    main()
