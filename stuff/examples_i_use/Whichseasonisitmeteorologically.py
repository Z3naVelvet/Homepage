date = input("Date: ")

parts = date.split(",")

month = int(parts[0].split(":")[1].strip())

if month >= 12 and month < 3:
    print("It is meteorologically: Winter")
if month >= 3 and  month < 6:
    print("It is meteorologically: Spring")
if month >= 6 and month < 9:
    print("It is meteorologically: Summer")
if month >= 9 and month < 12:
    print("It is meteorologically: Fall")
input()
