import csv


def open_csv(file_name):
    """_summary_

    Args:
        file_name:ファイル名を入力する

    Returns:
        ファイル内の値を配列で返す
    """
    with open(file_name + ".csv") as f:

        reader = csv.reader(f)

        values = []
        for row in reader:
            values.append(row)
    return values


def event_judgement(answer, question):
    """_summary_

    Args:
        answer: 入力値を格納
        question: 問題文を格納
    """
    if answer == question:
        print(f"{answer}と{question}は一致しました")
        
    else:
        print(f"{answer}と{question}は不一致です")