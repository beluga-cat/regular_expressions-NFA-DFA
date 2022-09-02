# DFA transition table CODE 
def createTT(statesCount,language):
    tt={}
    print("\nNote: Enter 'BREAK' when finish specifing transitions")
    for i in range(statesCount):
        dict={}
        print(f"\n\tCURRENT STATE: S{i}")

        for j in language:
            next_state=input(f"{j} : ").upper()
            dict[j] = next_state
        
        tt["S"+str(i)] = dict
    return tt

def checkRe(current_State,final_State,string,index):
    while True:
        if(current_State=="SX"):
            print("Isn't a Part of DFA")
            break
        elif(current_State!=final_State and index>len(string)-1):
            print("Isn't a Part of DFA")
            break
        elif(current_State==final_State and index>len(string)-1):
            print("Is a Part of DFA")
            break 
        else:
            current_State=tt[current_State][string[index]]
            index+=1

#Driver Code
states = int(input("Specify States Count: "))
lang = input("Specify Language: ")
language = []
for i in lang:
    language.append(i)


tt = (createTT(states,language))
print(tt)

ask = input("Specify String: ")
checkRe("S0",f"S{states-1}",ask,0)

