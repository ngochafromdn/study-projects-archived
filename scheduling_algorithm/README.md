
Information about the project : Read the report or the beamer slide below


# INSTRUCTIONS :

## Generate test case
Go to generateTestCase.py and run the function below where n is number of courses, m is
number of classrooms, classroomPath is classroom’s input path of your desire and coursePath
is course’s input path of your desire <br>

genTestCase (n , m , classroomPath , coursePath ) <br>

## Run the scheduling function

In arrange.py, print the function below where classroomPath is the input classroom path,
coursePath is the input course path, resultPath is the output path. <br>
 
 print(arrangeCourse(classroomPath , coursePath , resultPath )) <br>

After running, if our screen prints True, it only generates the result in the CSV output path. If
it prints False, it will show the suggestion (adding timeslots or adding classroom) and generate
the result in the output path <br>


_______________________________________________________________________________________________________________

# ALGORITHMS <br />

## INPUT:<br />
    - Courses' information (n courses): Course name, Faculty, Capacity <br />
    - Classrooms' information (m courses): Classroom name, Capacity, Schedule <br />

## OUTPUT: <br />
    - Can arrange --> True/False <br />
    - If true: Print schedule <br />
    - If false: Suggestion <br />

## DATA FORMAT: <br />
    - Courses' information: {course A: {faculty: faculty A, schedule: [sessionA, sessionB]}} <br />
    - Classrooms' schedule: {classroomA_capacity: {timeslot A: [day1, day 2]}} <br />
    - Conflict list (faculty's schedule): {faculty A: [day1-timeslotA, day2-timeslotB]} <br />
## Decoding

With csv file of n courses with course code, lecturer, capacity, and csv file of m classrooms with
classroom name, available time, our code is decoded as follows: <br />
 Course_list: List of all courses code with its capacity. This list is sorted ascendingly by
capacity. <br />
 Conflicting_dict: ffaculties’sname: Œtimeslotsçg. <br />
 Classroom_schedule: List of timeslots of 1:5 hours with classroom name, available time <br />
(day, timestamp). This list is generated ascendingly by capacity and time. <br />
1
 Back_up_Classroom_schedule: List of backup timeslots of 1:5 hours with classroom name,
available time (day, timestamp). This list is generated ascendingly by capacity and time.
 <br />

 Classroom_schedule only includes slots end before 4:30 p.m and Back_up_Classroom_schedule
includes the slots start after 4:45 p.m. <br />


This assumption can be set up differently by user. <br />

Our procedure is designed in two steps: generate a function that will find suitable timeslots
for each course which will satisfy our conditions. Then, in the main function, run the previous
function for all courses to get the final result. <br />

If the main algorithm print False, suggestions for
backup timeslots (night classes) or adding classroooms will be printed. Else, the result where
satisfy all constrains will be generated. <br />

Combining the encoding and procedure above, this is the pseudocode for scheduling problem,
which includes an extra function and the main algorithm <br />

## Pseudocode : 

<img width="551" alt="Ảnh chụp Màn hình 2022-12-23 lúc 23 00 49" src="https://user-images.githubusercontent.com/61641363/209364307-accb174b-faa9-483b-bcd3-6c5e98ed00e4.png"> 

<img width="483" alt="Ảnh chụp Màn hình 2022-12-23 lúc 23 01 17" src="https://user-images.githubusercontent.com/61641363/209364353-533c8b88-4067-4fa0-a69c-05736f3d0283.png">

_______________________________________________________________________________________________________________

## Report 

[CS102___Final_project _Read_me.pdf](https://github.com/ngantran03/algorithm_finalproject/files/10296106/CS102___Final_project._Read_me.pdf)

## Slide
[CS102___Final_project___Beamer (2).pdf](https://github.com/ngantran03/algorithm_finalproject/files/10296111/CS102___Final_project___Beamer.2.pdf)



