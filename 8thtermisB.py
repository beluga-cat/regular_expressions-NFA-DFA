#input
ask = input("Enter a string: ")
ask_list = []
for k in ask:
    ask_list.append(k)

print(len(ask_list))
if("a" and "b" not in ask_list):
    if(len(ask_list) >= 8):
        if(ask_list[7] == 'b'):
            print("Is Part of R.E.")

    else:
        print("Isn't Part of R.E. 1")
else:
    print("Isn't Part of R.E.")