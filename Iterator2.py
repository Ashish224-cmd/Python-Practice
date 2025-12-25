my_list = [4,7,5,0]
my_iter = iter(my_list) 

print(next(my_iter))
print(next(my_iter))

#next(obj) is same as obj.__next()

print(my_iter.__next__())
print(my_iter.__next__())
#this will raise an error 
print(my_iter.__next__()) 