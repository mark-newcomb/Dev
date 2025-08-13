# Main Python Development Script
import random
import sys

print(f"Hello, world!")

if len(sys.argv) > 1:
    for i in sys.argv:
        print(i)

# Data types
city = "Whittier"
birth_year = 1987
starting_wage = 6.75
car_years = [1967, 2007, 2012, 2018, 2022, 2024]
is_married = True
next_city = None
family_members = {"Dad": "Mark", "Mom": "Marissa", "Daughter": "Hazel", "Son": "Hudson"}

# my_favorite_num = input("What is your favorite number?")
my_favorite_num = 7
print(f"My fave number plus 5 is {int(my_favorite_num) + 5}")

for i in [city, birth_year, starting_wage, car_years, is_married, next_city]:
    print(f"Data type for {i} is {type(i)}")

for key in family_members.keys():
    print(f"{key}")

for key,value in family_members.items():
    print(f"{value} is the {key} in the family.")

random_num = random.randrange(0,100)
print(f"Random number is {random_num}")

def main():
    print("Hello, world!")

if __name__ == "__main__":
    main()

# Continue at W3 with Lists, Tuples, Sets, etc. 