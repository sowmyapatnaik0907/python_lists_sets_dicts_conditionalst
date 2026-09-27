# Dictionary Creation

student_marks = {
    "Sowmya": 85,
    "Parimala": 78,
    "Ramya": 92,
    "Swathi": 88,
    "Kavya": 75
}

print("Student marks:", student_marks)


# Access and print mark of a specific student

print("Sowmya's mark:", student_marks["Sowmya"])


# Add Janani

student_marks["Janani"] = 80

print("After adding Janani:", student_marks)


# Update mark of an older student

student_marks["Parimala"] = 82

print("After updating Parimala's mark:", student_marks)


# Print all keys

print("Keys:", student_marks.keys())


# Print all values

print("Values:", student_marks.values())


# Print all key-value pairs

print("Items:", student_marks.items())