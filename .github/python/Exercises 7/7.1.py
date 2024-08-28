seasons = ("Winter", "Spring", "Summer", "Autumn")
month = int(input("enter the number of the month(1-12)"))
if month in (12, 1, 2):
    season = seasons[0]
elif month in (3, 4, 5):
    season = seasons[1]
elif month in (6, 7, 8):
    season = seasons[3]
elif month in (9, 10, 11):
    season = seasons[4]
else:
    season = "invalid mouth number"
print(f"{season}")
