'''
We demonstrate in the following example, how you can count instance with class attributes. All we have to do is
to create a class attribute, which we call "counter" in our example
to increment this attribute by 1 every time a new instance will be create
to decrement the attribute by 1 every time an instance will be destroyed
'''

class C:
    counter = 0

    def __init__(self):
        type(self).counter += 1

    def __del__(self):
        type(self).counter -= 1

if __name__ == "__main__":
    x = C()
    print ("Number of instances: : " + str(C.counter))
    y = C()
    print ("Number of instances: : " + str(C.counter))
    del x
    print ("Number of instances: : " + str(C.counter))
    del y
    print ("Number of instances: : " + str(C.counter))
