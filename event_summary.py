import csv


def open_csv(file_name):
    with open(file_name + ".csv") as f:

        reader = csv.reader(f)

        values = []
        for row in reader:
            values.append(row)
    return values


def event_judgement(answer, question):
    if answer == question:
        print(f"{answer}と{question}は一致しました")
        
    else:
        print(f"{answer}と{question}は不一致です")


