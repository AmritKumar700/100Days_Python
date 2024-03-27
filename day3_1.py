print("Welcome to the rollercoaster:")
height = int(input("What is your height in cm? "))

if height >=120:
    print("You can ride rollercoaster!")
    age = int(input("What is your age? "))
    if age <=18:
        bill = 7
        print("Please pay $7.")
    else:
        bill = 12
        print("Please pay $12.") 
    want_photo = input("Do you want to take a photo? Type 'Y' for Yes and 'N' for No ")
    if want_photo == "Y":
        bill+=3
    print(f"Your Bill is {bill}")        
else:
    print("Sorry, can't proceed.")           