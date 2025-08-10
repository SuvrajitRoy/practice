def gcd(a,b):
    if (b==0):
        return a
    else:
        return gcd(b,a%b)
    a=int(input ("Ënter first number:"))
    b=int(input ("Ënter second number:"))
    GCD=gcd(a,b)
    print("GCD is:", GCD) 
      