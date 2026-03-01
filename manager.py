import json
import os
filename = "grades.json"

class StudentManger:
    
    def __init__(self,filename="grades.json"):
        self.filename = filename
        self.data = self.load()
        

    def load(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r") as file:
                try:
                    return json.load(file)
                except json.JSONDecodeError:
                    return []
        return []
    def save(self):
        with open(self.filename, "w") as file:
            json.dump(self.data, file, indent=4)


    def add_student(self):
        
        self.name = input("Enter name: ")
        

        
        self.stu_data ={
            "name" : self.name,
           
        }
        
        if any(student["name"] == self.name for student in self.data):
            print("Name already exists")
        else:
            self.data.append(self.stu_data)
            self.save()
            print("Student added successfully")
            


        



    def add_grade(self):
        name = input("Enter student name to add grade: ")
        subject = input("Enter subject: ")
        score  = float(input("Enter score: "))

        for student in self.data:
            if student["name"] == name:
                if "grades" not in student:
                    student["grades"] = []
                    student["grades"].append({
                        "subject": subject,
                        "score": score
            })
        if any(student["name"] == name for student in self.data):
            self.data[name]["subject"] = subject
            self.data[name]["score"] = score

            print("Grade added")
        
        else:
            print("Name doesnt exists")

        

        
  

    def get_report():
        pass
    def class_average():
        pass
    def top_student():
        pass
    

stud1 = StudentManger()
# stud1.add_student()
stud1.add_grade()