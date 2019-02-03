class Node:
    #Initialize the node object
    def __init__(self,data,prev,next):
        self.data=data
        self.next =None;
        self.prev = None;



#Linked List Class that contains the Node Object

class Linked_List:
    head = None
    tail = None

    def insert(self,data):
        new_node=Node(data,None,None)
        if self.head is None:
            #This functions checks to see if there is a value stored in the head variable
            #If no value is stored, then it sets the value of head to the value of new_node object
            #This will begin a new list
            self.head =new_node
            #Once the value of head is established, the tail is set to the new_node
            #That makes the first node both the head and the tail of the list
            #The head will remain constant but the tail will change values to each new element added into the list
            self.tail =new_node
        else:
            #This function exists if the list has already been created.
            #first
            new_node.prev=self.tail
            new_node.next=None;
            self.tail.next=new_node
            self.tail=new_node
    def Delete(self, Find):
        current_node=self.head#find the beginning of the list and create a temporary variable to store it's value

        while current_node is not None:
            if current_node.data == Find:#creating a basic find function to search the list
                if current_node.prev is not None:#Verify if previous node has a value
                    #reassign the pointer values for next and previous from the values of the previous node
                    current_node.prev.next=current_node.next
                    current_node.next.prev = current_node.prev
                else:
                    #If there are no previous nodes
                    self.head=current_node.next
                    current_node.next.prev=None
            current_node =current_node.next
    def Print(self):
        print ("My List Values: ")
        #we create a temporay variable to store the value of the Node
        #We set that value equal to the head
        current_node=self.head
        while current_node is not None:#while each new node contains a value, continue printing
            print(current_node.data)#print the value contained in data
            current_node =current_node.next#set the value of the temp variable current to the value of the next node



#Declare Main function
if __name__=='__main__':

    #Initialize linked list
    My_List = Linked_List()

    My_List.insert(1)
    My_List.insert(2)
    My_List.insert(3)
    My_List.Print()
    My_List.Delete(2)
    My_List.Print()
    My_List.Delete(3)
    My_List.Print()

