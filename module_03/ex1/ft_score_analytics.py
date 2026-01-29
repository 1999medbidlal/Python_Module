import sys

args = sys.argv
argc = len(args)
score = []
print("=== Player Score Analytics ===")
i = 1
if argc == 1:
    print(f"No scores provided. Usage: python3 "
          f"{args[0]} <score1> <score2> ...")
else:
    try:
        while i < argc:
            score += [int(args[i])]
            i += 1
        total_len = len(score)
        total = sum(score)
        average = total / total_len
        high = max(score)
        low = min(score)
        rang = high - low
        print(f"Scores processed: {score}")
        print(f"Total players: {total_len}")
        print(f"Total score: {total}")
        print(f"Average score: {average}")
        print(f"High score: {high}")
        print(f"Low score: {low}")
        print(f"Score range: {rang}")
    except ValueError:
        print(f"Error: oops, you typed ’{args[i]}’ instead of ’1000’")
