#!/usr/bin/env python3.5

# ----------------------------------------------------------------------
# Course.py
# Dave Reed
# 12/04/2016
# ----------------------------------------------------------------------

# ----------------------------------------------------------------------

class Course:
    """ """

    # ------------------------------------------------------------------

    def __init__(self, semester: str, year: int, department: str, number: int, instructor: str, credits: float, grade: str):

        """
        pre: none

        :param semester: a string that is either Fall or Spring
        :param year:  a four digit integer representing the year
        :param department: a string representing the department
        :param number: an integer that is the course number
        :param instructor: a string
        :param credits: a floating point value indicating number of credits
        :param grade: a letter grade one of: A, A-, B+, B, B-, C+, C, C-, D+, D, F
        """
        """
        pre: none

        post: constructs course object with specified parameters"""

        self.semester = semester
        self.year = int(year)
        self.department = department
        self.number = int(number)
        self.instructor = instructor
        self.credits = float(credits)
        self.grade = grade

    # ------------------------------------------------------------------

    def __str__(self):

        """
        pre: none

        post: returns a string representation of the Course with each attribute separated by a space in the order:
        semester, year, department, number, instructor, credits, grade
        for example:
        Fall 2016 CS 160 Reed 3.0 A
        """

        return self.semester + " " + self.year + " " + self.department + " " + self.number + " " + self.instructor + " " + self.credits + " " + self.grade

    # ------------------------------------------------------------------

    def toCSV(self) -> str:

        """
        pre: none

        post: returns a string with the attributes of the course separated by a comma in th order:
        semester, year, department, number, instructor, credits, grade
        for example:
        Fall,2016,CS,160,Reed,3.0,A
        """

        return self.semester + "," + self.year + "," + self.department + "," + self.number + "," + self.instructor + "," + self.credits + "," + self.grade

    # ------------------------------------------------------------------

    @classmethod
    def fromCSV(cls, csv: str) -> 'Course':

        """
        :param csv: a string in the format returned by the toCSV method
        :return: a Course object

        example call:
        c = Course.fromCSV("Fall,2016,CS,160,Reed,3.0,A")
        """

        course = csv.split(",")
        newCourse = Course(course[0], int(course[1]), course[2], int(course[3]), course[4], float(course[5]), course[6])

        return newCourse

    # ------------------------------------------------------------------
