import string
import json
import re


json_file = open('org.json')

file_element = json.load(json_file)
#print(file_element) 


def pOut(hd, child1, child2):
    print("level of leader is " + str(hd) + " above Employee " + str(child1))
    print("level of leader is 1 from " + str(child2))


def pOut1(l1, child):
    print("level of leader is " + str(l1) + " above Employee " + str(child))


def Find_Leader(x, y, root):
    child1 = x
    child2 = y
    height1 = int(FindLevel[x])
    height2 = int(FindLevel[y])
    if int(FindLevel[x]) > int(FindLevel[y]):
        t = x
        x = y
        y = t

    d = int(FindLevel[y])-int(FindLevel[x])
    while d > 0:
        y = parent[y]
        d = d-1
    if x == y:
        if parent[x] != root:
           print(parent[x] + " is Common leader of Employees " +
                 child1+" And " + child2)
        else:
           print(root + " is Common leader of Employees "+child1+" And " + child2)
           if (height1 > height2):
               hd = height1 - height2+1
               pOut(hd, child1, child2)
               return
           else:
               hd = height2 - height1+1
               pOut(hd, child2, child1)
               return
        if(height1 > height2):
           height3 = int(FindLevel[parent[x]])
           hd = height1-height3
           pOut(hd, child1, child2)

        else:
            height3 = int(FindLevel[parent[x]])
            hd = height2 - height3
            pOut(hd, child2, child1)

        return
    while parent[x] != parent[y]:
        x = parent[x]
        y = parent[y]
    print(parent[x] + " is Common leader of Employees " +
          child1+" And " + child2)
    if(parent[x] == root):
        height3 = 0
        l1 = height1 - height3
        pOut1(l1, child1)

        l1 = height2 - height3
        pOut1(l1, child2)

        return

    height3 = int(FindLevel[parent[x]])
    l1 = height1-height3
    pOut1(l1, child1)

    l1 = height2-height3
    pOut1(l1, child2)

parent = {}
FindLevel = {}


##print(type(data))
root = file_element['L0'][0]['name']

##print(type(root))

for l in file_element:
    j = 0
    for l1 in file_element[l]:

        if l != 'L0':
            name1 = file_element[l][j]['name']
            parent[name1] = file_element[l][j]['parent']
            FindLevel[name1] = l[1]
            j = j+1


x = input("Enter emp ids: ").split(' ')
# y=input("Enter emp id 2: ")
if x[0] == root or x[1] == root:
    print("Leader not found")
    exit(0)
if x[0] in parent:
    ans = True
else:
    ans = False
if x[1] in parent:
    ans1 = True
else:
    ans1 = False


if ans1 == True and ans == True:
    if x[0] == root or x[1] == root:
        print("Leader not found")
    else:
        Find_Leader(x[0], x[1], root)
else:
    print("Wrong emp id (or emp id not found)")
