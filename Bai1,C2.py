x=float(input("Nhap so tien: "))
lai =0
for i in range(1,19):
    lai   += x*(0.6/100)
    if (i%6==0):
      x += lai 
      lai = 0
      print (x)
   







