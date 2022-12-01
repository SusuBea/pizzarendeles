# listák
tipus = []
meret = []
feltet = []
ar = []
pizza_db = 1

def rendelesfelvet():
    pizza_db = 1
    # listák
    print("Add meg a pizza adatait!")
    tovabb = input("Akar új rendelést rögzíteni? i/n : ")
    print('*' * 20)
    if tovabb != "n":
        print(f"*{'1 - sajtos':18}*")
        print(f"*{'2 - gombás':<18}*")
        print(f"*{'3 - sonkás':<18}*")
        print('*' * 20)
        t = input("Válasszon pizzát: ")
        tipus.append(t)
        print('*' * 20)
        print(f"*{'1 - kicsi':18}*")
        print(f"*{'2 - normál':<18}*")
        print(f"*{'3 - nagy':<18}*")
        print('*' * 20)
        m = input("Válasszon méretet: ")
        meret.append(m)
        f = input("Kér extra feltétet: i/n: ")
        feltet.append(f)
        tovabb = input("Akar új rendelést rögzíteni? i/n: ")
        while tovabb != "n":
            pizza_db += 1
            print(f"{pizza_db}. pizza rendelés")
            print(f"*{'1 - sajtos':18}*")
            print(f"*{'2 - gombás':<18}*")
            print(f"*{'3 - sonkás':<18}*")
            print('*' * 20)
            t = input("Válasszon pizzát: ")
            tipus.append(t)
            print('*' * 20)
            print(f"*{'1 - kicsi':18}*")
            print(f"*{'2 - normál':<18}*")
            print(f"*{'3 - nagy':<18}*")
            print('*' * 20)
            m = input("Válasszon méretet: ")
            meret.append(m)
            f = input("Kér extra feltétet: i/n: ")
            feltet.append(f)
            tovabb = input("Akar új rendelést rögzíteni? i/n: ")
        print(" ")


def arszamitas1():
    tipus
    i = 0
    while i < len(tipus):
        if tipus[i] == "1":
            tipus[i] = 1000
        elif tipus == "2":
            tipus[i] = 1100
        elif tipus == "3":
            tipus[i] = 1200
        i+= 1
    print(f"tipus = {tipus}")

    i = 0
    meret
    while i < len(meret):
        if meret[i] == "1":
            meret[i] = 0.9
        elif meret[i] == "2":
            meret[i] = 1
        elif meret[i] == "3":
            meret[i] = 1.1
        i += 1
    print(f"meret = {meret}")

    i = 0
    feltet
    while i < len(feltet):
        if feltet[i] == "i":
            feltet[i] = 50
        elif feltet[i] == "n":
            feltet[i] = 0
        i += 1
    print(f"feltét = {feltet}")


def arszamitas2():
    meret
    tipus
    feltet
    ar = []
    sum = 0
    i = 0
    while i < len(tipus):
        a = (float(tipus[i]) * meret[i]) + feltet[i]
        ar.append(a)
        sum += a
        i += 1
    print(f"Az Ön rendelése {pizza_db} db pizza, mely összesen {sum} Ft.")

def rendeles_kiiras():
    global meret
    global tipus
    global feltet
    i = 0
    while i <len(meret):
        if meret[i] == 0.9:
            meret[i] = "kicsi"
        elif meret[i] == 1:
            meret[i] = "normal"
        elif meret[i] == 1.1:
            meret[i] = "nagy"
        i += 1

    i = 0
    while i < len(tipus):
        if tipus[i] == 1000:
            tipus[i] = "sajtos"
        elif tipus[i] == 1100:
            tipus[i] = "gombás"
        elif tipus[i] == 1200:
            tipus[i] = "sonkás"
        i += 1

    i = 0
    while i < len(feltet):
        if feltet[i] == 50:
            feltet[i] = "feltéttel"
        elif feltet[i] == 0:
            feltet[i] = "feltét nélkül"
        i += 1

    i= 0
    while i < len(tipus):
        print(f"Az Ön rendelése: 1 db {meret[i]}, {tipus[i]} pizza, {feltet[i]}: {ar[i]} Ft ")
        i += 1
























