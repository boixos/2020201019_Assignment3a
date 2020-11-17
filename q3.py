import os

timeToIndex = {'9:00AM': 0, '9:30AM': 1, '10:00AM': 2, '10:30AM': 3, '11:00AM': 4, '11:30AM': 5, '12:00PM': 6, '12:30PM': 7,
    '1:00PM': 8, '1:30PM': 9, '2:00PM': 10, '2:30PM': 11, '3:00PM': 12, '3:30PM': 13, '4:00PM': 14, '4:30PM': 15, '5:00PM': 16}
indexToTime = {0: '9:00AM', 1: '9:30AM', 2: '10:00AM', 3: '10:30AM', 4: '11:00AM', 5: '11:30AM', 6: '12:00PM', 7: '12:30PM',
    8: '1:00PM', 9: '1:30PM', 10: '2:00PM', 11: '2:30PM', 12: '3:00PM', 13: '3:30PM', 14: '4:00PM', 15: '4:30PM', 16: '5:00PM'}

def initFunc(ename,Eslots,BusySlots,StartTimes,EndTimes,AvailableSlots,FreeSlots,stemp,etemp):
 l = len(entries)
 for i in range(l):
    entries[i] = open('inputfiles/'+entries[i], "r")
    entries[i] = eval(entries[i].read())
    #print(type(entries[i]))
    ename.append(list(entries[i].keys())[0])
    sdate = list(entries[0][ename[0]].keys())  # .strip('dict_keys|(|)|[|]')
    #print(sdate)
    Eslots.append(list(entries[i][ename[i]].values()))
    BusySlots.append(Eslots[i][0])
    #print(BusySlots[i])
    for t in BusySlots[i]:
         t = t.split('-')
         stemp.append(t[0].strip(' '))
         etemp.append(t[1].strip(' '))
    stemp.append('5:00PM')
    etemp.insert(0, '9:00AM')
    StartTimes.append(stemp.copy())
    EndTimes.append(etemp.copy())
    stemp.clear()
    etemp.clear()
 return sdate

def FindAvlSlots(StartTimes,EndTimes,l):
 for i in range(l):
    l1 = len(StartTimes[i])
    for j in range(l1):
        if ((StartTimes[i][j] == '9:00AM') or (EndTimes[i][j] == '5:00PM') or (StartTimes[i][j] == EndTimes[i][j])):
            continue
        else:
            stemp.append(EndTimes[i][j]+" - "+StartTimes[i][j])
    AvailableSlots.append(stemp.copy())
    stemp.clear()
    FreeSlots.append(17*[0])
    for x in AvailableSlots[i]:
        x = x.split(' - ')
        #print(x)
        start = timeToIndex[x[0]]
        end = timeToIndex[x[1]]
        while start < end:
            FreeSlots[i][start] = 1
            start += 1

def FinFunc(SlotDuration,AndSlots,BlockedSlot):
 n = len(AndSlots)
 for i in range(n-1):
    if AndSlots[i] == 1:
        count = 0
        start = indexToTime[i]
        while AndSlots[i] == 1 and i < n-1:
            count += 1
            if count == SlotDuration:
                end = indexToTime[i+1]
                BlockedSlot.append(start + ' - ' + end)
                break
            i += 1
        if len(BlockedSlot) == 1:
            break


entries = os.listdir('inputfiles/')
for entry in entries:
    print(entry)
ename = []
Eslots = []
BusySlots = []
StartTimes = []
EndTimes = []
AvailableSlots = []
FreeSlots = []
stemp = []
etemp = []

sdate = initFunc(ename,Eslots,BusySlots,StartTimes,EndTimes,AvailableSlots,FreeSlots,stemp,etemp)
l = len(entries)

FindAvlSlots(StartTimes,EndTimes,l)

print(AvailableSlots)
#print(FreeSlots)
AndSlots = []
if l == 2:
    AndSlots = [FreeSlots[0][i] & FreeSlots[1][i] for i in range(17)]
elif l == 3:
    AndSlots = [FreeSlots[0][i] & FreeSlots[1][i] & FreeSlots[2][i]
                for i in range(17)]
elif l == 4:
    AndSlots = [FreeSlots[0][i] & FreeSlots[1][i] &
                FreeSlots[2][i] & FreeSlots[3][i] for i in range(17)]
elif l == 5:
    AndSlots = [FreeSlots[0][i] & FreeSlots[1][i] & FreeSlots[2]
                [i] & FreeSlots[3][i] & FreeSlots[4][i] for i in range(17)]
#print(AndSlots)

SlotDuration = float(input())
SlotDuration = 2*SlotDuration
BlockedSlot = []
FinFunc(SlotDuration,AndSlots,BlockedSlot)

output = open("output.txt", "w")
if not BlockedSlot:
    output.write('No Slot Available')
    output.close()
    exit()
print(BlockedSlot)
output.write("Available Slot(s) \n")
for i in range(l):
    output.write(str(ename[i])+': '+str(AvailableSlots[i]))
    output.write('\n')
output.write('\n')
output.write('Slot Duration: '+str(SlotDuration/2)+' hour(s)')
output.write('\n')
output.write('{'+"'"+sdate[0]+"'"+': '+str(BlockedSlot)+'}')
output.close()
