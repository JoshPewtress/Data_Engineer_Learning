# 🏁 Starting Off: Python Foundations and Data Processing

## 📌 Overview

> This section focuses on building foundational Python skills and applying them to basic data processing tasks.  
> The goal is to move from simple scripting toward building small, structured data pipelines by combining reusable patterns into complete workflows.

---

## 📚 Table of Contents

- [Project Structure](#-project-structure)
- [Learning Blocks](#-learning-blocks)
    - [Block 1: Fundamentals — Data Processing](#block-1-fundamentals--data-processing)
    - [Block 2: API Data Ingestion](#block-2-api-data-ingestion)
- [Concepts Reinforced](#-concepts-reinforced)
- [Notes for Future Me](#-notes-for-future-me)

---

<a id="-project-structure"></a>
<details>
<summary>📁 Project Structure</summary>
<br>

```text
DATA_ENGINEER_LEARNING/
│
├── python/
│   ├── fundamentals_data_processing/
│   │   ├── even_odd_split.py
│   │   ├── count_name_occurrences.py
│   │   ├── write_csv.py
│   │   ├── read_csv_and_count.py
│   │   ├── filter_scores_and_write_csv.py
│   │   ├── convert_csv_to_json.py
│   │   └── student_data_pipeline.py
│   │
│   └── api_data_ingestion/
│       ├── simple_request.py
│       └── get_pokemon_data.py
│
├── data/
│   ├── raw/
│   │   └── test_scores.csv
│   ├── processed/
│   │   ├── cleaned.csv
│   │   └── output.json
│   └── outputs/
│       └── summary.json
│
├── .gitignore
└── README.md
```
</details>

---

<a id="-learning-blocks"></a>
## 🧱 Learning Blocks

<a id="block-1-fundamentals--data-processing"></a>
<details>
<summary><strong>Block 1: Fundamentals — Data Processing 🟩</strong></summary>
<br>

> This block focuses on core Python concepts applied to structured data workflows.

> It covers:
> - Iteration and conditional logic
> - Data aggregation with dictionaries
> - Reading and writing CSV files
> - Data cleaning and transformation
> - Converting structured data to JSON
> - Building a complete data pipeline
<br>

---

<details>
<summary><strong>🔹 Working with Lists, Loops, and Conditionals</strong></summary>
<br>

**Script**  
- [View even/odd split implementation](./python/fundamentals_data_processing/even_odd_split.py)

**Purpose**:  
Learn how to iterate through a list and apply conditional logic to categorize data.

**What I Built**  
A function that separates a list of numbers into:
- even numbers
- odd numbers

**Key Takeaways**
- Using `%` (modulo) to determine even vs odd
- Iterating through lists with `for` loops
- Building new lists based on conditions
- Returning multiple values from a function

**Quick Reference**
```python
def sort_by_even_odd(numbers):
    even_numbers = []
    odd_numbers = []

    for num in numbers:
        if num % 2 == 0:
            even_numbers.append(num)
        else:
            odd_numbers.append(num)

    return even_numbers, odd_numbers
```

**Example Usage**
```python
numbers = [12, 47, 83, 29, 5, 64]
even, odd = sort_by_even_odd(numbers)

print(even)   # [12, 64]
print(odd)    # [47, 83, 29, 5]
```
</details>

---

<details>
<summary><strong>🔹 Using Dictionaries for Counting & Aggregation</strong></summary>
<br>

**Script**  
- [View name counting implementation](./python/fundamentals_data_processing/count_name_occurrences.py)

**Purpose**  
Learn how to count occurrences of items using dictionaries.

**What I Built**  
A function that counts how many times each name appears in a list.

**Key Takeaways**  
- Dictionaries are ideal for tracking frequency
- `.get(key, default)` avoids key errors and simplifies counting
- Pattern: *check* → *increment* → *store*
- This pattern is widely used in data processing and analytics

**Quick Reference**

```python
def count_duplicate_names(names):
    output = {}

    for name in names:
        output[name] = output.get(name, 0) + 1

    return output
```

**Example Usage**
```python
names = ["Alice", "Bob", "Alice", "Charlie", "Bob", "Alice"]
counts = count_duplicate_names(names)

print(counts)    # {'Alice': 3, 'Bob': 2, 'Charlie': 1}
```
</details>

---

<details>
<summary><strong>🔹 Reading and Writing CSV Files</strong></summary>
<br>

**Script**  
- [View CSV writing implementation](./python/fundamentals_data_processing/write_csv.py)
- [View CSV reading/count implementation](./python/fundamentals_data_processing/read_csv_and_count.py)

**Purpose**  
Learn how to create, read, and process structured data using CSV files.

**What I Built**  
Two scripts:
1. **CSV Writer**
    - Creates a CSV file from structured data
2. **CSV Reader + Processor**
    - Reads the CSV
    - Converts rows into dictionaries
    - Counts occurrences of names

**Key Takeaways**  
- How to write CSV files using `csv.writer`
- How to read CSV files using `csv.DictReader`
- CSV data is read as **strings by default**
- Separating file creation from processing improves clarity
- Reusing earlier patterns (dictionary counting) on file data

**Quick Reference — Writing CSV**
```python
import csv

with open(file_name, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)
```

**Quick Reference — Reading CSV**
```python
import csv

with open(file_name, "r", newline="") as file:
    reader = csv.DictReader(file)
    data = list(reader)
```
</details>

---

<details>
<summary><strong>🔹 Filtering and Cleaning Data</strong></summary>
<br>

**Script**  
- [View score filtering implementation](./python/fundamentals_data_processing/filter_scores_and_write_csv.py)

**Purpose**  
Learn how to filter records, remove unwanted data, and preserve the most useful version of repeated entries.

**What I Built**  
A script that:
- reads student scores from a CSV file
- keeps only scores greater than or equal to 80
- keeps the highest passing score for duplicate student names
- counts how many failing grades were removed
- writes the cleaned results to a new CSV file

**Key Takeaways**  
- Filtering rows based on conditions
- Converting CSV string values into integers before comparison
- Using dictionaries to collapse duplicate records
- Using `max()` to preserve the highest value for repeated names
- Writing cleaned data back to a CSV file

**Quick Reference**
```python
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
```
</details>

---

<details>
<summary><strong>🔹 Converting Cleaned Data to JSON</strong></summary>
<br>

**Script**  
- [View CSV to JSON conversion implementation](./python/fundamentals_data_processing/convert_csv_to_json.py)

**Purpose**  
Learn how to transform cleaned CSV data into a structured JSON format for downstream use.

**What I Built**  
A script that:
- reads cleaned student data from a CSV file
- skips non-student summary rows
- converts each student into a dictionary
- stores the result under a `"students"` key
- writes the final structure to a JSON file

**Key Takeaways**  
- JSON is useful for storing structured, nested data
- `json.dump()` writes Python dictionaries and lists to JSON
- CSV data often needs additional cleanup before transformation
- upstream design decisions can affect downstream processing

**Quick Reference**
```python
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
```

**Example Output**
```json
{
    "students": [
        {
            "name": "Alice",
            "score": 88
        },
        {
            "name": "Charlie",
            "score": 90
        }
    ]
}
```
</details>

---

<details>
<summary><strong>🔹 Building a Complete Data Pipeline ⚡</strong></summary>
<br>

**Script**  
- [View full data pipeline implementation](./python/fundamentals_data_processing/student_data_pipeline.py)

**Purpose**  
Combine earlier concepts into a single workflow that reads raw CSV data, filters passing scores, aggregates results, and writes a structured JSON summary.

**What I Built**  
A script that:
- reads student score data from a CSV file
- filters out scores below a passing threshold
- counts how many passing records each student has
- calculates total passing records
- calculates the number of unique passing students
- writes the final summary to a JSON file

**Key Takeaways**  
- Chaining functions together into a complete workflow
- Separating reading, filtering, transforming, and writing into distinct steps
- Using dictionaries to aggregate results
- Designing structured JSON output for summaries
- Reusing earlier patterns in a larger program

**Quick Reference**  
```python
def transform_to_dictionary(data):
    counts = {}

    for row in data:
        name = row["name"]
        counts[name] = counts.get(name, 0) + 1

    return {
        "counts": counts,
        "total_passing": len(data),
        "unique_students": len(counts)
    }
```

**Example Output**
```json
{
    "counts": {
        "Alice": 2,
        "Charlie": 1
    },
    "total_passing": 3,
    "unique_students": 2
}
```
</details>

---

</details>

<a id="block-2-api-data-ingestion"></a>
<details>
<summary><strong>Block 2: API Data Ingestion 🟪</strong></summary>
<br>

> This block focuses on pulling real-world data from an API, inspecting JSON responses, extracting useful fields, and preparing that data for further transformation and storage.

> It builds toward a small ingestion pipeline that:
> - requests external data
> - structures useful values
> - handles failed requests
> - writes clean outputs for later processing

---

<details>
<summary><strong>🔹 Fetching Data from an API</strong></summary>
<br>

**Script**  
- [View API request implementation](./python/api_data_ingestion/simple_request.py)

**Purpose**  
Learn how to retrieve data from an external API, inspect the response, and extract useful fields from returned JSON data.

**What I Built**  
A script that:
- sends a GET request to the Pokémon API
- retrieves data for a specified Pokémon
- checks for a successful response
- converts the response into JSON format
- extracts and displays selected attributes in a readable format

**Key Takeaways**
- Using `requests.get()` to call an external API
- Checking `response.status_code` before using the response
- Converting API responses into Python dictionaries using `.json()`
- Accessing nested data using dictionary keys
- Separating data retrieval logic from display logic

**Quick Reference**
```python
import requests

URL_NAME = "https://pokeapi.co/api/v2/pokemon/"

def get_pokemon_info(name):
    url = f"{URL_NAME}{name.lower()}"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Invalid response: {response.status_code}")
        return None

def display_pokemon_info(pokemon):
    print(f"Name: {pokemon['name'].capitalize()}")
    print(f"Base Experience: {pokemon['base_experience']}")
    print(f"Height: {pokemon['height']}")
    print(f"Weight: {pokemon['weight']}")
```

**Example Output**
```text
Name: Pikachu
Base Experience: 112
Height: 4
Weight: 60
```
</details>

---

<details>
<summary><strong>🔹 Structuring API Response Data</strong></summary>
<br>

**Script**  
- [View structured API transformation](./python/api_data_ingestion/get_pokemon_data.py)

**Purpose**  
Learn how to transform raw API JSON into a clean, reusable Python dictionary.

**What I Built**  
A script that:
- retrieves Pokémon data from the API
- extracts only relevant fields
- converts raw JSON into a structured dictionary
- separates API logic from transformation logic

**Key Takeaways**  
- Raw API responses should not be used directly, always transform them first
- Creating a transformation layer makes data reusable
- Functions should have a single responsibility (fetch vs transform)
- Returning consistent data shapes is critical for scaling

**Quick Reference**
```python
def transform_pokemon_data(pokemon):
    return {
        "name": pokemon["name"],
        "base_experience": pokemon["base_experience"],
        "height": pokemon["height"],
        "weight": pokemon["weight"]
    }
```

**Example Output**
```python
{
    "name": "pikachu",
    "base_experience": 112,
    "height": 4,
    "weight": 60
}
```

</details>

</details>

---

<a id="-concepts-reinforced"></a>
## 🛠️ Concepts Reinforced

Across these projects, I practiced:
- lists and loops
- conditionals
- dictionaries for counting and aggregation
- reusable functions
- reading and writing CSV files
- converting data to JSON
- building simple multi-step data pipelines
- making external API requests
- parsing and navigating JSON responses
- separating data retrieval from transformation logic
- designing consistent data structures for reuse

---

<a id="-notes-for-future-me"></a>
<details>
<summary>📝 Notes for Future Me</summary>
<br>

- Clean input early  
    → Use `.strip()` and `.lower()` to ensure consistent data

- Validate before using data  
    → Always check API responses (`status_code == 200`)  
    → Always guard against `None` before passing data forward

- Transform before use  
    → Never use raw API or CSV data directly  
    → Shape it into a consistent structure first

- Keep functions focused  
    → One job per function (fetch, transform, display)

- Be consistent with data structures  
    → Know when you're returning `{}` vs `[]` and stick to it

- Convert types explicitly  
    → CSV values are strings — use `int()` before comparisons

- Use dictionary patterns  
    → `.get(key, default)` is the cleanest way to count

- Make output readable  
    → Use `json.dump(..., indent=4)`

- Separate data concerns  
    → Raw data, processed data, and summaries should not be mixed

</details>