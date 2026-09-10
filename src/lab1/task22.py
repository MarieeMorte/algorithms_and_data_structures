def solve_pretty_patterns():
    with open('input.txt', 'r') as f:
        m, n = map(int, f.readline().strip().split())

    if m < n:
        height, width = n, m
    else:
        height, width = m, n

    total_masks = 1 << width

    compatible_masks = [[] for _ in range(total_masks)]

    for mask1 in range(total_masks):
        for mask2 in range(total_masks):
            compatible = True
            for col in range(width - 1):
                if ((mask1 >> col) & 1) == ((mask1 >> (col + 1)) & 1) == \
                        ((mask2 >> col) & 1) == ((mask2 >> (col + 1)) & 1):
                    compatible = False
                    break

            if compatible:
                compatible_masks[mask1].append(mask2)

    dp = [1] * total_masks

    for _ in range(1, height):
        new_dp = [0] * total_masks
        for mask1 in range(total_masks):
            if dp[mask1] == 0:
                continue
            for mask2 in compatible_masks[mask1]:
                new_dp[mask2] += dp[mask1]
        dp = new_dp

    result = sum(dp)

    with open('output.txt', 'w') as f:
        f.write(str(result))


if __name__ == "__main__":
    solve_pretty_patterns()
