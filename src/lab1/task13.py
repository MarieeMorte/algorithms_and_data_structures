def can_partition_into_three_equal_sums():
    with open('input.txt', 'r') as f:
        n = int(f.readline().strip())
        values = list(map(int, f.readline().strip().split()))

    total_sum = sum(values)

    if total_sum % 3 != 0:
        result = 0
    else:
        target = total_sum // 3

        subset_sum = [0] * (1 << n)

        for mask in range(1 << n):
            sum_mask = 0
            for i in range(n):
                if mask & (1 << i):
                    sum_mask += values[i]
            subset_sum[mask] = sum_mask

        dp = [False] * (1 << n)
        dp[0] = True

        for mask in range(1 << n):
            if not dp[mask]:
                continue

            for i in range(n):
                if mask & (1 << i):
                    continue

                new_mask = mask | (1 << i)
                if subset_sum[mask] + values[i] <= target:
                    dp[new_mask] = True

        result = 0
        for mask in range(1 << n):
            if subset_sum[mask] == target and dp[mask]:
                remaining_mask = ((1 << n) - 1) ^ mask
                if can_partition_into_two(remaining_mask, target, values, n):
                    result = 1
                    break

    with open('output.txt', 'w') as f:
        f.write(str(result))


def can_partition_into_two(mask, target, values, n):
    """Проверяет, можно ли разбить подмножество mask на 2 группы с суммой target"""
    total = 0
    for i in range(n):
        if mask & (1 << i):
            total += values[i]

    if total != 2 * target:
        return False

    sub_mask = mask
    while sub_mask:
        sum_sub = 0
        for i in range(n):
            if sub_mask & (1 << i):
                sum_sub += values[i]
        if sum_sub == target:
            remaining = mask ^ sub_mask
            sum_remaining = 0
            for i in range(n):
                if remaining & (1 << i):
                    sum_remaining += values[i]
            if sum_remaining == target:
                return True
        sub_mask = (sub_mask - 1) & mask

    return False


if __name__ == "__main__":
    can_partition_into_three_equal_sums()
