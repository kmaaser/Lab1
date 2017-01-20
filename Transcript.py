#!/usr/bin/env python3.5

# ----------------------------------------------------------------------
# Transcript.py
# David Reed
# Karenna Maaser
# 1/23/2017
# ----------------------------------------------------------------------

from Course import *

# ----------------------------------------------------------------------

class Transcript:

    # ------------------------------------------------------------------

    def __init__(self, name: str):

        """
        :param name: the name of the student
        """
        self.name = name
        self.courseList = list()



    # ------------------------------------------------------------------

    def addCourse(self, course: Course):

        """adds course to courses the student has taken

        :param course: the Course
        """

        self.courseList.append(course)


    # ------------------------------------------------------------------

    def gpa(self) -> float:

        """the GPA is calculated by adding the number of credits multiplied by the the quality points for the grade
         for each course divided by the sum of the number of credits

         the quality points for each grade are as follows:
         A 4.0, A- 3.7, B+ 3.3, B 3.0, B- 2.7, C+ 2.3, C 2.0, C- 1.7, D+ 1.3, D 1.0, F 0.0

        pre:

        post: returns the GPA for the students"""
        
        pass

    # ------------------------------------------------------------------

    def readFromFile(self, filename: str):

        """read the student name and courses from the specified file and adds them to the list of courses

        :param filename: name of file to read the data from; the format of the file must match the format
        the writeToFile method produces
        """

        pass

    # ------------------------------------------------------------------

    def writeToFile(self, filename: str):

        """writes the student name to the first line of the file and the CSV representation for each course is written
        one course per line; uses the Course toCSV method to create the line to write to each file

        :param filename: name of file to write

        """



        pass

    # ------------------------------------------------------------------

    def coursesByTerm(self, semester: str, year: int):

        """returns a list of Course objects that are from the specified semester and year
        :param semester:
        :param year:
        :return: list of Course objects that match the specified search criteria
        """
        termList = list()

        for courseInfo in self.courseList:
            if courseInfo.semester == semester:
                if courseInfo.year == year:
                    termList.append(courseInfo)
                    return termList
        return '-1'
    # ------------------------------------------------------------------

    def coursesByDepartment(self, department):

        """returns a list of Course objects that are from the specified department
        :param semester:
        :param year:
        :return: list of Course objects that match the specified search criteria
        """

        departmentList = list()

        for courseInfo in self.courseList:
            if courseInfo.department == department:
                departmentList.append(courseInfo)
                return departmentList
        return '-1'

    # ------------------------------------------------------------------

    def coursesByGrade(self, grade):

        """returns a list of Course objects that have the specified grade
        :param grade:
        :return: list of Course objects that match the specified search criteria
        """

        gradeList = list()

        for courseInfo in self.courseList:
            if courseInfo.grade == grade:
                gradeList.append(courseInfo)
                return gradeList
        return '-1'

    # ------------------------------------------------------------------
