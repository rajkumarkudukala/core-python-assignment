class Patient:
    def __init__(self, name, age, disease):
        self.name = name
        self.age = age
        self.disease = disease

def search(disease, patients):
    for i in range(len(patients)):
        if(patients[i].disease == disease):
            print(patients[i].name)

patients = []
n = int(input("Enter number of patients: "))

for i in range(n):
    name = input(f"Enter patient {i+1} name: ")
    age = int(input("Enter age: "))
    disease = input("Enter disease: ")
    patients.append(Patient(name, age, disease))

disease = input("Enter disease name to search: ")
search(disease, patients)

