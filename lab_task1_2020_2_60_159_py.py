import random

def read_student_ids(filename):         # Reads student IDs from a file and returns them as a list.

    try:
        with open(filename, 'r') as file:
            student_ids = [line.strip() for line in file.readlines()]
        return student_ids
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return []


def select_students_for_viva(student_ids):
    all_students = student_ids.copy()  # Make a copy of the original list
    viva_count = 1  # Counter for the number of vivas

    while student_ids:
        selected_student = random.choice(student_ids)       # Randomly select students until all are selected once
        student_ids.remove(selected_student)

        print(f"Viva #{viva_count}: {selected_student}")    # Print the selected student and viva number
        viva_count += 1


    print("\nAll students have been selected. Resetting the list.\n")       # when all students have been selected, reset the list
    student_ids.extend(all_students)  # Reset the list with all students

def main():
    filename = "/content/drive/MyDrive/student_ids.txt"  # Replace file name


    student_ids = read_student_ids(filename)     # Read the student IDs from the file
    if not student_ids:
        return

    select_students_for_viva(student_ids)        #  Select students for the viva

if __name__ == "__main__":
    main()
