import json
# TODO решите задачу
def task() -> float:

    with open("input.json") as file:
        data = json.load(file)

    list_of_multiplications = [(i["score"] * i["weight"]) for i in data]

    return round(sum(list_of_multiplications), 3)


print(task())
