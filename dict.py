# -*- coding: utf-8 -*-

dict1 = {'Name':'Zara','Age': 18, 'Gender': ['Female','Les']}

print(len(dict1))

print(dict1['Name'])

del dict1['Name']



dict1['Name'] = "none" #change the factor
print(dict1['Name'])


print(dict1)
print(str(dict1)) #same

list1 = list(range(20)) # a list 0-19
print(list1)

print(dict.keys(dict1)) #print the keys of dict1


dict2 = {} #list updating
dict2.update(dict1)
print(dict2)