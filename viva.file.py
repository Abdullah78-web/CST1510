"""more than 80 pass
79-41 resit 
less 40 fail function"""
class year1():
    def __init__(self, student_name, student_mark):
        self.student_name = student_name
        self.student_mark = student_mark


def grade(mark):
    while True:
        if mark > 80:
            return "pass"
            break
        elif mark >= 41:
            return "resit"
            break
        else:
            break



student_name = input("Enter the name: ")
student_mark = int(input("Enter the mark: "))

result = grade(student_mark)
print(student_name)
print(student_mark)
print(result)