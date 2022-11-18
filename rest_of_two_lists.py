# import modules
import numpy as np
import pandas as pd

# load lists
list1 = []
list2 = []

# compare lists, make new from rest
rest = []
for number in list1:
    if number not in list2:
        rest.append(number)

# load more information
info = np.loadtxt('info.csv',
                  delimiter=';', dtype='str')

# compare lists, make new from matches
rest_info = []
for row in range(len(info)):
    for number in rest:
        if number == int(info[row][0]):
            rest_info.append(data[row])

# make dataframe and export
df = pd.DataFrame(list_info)
df.to_csv('rest_info.csv', index=False)
