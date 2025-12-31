class Course:
    def __init__(self, c_id, c_name, c_credit):
        self.__c_id = c_id 
        self.__c_name = c_name
        #add c_credit into __init__
        self.__c_credit = c_credit

    @property
    def id(self):       return self.__c_id
    @property
    def name(self):     return self.__c_name
    #getter credit
    @property
    def credit(self):   return self.__c_credit

    def __str__(self):
        return f"ID: {self.__c_id}  Name: {self.__c_name}   Credits: {self.__c_credit}"
