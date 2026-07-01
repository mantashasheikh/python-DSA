class node():
    def __init__(self , data):
        self.data = data
        self.next = None
        
n1 = node(30)
print(n1.data)
print(n1.next)
n2 = node(40)
print(n2.data)
print(n2.next)
n3 = node(50)
print(n3.data)
print(n3.next)    
n1.next = n2
n2.next = n3
print("data of n1 : ", n1.data)
print("data of n2 : ", n1.next.data)
print("data of n3 : ", n1.next.next.data)