import sched


SchoolMarks=[25,56,59,15,23]
SchoolMarks.sort() #to arrange the list in ascending order
print(SchoolMarks) #result: [15, 23, 25, 56, 59]

SchoolMarks.reverse() #arrange the list in descending order
print(SchoolMarks) # [59, 56, 25, 23, 15]

SchoolMarks.append("Ram") #adds "Ram" at the end of the list 
print(SchoolMarks)

SchoolMarks.insert(3,8) #adds 8 at third index
print(SchoolMarks)

SchoolMarks.pop(2) #to remove 2nd index from the list. 
print(SchoolMarks)

SchoolMarks.remove(59) #to remove 59 from the list, takes only one argument
print(SchoolMarks)


#for more methods, need to search google: python list methods

