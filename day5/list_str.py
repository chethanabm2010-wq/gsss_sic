#Convert a list into string

list1= ['a','b','c','1','2','3']
my_str = ''.join(list1)
print(f' str =(my_str)')

#convert a  string into a list:
list2=[element for element in my_str ] # list comprehension
print(f' list ={list2}')