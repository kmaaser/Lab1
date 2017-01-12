#!/usr/bin/env python3.5

#----------------------------------------------------------------------
# menu.py
# Dave Reed
# 12/04/2016
#----------------------------------------------------------------------

from Transcript import *

#----------------------------------------------------------------------

def menuChoice():
    print()
    print('1: Read file')
    print('2: Write file')
    print('3: Add Course')
    print('4: GPA')
    print('5: Courses by term')
    print('6: Courses by department')
    print('7: Courses by grade')
    print('8: Quit')
    return int(input('enter choice: '))

#----------------------------------------------------------------------

def main():

    t = Transcript('')
    while True:
        choice = menuChoice()
        if choice == 1:
            filename = input('enter filename: ')
            t.readFromFile(filename)
        elif choice == 2:
            filename = input('enter filename: ')
            t.writeToFile(filename)
        elif choice == 3:
            semester = input('enter Fall or Spring: ')
            year = int(input('enter year: '))
            department = input('enter department: ')
            number = int(input('enter number: '))
            instructor = input('enter instructor: ')
            credits = float(input('enter credits: '))
            grade = input('enter grade: ').upper()
            c = Course(semester, year, department, number, instructor, credits, grade)
            t.addCourse(c)
        elif choice == 4:
            print('GPA: {:5.3f}'.format(t.gpa()))
        elif choice == 5:
            semester = input('enter Fall or Spring: ')
            year = int(input('enter year: '))
            courses = t.coursesByTerm(semester, year)
            for c in courses:
                print(c)
        elif choice == 6:
            department = input('enter department: ')
            courses = t.coursesByDepartment(department)
            for c in courses:
                print(c)
        elif choice == 7:
            grade = input('enter grade: ').upper()
            courses = t.coursesByGrade(grade)
            for c in courses:
                print(c)
        elif choice == 8:
            break

#----------------------------------------------------------------------

if __name__ == '__main__':
    main()
