import pandas as pd
import random

def generateClassroomList(m, path):
    #Input: m classrooms
    #output: the classroom list (like the input file)
    classroom, capacity, time = [], [], []
    classroomSize = [10, 30, 30, 45, 45, 50, 50, 50, 50, 50, 50]
    if m//11 > 0:
        for i in range (m//11):
            for j in range (11):
                classroom.append('Classroom ' + str(j))
                capacity.append(classroomSize[j])
                time.append('all')
    for i in range (m%11):
        classroom.append('Classroom ' + str(m/11 + i))
        capacity.append(50)
        time.append('all')
    result = {'Classroom': classroom, 'capacity': capacity, 'time': time}
    pd.DataFrame(result).to_csv(path)

def generateCourseList(n, path):
    #input n course
    #output: input file
    courseCode, courseFaculty, courseCapacity = [], [], []
    allCapacity = [10, 25, 40, 50]
    allFaculty = []
    for i in range ((n - n//10)//2 + 1):
        allFaculty.append('Faculty ' + str(i))
        allFaculty.append('Faculty ' + str(i))
    for i in range (n//10):
        allFaculty.append('Faculty ' + str(n - n//10 + i))
    for i in range (n):
        courseCode.append('Course ' + str(i))
        facultyNum = random.randint(0, len(allFaculty) - 1) if len(allFaculty) - 1 > 0 else 0
        courseFaculty.append(allFaculty[facultyNum])
        allFaculty.pop(facultyNum)
        courseCapacity.append(allCapacity[random.randint(0, 3)])
    result = {'Course Code': courseCode, 'Faculty & Visiting Faculty': courseFaculty, 'Capacity': courseCapacity}
    pd.DataFrame(result).to_csv(path)

def genTestCase(n, m, classroomPath, coursePath):
    print(generateClassroomList(m, classroomPath))
    print(generateCourseList(n, coursePath))