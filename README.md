# 🏁 Data Engineering Learning Journey

## 📌 Overview

> This progression reflects the transition from scripting to building data systems.  
> The goal is to move from simple scripting toward building small, structured data pipelines by combining reusable patterns into complete workflows.

---

## 📚 Table of Contents

- [Project Structure](#-project-structure)
- [Learning Blocks](#-learning-blocks)
    - [Block 1: Fundamentals — Data Processing](#block-1-fundamentals--data-processing)
    - [Block 2: API Data Ingestion](#block-2-api-data-ingestion)
    - [Block 3: Data Storage and Querying](#block-3-data-storage-and-querying)
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
│   ├── api_data_ingestion/
│   │   ├── simple_request.py
│   │   ├── get_pokemon_data.py
│   │   ├── pokemon_data_pipeline.py
│   │   ├── filter_pokemon_data.py
│   │   ├── pokemon_data_error_handling.py
│   │   └── pokemon_etl_pipeline.py
│   │
│   └── data_storage_and_querying/
│       ├── pokemon_db_setup.py
│       └── pokemon_query_engine.py
│
├── data/
│   ├── raw/
│   │   ├── test_scores.csv
│   │   └── pokemon_data.json
│   ├── processed/
│   │   ├── cleaned.csv
│   │   └── output.json
│   ├── outputs/
│   │    ├── summary.json
│   │    └── pokemon_summary.json
│   └── pokemon.db # generated at runtime (not committed)
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
- counts how many passing records each student has earned
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

> It builds toward a complete data ingestion pipeline that:
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

---

<details>
<summary><strong>🔹 Collecting and Saving API Data</strong></summary>
<br>

**Script**  
- [View API ingestion pipeline](./python/api_data_ingestion/pokemon_data_pipeline.py)

**Purpose**  
Learn how to combine API requests, data transformation, and file output into a simple ingestion workflow.

**What I Built**  
A script that:
- loops through a list of Pokémon
- retrieves data for each one using the API
- transforms each response into a structured format
- aggregates the results into a structured dataset
- writes the final dataset to a JSON file

**Key Takeaways**  
- Looping over multiple API calls to build a dataset
- Aggregating structured records into a single collection
- Writing external data to disk using `json.dump()`
- Skipping invalid responses without breaking the pipeline
- Beginning to think in terms of ingestion pipelines

**Quick Reference**
```python
def transform_pokemon_data(pokemon_list):
    output = {}

    for pokemon in pokemon_list:
        pokemon_data = get_pokemon_data(pokemon)

        if pokemon_data:
            output[pokemon_data["name"].capitalize()] = {
                "height": pokemon_data["height"],
                "weight": pokemon_data["weight"],
                "base_experience": pokemon_data["base_experience"]
            }

    return output
```

**Example Output**
```python
{
    "Pikachu": {
        "height": 4,
        "weight": 60,
        "base_experience": 112
    },
    "Charizard": {
        "height": 17,
        "weight": 905,
        "base_experience": 240
    }
}
```

</details>

---

<details>
<summary><strong>🔹 Filtering and Summarizing API Data</strong></summary>
<br>

**Script**  
- [View filtering implementation](./python/api_data_ingestion/filter_pokemon_data.py)

**Purpose**  
Learn how to filter a dataset based on a condition and produce a structured summary of the results.

**What I Built**  
A script that:
- reads Pokémon data from a JSON file
- filters Pokémon based on base experience
- extracts relevant fields into a clean structure
- builds a list of filtered records
- returns both the filtered dataset and a count of matching entries

**Key Takeaways**  
- Filtering structured data using conditional logic
- Iterating through nested dictionaries (`key`, `value`)
- Converting dictionary-based data into a list of records
- Building summary outputs that include both data and metadata
- Reusing earlier patterns (filter → transform → summarize) on real datasets

**Quick Reference**
```python
def filter_by_base_experience(pokemon, min_exp):
    filtered = []

    for key, value in pokemon.items():
        if value["base_experience"] > min_exp:
            height = value["height"]
            weight = value["weight"]
            base_experience = value["base_experience"]

            filtered.append({
                "name": key,
                "height": height,
                "weight": weight,
                "base_experience": base_experience
            })

    return {
        "high_experience": filtered,
        "count": len(filtered)
    }
```

**Example Output**
```python
{
    "high_experience": [
        {
            "name": "Charizard",
            "height": 17,
            "weight": 905,
            "base_experience": 240
        }
    ],
    "count": 1
}
```

</details>

---

<details>
<summary><strong>🔹 Handling Invalid Data and API Errors</strong></summary>
<br>

**Script**  
- [View error handling implementation](./python/api_data_ingestion/pokemon_data_error_handling.py)

**Purpose**  
Learn how to make API-driven workflows resilient by handling invalid input, failed requests, and unexpected data without crashing the program.

**What I Built**  
A script that:
- normalizes user input before making API requests
- skips blank or invalid Pokémon inputs
- handles failed API responses gracefully
- continues processing valid records without interruption
- extracts selected fields into a structured format

**Key Takeaways**
- Always normalize input early (`.strip()` and `.lower()`)
- Never assume external data is valid
- Use conditional checks to prevent runtime errors
- Skip invalid records instead of stopping the program
- Keep validation logic close to where data is used

**Quick Reference**
```python
def get_pokemon_data(name):
    name = name.strip().lower()

    if name:
        url = f"{URL_NAME}pokemon/{name}"
        response = requests.get(url)

        if response.status_code == 200:
            return response.json()
        else:
            print(f"Skipping '{name}', no record was found.")
            return None
    else:
        print(f"Skipping '{name}', blank entry.")
        return None
```

**Example Output**
```python
Skipping 'invalidmon', no record was found.
Skipping '', blank entry.
[
    {'id': 25, 'name': 'pikachu', 'weight': 60},
    {'id': 6, 'name': 'charizard', 'weight': 905}
]
```

</details>

---

<details>
<summary><strong>🔹 Building a Complete API Data Pipeline ⚡</strong></summary>
<br>

**Script**  
- [View full ETL pipeline implementation](./python/api_data_ingestion/pokemon_etl_pipeline.py)

**Purpose**  
Combine API ingestion, validation, transformation, filtering, and file output into a single cohesive workflow.

**What I Built**  
A complete pipeline that:
- accepts user input for Pokémon names
- normalizes and validates input
- retrieves data from the Pokémon API
- skips invalid or blank entries
- transforms API responses into structured records
- saves the raw dataset to a JSON file
- filters Pokémon based on base experience
- builds a structured summary of results
- writes the final summary to a separate JSON file

**Key Takeaways**
- Combining multiple functions into a cohesive data workflow
- Separating raw data from processed outputs
- Reusing helper functions to maintain DRY code
- Designing consistent data structures across pipeline stages
- Thinking in terms of Extract → Transform → Load (ETL)

**Quick Reference**
```python
def main():
    pokemon_input = get_user_input()

    pokemon_data = collect_pokemon_data(pokemon_input)

    if pokemon_data:
        write_json_file(RAW_FILE_PATH, pokemon_data)
        good_data, bad_data = filter_by_base_experience(pokemon_data, 100)
        pokemon_summary = build_pokemon_summary(good_data, bad_data)
        write_json_file(SUMMARY_FILE_PATH, pokemon_summary)
```

**Example Output**
```python
{
    "high_experience": [
        {
        "name": "lugia",
        "height": 52,
        "weight": 2160,
        "base_experience": 306
        }
    ],
    "low_experience": [
        {
            "name": "onix",
            "height": 88,
            "weight": 2100,
            "base_experience": 77
        }
    ],
    "high_experience_count": 1,
    "low_experience_count": 1
}
```

</details>

---

</details>

<a id="block-3-data-storage-and-querying"></a>
<details>
<summary><strong>Block 3: Data Storage and Querying 🟦</strong></summary>
<br>

> This block introduces persistent data storage using a relational database and shifts data processing from in-memory operations to structured querying.  

> It focuses on:
> - storing structured data in a database
> - defining table schemas
> - inserting and managing records
> - querying data using SQL
> - integrating SQL with Python workflows

---

<details>
<summary><strong>🔹 Storing Data in SQLite</strong></summary>
<br>

**Script**  
- [pokemon_db_setup.py](./python/data_storage_and_querying/pokemon_db_setup.py)

**Purpose**  
Store previously collected API data in a structured database instead of JSON files.  
This builds directly on the API ingestion pipeline by introducing a persistent storage layer for collected data.  
The database file is generated at runtime and is excluded via `.gitignore`.  

**What I Built**  
A script that:

- reads Pokémon data from a JSON file
- creates a SQLite database (`pokemon.db`)
- defines a table schema for Pokémon data
- inserts records into the database
- queries stored data and prints results

**Key Takeaways**

- Databases store data persistently beyond script execution
- SQL tables define structured schemas for data
- Python can execute SQL commands using `sqlite3`
- Parameterized queries (`?`) prevent SQL injection
- Data can now be queried instead of iterated manually
- This marks the transition from scripting → data systems

**Quick Reference**
```python
conn = sqlite3.connect("data/pokemon.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS pokemon (
    id INTEGER PRIMARY KEY,
    name TEXT UNIQUE,
    height INTEGER,
    weight INTEGER,
    base_experience INTEGER
)
""")
```

**Console Output (Script Preview)**
```text
(1, 'lugia', 52, 2160, 306)
(2, 'onix', 88, 2100, 77)
```

**Database View (SQLite)**
| ID | Name | Height | Weight | Base Experience |
| :--- | :--- | :--- | :--- | :--- |
| 1 | lugia | 52 | 2160 | 306 |
| 2 | onix | 88 | 2100 | 77 |
| 3 | pikachu | 4 | 60 | 112 |
| 4 | bulbasaur | 7 | 69 | 64 |

</details>

---

<details>
<summary><strong>🔹 Querying Data with SQL</strong></summary>
<br>

**Script**  
[pokemon_query_engine.py](./python/data_storage_and_querying/pokemon_query_engine.py)

**Purpose**  
Retrieve and filter stored data using SQL queries instead of Python loops.

**What I Built**  
A script that:  
- connects to the existing SQLite database
- queries Pokémon based on specific conditions
- sorts and limits results using SQL
- formats and displays the results in a readable way

**Key Takeaways**

- SQL can handle filtering, sorting, and limiting data directly
- Python should orchestrate queries, not replace them
- Using `sqlite3.Row` allows access to columns by name instead of index
- Selecting specific columns is better practice than using `SELECT *`
- This marks the shift from storing data → querying data effectively

**Quick Reference**
```sql
# Example Query (High Experience Pokémon)

SELECT id, name, height, weight, base_experience
FROM pokemon
WHERE base_experience > ?
ORDER BY base_experience DESC
LIMIT 3
```

```sql
# Example Query (Lightweight Pokémon)

SELECT id, name, height, weight, base_experience
FROM pokemon
WHERE weight < ?
ORDER BY weight ASC
```

**Console Output (Script Preview)**
```text
Top Pokémon by Base Experience:
Name: Lugia | Base Experience: 306
Name: Rayquaza | Base Experience: 306
Name: Umbreon | Base Experience: 184

Lightest Pokémon by Weight:
Name: Pikachu | Weight: 60
Name: Bulbasaur | Weight: 69
```

</details>

</details>

---

<a id="-concepts-reinforced"></a>
## 🛠️ Concepts Reinforced

Across these blocks, I practiced:

- Python fundamentals (loops, conditionals, data structures)
- Data transformation and aggregation
- CSV and JSON data handling
- API data ingestion and validation
- Building multi-step data pipelines
- Separating extraction, transformation, and output logic
- Introducing persistent storage with SQLite
- Executing SQL queries from Python
- Designing structured data schemas
- Understanding when to use SQL vs Python
- Using SQL for filtering, sorting, and limiting datasets

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
    → One job per function (fetch, validate, transform, display, save)

- Be consistent with data structures  
    → Know when you're returning `{}` vs `[]` and stick to it

- Convert types explicitly  
    → CSV values are strings — use `int()` before comparisons

- Use dictionary patterns  
    → `.get(key, default)` is the cleanest way to count

- Make output human-readable  
    → Use `json.dump(..., indent=4)`

- Separate data concerns  
    → Raw data, processed data, and summaries should not be mixed

- File paths should match project structure  
    → Keep output in `data/raw`, `data/processed`, or `data/outputs`

- Databases are not just storage  
    → They are tools for querying and analysis

- Avoid overusing Python loops on structured data  
    → SQL is often more efficient and readable

- Always use parameterized queries  
    → Protects against SQL injection and errors

- Structure your schema carefully  
    → Changing it later is harder than designing it well early

- Think in rows and tables, not just dictionaries

- Let SQL do the heavy lifting  
    → Filtering, sorting, and limiting should happen in the database when possible

</details>