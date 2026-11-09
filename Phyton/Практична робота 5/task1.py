Name = "Sasha"
Surname = "Romanitch"
Group = "IT-32"
Year = "2009"
print(f"{Name} {Surname} {Group}")
def print_card():
    print(f"Name: {Name} {Surname}")
    print(f"Group: {Group}")
    print(f"Birth year: {Year}")
def print_card_args(name, surname, year, groap=Group):
    print(f"{name} {surname} {groap} {year}")
print("--- no parametrs, call 1 ---")
print_card()
print("--- no parametrs, call 2 ---")
print_card()
print("--- no parametrs, call 3 ---")
print_card()
print("--- positional argument ---")
print_card_args(Name, Surname, Year, Group)
print("--- keyword argument ---")
print_card_args(Name, Surname, year=Year, group=Group)
print("--- default group ---")
print_card_args(Name, Surname, Year)
