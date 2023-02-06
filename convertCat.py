#Function to calculate age in cat years
def compute_cat_years(myAge: float):
    earlyYears = 2
    earlyYears *= 12
    laterYears = myAge - 10
    laterYears *= 4
    print(earlyYears)
    print(laterYears)
    myAgeInCatYears = earlyYears + laterYears
    print(myAgeInCatYears)

if __name__ == "__main__":
    myAge = 14
    compute_cat_years(myAge)
