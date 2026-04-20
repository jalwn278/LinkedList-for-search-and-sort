import sys
import csv
import os
import cowsay

my_list = None
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        node = Node(data)
        if self.head == None:
            self.head = node
            return
        node.next = self.head
        self.head = node
        
        """
        Sequential version
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
           last_node = self.head
           while last_node.next:
                last_node = last_node.next
            last_node.next = new_node
            """
        

    def display(self):
        if not self.head:
            return "Nope"
        ptr = self.head
        while ptr:
            print(ptr.data, end="->")
            ptr = ptr.next
        print("Done")
            

    def Bubble(self):
        """
        default: check the first array of data
        """
        if not self.head or not self.head.next:
            return self.display()
        
        end = None
        while self.head.next != end:
            current = self.head
            while current.next != end:
                if current.data > current.next.data:
                    current.data, current.next.data = current.next.data, current.data
                current = current.next
            end = current
        
        return self.display()


    def Selection(self):
        """
        default: check the first array of data
        """
        if not self.head or not self.head.next:
            return self.display()
        
        i = self.head
        while i.next:
            mini_node = i
            j = i.next
            while j:
                if j.data < mini_node.data:
                    mini_node = j
                j = j.next
            i.data, mini_node.data = mini_node.data, i.data
            i = i.next

        return self.display()
    

    def Merge(self):
        if not self.head or not self.head.next:
            return self.display()
        
        self.head = self.sortmerge(self.head)
        return self.display()

    def sortmerge(self,head):
        """
        Only when the recursion is over, it give back value
        """
        if not head or not head.next:
            return head

        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        mid = slow.next
        slow.next = None

        left = self.sortmerge(head)
        right = self.sortmerge(mid)

        return self.addmerge(left, right)

    
    def addmerge(self, l1, l2):
        ptr = Node(0)
        door = ptr

        while l1 and l2:
            if l1.data < l2.data:
                door.next = l1
                l1 = l1.next

            else:
                door.next = l2
                l2 = l2.next

            door = door.next

        door.next = l1 if l1 else l2

        return ptr.next 



    def Linear(self,request):
        if not self.head or not self.head.next:
            return self.display()
        
        ptr = self.head
        while ptr != None:
            if request in ptr.data:
                return f"{ptr.data} is here"
            ptr = ptr.next
        
        return "Doesn't found"

    def Binary(self, request):
        """
        It only support check the first row of your csv/txt
        """
        if not self.head or not self.head.next:
            return self.display()
        
        arr = []
        ptr = self.head
        while ptr:
            arr.append(ptr.data)
            ptr = ptr.next
        
        low = 0
        high = len(arr) - 1

        while low <= high:
            mid = (low + high) // 2
            if arr[mid][0] == request:
                return f"{arr[mid]} is here"
            elif arr[mid][0] < request:
                low = mid + 1
            else:
                high = mid - 1
        return "Doesn't found"
            
    

def main():
    if sys.argv[1] == "-h" or sys.argv[1] == "-help":
        sys.exit('This module support ["-Linear", "-Binary", "-Selection", "-Bubble", "-Merge"] data in linkedlist by One-One relations in .csv and .txt to give ideal output')

    elif sys.argv[1] == "egg":
        egg()


    else:
        if len(sys.argv) != 3:
            sys.exit("It's too long so too short")
        if not sys.argv[1].endswith(".csv") and not sys.argv[1].endswith(".txt"):
            sys.exit("eg: xxx.py .csv/.txt  -format")
        elif sys.argv[2] not in ("-Linear", "-Binary", "-Selection", "-Bubble", "-Merge"):
            sys.exit("Print xxx.py -h / --help to check supported algorithms")

        else:
            _,extension = os.path.splitext(sys.argv[1])

            convert(extension)


        
def convert(extension):
    global my_list
    if extension == ".txt":
        try:
            datas, names = [], []
            with open(sys.argv[1], "r") as input:
                for line in input:
                    parts = line.strip().split()
                    if len(parts) == 2:
                        datas.append(parts[0])
                        names.append(parts[1])
                    else:
                        sys.exit("Library only support One-One relations")

        except (FileNotFoundError, ValueError):
            sys.exit(f"Couldnt read {sys.argv[1]}")

        my_list = LinkedList()
        for _ in zip(datas, names):
            my_list.append(_)
        format(my_list)
        

    elif extension == ".csv":
        ind = []
        try:
            with open(sys.argv[1], "r") as input:
                reader = csv.DictReader(input)
                keys = reader.fieldnames
                for row in reader:
                    item = {key: row[key] for key in keys}
                    ind.append(item)
        
        except (FileNotFoundError, ValueError, KeyError):
            sys.exit(f"Couldn't read {sys.argv[1]}")

        my_list = LinkedList()
        for item in ind:
            my_list.append(tuple(item.values()))
        format(my_list)
                    

def format(my_list):
    method_name = sys.argv[2].lstrip("-")
    if method_name in ["Selection", "Bubble", "Merge"]:
        func = getattr(my_list, method_name)
        func()
    else:
        request = input("Search for whom? ")
        func = getattr(my_list, method_name)
        result = func(request)
        print(result)

def egg():
    cowsay.cow("Thanks for using my library")

    
if __name__ == "__main__":
    main()