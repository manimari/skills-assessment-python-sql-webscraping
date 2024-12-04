from collections import Counter

def find_duplicate(numbers: list) -> list:
    """
    Finds duplicate numbers in a list.

    Args:
        numbers: A list of numbers.

    Returns:
        A list of integers that appear more than once in the input list.
    """
    # Count the occurrences of each number in the list
    count = Counter(numbers)
    # Return numbers that occur more than once
    return [num for num, freq in count.items() if freq > 1]

# Example list of numbers
numbers = [1, 2, 3, 2, 4, 5, 4, 6]
print("Input numbers:", numbers)
print("Duplicates:", find_duplicate(numbers))