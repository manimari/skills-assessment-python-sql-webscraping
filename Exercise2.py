def read_grades_file(file_path: str) -> dict:
    """
    Reads the grades file and stores the data in a dictionary.
    
    Args:
        file_path (str): Path to the file containing grades.

    Returns:
        Dictionary with student names as keys and grades as values.
    """
    grades = {}
    try:
        with open(file_path, 'r') as file:
            for line in file:
                try: 
                    name, grade = line.split(':')
                    grades[name.strip()] = int(grade.strip())
                except ValueError:
                    print(f"Skipping invalid line: {line.strip()}")
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except Exception as e:
        print(f"Error reading file: {e}")
    return grades


def calculate_average(grades: dict) -> float:
    """
    Calculates the average grade from a dictionary of grades.
    
    Args:
        grades: Dictionary of grades, where keys are student names and values are their grades.
    
    Returns:
        Average grade. Returns 0 if the dictionary is empty.
    """
    if not grades:
        return 0
    total = sum(grades.values())
    count = len(grades)
    return total / count


def main():
    """
    Main function to read grades from a file and calculate the average.
    """
    file_path = 'grades.txt'  
    grades = read_grades_file(file_path)
    if grades:
        print("Grades:", grades)
        average = calculate_average(grades)
        print(f"Average Grade: {average:.2f}")
    else:
        print("No grades to process.")


if __name__ == "__main__":
    main()