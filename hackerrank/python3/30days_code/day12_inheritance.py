

class Student(Person):
  #   Class Constructor
  #   
  #   Parameters:
  #   firstName - A string denoting the Person's first name.
  #   lastName - A string denoting the Person's last name.
  #   id - An integer denoting the Person's ID number.
  #   scores - An array of integers denoting the Person's test scores.
  #
  # Write your constructor here
  def __init__(self, firstName, lastName, idNumber, score):
    super().__init__(firstName, lastName, idNumber)
    self.score = score
  def calculate(self):
  #   Function Name: calculate
  #   Return: A character denoting the grade.
  #
  # Write your function here      
    a_s = sum(self.score)/len(self.score)
    if(a_s<40):
      return "T"
    elif(a_s<55):
      return "D"
    elif(a_s<70):
      return "P"
    elif(a_s<80):
      return "A"
    elif(a_s<90):
      return "E"
    else:
      return "O"