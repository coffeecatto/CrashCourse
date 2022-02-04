name = "dupa cycki"
print(name.title())
print(name.upper())
print(name.lower())

print("Zabawa ze zmiennymi F")

first_name = "janusz"
last_name = "chryzostom"
full_name = f"{first_name} {last_name}"
print(full_name)

# przy f-string wystarczy w tych smiesznych nawiasach dac zmienne by dzialalo
print(f"Witoj, {full_name.title()}!")

message = f"Superpajton tezd; {full_name.title()} ssie bonka dla {name.upper()}!"
print(message)

print("\tTest taba \n\toraz przechodzenia do nowej linii")

# whitespace stripping with rstrip/lstrip
fav_lang = "Pajton " 
print(f"-{fav_lang}-")
print(f"-{fav_lang.rstrip()}-")

# also can be done at a variable lvl

fav_lang = "Pajton "
fav_lang = fav_lang.rstrip()
print(f"={fav_lang}=")