try:
    # Get input from user for marks in three subjects
    subject1_marks = float(input("Enter marks for subject 1: "))
    subject2_marks = float(input("Enter marks for subject 2: "))
    subject3_marks = float(input("Enter marks for subject 3: "))
    
    # Calculate total marks and percentage
    total_marks = subject1_marks + subject2_marks + subject3_marks
    total_percentage = (total_marks /3)
    
    print(f"Total marks: {total_marks}")
    print(f"Total percentage: {total_percentage}")
except ValueError:
    print("Invalid input. Please enter valid numeric values for marks.")