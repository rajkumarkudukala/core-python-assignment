class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    def average(self):
        return round(sum(self.marks)/len(self.marks),2)
    
def topper(Averages):
    top = max(Averages, key=Averages.get)
    return top
    
n = int(input("Enter number of students: "))

Students = []
Averages = {}

for i in range(n):
    name = input("Enter student name: ")
    marks = list(map(int, input("Enter marks of 3 subjects (space seperated):").split()))
    Students.append(Student(name,marks))
    Averages[name] = Students[i].average()

print("Averages:",Averages)
print("Topper:",topper(Averages))
