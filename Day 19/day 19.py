print("Loan Calculator")
print()
print("$1000 over 10 years at 5% APR")
print()
loan = 1000
apr = 0.05
for i in range(10):
  loan += (loan*apr)
  print("Year",i+1,"is",
round(loan,2))
print()
interest = loan - 1000
print(round(interest,2),"is the interest earned")