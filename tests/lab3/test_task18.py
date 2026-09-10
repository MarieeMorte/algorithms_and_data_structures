from test_utils import check, run_task, solution_path


def check_mst(input_data: str, expected: str, tol: float = 1e-6):
    output, elapsed, mem_bytes = run_task(solution_path(18), input_data)
    got = float(output)
    exp = float(expected)
    assert abs(got - exp) < tol, f"Ожидалось ≈{exp}, получено {got}"
    print(f"\n[task18] time={elapsed:.3f}s memory={mem_bytes} B (net)")
    print(f"  output: {output}")


def test_minimal():
    check(18, "1\n0 0\n", "0.000000000")


def test_minimal_two_points():
    check(18, "2\n0 0\n3 4\n", "5.000000000")


def test_example_1():
    check(18, "4\n0 0\n0 1\n1 0\n1 1\n", "3.000000000")


def test_example_2():
    check_mst("5\n0 0\n0 2\n1 1\n3 0\n3 2\n", "7.064495102", tol=1e-6)


def test_maximal():
    n = 200
    lines = [str(n)]
    for i in range(n):
        lines.append(f"{i} 0")
    check_mst("\n".join(lines) + "\n", "199.000000000", tol=1e-6)


def test_two_points_horizontal():
    check(18, "2\n0 0\n5 0\n", "5.000000000")


def test_two_points_vertical():
    check(18, "2\n0 0\n0 7\n", "7.000000000")


def test_triangle():
    # Равносторонний прямоугольный треугольник: 3-4-5
    check(18, "3\n0 0\n4 0\n0 3\n", "7.000000000")


def test_square():
    check(18, "4\n0 0\n0 1\n1 0\n1 1\n", "3.000000000")


def test_collinear():
    check(18, "3\n0 0\n1 0\n2 0\n", "2.000000000")


def test_negative_coordinates():
    check(18, "2\n-3 -4\n0 0\n", "5.000000000")


def test_same_x_different_y():
    check(18, "3\n0 0\n0 1\n0 2\n", "2.000000000")


def test_far_apart():
    check(18, "2\n-1000 -1000\n1000 1000\n", f"{2000 * 2 ** 0.5:.9f}")
