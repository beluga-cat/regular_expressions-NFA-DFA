#Input
ask = input("Enter Characters: ")
ask_list = []
for i in ask:
    ask_list.append(i)
print("========================")
print("Integer: ")
#Integer
integer = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "-", "+"]
flagI = False
for i in ask_list:
    if(i in integer):
        flagI = True
    else:
        print("Isn't a Integer")
        flagI = False
        break

if(flagI == True):
    print("Is a Integer")
print("========================")
print("========================")
print("Float: ")
#Float
Float = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "-", "+", "."]
flagF = False
for i in ask_list:

    if(i in Float and "." in ask_list):
        flagF = True
    else:
        print("Isn't a Float")
        flagF = False
        break

if(flagF == True):
    print("Is a Float")

print("========================")
print("========================")
print("Variable Name: ")
#Variable Name
Variable = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "_"]
Variable1 = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
flagV = False
for i in ask_list:
    if(ask_list[0] in Variable1):
        print("Isn't a Variable Name")
        flagV = False
        break
    if(i in Variable):
        flagV = True
    else:
        print("Isn't a Variable Name1")
        flagV = False
        break

if (flagV == True):
    print("Is a Variable Name ")

print("========================")
print("========================")
print("String: ")
#String
String = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
flagS = False
for i in ask_list:
    if(i in String):
        flagS = True
    else:
        flagS = False
        break

if((flagS == True and flagV == True) or (flagS == False and flagV == True) or (flagS == True and flagV == False)):
    print("Is a String")

else:
    print("Isn't a String")