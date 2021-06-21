str = str(input("Card number:"))
strlength = len(str)
masked = strlength - 4
slimstr = str[masked:]
print("*" * masked + slimstr)

