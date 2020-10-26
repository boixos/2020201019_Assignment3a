f1 = open("Employee1.txt","r")
f2 = open("Employee2.txt","r")
f1 = eval(f1.read())
f2 = eval(f2.read())
eName1 = list(f1.keys())[0]
eName2 = list(f2.keys())[0]
sdate = list(f1[eName1].keys())
print(sdate)
#lx = f1.split('')
#print(lx)
#print(f1['Employee1'])
ef1 = f1[eName1]
ef2 = f2[eName2]
#print(ef1)
#print(ef2)
emp1 = list(ef1.values())
emp2 = list(ef2.values())
#print(emp1[0][1])
#print(type(f3[0][1]))

est1 = []
eet1 = []
est2 = []
eet2 = []
avl1 = []
avl2 = []
for x in emp1[0]:
    y = x.split('-')
    est1.append(y[0].strip())
    eet1.append(y[1].strip())
est1.append('5:00PM') 
eet1.insert(0,'9:00AM')   
for x in emp2[0]:
    y = x.split('-')
    # y[0] = y[0].strip()
    # y[1] = y[1].strip()
    est2.append(y[0].strip())
    eet2.append(y[1].strip())
est2.append('5:00PM') 
eet2.insert(0,'9:00AM') 
# print(est1)
# print(eet1)
r = len(eet1)
for i in range(r):
    if ((est1[i] == '9:00AM') or (eet1[i] == '5:00PM') or (est1[i] == eet1[i])) :
        continue
    else:
        avl1.append(eet1[i]+" - "+est1[i])
  
  
print(eName1+':',avl1) 
# print(est2)
# print(eet2)
r = len(eet2)
for i in range(r):
    if (est2[i] == '9:00AM') or (eet2[i] == '5:00PM') or (est2[i] == eet2[i]):
        continue
    else:
        avl2.append(eet2[i]+" - "+est2[i])
  
print(eName2+':',avl2) 
timeToIndex = {'9:00AM':0, '9:30AM':1, '10:00AM':2, '10:30AM':3, '11:00AM':4, '11:30AM':5, '12:00PM':6, '12:30PM':7, '1:00PM':8, '1:30PM':9, '2:00PM':10, '2:30PM':11, '3:00PM':12, '3:30PM':13, '4:00PM':14, '4:30PM':15, '5:00PM':16}
indexToTime = {0:'9:00AM', 1:'9:30AM', 2:'10:00AM', 3:'10:30AM', 4:'11:00AM', 5:'11:30AM', 6:'12:00PM', 7:'12:30PM', 8:'1:00PM', 9:'1:30PM', 10:'2:00PM', 11:'2:30PM', 12:'3:00PM', 13:'3:30PM', 14:'4:00PM', 15:'4:30PM', 16:'5:00PM'}


#print(avl1[0])
EmptySlots1 = 17*[0]
EmptySlots2 = 17*[0]
l = len(avl1)
i = 0
for x in avl1:
    x = avl1[i].split('-')
    x[0] = x[0].strip(',| ')
    x[1] = x[1].strip(',| ')
    i+=1
    #print(x[0])
    start = timeToIndex[x[0]]
    end  = timeToIndex[x[1]]
    #print(start)
    #print(end)
    while start < end:
        EmptySlots1[start] = 1
        start+=1

#print(EmptySlots)


l = len(avl2)
i = 0
for i in range(l):

    x = avl2[i].split('-')
    x[0] = x[0].strip(',| ')
    x[1] = x[1].strip(',| ')
    i+=1
    start = timeToIndex[x[0]]
    end = timeToIndex[x[1]]
    while start < end:
        EmptySlots2[start] = 1
        start+=1  
#print(EmptySlots2)
AvailableSlots = [EmptySlots1[i]&EmptySlots2[i] for i in range(len(EmptySlots2))]
#print(AvailableSlots)              
#print(avl2)
iDuration = float(input())
Duration = 2*iDuration 
#print(Duration)
BlockedSlot = []
i=0
while i < len(AvailableSlots)-1:
    if AvailableSlots[i]==1:
       # print("1")
        count = 0
        start = indexToTime[i]
        while AvailableSlots[i]==1 and i < (len(AvailableSlots)-1):
            count+=1
            #print(Duration)
            if count == Duration:
                end = indexToTime[i+1]
                #print(start)
                #print(end)
                BlockedSlot.append(start + ' - ' + end)
                break
            i+=1
        if len(BlockedSlot) == 1:
            break
    i+=1
#print(BlockedSlot)    
output = open("output1.txt","w")
if BlockedSlot == []:
    output.write('No Slot Available')
    print('No Slot Available')
    output.close()
    exit()
sdate = str(sdate)
sdate = sdate.strip('[|]')    
sdate = sdate.strip("'") 
BlockedSlot =  str(BlockedSlot).strip("'")   
sd = {
    sdate : BlockedSlot
}
print(BlockedSlot)
line1 = 'Available slot(s)'
line2 = eName1+': '+str(avl1)
line3 = eName2+': '+str(avl2)
line4 = ''
line5 = 'Slot Duration: '+str(iDuration)
line6 = str(sd)
lines = [line1,line2,line3,line4,line5,line6]
for line in lines:
    output.write(line)
    output.write("\n")
output.close()