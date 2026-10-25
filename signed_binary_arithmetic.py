# Expression 1: +46 + (+29)

a = 46
b = 29
result = a + b

print("Expression 1: +46 + (+29)")
print("First operand:", format(a & 255, '08b'))
print("Second operand:", format(b & 255, '08b'))
print("Binary result:", format(result & 255, '08b'))
print("Decimal result:", result)

if result > 127 or result < -128:
    print("Overflow: Yes")
else:
    print("Overflow: No")

print()

# Expression 2: (-48) - (-23)

a = -48
b = -23
result = a - b

print("Expression 2: (-48) - (-23)")
print("First operand:", format(a & 255, '08b'))
print("Second operand:", format(b & 255, '08b'))
print("Binary result:", format(result & 255, '08b'))
print("Decimal result:", result)

if result > 127 or result < -128:
    print("Overflow: Yes")
else:
    print("Overflow: No")
