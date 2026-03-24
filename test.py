text = "I have 5 apples and 10 oranges, price is 0.5 each. Card number is ....3672."

result = ""
number = ""
dot_used = False

for ch in text:
    if ch.isdigit():
        number += ch

    elif ch == "." and number != "" and not dot_used:
        number += ch
        dot_used = True

    else:
        if number != "":
            result += str(float(number) * 10)
            number = ""
            dot_used = False

        result += ch

if number != "":
    result += str(float(number) * 10)

print(result)