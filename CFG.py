def T(str):
    if(len(str)==0):
        return False
    elif(str[0]=="d"):
        return S(str[1:])
    elif(str[0]=="e"):
        return S(str[1:])
    else:
        return False


def F(str):
    if(len(str)==0):
        return True
    elif(len(str)!=0):
        return T(str)
    else:
        return False

def S(str):
    if(len(str)==0):
        return False
    if(str[0]=="a"):
        return F(str[1:])
    elif(str[0]=="b"):
        return F(str[1:])
    else:
        return False


#Driver Code
ask = input("Specify String: ")
str = []
for i in ask:
    str.append(i)


print(S(str))






# def S(str):
#     if(len(str)==0):
#         return False
#     elif(str[0]=="a"):
#         return Z(str[1:])
#     elif(str[0]=="b"):
#         return Z(str[1:])    
#     else:
#         return False

# def Z(str):
#     if(len(str)==0):
#         return True
#     elif(str[0]=="a"):
#         return Z(str[1:])
#     elif(str[0]=="b"):
#         return Z(str[1:])
#     else:
#         return False

# def S(str):
#     if(len(str)==0):
#         return False
#     elif(str[0]=="a" and str[-1]=="b"):
#         return M(str[1:-1])
#     else:
#         return False
    
# def M(str):
#     if(len(str)==0):
#         return True
#     elif(str[0]=="a"):
#         return M(str[1:])

#     elif(str[0]=="b"):
#         return M(str[1:])

#     else:
#         return False

# def S(str):
#     if(len(str)==0):
#         return False
#     elif(str[0]=="a"):
#         return B(str[1:])
#     else:
#         return False

# def B(str):
#     if(len(str)==0):
#         return True
#     elif((str[0]=="a") and (str[-1]=="b")):
#         return B(str[1:])
#     elif((len(str)==1) and (str[0]=="b") and (str[-1]=="b")):
#         return B(str[1:])
#     elif((len(str)==1) and len(str)==1 and str[0]=="b"):
#         return B(str[1:])

#     else:
#         return False


