students = ['hamza', 'usama', 'ameen', 'shahzaib','hamza', 'usama', 'ameen', 'shahzaib','hamza', 'usama', 'ameen', 'shahzaib','hamza', 'usama', 'ameen', 'shahzaib']


for abc in students:
    

    print(f"The name of students is: {abc}")
    print(f"Every students is got good percentage: {abc}")  # IF print have indention that means it will in the loop.
    for cde in abc:
        print(f"Hello {cde}")

print(f"As a resutl the best students is: {abc}")  # If we remove the indention then it will not include in the loop