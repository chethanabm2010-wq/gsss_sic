capitals =['panjim','bhubaneshwar','guwahti','aizwal','imphal','agartala','gangtok','kohima','itanagar','shilong']
print(capitals)  # by default entire list
print(capitals[:]) # by default from beginning to end
print(capitals[::])  # by default from beginning to end and default increment of 1
print(capitals[10])  # IndexError 
print(capitals[1:17])  # no index error in slicing
print(capitals[3:2])  # empty list
print(capitals[3:3]) #empty list
print(capitals[3:2:-1]) 
print(capitals[::3]) 
print(capitals[:-15:-1])  #entire list in reverse with no error
print(capitals[::-1])
print(capitals[-15:-1:1]) # start   from index -15 and go till last  but element in forward  direction with a jump  of 1
print(capitals[:-15:2])   #empty list 