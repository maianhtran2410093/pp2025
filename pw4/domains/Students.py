class Student:
    def __init__(self, s_id, s_name, s_dob):
        self.__s_id = s_id  #apply encapsulation throughout
        self.__s_name = s_name
        self.__s_dob = s_dob
        #add s_gpa into __init__
        self.__s_gpa = 0.0

    @property
    def id(self):   return self.__s_id
    @property
    def name(self): return self.__s_name
    #getter gpa
    @property
    def gpa(self):  return self.__s_gpa
    #setter gpa
    @gpa.setter
    def gpa(self, value):
        self.__s_gpa = value
    def __str__(self):
        return f"ID: {self.__s_id}  Name: {self.__s_name}   DoB: {self.__s_dob}     GPA: {self.__s_gpa}"
