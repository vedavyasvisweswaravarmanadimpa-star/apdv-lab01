principal = 100
rate = 0.05
 
year1 = principal * (1 + rate)
year2 = principal * (1 + rate) ** 2
year3 = principal * (1 + rate) ** 3
 
print("After 1 year :", round(year1, 2))
print("After 2 years:", round(year2, 2))
print("After 3 years:", round(year3, 2))