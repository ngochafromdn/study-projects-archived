#Link to pseudocode : https://docs.google.com/document/d/13Lykak17ZtCOIo895I_IyvRv7N71XhVDoHSyd5oH-30/edit
import pandas as pd
import copy
import json 
import sys

timeSlotDF = pd.read_csv(r'timeslot.csv')
courseDF = pd.read_csv(r'course_list_final.csv')
jsonFile = open('Conflicting_dict_final.json')
conflictingDict = json.load(jsonFile)

def capaCheck(capaCourse, capaTimeSlot):
    if (int(capaCourse) < capaTimeSlot):
        return True
    else:
        return False

def naiveAlg(timeSlot, course, conflictDict):
    
    result = ''

    courseCode = course['Course Code'].values.tolist() # A
    capaTimeSlot = timeSlot['capacity'].values.tolist()
    dayTimeSlot = timeSlot['day'].values.tolist()
    timeTimeSlot = timeSlot['time'].values.tolist()

    lenCourseCode = len(courseCode) # n
    lenTimeSlot = len(timeSlot['classroom_name']) # m

    if (lenCourseCode > lenTimeSlot):

        print('Increase at least ', lenTimeSlot - lenCourseCode, ' timeslot')
        return False, 0
    
    else:
        
        emptyList = [None] * (lenTimeSlot - lenCourseCode)
        courseCode = courseCode + emptyList
        minCapaConflict = 10e9
        minLecturerConflict = 10e9
        
        #Perm
        pool = tuple(courseCode)

        r = None
        n = len(pool)
        r = n if r is None else r   
        if r > n:
            pass
        indices = list(range(n))
        cycles = list(range(n, n-r, -1))

        perm = tuple(pool[i] for i in indices[:r]) # Original one

        #####
        capaConflictHere = 0 
        lecturerConflictHere = 0

        for ind in range(len(perm)):

            if perm[ind] == None:
                continue

            else: 
                if capaCheck(perm[ind][-2:], capaTimeSlot[ind]):
                    continue

                else: 

                    capaConflictHere += 1

        if minCapaConflict > capaConflictHere:
                minCapaConflict = capaConflictHere
                result = perm

        for lecturer, lectClass in conflictDict.items(): 

            if len(lectClass) == 1:
                continue

            else: 

                lectDayTime = []
                for cl in lectClass:

                    pos = perm.index(cl)
                    lectDayTime.append((dayTimeSlot[pos], timeTimeSlot[pos]))
                
                for no in range(len(lectClass) - 1):
                    for no1 in range(no + 1, len(lectClass)):

                        if (lectDayTime[no] == lectDayTime[no1]):
                            lecturerConflictHere += 1
                
        if (minCapaConflict == capaConflictHere) and (minLecturerConflict > lecturerConflictHere):
            minLecturerConflict = lecturerConflictHere
            result = perm

        if (minCapaConflict == 0) and (minLecturerConflict == 0):
            return True, result
        #####

        while n:

            for i in reversed(range(r)):

                cycles[i] -= 1

                if cycles[i] == 0:

                    indices[i:] = indices[i+1:] + indices[i:i+1]
                    cycles[i] = n - i

                else:

                    j = cycles[i]
                    indices[i], indices[-j] = indices[-j], indices[i]
                    perm = (tuple(pool[i] for i in indices[:r]))

                    #####

                    capaConflictHere = 0 
                    lecturerConflictHere = 0

                    for ind in range(len(perm)):

                        if perm[ind] == None:
                            continue

                        else: 

                            if capaCheck(perm[ind][-2:], capaTimeSlot[ind]):
                                continue

                            else: 

                                capaConflictHere += 1

                    if minCapaConflict > capaConflictHere:
                            minCapaConflict = capaConflictHere
                            result = perm
                    
                

                    for lecturer, lectClass in conflictDict.items(): 

                        if len(lectClass) == 1:
                            continue

                        else: 

                            lectDayTime = []
                            for cl in lectClass:

                                pos = perm.index(cl)
                                lectDayTime.append((dayTimeSlot[pos], timeTimeSlot[pos]))
                            
                            for no in range(len(lectClass) - 1):
                                for no1 in range(no + 1, len(lectClass)):

                                    if (lectDayTime[no] == lectDayTime[no1]):
                                        lecturerConflictHere += 1
                            
                    if (minCapaConflict == capaConflictHere) and (minLecturerConflict > lecturerConflictHere):
                        minLecturerConflict = lecturerConflictHere
                        result = perm

                                    


                    if (minCapaConflict == 0) and (minLecturerConflict == 0):
                        return True, result
                    #####


                    break
            else:
                break
        #EndPerm

    print('Need to increase ', minCapaConflict, ' suitable classroom and ', minLecturerConflict, ' timeslot')

    return False, result


print(naiveAlg(timeSlotDF, courseDF, conflictingDict))



