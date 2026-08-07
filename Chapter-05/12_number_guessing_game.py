secret_number = 57
guess = 0

margin = 4

while guess != secret_number:
    guess = int(input ("guess: "))

    if guess >= secret_number + margin:
        print("Too High")

    elif guess <= secret_number - margin:
        print("Too Low")

print("Correct Answer")


print("\n ====================")
print("\n")

secret_number = 102
guess = 0

while guess != secret_number:
    guess = int(input ("guess: "))

    if guess >= secret_number + 5:
        print("Way Too High 🚀")

    elif guess > secret_number and guess < secret_number + 5 :
        print("Slightly High 🙂")

    elif guess < secret_number and guess > secret_number - 5 :
        print("Slightly Low 🙂")  

    elif guess <= secret_number - 5:
            print("Way Too Low ❄️")          
        
print("Correct Answer")

print("\n")