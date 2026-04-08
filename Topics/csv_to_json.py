import csv, json

FILE_NAME = "Files\\cleaned.csv"

def read_from_csv(file_name):
    with open(file_name, "r", newline="") as file:
        reader = csv.DictReader(file)
        return list(reader)

def transform_to_students(data):
    students = []

    for row in data:
        if row["name"] == "Number of failing grades":
            continue

        students.append({
            "name": row["name"],
            "score": int(row["score"])
        })

    return {"students": students}

def write_to_json(file_name, data):
    with open(file_name, "w") as file:
        json.dump(data, file, indent=4)

def main():
    data = read_from_csv(FILE_NAME)
    students_list = transform_to_students(data)
    write_to_json("Files\\output.json",students_list)

main()