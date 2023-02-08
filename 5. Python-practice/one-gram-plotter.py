'''
This Python function are to track the Internaltion Space Station's current position, posting updates every 10 secoonds.
Name: Le Thi Hong Ha (ID:210205), Nguyen Hoang Ngoc Ha (ID:210206)
Time : 24 hours
'''
# import one_gram_reader
# years, counts = one_gram_reader.read_wfile("request", [2000, 2010], "very_short.csv")
# total = one_gram_reader.read_total_counts("total_counts.csv")

def normalize_counts(years, counts, total):
    '''return the normalized word count'''
    total_during_year=[]
    for i in range(len(counts)):
        total_during_year.append(counts[i]/total[years[i]])
    return total_during_year

def plot_words(words, year_range, wfile, tfile):
    '''plot the relative popularity of words over time'''
    import matplotlib.pyplot as plt
    import one_gram_reader
    total_during_year=[]
    for i in range(len(words)):
        years[i], counts[i] = one_gram_reader.read_wfile(words[i], year_range, wfile)
        total[i]= one_gram_reader.read_total_counts(tfile)
        total_during_year.append(normalize_counts(years[i],counts[i],total[i]))
        plt.savefig('abc.png')
        plt.plot(years[i],total_during_year[i], label = words[i])
    plt.legend()
    plt.show()

def plot_relative_popularity(word1, word2, year_range, wfile, tfile):
    import matplotlib.pyplot as plt
    import one_gram_reader
    for word in [word1, word2]:
        if total_during_year ==[]:
            years, counts = one_gram_reader.read_wfile(word, year_range, wfile)
            total= one_gram_reader.read_total_counts(tfile)
            total_during_year.append(normalize_counts(years,counts,total))
        else:
            for i in range(len(total_during_year)):
                years, counts = one_gram_reader.read_wfile(word, year_range, wfile)
                total= one_gram_reader.read_total_counts(tfile)
                final_total_during_year.append(total_during_year[i]/normalize_counts(years,counts,total)[i])
    plt.savefig('cde.png')
    plt.plot(years,final_total_during_year, label = word1+'/'+word2)
    plt.legend()
    plt.show()