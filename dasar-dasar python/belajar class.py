class People:
    def __init__(self, name, age, job):
        self.name = name
        self.age = age
        self.job = job

    def information(self):
        print('Name : ', self.name)
        print('Age  : ', self.age)
        print('Job  : ', self.job)

# MAIN
manager = People('Abe', 22, 'Manager')
employee = People('Jean', 20, 'Employee')

manager.information()
print("")
employee.information()