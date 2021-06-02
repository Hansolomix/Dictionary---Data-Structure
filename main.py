# Dict items are key value pairs enclosed in curley brackets
# Dict is ordered as of python 3.7
# Dict is mutable
# Dict Keys are unique, cannot have duplicates
# Elements can be of different data types

# '''
# Dict Attributes
# '''

# print(dir(dict))
# print(help(dict.pop))

# '''
# Creating Python Dictionary
# '''

# dict_example = {}
# dict_example = {'name': 'kingsley' , 'age':37}
# dict_example = dict ( [(1, 'car') , (2, 'bicycle')] )
# print(dict_example)

'''
Access Dictionary Values
'''

student = {'name': 'kingsley' , 'age' : 37 }
print( student ['age'] ) # => 37
print( student.get('age') ) # => 37
print( student.keys() ) # => dict_keys(['name','age'])
print( student.values() ) # => dict_values(['kingsley',37])

student = [ {'name' : 'kingsley', 'age':37} , {'name':'Lisa' , 'age': 34 } ]
# print(student[1])['name']# =>{'name': 'Lisa' , 'age':34 }

for i in range (len(student)):
     print(student[i]['name'])# => Lisa
     print(student[i]['age'])# =>34

# =============

'''
Changing dictionary Elements
'''

student = {'name': 'kingsley' , 'age' : 37 }
student['age'] = 35
print(student)# => {'name':'kingsley' , 'age' :35 }

# using update to replace
student = {'name':'kingsley' , 'age' :37 }
student.update( {'name':'Jennifer' , 'age' : 30 } )
print(student) # => {'name':'Jennifer', 'age': 30}

# Using setdefault
student = {'name':'kingsley' , 'age' :37 }
student.setdefault('name', 'Steve') #=> {'name':'kingsley','age':37}

student = {'name':'kingsley','age' :37 }
student.setdefault('subject' , 'Python')
print(student)# =>{'name':'kingsley','age':37,'subject':'Python'}

# ============

'''
Remove element from dictionary
'''

# using pop to remove
student= {'name':'kingsley', 'age':37 }
student.pop('name')
print(student) # =>{'age':37}

# using popitem to remove
student = {'name':'kingsley', 'age' :37 }
student.popitem()
print(student)#=> {'name':'kingsley'}

# using clear 
student = {'name':'kingsley', 'age':37 }
student.clear()
print(student)

# using delete
student = {'name' :'kingsley' , 'age':37 }
# del student
# print(student)

# ========

'''
Dictionary Membership Test
'''

student = {'name':'kingsley', 'age':37 }
print('name' in student) #=> True
print('age'not in student) #=> False

# ========











