# Write a program to update the 'grade' value to 'A', and add a new
# key-value pair for 'major' with the value 'Computer Science'.


# Create a dictionary of student:

student = {
    "name": "john",
    "age": 22,
    "grade": "B"
}

# Update the 'grade' value to 'A':
updated = student["grade"] = "A"

# Add a new key-value pair for 'major' with the value 'Computer Science':
student.update({"major": "computer science"})

# Print student: 
print(student)