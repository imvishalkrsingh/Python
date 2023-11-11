try:
    # Get input from user for length and breadth
    length = float(input("Enter the length of the rectangle: "))
    breadth = float(input("Enter the breadth of the rectangle: "))
    
    # Calculate the area
    area = length * breadth
    
    # Display the result
    print(f"The area of the rectangle with length {length} and breadth {breadth} is {area}")
except ValueError:
    print("Invalid input. Please enter valid numeric values for length and breadth.")

