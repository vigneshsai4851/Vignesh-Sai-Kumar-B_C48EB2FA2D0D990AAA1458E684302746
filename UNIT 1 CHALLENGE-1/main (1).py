def leapyear(n):
  if (n%4==0 or n%400==0):
       print(n,"is a leap year")
  else:
       print(n,"is not a leap year")

year=int(input("Enter a year :"))
result=leapyear(year)

     