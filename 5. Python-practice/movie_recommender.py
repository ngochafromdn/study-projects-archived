'''
This Python function is to solve homework 7: recommend the movies for users
Name: Le Thi Hong Ha (ID:210205), Nguyen Hoang Ngoc Ha (ID:210206)
Time : 2 hours
'''

fileName = 'ratings.txt'

def create_user_list(fileName):
    '''read a text file and return its database into a list of dictionaries'''
    try:
        with open(fileName,'r') as file:
            user_list=[]
            for i in range(943):
                user_list.append(dict())
            for row in file:
                new_row = row.split(' ')
                title=''
                for j in range(1,len(new_row)-1):
                    title += ' '+new_row[j]
                user_list[int(new_row[0])][title.lstrip(' ')] = int(new_row[-1].rstrip('\n'))
            return user_list
    except FileNotFoundError:
        print('This file is not found')
        return []


def rate_film(user_ratings={}):
    '''transfer the user input to a dict'''
    title = input("Please enter the title of a movie: ")
    while title != "":
        rating = input("Please enter your rating for the movie:")
        while rating not in ['-5','-3','1','3','5']:
            print("Sorry -- only permitted values are -5, -3, 1, 3, 5")
            rating = input("Please enter your rating for the movie: ")
        user_ratings.update({title:int(rating)})
        title = input("Please enter the title of a movie: ")
    return user_ratings

        
def compute_dot_product(vec1,vec2):
    '''compute the dot product of two vectors'''
    dot = 0
    for i in vec1:
        if i in vec2:
            x = vec1[i] * vec2[i]
        else:
            x = 0
        dot += x
    return dot


def recommend_movies():
    '''print out the recommended list of movies based on the new user's rating'''
    print ("*** Welcome to the movie recommender engine ***")
    user_list = create_user_list(fileName)
    new_user = rate_film(user_ratings={})
    highest_dot = 0
    nearest_id = 0
    for i in range(943):
        dot_product = compute_dot_product(user_list[i],new_user)
        if dot_product > highest_dot:
            highest_dot = dot_product
            nearest_id = i
    list_of_recommendation = []
    for rating in user_list[nearest_id]:
        if rating not in new_user and user_list[nearest_id][rating] == 5:
            list_of_recommendation.append(rating)
    return list_of_recommendation

