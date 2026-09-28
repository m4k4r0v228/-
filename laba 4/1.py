# TODO решите задачу

import json

def task() -> float:
    with open("input.json") as f:
        data = json.load(f)

    sum = 0

    for item in data:
        sum = sum + item["score"] * item["weight"]
        itog = round(sum, 3)
    return itog

print(task())

