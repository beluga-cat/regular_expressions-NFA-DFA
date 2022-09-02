#input
ask = input("Enter a string: ")
ask_list = []
for k in ask:
    ask_list.append(k)

#Driver Code
counta = 0
countb = 0
j = 0
while j <= len(ask_list):
    for i in ask_list:
        if(i == "a"):
            counta = counta + 1
        if(i == "b"):
            countb = countb + 1

    break

            

if (counta % 2 == 0 and countb % 2 != 0 and 'ba' not in ask):
    print("Is Part of R.E.")
else:
    print("Is'nt Part Of R.E.")