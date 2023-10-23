import csv

def open_csv(file_name):
    with open(file_name + ".csv") as f:

        reader = csv.reader(f)

        values = []
        for row in reader:
            values.append(row)
    return values


x = open_csv("question")
print(x)
