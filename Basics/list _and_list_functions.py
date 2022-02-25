#List: Mutable


cars = ['audi', 'bmw', 'benz', 'acura', 'lexus']
num = [20, 2, 3, 4, 5, 6, 7, 8]


print(cars[2])
print(num[1])
print(num.sort())
print(num.reverse())

#In negative slicing take only -1 and dont take more than that
#Slicing using indexing
print(num[:3:]) 


#Get the Max value
print(max(num))



#Append:  Adds at the end
num.append(100)
#Insert: ask for index value as argument with the value
num.insert(3,1000)

#Remove: removes values what you mention
num.remove(3)


#pop: removes from end of the list
num.pop()

#Tupals: Immutable

tp = (1, 2, 3, 4)
print(tp)

# This gives just the element
tp_with_one_element= (4)
print(tp_with_one_element)
# in order to get it as a tuple we need to put ',' at the end of the element
tp_with_one_element= (4,)
print(tp_with_one_element)

#Swap 2 Numbers
a =1
b =2
a, b = b, a
print(a, b)