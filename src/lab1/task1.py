def solve_fractional_knapsack():
    with open('input.txt', 'r') as f:
        first_line = f.readline().strip()
        while first_line == '':
            first_line = f.readline().strip()
        n, capacity = map(int, first_line.split())

        items = []
        for _ in range(n):
            line = f.readline().strip()
            while line == '':
                line = f.readline().strip()
            price, weight = map(int, line.split())
            items.append((price, weight))

    items.sort(key=lambda x: x[0] / x[1] if x[1] > 0 else float('inf'), reverse=True)

    total_value = 0.0
    remaining_capacity = capacity

    for price, weight in items:
        if remaining_capacity <= 0:
            break

        if weight == 0:
            total_value += price
            continue

        if weight <= remaining_capacity:
            total_value += price
            remaining_capacity -= weight
        else:
            fraction = remaining_capacity / weight
            total_value += price * fraction
            remaining_capacity = 0

    with open('output.txt', 'w') as f:
        f.write(f"{total_value:.4f}")


if __name__ == "__main__":
    solve_fractional_knapsack()
