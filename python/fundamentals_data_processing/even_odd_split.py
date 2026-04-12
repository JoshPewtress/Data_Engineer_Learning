def sort_by_even_odd(numbers):
    even_numbers = []
    odd_numbers = []
    
    for num in numbers:
        if num % 2 == 0:
            even_numbers.append(num)
        else:
            odd_numbers.append(num)
    
    return even_numbers, odd_numbers

def test(numbers):
    print(f"Starting sort of: {numbers}")
    even_numbers, odd_numbers = sort_by_even_odd(numbers)
    print(f"Printing even numbers: {even_numbers}")
    print(f"Print odd numbers: {odd_numbers}")
    print("=======")

def main():
    list1 = [12, 47, 83, 29, 5, 64]
    list2 = [91, 3, 56, 78, 22, 14, 67, 39]
    list3 = [8, 44, 71, 26, 90]

    test(list1)
    test(list2)
    test(list3)

main()