''''

Python Immutable Function Argument – Example and Explanation

''''



def fool(a):
    #function block
    a+=1
    print('id of a:',id(a))#id of y and a are same
    return a

#main or caller block
x=10
y = fool(x)

#value of x is unchanged
print ('x:',x)

#value of y is the return of the function fool
#after adding 1 to argument 'a' which is actual variable 'x'

print ('y:',y)

print ('id of x:',id(x)) #id of x
print ('id of y:',id(y)) #id of y,different from x


'''
Explanation:

Original object integer x is immutable (unchangeable). A new local duplicate copy a of the integer object x is created and used inside the function foo1() because integers are immutable objects and can’t be changed in placed. The caller main block where variable x is created has no effect on the value of the variable x.
The value of variable y is the value of variable a returned from function foo1() after adding 1.
Variable x and y are different as you can see their id values are different.
Variable y and a are same as you can see their id values are same. Both point to same integer object.
'''
