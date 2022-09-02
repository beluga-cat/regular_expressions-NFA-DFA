def createTT(statesCount,language):
    tt={}
    print("\nNote: Enter 'BREAK' when finish specifing transitions")
    for i in range(statesCount):
        dict={}
        print(f"\n\tCURRENT STATE: S{i}")
        for j in language:
            dict[j]=[]
            while True:
                next_state=input(f"{j} : ").upper()
                if(next_state=="BREAK"):
                    break
                dict[j].append(next_state)
        tt[f"S{i}"] = dict
    return tt


#Driver Code
states = int(input("Specify States Count: "))
lang = input("Specify Language: ")
language = []
for i in lang:
    language.append(i)


tt = (createTT(states,language))
print(tt)