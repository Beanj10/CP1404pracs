CODE_TO_NAME = {"aliceblue" : "#f0f8ff", "antiquewhite" : "#faebd7",
                "antiquewhite1" : "#ffefdb", "antiquewhite2" : "#eedfcc",
                "antiquewhite3"	: "#cdc0b0", "antiquewhite4" : "#8b8378",
                "aquamarine1" : "#7fffd4", "aquamarine2" : "#76eec6",
                "aquamarine4" : "#458b74", "azure1" : "#f0ffff"}

print(CODE_TO_NAME)

colour_code = input("Enter short Colour: ").lower()
while colour_code != "":
    if colour_code in CODE_TO_NAME:
        print(colour_code, "is", CODE_TO_NAME[colour_code])
    else:
        print("Invalid short state")
    colour_code = input("Enter short Colour: ").lower()