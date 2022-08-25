# Podemos utilzar el método especial  __init__ (conocido como constructor)
# y el objeto actual self para hacer un creador de objetos del tipo definido con la
# palabra reservada class
# 
class Developer:
  def __init__(self, name, position, *skills):
    self.name = name
    self.position = position
    self.skills = [*skills]

dev_one = Developer('Bob', "Junior Dev", "Ruby","Git", "Linux")
dev_two = Developer('Alice', "Senior Fullstack Developer", "Python","Git", "HTML", "CSS", "Javascript")

print(dev_one.skills)