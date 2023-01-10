import pandas as pd
import copy
from encodingInput import *

day = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri']
time = ['8:00 - 9:30', '9:45 - 11:15', '1:15 - 2:45', '3:00 - 4:30', '4:45 - 6:15', '6:30 - 8:00']

def optimalSchedule(tempClassroomSchedule, classroom):
    #arrange 2-days schedule 
    for time in tempClassroomSchedule: #check each timeslot
        if len(tempClassroomSchedule[time]) < 2: #if there aren't any 2 days that contain the timeslot --> Check another
            continue
        else: #sessionA: the earliest, sessionB: arrange accordingly
            sessionA = classroom + str(tempClassroomSchedule[time][0]) + str(time)
            if len(tempClassroomSchedule[time]) >= 3:
                sessionB = classroom + str(tempClassroomSchedule[time][2]) + str(time)
            else:
                sessionB = classroom + str(tempClassroomSchedule[time][-1]) + str(time)
            result = [sessionA, sessionB]
            return result
            
    #can't arrange into 2-days schedule --> arrange into 1-day schedule (3-hours course)
    for index in range(1, 4): #check 3 different 3-hours timeslots 
        if (str(index) not in tempClassroomSchedule) | (str(index + 1) not in tempClassroomSchedule):
            continue 
        elif (len(tempClassroomSchedule[str(index)]) == 0) | (len(tempClassroomSchedule[str(index + 1)]) == 0):
            continue
        pivot = tempClassroomSchedule[str(index)][0]
        if tempClassroomSchedule[str(index + 1)][0] == pivot:
            sessionA = classroom + str(tempClassroomSchedule[str(index)][0]) + str(index)
            sessionB = classroom + str(tempClassroomSchedule[str(index + 1)][0]) + str(index + 1)
            result = [sessionA, sessionB]
            return result
    return [] #can't arrange

# def suggestion(course, courseDetail, conflictList):
    

def arrangeTime(course, faculty, conflictList, tempClassroomSchedule):
    conflict = conflictList[faculty] #conflictTime based on faculty
    for classroom in tempClassroomSchedule:
        if int(classroom[:2]) < int(course[-2:]): #if classroom's capacity < course's capacity --> check the next classroom
            continue
        else:
            for time in conflict: #max = 4
                if (time[1] in (tempClassroomSchedule[classroom])):
                    if (time[0] in tempClassroomSchedule[classroom][time[1]]):
                        tempClassroomSchedule[classroom][time[1]].remove(time[0]) #remove conflict --> available time slots
            schedule = optimalSchedule(tempClassroomSchedule[classroom], classroom)
            if len(schedule) == 2: #if can arrange: break, else: check the next classroom
                return schedule
    # schedule = suggestion(course, courseDetail, conflictList)
    return []


def updateClassroomSchedule(scheduleList, schedule):
    #session: 45441 --> session[:-2] = classroom Code, session[-1] = time, session[-2] = day
    for session in schedule:
        scheduleList[session[:-2]][session[-1]].remove(session[-2]) 
        if len(scheduleList[session[:-2]][session[-1]]) == 0: #remove empty time slot
            scheduleList[session[:-2]].pop(session[-1])
        if len(scheduleList[session[:-2]]) == 0: #remove empty classroom
            scheduleList.pop(session[:-2])
    return scheduleList

def updateConflict(conflictList, schedule, faculty):
    for session in schedule:
        conflictList[faculty].append(session[-2:])
    return conflictList

def printOutput(schedule):
    classroom = schedule[0][:-2]
    currentDayA = day[int(schedule[0][-2]) - 1]
    currentDayB = day[int(schedule[1][-2]) - 1]
    currentTimeA = time[int(schedule[0][-1]) - 1]
    currentTimeB = time[int(schedule[1][-1]) - 1]
    return classroom, currentDayA, currentDayB, currentTimeA, currentTimeB

def arrangeCourse(classroomPath, coursePath, resultPath):
    canArrange = True
    #decoding schedule
    courseName, courseCapacity, courseDay, courseTime, courseClassroom = [], [], [], [], []

    classroomSchedule, backupCR, courseList, conflictList, courseFaculty = main(classroomPath, coursePath)

    for courseIndex in range (len(courseList)):
        add = False
        course = courseList[courseIndex]
        faculty = courseFaculty[courseIndex]

        #append the course information
        courseName.append(course[:-3])
        courseCapacity.append(course[-2:])

        #scheduling
        tempClassroomSchedule = copy.deepcopy(classroomSchedule)
        schedule = arrangeTime(course, faculty, conflictList, tempClassroomSchedule) #schedule format: 45115 --> classroom = sechdule[:-2], day = schedule[-2], time = schedule[-1]

        #if can't arrange into any timeslot
        if schedule == []: 
            canArrange = False
            tempBackupCR = copy.deepcopy(backupCR)
            schedule = arrangeTime(course, faculty, conflictList, tempBackupCR)
            if schedule == []:
                print('Do not have enough classroom')
                continue
            else:
                add = True

        classroom, currentDayA, currentDayB, currentTimeA, currentTimeB = printOutput(schedule)
        
        
        #schedule of the course 
        courseClassroom.append(classroom)

        #day and time
        if currentDayA == currentDayB: #the same day
            updatedTimeA = list(map(str, currentTimeA.split(' - ')))[0]
            updatedTimeB = list(map(str, currentTimeB.split(' - ')))[1]
            courseDay.append(currentDayA)
            courseTime.append(updatedTimeA + ' - ' + updatedTimeB)
            if add:
                print('Need to add the slot ' + updatedTimeA + ' - ' + updatedTimeB + ' on ' + currentDayA + ' for classroom ' + schedule[0][:3] + ' for course ' + course)
        else: 
            courseDay.append(currentDayA + '_' + currentDayB)
            courseTime.append(currentTimeA)
            if add:
                print('Need to add slot ' + currentTimeA + ' on ' + currentDayA + ' and ' + currentDayB + ' for classroom ' + schedule[0][:3] + ' for course ' + course)

        if add == False:
            classroomSchedule = updateClassroomSchedule(classroomSchedule, schedule) #remove taken time slots 
        elif add == True:
            backupCR = updateClassroomSchedule(backupCR, schedule)

        conflictList = updateConflict(conflictList, schedule, faculty) #update faculty's schedule (conflict list)

    result = {'Course Name': courseName, 'Course Faculty': courseFaculty, 'Course Capacity': courseCapacity, 'Day': courseDay, 'Time': courseTime, 'Classroom': courseClassroom}
    pd.DataFrame(result).to_csv(resultPath)
    return canArrange

# def test():
#     courseInfo = generateCourseInfo()
#     courseList = generateCourseCode()
#     conflictList = {'Truong Trung Kien': ['13', '33']}
#     classroomSchedule = generateClassroomSchedule()
#     course = 'CS203_Fall2022_S01_40'
#     tempClassroomSchedule = classroomSchedule.copy()
#     schedule = arrangeTime(course, courseInfo[course], conflictList, tempClassroomSchedule) #schedule of the course
#     courseInfo[course]['Schedule']  = schedule #update schedule in courseInfo
#     classroomSchedule = updateClassroomSchedule(classroomSchedule, schedule, course)
#     faculty = courseInfo[course]['Faculty']
#     conflictList = updateConflict(conflictList, schedule, faculty)
#     return courseInfo

