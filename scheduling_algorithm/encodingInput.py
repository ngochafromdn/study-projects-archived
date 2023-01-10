import pandas as pd

day = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri']
time = ['8:00 - 9:30', '9:45 - 11:15', '1:15 - 2:45', '3:00 - 4:30', '4:45 - 6:15', '6:30 - 8:00']

def readInput(classroomPath, coursePath):
    classroomList = pd.read_csv(classroomPath)
    classroomList.sort_values(by = 'capacity', inplace=True)

    # classroom input: Classroom name, Capacity, Available Time
    # Step 1: Define classroom code based on capacity
    # Step 2: Define classroom available timeslot based on classroom code and time

    courseData = pd.read_csv(coursePath)
    return classroomList, courseData
#courseData input: Course name, Faculty, Capacity
#Step 1: Generate course code for each course (courseName + capacity)
#Step 2: Generate conflicting courses list based on faculties

def generateClassroomSchedule(classroomList): #format: {classroom: {timeslot: day 1, day 2}}
    classroomSchedule = {} #list of different timeslot
    backupCR = {}
    code = 1
    for classroomName in classroomList['Classroom'].tolist():
        classroomCode = str(classroomList['capacity'][classroomList['Classroom'] == classroomName].iloc[0]) + str(code)
        classroomSchedule[classroomCode], backupCR[classroomCode] = {}, {}
        time = str(classroomList['time'][classroomList['Classroom'] == classroomName].iloc[0])
        if time == 'all':
            for i in range (1, 5):  #from timeslot 1 - 4 in a day
                classroomSchedule[classroomCode][str(i)] = []
                for j in range (1, 6): #from day 1 - day 5 in a week
                    classroomSchedule[classroomCode][str(i)].append(str(j))
            for i in range (5, 7):
                backupCR[classroomCode][str(i)] = []
                for j in range (1, 6): #from day 1 - day 5 in a week
                    backupCR[classroomCode][str(i)].append(str(j))
        else:
            schedule = list(map(str, time.strip().split(' ')))
            for eachTime in schedule:
                day, time = map(str, eachTime.split('_'))
                if day not in classroomSchedule:
                    classroomSchedule[classroomCode][time] = [day]
                else:
                    classroomSchedule[classroomCode][time].append(day)
        code += 1
    return classroomSchedule, backupCR    

def generateCourseCode(courseData):
    courseList = []
    for i in range (len(courseData['Course Code'])):
        courseInfo = courseData.loc[i]
        courseList.append(str(courseInfo['Course Code']) + '_' + str(courseInfo['Capacity']))
    return courseList

# def facultyInformation(courseData):
#     conflictList = {}
#     facultyList = courseData['Faculty & Visiting Faculty'].tolist()
#     haveMeeting = str(input('Do all the faculties have a meeting?'))
#     if haveMeeting == 'True': 
#         plaintextDay = str(input('Please enter the meeting day: '))
#         while plaintextDay not in day:
#             plaintextDay = str(input('Please enter the meeting day: '))
#         for i in range (len(day)):
#             if plaintextDay == day[i]:
#                 encodingDay = str(i + 1)
#                 break
#         plaintextTime = str(input('Please enter the meeting time: '))
#         while plaintextTime not in time:
#             plaintextTime = str(input('Please enter the meeting time: '))
#         for i in range (len(time)):
#             if plaintextTime == time[i]:
#                 encodingTime = str(i + 1)
#                 break
#     for faculty in courseData['Faculty & Visiting Faculty'].unique().tolist():
#         conflictList[faculty] = []
#         if haveMeeting == 'True':
#             conflictList[faculty].append(encodingDay + encodingTime)
#     return conflictList, facultyList

def testfacultyInformation(courseData):
    conflictList = {}
    facultyList = courseData['Faculty & Visiting Faculty'].tolist()
    encodingDay = str(1)
    encodingTime = str(3)
    for faculty in courseData['Faculty & Visiting Faculty'].unique().tolist():
        conflictList[faculty] = []
        conflictList[faculty].append(encodingDay + encodingTime)
    return conflictList, facultyList

def main(classroomPath, coursePath):
    #input: 2 input files
    #output: classroomSchedule, backupCR, courseList, conflictList, facultyList
    classroomList, courseData = readInput(classroomPath, coursePath)
    classroomSchedule, backupCR = generateClassroomSchedule(classroomList)
    courseList = generateCourseCode(courseData)
    conflictList, facultyList = testfacultyInformation(courseData)
    return classroomSchedule, backupCR, courseList, conflictList, facultyList