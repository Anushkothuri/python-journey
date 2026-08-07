#if standalone
score=100
if score>=90:
    print("Grade A")
print()
#if-else
score = int(input("Enter score: "))
if score >= 90:
    print("Grade A")
else:
    print("Fail")
print()
#elif
score = int(input("Enter score: "))
if score >= 90:
    print("Grade A")
elif score>=80:
    print("Grade B")
elif score>=70:
    print("Grade C")
else:
    print("Fail")
print()