from fnmatch import fnmatchcase


class Employee:
    def __init__(self,fname,lname) -> None:
        self.fname=fname
        self.lname=lname
       # self.email=f"{fname}{lname}@aorion.com"

    def Explain(self):
        return f"This employee name is {self.fname} {self.lname} "
    @property
    def email(self  ):
        if (self.fname or self.lname)==None:
            return "Email is not set"
        return f"{self.fname}.{self.lname}@aorion.com"



    @email.setter
    def email(self, string):
        print("Setting now...")
        names = string.split("@")[0]
        self.fname=names.split(".")[0]
        self.lname=names.split(".")[1]


    @email.deleter
    def email(self):
        self.fname=None
        self.lname=None


skillf=Employee("Skill","F")
o="This is a string."
#print(dir(skillf))
import inspect
print(inspect.getmembers(skillf))