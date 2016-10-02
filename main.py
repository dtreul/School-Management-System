import webapp2
import jinja2
import os

from school import *  # @UnusedWildImport
import datahandler




JINJA_ENVIRONMENT = jinja2.Environment(
                                       loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
                                       extensions=['jinja2.ext.autoescape'],
                                       autoescape=True)


class MainPage(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('web/index.html')
        self.response.write(template.render())

class APIPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('Hello, World!')


class StudentHandler(webapp2.RequestHandler):
    def get(self):
        requestString = self.request.get('idNumber')
        if requestString == '':
            # no request so return list of all students
            self.response.write(datahandler.getAllEntities(Student))
                
        else:
            requestID = int(requestString)
            self.response.write(datahandler.getEntity(requestID, 'Student'))
        
        
    def put(self):
        requestString = self.request.body
        requestDict = eval(requestString)
        requestAddress = requestDict['address']
        student = Student(
                          firstName = requestDict['firstName'],
                          lastName = requestDict['lastName'],
                          idNumber = requestDict['idNumber'],
                          department = requestDict['department'],
                          address = Address(
                                            street = requestAddress['street'],
                                            city = requestAddress['city'],
                                            state = requestAddress['state'],
                                            zipcode = requestAddress['zipcode']),
                          phone = requestDict['phone'],
                          courses = requestDict['courses'],
                          units = requestDict['units'],
                          id = requestDict['idNumber']
                          )
        datahandler.putEntity(student)
        for courseID in requestDict['courses']:
            enrollStudent(int(requestDict['idNumber']), int(courseID))

    def post(self):
        requestID = int(self.request.get('idNumber'))
        requestString = self.request.body
        requestDict = eval(requestString)
        datahandler.postEntity(requestID, 'Student', requestDict)
        
    def delete(self):
        requestString = self.request.get('idNumber')
        requestID = int(requestString)
        datahandler.deleteEntity(requestID, 'Student')
        

class InstructorHandler(webapp2.RequestHandler):
    def get(self):
        requestString = self.request.get('idNumber')
        if requestString == '':
            # no request so return list of all instructors
            self.response.write(datahandler.getAllEntities(Instructor))
                
        else:
            requestID = int(requestString)
            self.response.write(datahandler.getEntity(requestID, 'Instructor'))

    def put(self):
        requestString = self.request.body
        requestDict = eval(requestString)
        requestAddress = requestDict['address']
        instructor = Instructor(
                          firstName = requestDict['firstName'],
                          lastName = requestDict['lastName'],
                          idNumber = requestDict['idNumber'],
                          department = requestDict['department'],
                          address = Address(
                                            street = requestAddress['street'],
                                            city = requestAddress['city'],
                                            state = requestAddress['state'],
                                            zipcode = requestAddress['zipcode']),
                          phone = requestDict['phone'],
                          courses = requestDict['courses']
                          )
        datahandler.putEntity(instructor)
        
    def post(self):
        requestID = int(self.request.get('idNumber'))
        requestString = self.request.body
        requestDict = eval(requestString)
        datahandler.postEntity(requestID, 'Instructor', requestDict)
        
    
    def delete(self):
        requestString = self.request.get('idNumber')
        requestID = int(requestString)
        datahandler.deleteEntity(requestID, 'Instructor')

class DepartmentHandler(webapp2.RequestHandler):

    def get(self):
        requestString = self.request.get('idNumber')
        if requestString == '':
            # no request so return list of all departments
            self.response.write(datahandler.getAllEntities(Department))
                
        else:
            requestID = int(requestString)
            self.response.write(datahandler.getEntity(requestID, 'Department'))

    def put(self):
        requestString = self.request.body
        requestDict = eval(requestString)
        department = Department(
                          departmentName = requestDict['departmentName'],
                          courses = requestDict['courses'],
                          idNumber = requestDict['idNumber']
                          )
        datahandler.putEntity(department)
        
        
    def post(self):
        requestID = int(self.request.get('idNumber'))
        requestString = self.request.body
        requestDict = eval(requestString)
        datahandler.postEntity(requestID, 'Department', requestDict)
        
    def delete(self):
        requestString = self.request.get('idNumber')
        requestID = int(requestString)
        datahandler.deleteEntity(requestID, 'Department')
        


class CourseHandler(webapp2.RequestHandler):
    def get(self):
        requestString = self.request.get('idNumber')
        if requestString == '':
            # no request so return list of all courses
            self.response.write(datahandler.getAllEntities(Course))
                
        else:
            requestID = int(requestString)
            self.response.write(datahandler.getEntity(requestID, 'Course'))

    def put(self):
        requestString = self.request.body
        requestDict = eval(requestString)
        print requestDict['units']
        locationDict = requestDict['location']
        course = Course(
                          idNumber = requestDict['idNumber'],
                          department = requestDict['department'],
                          courseName = requestDict['name'],
                          instructor = int(requestDict['instructor']),
                          time = requestDict['time'],
                          place = Location(
                                           building = locationDict['building'],
                                           roomNumber = locationDict['roomNumber']),
                          students = requestDict['students'],
                          units = requestDict['units']
                          )
        datahandler.putEntity(course)
        
    def post(self):
        requestID = int(self.request.get('idNumber'))
        requestString = self.request.body
        requestDict = eval(requestString)
        datahandler.postEntity(requestID, 'Course', requestDict)

    def delete(self):
        requestString = self.request.get('idNumber')
        requestID = int(requestString)
        datahandler.deleteEntity(requestID, 'Course')
        

class QuarterHandler(webapp2.RequestHandler):
    def get(self):
        requestString = self.request.get('idNumber')
        if requestString == '':
            # no request so return list of all quarters
            self.response.write(datahandler.getAllEntities(Quarter))
                
        else:
            requestID = int(requestString)
            self.response.write(datahandler.getEntity(requestID, 'Quarter'))

    def put(self):
        requestString = self.request.body
        requestDict = eval(requestString)
        quarter = Quarter(
                          term = requestDict['term'],
                          year = requestDict['year'],
                          courses = [],
                          idNumber = int(requestDict['year']) * 10 + int(requestDict['term'])
                          )
        datahandler.putEntity(quarter)
        
    def post(self):
        requestID = int(self.request.get('idNumber'))
        requestString = self.request.body
        requestDict = eval(requestString)
        datahandler.postEntity(requestID, 'Quarter', requestDict)

    def delete(self):
        requestString = self.request.get('idNumber')
        requestID = int(requestString)
        datahandler.deleteEntity(requestID, 'Quarter')
        


class StudentCourseLister(webapp2.RequestHandler):
    def get(self):
        requestString = self.request.get('idNumber')
        if requestString == '':
            self.response.write("no student")
        else:
            requestID = int(requestString)
            self.response.write(studentsCourses(requestID))
            
            
class CourseStudentLister(webapp2.RequestHandler):
    def get(self):
        requestString = self.request.get('idNumber')
        if requestString == '':
            self.response.write("no course")
        else:
            requestID = int(requestString)
            self.response.write(coursesStudents(requestID))
            
class StudentDropper(webapp2.RequestHandler):
    def put(self):
        studentID = self.request.get('studentID')
        courseID = self.request.get('courseID')
        if studentID is not '' and courseID is not '':
            dropStudent(int(studentID), int(courseID))
        else:
            self.response.write('no such student or course')
            

class StudentEnroller(webapp2.RequestHandler):
    def put(self):
        studentID = self.request.get('studentID')
        courseID = self.request.get('courseID')
        if studentID is not '' and courseID is not '':
            enrollStudent(int(studentID), int(courseID))
        else:
            self.response.write('no such student or course')
            
class QuartersCourses(webapp2.RequestHandler):
    def get(self):
        year = self.request.get('year')
        quarter = self.request.get('quarter')
        departmentID = self.request.get('departmentID')
        if year is not '' and quarter is not '' and departmentID is not '':
            self.response.write(listCourses(int(year), int(quarter), int(departmentID)))
        else:
            self.response.write('no such quarter or department') 
            
            
class DepartmentsCourses(webapp2.RequestHandler):
    def get(self):
        idNumber = self.request.get('idNumber')
        if idNumber is not '':
            department = datahandler.getEntity(int(idNumber), 'Department')
            department = eval(department)
            if department != {}:
                self.response.write(department['courses'])
            else:
                self.response.write('{}')
        else:
            self.response.write('no such quarter or department') 


class StudentWebPage(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('web/student/index.html')
        self.response.write(template.render())
        
class InstructorWebPage(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('web/instructor/index.html')
        self.response.write(template.render())
        
class DepartmentWebPage(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('web/department/index.html')
        self.response.write(template.render())
        
class CourseWebPage(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('web/course/index.html')
        self.response.write(template.render())
        
class QuarterWebPage(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('web/quarter/index.html')
        self.response.write(template.render())
        
        
class QuarterAdd(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('web/quarter/addquarter.html')
        self.response.write(template.render())
        
    def post(self):
        termConverter = {'Fall': 1, 'Winter': 2, 'Spring': 3, 'Summer': 4}
        term = self.request.get('term')
        year = self.request.get('year')
        quarter = Quarter(
                          term = termConverter[term],
                          year = int(year),
                          courses = [],
                          idNumber = int(year) * 10 + termConverter[term]
                          )
        datahandler.putEntity(quarter)
        self.response.write('Quarter added')
        
class StudentAdd(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('web/student/addstudent.html')
        self.response.write(template.render())
        
    def post(self):
        requestString = self.request.body
        print requestString
        requestDict = eval(requestString)
        self.response.write(requestDict)
    
class DepartmentAdd(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('web/department/adddepartment.html')
        self.response.write(template.render())
        
    def post(self):
        requestString = self.request.body
        print requestString
        requestDict = eval(requestString)
        self.response.write(requestDict)
    

class EnrollWebPage(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('web/student/enroll.html')
        self.response.write(template.render())
        
    def post(self):
        studentID = self.request.get('studentID')
        courseID = self.request.get('courseID')
        enrollStudent(eval(studentID), eval(courseID))
        self.response.write('Student Enrolled')
        
        
class DropWebPage(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('web/student/drop.html')
        self.response.write(template.render())
        
    def post(self):
        studentID = self.request.get('studentID')
        courseID = self.request.get('courseID')
        dropStudent(eval(studentID), eval(courseID))
        self.response.write('Student Dropped')

class DepartmentOfferedWebPage(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('web/department/offered.html')
        self.response.write(template.render())


class CourseOfferedWebPage(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('web/course/offered.html')
        self.response.write(template.render())

class ViewStudent(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('web/student/viewstudent.html')
        self.response.write(template.render())

class QuarterCoursesOffered(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('web/quarter/offered.html')
        self.response.write(template.render())

class ViewQuarter(webapp2.RequestHandler):
    def get(self):
        term = self.request.get('term')
        year = self.request.get('year')
        if term is '' and year is '':
            template = JINJA_ENVIRONMENT.get_template('web/quarter/viewquarter.html')
            self.response.write(template.render())
        else:
            termConverter = {'Fall': 1, 'Winter': 2, 'Spring': 3, 'Summer': 4}
            self.response.write(datahandler.getEntity(int(year)*10+termConverter[term], 'Quarter'))


class InstructorAdd(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('web/instructor/addinstructor.html')
        self.response.write(template.render())
        
    def post(self):
        requestString = self.request.body
        print requestString
        requestDict = eval(requestString)
        self.response.write(requestDict)

class ViewInstructor(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('web/instructor/viewinstructor.html')
        self.response.write(template.render())
        
        
class ViewDepartment(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('web/department/viewdepartment.html')
        self.response.write(template.render())

class ViewCourse(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('web/course/viewcourse.html')
        self.response.write(template.render())


app = webapp2.WSGIApplication([
    ('/api', APIPage),
    ('/api/student', StudentHandler),
    ('/api/student/courses', StudentCourseLister),
    ('/api/enrollstudent', StudentEnroller),
    ('/api/dropstudent', StudentDropper),
    ('/api/instructor', InstructorHandler),
    ('/api/department', DepartmentHandler),
    ('/api/department/courses', DepartmentsCourses),
    ('/api/course', CourseHandler),
    ('/api/course/students', CourseStudentLister),
    ('/api/quarter', QuarterHandler),
    ('/api/quarter/courses', QuartersCourses),
    ('/student', StudentWebPage),
    ('/student/add', StudentAdd),
    ('/student/enroll', EnrollWebPage),
    ('/student/drop', DropWebPage),
    ('/student/view', ViewStudent),
    ('/instructor', InstructorWebPage),
    ('/instructor/add', InstructorAdd),
    ('/instructor/view', ViewInstructor),
    ('/department', DepartmentWebPage),
    ('/department/add', DepartmentAdd),
    ('/department/offered', DepartmentOfferedWebPage),
    ('/department/view', ViewDepartment),
    ('/course', CourseWebPage),
    ('/course/offered', CourseOfferedWebPage),
    ('/course/view', ViewCourse),
    ('/quarter', QuarterWebPage),
    ('/quarter/offered', QuarterCoursesOffered),
    ('/quarter/view', ViewQuarter),
    ('/quarter/add', QuarterAdd),
    ('/', MainPage)
    
], debug=True)