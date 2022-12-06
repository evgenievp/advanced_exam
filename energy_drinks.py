from collections import deque

caffeine = deque([int(x) for x in input().split(", ")])
drinks = deque([int(x) for x in input().split(", ")])

total = 0
while caffeine and drinks:
    caffe = caffeine[-1]
    drink = drinks[0]
    if caffe * drink + total <= 300:
        caffeine.pop()
        drinks.popleft()
        total += (drink * caffe)
    else:
        caffeine.pop()
        drinks.append(drinks.popleft())
        if (total - 30) <= 0:
            continue
        total -= 30

if drinks:
    print(f"Drinks left: {', '.join(str(x) for x in drinks)}")
else:
    print(f"At least Stamat wasn't exceeding the maximum caffeine.")

print(f"Stamat is going to sleep with {total} mg caffeine.")