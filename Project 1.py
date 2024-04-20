#Traffic lights

Signal=input("red or yellow or green: ")
Signal=Signal.upper()
if Signal=="RED":
    print("Stop")
elif Signal=="YELLOW":
    print("Wait")
elif Signal=="GREEN":
    print("Go")
else:
    print("Choose from the given options")