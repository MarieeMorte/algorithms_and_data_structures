def solve_lecture_scheduling():
    with open('input.txt', 'r') as f:
        n = int(f.readline().strip())

        lectures = []
        for _ in range(n):
            start, end = map(int, f.readline().strip().split())
            lectures.append((start, end))

    lectures.sort(key=lambda x: x[1])

    count = 0
    last_end_time = 0

    for start, end in lectures:
        if start >= last_end_time:
            count += 1
            last_end_time = end

    with open('output.txt', 'w') as f:
        f.write(str(count))


if __name__ == "__main__":
    solve_lecture_scheduling()
