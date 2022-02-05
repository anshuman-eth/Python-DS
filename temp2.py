class Employee:

  __leaves=8 
  pass
  def __init__(self, name, salary, role):
    self.name=name
    self.salary=salary
    self.role=role
  def printdetails(self):
    return f"Name is {self.name}. Salary is {self.salary} and role is {self.role}"


  @classmethod
  def change_leaves(cls, newleaves):
    cls.leaves=newleaves
  @classmethod
  def from_str(cls,string):
    params=string.split("-")
    return cls(params[0], params[1],params[2])
    #return cls(*string.split("-"))

  @staticmethod
  def print_good(str):
    print("This is good " + str)



class programmer(Employee):
  def __init__(self, name, salary, role, languages):
    self.name=name
    self.salary=salary
    self.role=role
    self.languages=languages

  def printprog(self):
    return f"The programmer's name is {self.name}. Salary is {self.salary}. Role is {self.role}. The languages are {self.languages}."

class player:
  var=2
  no_of_games=4
  def __init__(self, name, game):
      self.name=name
      self.game=game

  def printdetails(self):
    return f"Name is {self.name}. Game is {self.game}."


class coolProgrammer( Employee, player):
  language="C++"
  def printlanguage(self):
    print(self.language)



emp1=Employee("Anshuman",155,"Student")
emp2=Employee("Shivam",5,"Business")

print(emp1+emp2)