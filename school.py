'''

School module containing all classes containing data for the school management system

'''

from google.appengine.ext import ndb
import datahandler


class Address(ndb.Model):
    '''
    Address class containing basic address information
    '''
    street = ndb.StringProperty()
    city = ndb.StringProperty()
    state = ndb.StringProperty()
    zipcode = ndb.StringProperty()

class Location(ndb.Model):
    '''
    Location class containing information for class location
    '''
    building = ndb.StringProperty()
    roomNumber = ndb.IntegerProperty()

class Student(ndb.Model):
    '''
    Student class containing all student data, inherited from Person
    '''
    firstName = ndb.StringProperty()
    lastName = ndb.StringProperty()
    idNumber = ndb.IntegerProperty()
    department = ndb.IntegerProperty()
    address = ndb.StructuredProperty(Address)
    phone = ndb.StringProperty()
    courses = ndb.IntegerProperty(repeated=True, write_empty_list=True) # list of course ID's        
    units = ndb.IntegerProperty()

    name = "Student"

class Instructor(ndb.Model):
    '''
    Instructor class containing all instructor data
    '''
    firstName = ndb.StringProperty()
    lastName = ndb.StringProperty()
    idNumber = ndb.IntegerProperty()
    department = ndb.IntegerProperty()
    address = ndb.StructuredProperty(Address)
    phone = ndb.StringProperty()
    courses = ndb.IntegerProperty(repeated=True, write_empty_list=True) # list of course ID's        

    name = "Instructor"



class Quarter(ndb.Model):
    '''
    Quarter class containing quarter information, list of courses
    '''
    idNumber = ndb.IntegerProperty()
    term = ndb.IntegerProperty() # fall=1, winter=2, spring=3 summer=4
    year = ndb.IntegerProperty()
    courses = ndb.IntegerProperty(repeated=True, write_empty_list=True) # list of course ID's

    name = "Quarter"

    
class Department(ndb.Model):
    '''
    Department class containing information about people in the department
    '''
    departmentName = ndb.StringProperty()
    courses = ndb.IntegerProperty(repeated=True, write_empty_list=True)
    idNumber = ndb.IntegerProperty()
    
    name = "Department"


class Course(ndb.Model):
    '''
    Course class containing all course data
    '''
    #TODO: maybe make a time class,
    idNumber = ndb.IntegerProperty()
    quarter = ndb.StructuredProperty(Quarter)
    department = ndb.IntegerProperty()
    units = ndb.IntegerProperty()
    courseName = ndb.StringProperty()
    instructor = ndb.IntegerProperty() #instructor ID
    time = ndb.StringProperty() # change later?
    place = ndb.StructuredProperty(Location)
    students = ndb.IntegerProperty(repeated=True, write_empty_list=True) #list of student ID's


    name = "Course"



def dropStudent(studentID, courseID):
    studentCourseList = studentsCourses(studentID)
    if courseID in studentCourseList:
        studentCourseList.remove(courseID)
    datahandler.postEntity(studentID, 'Student', {'courses': studentCourseList})
    
    studentCourseList = coursesStudents(courseID)
    if studentID in studentCourseList:
        studentCourseList.remove(courseID)
    datahandler.postEntity(courseID, 'Course', {'students': studentCourseList})
    
def enrollStudent(studentID, courseID):
    studentCourseList = studentsCourses(studentID)
    if courseID not in studentCourseList:
        studentCourseList.append(courseID)
    datahandler.postEntity(studentID, 'Student', {'courses': studentCourseList})
    
    studentCourseList = coursesStudents(courseID)
    if studentID not in studentCourseList:
        studentCourseList.append(courseID)
    datahandler.postEntity(courseID, 'Course', {'students': studentCourseList})
    
    
def studentsCourses(studentID):
    return datahandler.getEntityDic(studentID, 'Student')['courses']

def coursesStudents(courseID):
    return datahandler.getEntityDic(courseID, 'Course')['students']
    
def listCourses(year, quarter, departmentID):
    keyString = str(year) + str(quarter)
    quarter = datahandler.getEntityDic(int(keyString), 'Quarter')
    outList = []
    for courseID in quarter['courses']:
        if datahandler.getEntityDic(courseID, 'Course')['department'] is departmentID:
            outList.append(courseID)
    return outList
    