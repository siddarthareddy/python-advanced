from typing import List

def fib(n: int) -> List[int]:
    numbers = []
    current, nxt = 0, 1
    while len(numbers) < n:
        current, nxt = nxt, current+ nxt
        numbers.append(current)

    return numbers

result = fib(50)


for n in result:
    print(n, end=', ')
    if n > 10000:
        break

# alternative way to do that?
# create a "generator"
def fib():
    current, nxt = 0, 1
    while True:
        current, nxt = nxt, current+ nxt
        yield current

result = fib()

# as we see below, it "generates" values
# does "iterate" over existing values, but generates them
for n in result:
    print(n, end=', ')
    if n > 10000:
        break

print()
print("Done")