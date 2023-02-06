#Function to calculate age in dog years
def compute_dog_years(myAge: float):
    earlyYears = 2
    earlyYears *= 10.5
    laterYears = myAge - 2
    laterYears *= 4
    print(earlyYears)
    print(laterYears)
    myAgeInDogYears = earlyYears + laterYears
    print(myAgeInDogYears)

if __name__ == "__main__":
    myAge = 14
    compute_dog_years(myAge)
