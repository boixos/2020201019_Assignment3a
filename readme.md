# Assignment3c
  I've used VScode for all the question created .py file for each questions. All codes were working fine. Please Check if something doesn't work.

Repo link PartA: https://github.com/boixos/2020201019_Assignment3a/tree/main
Repo link PartB: https://github.com/boixos/2020201019_Assignment3a/tree/PartB
Repo link PartC: https://github.com/boixos/2020201019_Assignment3a/tree/PartC


## Question 1
  Make sure to provide `org.json` file for input in same folder as program.
  Please enter the Number of Employees in range 3-5 and Employee id in range 001-999. if there isn't any leader b/w the IDs `Leader Not Found` will be printed.
  No Changes were made, Program is same as in PartB.
## Question 2
  Make sure to provide `date_calculator.txt` file for input in same folder as program.
  Please enter the dateformat (for ex: dd/mm/yyyy or mm-dd-yyy) in command line argument.
  No Changes were made, Program is same as in PartB.

## Question 3
  Make sure to put all and only inputtext files in a folder name `inputfiles`, In same directory as q3.py.
  ###Changes:
     Code from line 22 to 41 is moved to a separate function `initFunc`.
     Code from line 44 to 61 is moved to a separate function `FindAvlSlots`.
     Code from line 81 to 94 is moved to a separate function `FinFunc`.
     In line 11 of PartC (line 23 of PartB) `entries[i] = open(entries[i], "r")` is changed to 
     `entries[i] = open('inputfiles/'+entries[i], "r")` so that you don't have to put inputfiles in two place (once in a folder name          `inputfiles` and also in same directory with q3.py), instead put all the files in folder name `inputfiles` only.
