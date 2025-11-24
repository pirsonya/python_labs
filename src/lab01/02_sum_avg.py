a, b = input(), input()
a, b = a.replace(",", "."), b.replace(",", ".")
a, b = float(a), float(b)
print(
    "a:", " ", a, "\nb:", " ", b, "\nsum=", a + b, ";", " ", "avg=", (a + b) / 2, sep=""
)
