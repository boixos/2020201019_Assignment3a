import string
import json
import re


json_file = open('org.json')

file_element = json.load(json_file)
#print(file_element) 

def pOut1(l1, child):
    print("level of leader is " + str(l1) + " above Employee " + str(child))


def Find_Leader(x, y, root):

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
           return parent[x]
        else:
           return root 
           
    while parent[x] != parent[y]:
        x = parent[x]
        y = parent[y]
    return parent[x]
    
parent = {}
FindLevel = {}


##print(type(data))
root = file_element['L0'][0]['name']

##print(type(root))
FindLevel[root] = 0
for l in file_element:
    j = 0
    for l1 in file_element[l]:

        if l != 'L0':
            name1 = file_element[l][j]['name']
            parent[name1] = file_element[l][j]['parent']
            FindLevel[name1] = l[1]
            j = j+1
print(parent)
print(FindLevel)

x = input("Enter Number of Employees and emp ids: ").split(' ')
# y=input("Enter emp id 2: ")
NumberOfEmp = int(x.pop(0))
x.sort()
ans = NumberOfEmp*[0]
for t in x:
    if t == root:
      print("Leader not found")
      exit(0)
for i in range(NumberOfEmp):
    if x[i] in parent:
       # print(i)
        ans[i] = True
       # print(ans[i])
    else:
        ans[i] = False
        print("Wrong emp id (or emp id not found)")
        exit(0)

if NumberOfEmp == 3:
    temp = Find_Leader(x[0],x[1],root)
    t2 = Find_Leader(temp,x[2],root)
    print(t2+ " is Common leader of Employees " + "Employee "+x[0]+", Employee "+x[1]+" And Employee "+x[2])
    h = int(FindLevel[t2])
    h1 = int(FindLevel[x[0]])
    h2 = int(FindLevel[x[1]])
    h3 = int(FindLevel[x[2]])
    pOut1(abs(h-h1),x[0])
    pOut1(abs(h-h2),x[1])
    pOut1(abs(h-h3),x[2])
if NumberOfEmp == 4:
    temp = Find_Leader(x[0],x[1],root)
    t2 = Find_Leader(temp,x[2],root)
    if t2 == root:
       print(t2+ " is Common leader of " + "Employee "+x[0]+", Employee "+x[1]+", Employee "+x[2]+" And Employee "+x[3])
       h = int(FindLevel[t2])
    else:
        t3 = Find_Leader(t2,x[3],root)
        print(t3+ " is Common leader of " + "Employee "+x[0]+", Employee "+x[1]+", Employee "+x[2]+" And Employee "+x[3])
        h = int(FindLevel[t3])
    
    h1 = int(FindLevel[x[0]])
    h2 = int(FindLevel[x[1]])
    h3 = int(FindLevel[x[2]])
    h3 = int(FindLevel[x[3]])
    pOut1(abs(h-h1),x[0])
    pOut1(abs(h-h2),x[1])
    pOut1(abs(h-h3),x[2]) 
    pOut1(abs(h-h3),x[3])    
if NumberOfEmp == 5:
    temp = Find_Leader(x[0],x[1],root)
    t2 = Find_Leader(temp,x[2],root)
    if t2 == root:
       print(t2+ " is Common leader of " + "Employee "+x[0]+" Employee "+x[1]+" Employee "+x[2]+" Employee "+x[3]+" And Employee "+x[4])
       h = FindLevel[t2]
    else:
        t3 = Find_Leader(t2,x[3],root)
        if t3 == root:
            h = FindLevel[t2]
            print(t3+ " is Common leader of " + "Employee "+x[0]+", Employee "+x[1]+", Employee "+x[2]+", Employee "+x[3]+" And Employee "+x[4])
        else: 
            h = FindLevel[t2]
            t4 = Find_Leader(t3,x[4],root)
            print(t4+ " is Common leader of " + "Employee "+x[0]+", Employee "+x[1]+", Employee "+x[2]+", Employee "+x[3]+" And Employee "+x[4])
    h1 = int(FindLevel[x[0]])
    h2 = int(FindLevel[x[1]])
    h3 = int(FindLevel[x[2]])
    h3 = int(FindLevel[x[3]])
    h4 = int(FindLevel[x[4]])
    pOut1(abs(h-h1),x[0])
    pOut1(abs(h-h2),x[1])
    pOut1(abs(h-h3),x[2]) 
    pOut1(abs(h-h3),x[3])         
    pOut1(abs(h-h4),x[4]) 