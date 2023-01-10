import csv
import pandas as pd
import json

#input the annotated scene file here by changing Annotated_scene_file to the file name
data_scene = pd.read_csv(Annotated_scene_file) 

def percentage_data_scene():
    #function which prints the 4 information below 
    print('Number of scene:',data_scene.count()[1])
    print('Average time per scene:',data_scene['duration (seconds)'].mean())
    print('Percetage of food existing over all',data_scene['food_focus_existing (1 or 0)'].sum()/data_scene['food_focus_existing (1 or 0)'].count())
    print('Percetage of Youtuber existing over all',data_scene['Youtuber_existing (1 or 0)'].sum()/data_scene['Youtuber_existing (1 or 0)'].count())
def scene_objects(AI_visual_file):
    #function which creates top 3 places in 6 lists( name_of_place, percentage_of_place)
    #input the AI_visual_file here to the data_visual variable
    data_visual = [json.loads(line) for line in open(AI_visual_file, 'r')]
    #top 3 scene in 6 lists from max_1, max_value_1... to max_value_3
    max1=[] #list includes the maximum scenes
    max_value1=[]
    max2=[]
    max_value2=[]
    max3=[]
    max_value3=[]
    begin_scene=0
    for index in range(0,data_scene['duration (seconds)'].count()):
        #the function which go to each scene to take the color and its value
        new_dict={}
        #the dict which contains the color and its total value in each annotated scene
        sorted_dict={}
        #new dict after being sorted
        sorted_keys={}
        #keys of the sorted_dict
        for name_of_scene in range(data_scene['Start_time (seconds)'][index],data_scene['end_time (seconds)'][index]+1,1):
                for scene in data_visual[name_of_scene]['imgfeatures']['classify'].keys():
                    if scene not in new_dict.keys():
                        x=data_visual[name_of_scene]['imgfeatures']['classify'][scene]
                        new_dict.update({scene:x})
                    else:
                        new_dict[scene]=data_visual[name_of_scene]['imgfeatures']['classify'][scene]+new_dict[scene]
                sorted_keys = sorted(new_dict, key=new_dict.get)  
                for key in sorted_keys:
                     #sort the new dict from smallest to highest
                    sorted_dict[key] = new_dict[key]
        max1.append(list(sorted_dict.keys())[-1])
        max_value1.append(sorted_dict[list(sorted_dict.keys())[-1]])
        max2.append(list(sorted_dict.keys())[-2])
        max_value2.append(sorted_dict[list(sorted_dict.keys())[-2]])
        max3.append(list(sorted_dict.keys())[-1])
        max_value3.append(sorted_dict[list(sorted_dict.keys())[-3]])
    return max1, max_value1, max2, max_value2, max3, max_value3

def add_objects_value_function(AI_visual_file):
#add 6 column lists to the scene_color data frame
    (a,b,c,d,e,f)=scene_objects(AI_visual_file)
    data_scene['max_1']=a
    data_scene['max_1_value']=b
    data_scene['max_2']=c
    data_scene['max_2_value']=d
    data_scene['max_3']=e
    data_scene['max_3_value']=f

def write_excel_file(FileName):
#function to write the excel file from data_scene variable
    import xlsxwriter
    data_scene.to_excel(FileName, engine='xlsxwriter')
"""
To extract a place excel file and print the information:
1. Input the annotated scene
2. Run percentage_data_scene() function if you want to see information of the file
3. Run the add_objects_value_function(AI_visual_file) with argument AI_visual_file, then run write_excel_file(FileName) with the name of file following with.xlsx 
"""
