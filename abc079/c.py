
N = input()
A, B, C, D = N[0], N[1], N[2], N[3]

def fn(op1, op2, op3):
    msg = A + op1 + B + op2 + C + op3 + D
    if eval(msg) == 7:
        print(msg + "=7")
        exit()


for op1 in ("+","-"):
    for op2 in ("+","-"):
        for op3 in ("+","-"):
            fn(op1, op2, op3)
