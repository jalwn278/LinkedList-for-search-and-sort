# YOUR PROJECT TITLE
    #### Video Demo:  https://youtu.be/rGGmg26RVe8?si=S2uk7VszxFviczFP
    #### Description:
    This is a module to deal with One-One relations of datas in .txt or .csv. You re reauired to input eg:python3 Project.py xxx.txt/.cxv -Bubble to sort or search specific data and gain ideal output. You're allowed to use this as a library by import project or from project import LinkedList and something else

    To implement this module I use linkedlist to give data some basic calculation. Such as Bubble, Merge, Selection sort and Linear, Binary search, which are all I'm familiar with.
    In main, I required to give a valid input, users can also input "python3 project.py -h" to search for help. After getting valid input, I will use os.path.splitext() get extensions name and use proper way yo extract datas

    In convert:For .txt I use 2 dynamic arrays to store datas and append them into LinkedList() object by zipping it into tuple. And in.csv, I thought ListDictionary is a great solution so I store them by 
    "item = {key: row[key] for key in keys}
    ind.append(item)" 
    and for consistence, I extract values from every item in ind and store them in object by tuple()and for every file I use a try-expect way to defend FileNotFoundError, ValueError and KeyError

    In format: At the begining I don't really know how to convert my string "-Selection" into a function, so I tend to google for help and know by introducing a getatter interface "func = getattr(my_list, method_name)
        func() method could be called correctly! That's really helpful!

    It turns to my class Node and LinkedList. In node I create a common node to store a single node and in LinkedList, I use linear way to append every node from my convert function and for every specific method I will give it a detailed introduction.

    (1) Selection sort
    In selection sort my goal is to iterate the whole linked list and find the minimum to put in the front. To finish it I need a node "i" to store the current first node and while "i.next" exists I create its next node "j" and "mini_node = i" and while "j" exists I iterate the following node and let the minimum one equals mini_node once I finish iteration, I could just let mini_node and i switch their data

    (2) Bubble sort
    In bubble sort switch between evry two node it's important and my goal is to put the biggest one in the tail so I need a "end" to check whether the lsit arrive its end by "while self.head.nexr != end" and let a "current" node to iterate its data by "while current != end" with hte next one if he is bigger than next  and use end = current to update the end

    (3) Merge sort
    In merge sort, recursive idea is very useful. To merge every half linkedlist I could use fast and slow node when the fast one arrive its end the slow one just arrive the mid so we could cut the list by mid, and check "sortmerge(head) sortmerge(mid)" and once it didn't arrive its end, the recursion will continue. And the basic condition is that self.head or self.head.next == None when it happens we can return the current head and go to the addmerge function.
    In addmerge function we create a empy node as the head of the list and add two list l1 l2 into it and to guarenteen all the node is added after we finish adding one list, we need "door.next = l1 if l1 else l2" to add all and return the ptr.next

    (4) Linear search
    Just iterate all!lmao

    (5) Binary search
    In sommon Binary search we use array because it wouldn't lost the rest part when we search, so we must change the linkedlist into an array and by common Binary search function, it's found!


    Test_projets: In test.py due to the sys module we use monkeypatch to change these outsider value and use "with pytest.raises(SystemExit) as e:
        main()
    assert "This module support" in e.value.code"
    to defend Error brake my file and in test.py we couldn't input so I use a lambda function and builtins.input to get inside input 
    And in extensions text I need to create a tmoporary director and file to check its function
    "d = tmp_path / "test_dir_csv"
    d.mkdir()
    file_path = d / "data.csv"
    file_path.write_text("id,name\n1,Alice\n2,Bob")"
    and use it by convert(".cxv") 
