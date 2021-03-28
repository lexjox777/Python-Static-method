class Student:
  def __init__(self,scores = []):
    self.scores = scores

  def avg(self):
    return round(sum(self.scores)/ len(self.scores))

# static method is a decorator and does not have access to instance method
  @staticmethod
  def notice():
    return "Exam next week!"

kingsley= Student(scores=[3,5,7,8,7])

print(Student.notice())
print(kingsley.notice())

# static method dont link to an object while instance method is linked to an object