import csv

FILE_NAME = "Files\\test_scores.csv"

def read_from_csv(file_name):
    with open(file_name, "r", newline="") as file:
        reader = csv.DictReader(file)
        return list(reader)

def filter_by_score(data):
    filtered_scores = {}
    failed_count = 0

    for row in data:
        name = row["name"]
        score = int(row["score"])
        if score >= 80:
            filtered_scores[name] = max(filtered_scores.get(name, score), score)
        else:
            failed_count += 1
    
    return filtered_scores, failed_count

def save_to_csv(file_name, filtered_scores, failed_count):
    fieldnames = ["name", "score"]

    with open(file_name, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()

        for name, score in filtered_scores.items():
            writer.writerow({"name": name, "score": score})

        writer.writerow({"name": "Number of failing grades", "score": failed_count})

def main():
    data = read_from_csv(FILE_NAME)
    filtered_scores, failed_count = filter_by_score(data)
    save_to_csv("Files\\cleaned.csv", filtered_scores, failed_count)

main()