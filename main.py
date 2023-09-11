import os
os.system("color")

data = []
print("Please paste your referenced sources.\n")
while True:
    line = input().strip()
    if not line:
        break
    data.append(line)
print("\u001b[36m")
print("\n".join(sorted(data)))
print("\u001b[0m")