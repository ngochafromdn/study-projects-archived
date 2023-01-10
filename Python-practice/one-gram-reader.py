'''
This Python function is to track the relative popularity of words over time..
Name: Le Thi Hong Ha (ID:210205), Nguyen Hoang Ngoc Ha (ID:210206)
Time : 2 hours
'''
def read_wfile(word, year_range, wfile):
    '''read in the wfile provided and return two lists representing the counts and years for the word provided'''
    import csv
    years=[]
    counts=[]
    with open(wfile, 'r') as file:
        reader = csv.reader(file, delimiter = '\t')
        for row in reader:
            if row[0]==word:
                if (int(row[1]) <= year_range[1]) and (int(row[1])>=year_range[0]):
                    years.append(int(row[1]))
                    counts.append(int(row[2]))
        return years, counts  

def read_total_counts(tfile):
    '''read in the tfile provided and return a dictionary of total word counts.'''
    import csv
    total_counts={}
    with open(tfile, 'r') as file:
        reader = csv.reader(file, delimiter = ',')
        for row in reader:
            total_counts[int(row[0])] = int(row[1])
    return total_counts