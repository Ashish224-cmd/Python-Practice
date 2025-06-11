# my_list = [4,7,5,0]
# my_iter = iter(my_list)
# print(next(my_iter))
# print(next(my_iter))
# print(next(my_iter))
# print(my_iter.__next__())
# print(my_iter.__next__())

# mytuple = ("apple","banana","cherry")
# print(mytuple)
# myit = iter(mytuple)
# print(myit)
# print(next(myit))

# #string
# mystr = "banana"
# myit = iter(mystr)
# print(next(myit))
# print(myit.__next__())


#Create your own Iterator
class PowTwo:
    def __init__(self,max=0):
        self.max = max
    
    def __iter__(self):
        self.n=0
        return self
    def __next__(self):
        if self.n <= self.max:
            result = 2**self.n
            self.n+=1
            return result
        else:
            raise StopIteration
        
a = PowTwo(3)
i = iter(a)
print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i))