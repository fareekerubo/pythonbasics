class Student:
     def __init__(self,first,last,marks):
         self.first = first
         self.last=last
         self.marks=marks
         self.email= first +'.'+ last

     def fullname(self):
        return '{} {}'.format(self.first, self.last)
     def apply_average(self):
        self.average = int(self.average * 1.04)


stud_1 = Student('farida','kerubo',250)
stud_2 = Student('precious','kwamboka',600)

print(stud_1.average)
stud_1.apply_average()
#print(stud_1.average)

