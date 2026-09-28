# TODO импортировать необходимые молули
import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
      # TODO считать содержимое csv файла
    file1 = open(INPUT_FILENAME, "r")
    reader = csv.DictReader(file1, delimiter=",")
    data = []
    for row in reader:
        data.append(row)
    file1.close()
      # TODO Сериализовать в файл с отступами равными 4
    file2 = open(OUTPUT_FILENAME, "w")
    json.dump(data, file2, indent=4)
    file2.close()

if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")

