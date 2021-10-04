t=0
l = 0
s = 0
h = 0
for i in range(1,11):
 i = input('Feeling Like ("L"), Sad ("S"), and Heart("H")? ')
 if i.upper()and i == "L": 
  
    l+=1
    t+=1
    
 elif i.upper() and i == "S":
    s+=1
    t+=1
 elif i.upper() and i == "H":
    h+=1
    t+=1
   
 else:
    
    print("Invalid input , accepts only (L/S/H).")
a=l/t*100
b=s/t*100
c=h/t*100
print("============")
print("Total is %d"%t)
print("============")
print("Like: %d (%.2f%%)"%(l,a))
print("Sad: %d (%.2f%%)"%(s,b))
print("Heart: %d (%.2f%%)"%(h,c))