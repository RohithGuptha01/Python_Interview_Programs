Original_String = (input("Enter Any String : "))

# Empty String
Reversed_String = ""

for i in Original_String:
    Reversed_String = i + Reversed_String
print(f"Reversed String for {Original_String} is {Reversed_String}")

if (Original_String == Reversed_String):
    print("Yes, It is Palindrome")
else:
    print("Not a Palindrome")