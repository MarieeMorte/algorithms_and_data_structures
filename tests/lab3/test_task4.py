from test_utils import check, run_task, solution_path


def check_toposort(input_data: str, n: int, edges: list[tuple[int, int]]):
    output, elapsed, mem_bytes = run_task(solution_path(4), input_data)
    order = list(map(int, output.split()))
    assert len(order) == n, f"Ожидалось {n} вершин, получено {len(order)}"
    assert sorted(order) == list(range(1, n + 1)), "Не все вершины присутствуют ровно один раз"
    pos = {v: i for i, v in enumerate(order)}
    for u, v in edges:
        assert pos[u] < pos[v], f"Нарушен порядок: {u} -> {v}"
    print(f"\n[task4] time={elapsed:.3f}s memory={mem_bytes} B (net)")
    print(f"  output: {output[:200]}")


def test_minimal():
    check(4, "1 0\n", "1")


def test_example_1():
    check_toposort("4 3\n1 2\n4 1\n3 1\n", 4, [(1, 2), (4, 1), (3, 1)])


def test_example_2():
    check_toposort("4 1\n3 1\n", 4, [(3, 1)])


def test_example_3():
    check_toposort(
        "5 7\n2 1\n3 2\n3 1\n4 3\n4 1\n5 2\n5 3\n",
        5,
        [(2, 1), (3, 2), (3, 1), (4, 3), (4, 1), (5, 2), (5, 3)],
    )


def test_maximal():
    n = 100000
    m = 99999
    lines = [f"{n} {m}"]
    edges = []
    for i in range(1, n):
        lines.append(f"{i} {i + 1}")
        edges.append((i, i + 1))
    check_toposort("\n".join(lines) + "\n", n, edges)


def test_no_edges():
    check_toposort("4 0\n", 4, [])


def test_chain():
    check_toposort("5 4\n1 2\n2 3\n3 4\n4 5\n", 5, [(1, 2), (2, 3), (3, 4), (4, 5)])


def test_reverse_chain():
    check_toposort("5 4\n5 4\n4 3\n3 2\n2 1\n", 5, [(5, 4), (4, 3), (3, 2), (2, 1)])


def test_star():
    check_toposort("5 4\n1 2\n1 3\n1 4\n1 5\n", 5, [(1, 2), (1, 3), (1, 4), (1, 5)])


def test_two_chains():
    check_toposort(
        "6 4\n1 2\n2 3\n4 5\n5 6\n",
        6,
        [(1, 2), (2, 3), (4, 5), (5, 6)],
    )
