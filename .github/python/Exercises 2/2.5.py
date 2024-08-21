talent = float(input("enter talents"))
pound = float(input("enter pounds"))
lot = float(input("enter lots"))
grams_1 = talent*20*32*13.3+pound*32*13.3+lot*13.3
kilograms = int(grams_1/1000)
grams = float(grams_1-(kilograms*1000))
print(f"The weight in modern units:\n{kilograms}kilograms and {grams:.2f} grams")
