a=float(input("Nhap so a: "))
b=float(input("Nhap so b: "))
ch= str (input("Nhap (+,-,*,/):"))
tinh=0
if (ch=='+'):
  tinh = a + b
elif (ch=='-'):
    tinh= a-b
elif (ch=='*'):
   tinh=a*b
elif (ch=='/'):
   tinh=a/b
else :
   print (" sai roi ba ")
print ("Phep tinh ", tinh)


