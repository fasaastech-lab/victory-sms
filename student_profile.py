"""
Fee balance
Aisha Bello — 45,000
Emeka Okafor — 0
Fatima Aliyu — 22,500
David Okon — 45,000
Zainab Musa — 15,000
"""

student_name = [
    "Aisha Bello",
    "Emeka Okafor",
    "Fatima Aliyu",
    "David Okon",
    "Zainab Musa",
]
balance = [45000, 0, 22500, 45000, 15000]
pairs = list(zip(student_name, balance))

for name, student_balance in pairs:
    if student_balance == 0:
        print(f"{name} is not owing\n")
    else:
        print(f"{name} has an outstanding balance")
