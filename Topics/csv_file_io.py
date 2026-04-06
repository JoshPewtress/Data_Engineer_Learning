import csv

FILE_NAME = "Files\\test_scores.csv"

def create_csv_file(file_name, data):
    try:
        with open(file_name, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(data)
            print(f"Path: {file_name} is created.")
    except FileExistsError:
        print(f"Path: {file_name} already exists.")


def test(data):
    print(f"Attempting to create csv file with path {FILE_NAME}")
    create_csv_file(FILE_NAME, data)

def main():
    test_scores = [
        ["name", "score"],
        ["Alice", 85],
        ["Bob", 72],
        ["Charlie", 90],
        ["Alice", 88]
        ]
    test(test_scores)

main()