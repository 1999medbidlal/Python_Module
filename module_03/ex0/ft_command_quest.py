import sys

args = sys.argv
argc = len(args)
print("=== Command Quest ===")
if argc == 1:
    print("No arguments provided!")
    print(f"Program name: {args[0]}")
else:
    print(f"Program name: {args[0]}")
    print(f"Arguments received: {argc - 1}")
i = 1
while i < argc:
    print(f"Argument {i}: {args[i]}")
    i += 1
print(f"Total arguments: {argc}")
