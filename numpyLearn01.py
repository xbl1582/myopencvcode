import numpy as np

def arraychange():

    print(np.int8(3.14159));
    print(np.float64(9));
    print(np.float_(True));

def createarray():
    n1=np.array([1,2,3])
    n2=np.array([0.1,0.2,0.3])
    n3=np.array([[1,2],[3,4]])
    print(n1)
    print(n2)
    print(n3)
    n4=np.array(n1,dtype=np.float_);
    print(n4)
    n5=np.array(n1,ndmin=3)
    print(n5)
    n6=np.empty([2,3]);
    print(n6)
    n7 = np.zeros([2, 3]);
    print(n7)
    n8 = np.ones([2, 3]);
    print(n8)
    n9 = np.random.randint(2,10,[2,3]);
    print(n9)
    print(n1[0])