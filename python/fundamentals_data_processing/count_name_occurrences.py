def count_duplicate_names(names):
    output = {}

    for name in names:
        output[name] = output.get(name, 0) + 1

    return output

def test(names):
    print(f"Testing with list: {names}")
    duplicates_counted = count_duplicate_names(names)
    print(f"Names counted: {duplicates_counted}")
    print("======")

def main():
    test_one = ["Alice", "Bob", "Alice", "Charlie", "Bob", "Alice"]
    test_two = ["Eve", "Liam", "Eve", "Noah", "Olivia", "Eve", "Liam", "Sophia"]
    test_three = ["Mason", "Ava", "Mason", "Ava", "Ethan", "Mia", "Mason"]

    test(test_one)
    test(test_two)
    test(test_three)

main()