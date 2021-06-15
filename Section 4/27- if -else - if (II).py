option = input("\nWant to continue? (Y)es or (N)ot\n")

if option[0] == "Y" or option[0] == "y":
    print("Donwloading...")
elif option[0] == "N" or option[0] == "n":
    print("Aborted")
else:
    print(option, "is not recognized")