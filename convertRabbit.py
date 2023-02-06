#Function to calculate age in rabbit years
def compute_rabbit_years(myAge: float):
    allYears = 6
    myAgeInRabbitYears = myAge * allYears
    print(myAgeInRabbitYears)

if __name__ == "__main__":
    myAge = 14
    compute_rabbit_years(myAge)
