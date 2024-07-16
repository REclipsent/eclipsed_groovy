from json import load
from random import choice


def roll_agent(role: str = None):
    with open('./agents.json', 'r') as f:
        json_data = load(f)

    if role is None:
        return choice(json_data)["Name"]

    try:
        role = role[0].lower()

        match role:
            case "c":
                role = "Controller"
            case "d":
                role = "Duelist"
            case "s":
                role = "Sentinel"
            case "i":
                role = "Initiator"
            case _:
                raise ValueError(f"Invalid role: {role}")

        return choice(list(filter(lambda agent: agent["Role"] == role, json_data)))["Name"]
    except IndexError:
        return choice(json_data)["Name"]
    except ValueError:
        return choice(json_data)["Name"]
