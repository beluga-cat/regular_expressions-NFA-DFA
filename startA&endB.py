#input
ask = input("Enter a string: ")
ask_list = []
for k in ask:
    ask_list.append(k)



if(ask_list[0] == "a" and ask_list[-1] == "b"):
    print("Is Part of R.E.")
else:
    print("Isn't Part of R.E.")