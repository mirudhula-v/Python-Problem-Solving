a=float(input())
b=float(input())
choice=input("enter your choice")
match choice:
    case'+':
        print("sum:",a+b)
    case'-':
        print("diff:",a-b)
    case'*':
        print("mul:",a*b)
    case'_':
        print("invalid")
