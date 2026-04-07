import csv

FILE_NAME = "Files\\test_scores.csv"

def read_csv_file(file_name):
    try:
        with open(file_name, "r", newline="") as file:
            reader = csv.DictReader(file)
            return list(reader)
    except FileNotFoundError:
        print(f"'{file_name}' was not found.")
        return []

def count_name_occurrences(data):
    counts = {}

    for row in data:
        name = row["name"]
        counts[name] = counts.get(name, 0) + 1

    return counts

def test():
    data = read_csv_file(FILE_NAME)
    results = count_name_occurrences(data)
    print(results)

def main():
    test()

main()