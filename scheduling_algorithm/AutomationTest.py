from encodingInput import *
from generateTestCase import *
from arrange import *
import pandas as pd
import time 

testCase, result, runTime, nList, mList = [], [], [], [], []
n = 5000
times = 20

for m in range (564, 569):
    for i in range (times):
        mList.append(m)
        nList.append(n)
        testCase.append(i)
        classroomPath = '/Users/lap12021/Desktop/algorithm_finalproject/Test case/Input/classroom_case' + str(i) + 'n' + str(n) + 'm' + str(m)
        coursePath =  '/Users/lap12021/Desktop/algorithm_finalproject/Test case/Input/course_case' + str(i) + 'n' + str(n) + 'm' + str(m)
        resultPath = '/Users/lap12021/Desktop/algorithm_finalproject/Test case/Output/case' + str(i) + 'n' + str(n) + 'm' + str(m)
        genTestCase(n, m, classroomPath, coursePath)
        start_time = time.time()
        canArrange = arrangeCourse(classroomPath, coursePath, resultPath)
        run_time = time.time() - start_time
        result.append(canArrange)
        runTime.append(run_time)
        print('Done' + str(m) + str(i))
outputFile = {'Test case': testCase, 'Can Arrange?': result, 'Running time': runTime, 'n': nList, 'm': mList}
pd.DataFrame(outputFile).to_csv('/Users/lap12021/Desktop/algorithm_finalproject/Test case/case1_' + 'n=' + str(n) + '.csv')
