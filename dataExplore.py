import pandas as pd

# import numpy as np

# import os

# print (os.getcwd())



# n1 = np.array([1,3,3,4])

# fname = '/Users/sunny/Downloads/sedata.csv'
fname = '/Users/sunny/Documents/trans.csv'

fname = '/Users/sunny/Documents/trans.xlsx'


# fname2 = "mycsv.txt"

# df1 = pd.read_csv(fname)
df1 = pd.read_excel(fname)

print (df1)
result= df1.pivot(index='ID', columns='Product', values='Sales')

# result

print 'hello'

# print (df1)

'''
df1 = df1[0:25]

print (df1.shape)

print(df1.columns)

v1 = df1['num_inbound']

v2 = df1['num_outbound']

ans = v1 + v2



print ('printing the ans: ', ans)

posdf = df1[df1['first_agent_experience_days'] >= 0]

# data = posdf.fillna('this is empty')

# data = posdf.fillna(- 1)
#
# # posdf.drop_duplicates(keep=False,inplace=True)
#
# data.drop_duplicates(subset="First Name", keep=False, inplace=True)
#
# posdf.sort
#
# # if data == '0' or 0:
# #
# #     data = posdf.fillna('this is 0')



# print (data)

# posdf.isnull()

# posdf = df1['first_agent_experience_days'] >= 0

# print('posdf', posdf)

# print (posdf.shape)
#
# # dropDf = posdf.drop(['notes_concatinated', 'first_response_time', 'Unnamed: 21' ],1)
#
# print (dropDf.shape)
#
# rowsRemoved = df1.shape[0] - posdf.shape[0]
#
# print ('print  number of rows removed are:  ',rowsRemoved)




# print (df1)

# print (df1.head())

# n1 = df1.to_numpy()

# print(n1.shape)

# print (n1[0:5,10:12])

# n1 [:, n1[1]]

# df2 = pd.read_csv("mycsv2.txt")

# n2 = df2.to_numpy()

# n3 = n1 + n2

# print ("orgininal")

# print (n1)

# print (n2)

# print ("post addition")

# print (n3)

# print (df1)

# print (n1)

# print (n1.shape)

# out = n1[0:2]

# print (out)

'''
