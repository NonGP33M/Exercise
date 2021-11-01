import random
stdin = ["641011051","6410110052","6410110056",
            "6310120060","6310120048",
            "6210110459","6210110334","6210110291",
            "6110110217","6110110203"]

random.seed(int(input()))
out = []
n = random.randint(0,2)
out.append(stdin[n])
n = random.randint(3,4)
out.append(stdin[n])
n = random.randint(5,7)
out.append(stdin[n])
n = random.randint(8,9)
out.append(stdin[n])
print(out)