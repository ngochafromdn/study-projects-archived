"""
Linear Algebra final project implementation in a real market in a real-time data
Author: Linear Olympia team
    - Than Doan Thuan
    - Bui Doan Khanh Quan
    - Nguyen Hoang Ngoc Ha
    - Nguyen Dang Tien Dung
    - Ngo Phuong Nam
"""

# Initially, import necessary packages as well as download them in the local machine.
from tvDatafeed import TvDatafeed, Interval # This package helps to read the real price data in Tradingview site
import datetime
import pandas as pd
import numpy as np
import statistics as st
tv = TvDatafeed()
#username = 'user', password = 'LinearOlympia2021'

# First of all, prompt the user to input all the stocks he or she wish to invest
n = int(input("Please input the number of stocks: "))
price_list = []
for i in range(n):
    # In order to get the data successfully in Tradingview, for each stock, the user should prompt
    # the three letters ticker symbol of the stock and its exchange like HOSE, HNX, UPCOM
    stock = input("Please input the ticker symbol: ")
    exchange = input("Please input the exchange of stock: ")
    x = tv.get_hist(stock,exchange)
    # We focus on the closing price
    price_list.append(x["close"])

# Second of all, find the return and variance for each stock
# Return = Pt / Pt-1
return_list = []
variance_list = []
all_return_list = []
for x_stock in price_list:
    x = []
    for i in range(1,len(x_stock)):
        x.append((x_stock[i]/x_stock[i-1])-1)
    return_list.append(st.mean(x))
    variance_list.append(st.variance(x))
    all_return_list.append(x)

# Third of all, construct the covariance matrix from the first stock to the nth stock
covariance_matrix = np.cov(np.array(all_return_list))
if np.linalg.det(covariance_matrix) != 0:
    inv_cor_matrix = np.linalg.inv(covariance_matrix)
else:
    inv_cor_matrix = np.linalg.pinv(covariance_matrix)

# Prepare data for (6) formula in the model
one_vector_horizontal = np.array([1]*n)
one_vector_vertical = one_vector_horizontal.reshape(n,1)

return_list_vertical = np.array(return_list).reshape(n,1)

result = []
multiply_1 = inv_cor_matrix@one_vector_vertical
determinor = one_vector_horizontal@inv_cor_matrix@one_vector_vertical
multiply_return = inv_cor_matrix@return_list_vertical
multiply_1_1= one_vector_horizontal@inv_cor_matrix@return_list_vertical

t = 0
# These lists correspond to the five columns on the right of the table result from the paper
t_list = []
sum_list = []
mean_list = []
variance_list = []
maximum_list = []
ratio_list = []
flag = True

# Iterate until there is a negative weight
while(flag):
    weight = (1 / determinor[0]) * multiply_1 + t * (multiply_return - ((multiply_1_1[0] / determinor[0]) * multiply_1))
    for each_weight in weight:
        if each_weight < 0:
            flag = False
            break
    if flag == True:
        t_list.append(t)
        result.append(weight)
        t += 0.001
        
        # Find the value of the sum column. In theory, the summation on the weight vector should be 1.
        sum_list.append(np.transpose(weight) @ one_vector_vertical)
        
        # Find the mean of return with the inclusion of the weight
        # Formula: mean = r1.w1 + r2.w2 + ... + rn.wn
        s = 0
        for i in range(len(return_list)):
            s += return_list[i]*weight[i][0]
        mean_list.append(s)
        
        # Find the variance of return 
        variance_list.append(np.transpose(weight) @ covariance_matrix @ weight)
        # Find the maximum. It is equivalent to the subtraction between the mean and the variance
        maximum_list.append(mean_list[-1] - variance_list[-1])
        # Find the ratio. It is equivalent to the subtraction between the mean and the variance
        ratio_list.append(mean_list[-1]/variance_list[-1])

# In theory, the optimal portfolio is the one having the largest ratio value
biggest_ratio = max(list(ratio_list)) # Find the largest ratio value
# Create a data frame to show all the weight possibles
data  = pd.DataFrame({"t":t_list, "weight": result, "sum": sum_list, "mean": mean_list, "variance": variance_list, 'maximum': maximum_list, "ratio": ratio_list}) 

# Locate the index of the largest ratio
for i in range(len(ratio_list)):
    if ratio_list[i] == biggest_ratio:
        index = i

# Convert the result to csv file if necessary
data.to_csv('file_name.csv', encoding='utf-8')
# Pring the result which is the optimal portfolio
print(data.iloc[index,:])
        
    
