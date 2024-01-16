marksInput = int(input("Enter Your Marks: "))
if 91 <= marksInput <= 100:
    print("A1")
elif 81 <= marksInput <= 90:
    print("A2")
elif 71 <= marksInput <= 80:
    print("B1")
elif 61 <= marksInput <= 70:
    print("B2")
elif 51 <= marksInput <= 60:
    print("C1")
elif 41 <= marksInput <= 50:
    print("C2")
elif 33 <= marksInput <= 40:
    print("D")
elif 21 <= marksInput <= 32:
    print("E1")
elif 20 <= marksInput <= 0:
    print("E2")
else:
    print("Enter The Valid Marks Between 1 & 100 And Must Be A Positive Intiger")