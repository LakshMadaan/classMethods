# create a class called students and use methods to input, print, total, average and to tell high and low grades.

class Students:
    def __init__(self,fN,lN):
        self.firstName=fN
        self.lastName=lN
    def inputGrades(self,ng):
        self.grades=[]
        self.ng=ng
        for i in range(0,ng,1):
            grd=float(input('Enter your grade: '))
            self.grades.append(grd)
        return self.grades
    def printGrades(self,ng,grades):
        self.grades=grades
        self.ng=ng
        for i in range(0,ng,1):
            print(grades[i])
    def totGrades(self,ng,grades):
        self.ng=ng
        self.grades=grades
        self.total=0
        for i in range(0,ng,1):
            self.total+=grades[i]
        return self.total    
    def avrGrades(self,total,ng):
        self.total=total
        self.ng=ng
        avr=self.total/self.ng
        return avr
    def highGrade(self,grades):
        self.grades=grades
        highGrade=max(self.grades)
        return highGrade
    def lowGrade(self,grades):
        self.grades=grades
        lowGrade=min(self.grades)
        return lowGrade

student1=Students('Laksh','Madaan')
print(student1.firstName,student1.lastName)
student1.inputGrades(5)
print('Student 1 grades are:')
student1.printGrades(student1.ng,student1.grades)
print('Student 1 total: ',student1.totGrades(student1.ng,student1.grades))
print('Student 1 average: ',student1.avrGrades(student1.total,student1.ng))
print('Student 1 high grade: ',student1.highGrade(student1.grades,student1.ng))
print('Student 1 low grade: ',student1.lowGrade(student1.grades,student1.ng))


student2=Students('Rishabh','Gupta')
print(student2.firstName,student2.lastName)
student2.inputGrades(5)
print('Student 2 grades are:')
student2.printGrades(student2.ng,student2.grades)
print('Student 2 total: ',student2.totGrades(student2.ng,student2.grades))
print('Student 2 average: ',student2.avrGrades(student2.total,student2.ng))
print('Student 2 high grade: ',student2.highGrade(student2.grades,student2.ng))
print('Student 2 low grade: ',student2.lowGrade(student2.grades,student2.ng))