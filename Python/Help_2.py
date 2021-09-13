def slope(a,b,c):
    if(b != "0"):
        sl = int(a)*(-1)/int(b)
        if(int(sl) == float(sl)):
            return str(int(sl))
        else:
            return str(sl)
    else:
        return "Not Available"

def xIntercept(a,b,c):
    if(a != "0"):  
        xi = int(c)*(-1)/int(a)
        if(int(xi) == float(xi)):
            return str(int(xi))
        else:
            return str(xi)
    else:
        return "Not Available"
    
def yIntercept(a,b,c):
    if(b != "0"):
        yi = int(c)*(-1)/int(b)
        if(int(yi) == float(yi)):
            return str(int(yi))
        else:
            return str(yi)
    else:
        return "Not Available"
    
print(" *** XY  Intercept ***\n -- ax + by + c = 0 --")
a,b,c = input("Enter a b c : ").split()
print ("Slope = " + slope(a,b,c))
print ("x-intercept => " + xIntercept(a,b,c))
print ("y-intercept => " + yIntercept(a,b,c))