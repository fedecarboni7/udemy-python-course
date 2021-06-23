i = int("5")
print("int(""5""):",i, type(i), sep="\t")

f = float("89.6")
print("float(""89.6""):",f, type(f), sep="\t")

print("bin(345):",bin(345), sep="\t")

print("hex(32):", hex(32), sep="\t")

print("int(""0b01010101011001"", 2):", int("0b01010101011001", 2), sep="\t")

print("int(""0x21"", 16):", int("0x21", 16), sep="\t")

print("abs(-12):", abs(-12), sep="\t")

print("round(23.499):", round(23.499), sep="\t")

print("pow(2,8):", pow(2,8), sep="\t")

a,b,c = zip([1,2,3], ["Sí", "No", "Tal vez"])
print(f"a: {a}, b: {b}, c: {c}")

print("list(zip(...)):", list(zip([1,2,3], ["Sí", "No", "Tal vez"])))

print("dict(zip(...)):", dict(zip([1,2,3], ["Sí", "No", "Tal vez"])))