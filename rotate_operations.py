# Rotate Right Without Carry (ROR)

a = "11010101"

print("ROR")
print("Original:", a)

for i in range(3):
    last = a[7]
    a = last + a[0:7]
    print("Step", i + 1, ":", a)

print("Final ROR:", a)
print()

# Rotate Right With Carry (RCR)

a = "11010101"
carry = "0"

print("RCR")
print("Original:", a)
print("Initial carry:", carry)

for i in range(3):
    last = a[7]
    a = carry + a[0:7]
    carry = last
    print("Step", i + 1, ":", a, "Carry:", carry)

print("Final RCR:", a)
print("Final carry:", carry)
