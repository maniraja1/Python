#### How to define list, tuples and sets

emptylist=[]
emptylist=list()

emptytuple=()
emptytuple=tuple()

emptyset={} #### This is a dictionary do not use this
emptyset=set()

##emptydict={}
##enptydict=dict()

course = ['math','history','science','geography']

print(course)
course.sort()
print(course)
course.sort(reverse=True)
print(course)
c1=sorted(course)
print(course)
print(c1)
print(min(course))
print(course)
print(course[2:]) ### This print the list from the 3 element (because list starts from 0) till the last element
print(course[:2]) ### This prints out the list from the first 2 elements (0,1) always the uper bound is exclusive and the lower bound is inclusive
print(course.index('math'))
print('art' in course)
for index,value in enumerate(course,start=1): ### This provides with the index and elemnt. if you omit start=1 then the index starts from 0
    print(index,value)

course_str=','.join(course) ### This converts the list to a string where elements are seperate by commas
print(course_str)

print(course_str.split(','))#### This splits a string separated by coma to a list

#### Found this interesting behavior where when you copy a list to a second list and make changes to the original list then the second list also has the change
course2=course
print(course)
print(course2)
course.insert(0,'art')
print(course)
print(course2)

#### Now if you createa blank list and then enumerate through original list and then populate the new list any items you add to the origial list will not be visible to the new list
course3=[]
for i in course:
    course3.append(i)
print(course3)

course.insert(0,'trignometry')

print(course)
print(course2)
print(course3)


#### tuples are same as list but tuples are immutable whereas list are mutabe
#### Sets are ordered ad removesduplicate
#### Sets are optimized to search if a vakue is in the set and also to see commonalities between 2 sets and the difference between 2 sets

emptydict={'Name':'John','age':30}

print(emptydict)
print(emptydict['Name'])
print(emptydict.get('Name1','NA'))
print(emptydict.__getitem__('Name'))
emptydict['Name']='Jane'
print(emptydict)
emptydict.update({'Name':'Robert','Phone':'000','phone2':'111'})
print(emptydict)

del emptydict['age']
print(emptydict)

print(emptydict.pop('phone2'))
print(emptydict)

print(emptydict.__len__())
print(emptydict.keys())
print(emptydict.values())
print(emptydict.items())
print(emptydict.__getitem__('Name'))
print(emptydict.)