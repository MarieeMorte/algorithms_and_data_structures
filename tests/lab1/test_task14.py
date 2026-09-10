import random

from test_utils import check


def test_minimal():
    check(14, "0\n", "0")


def test_example_1():
    check(14, "1+5\n", "6")


def test_example_2():
    check(14, "5-8+7*4-8+9\n", "200")


def test_maximal_add():
    expr = "+".join(["9"] * 15)
    check(14, expr + "\n", "135")


def test_maximal_mul():
    expr = "*".join(["9"] * 15)
    check(14, expr + "\n", str(9 ** 15))


def test_single_digit():
    check(14, "5\n", "5")


def test_single_digit_nine():
    check(14, "9\n", "9")


def test_single_add():
    check(14, "1+5\n", "6")


def test_single_sub():
    check(14, "9-3\n", "6")


def test_single_mul():
    check(14, "2*4\n", "8")


def test_sub_negative():
    check(14, "0-5\n", "-5")


def test_all_zeros():
    check(14, "0+0+0\n", "0")


def test_mul_chain():
    check(14, "2*3*4\n", "24")


def test_sub_chain_trap():
    # 1-2-3-4: max = 1-((2-3)-4) = 6
    check(14, "1-2-3-4\n", "6")


def test_sub_then_mul():
    # 1-2*3: max = (1-2)*3 = -3
    check(14, "1-2*3\n", "-3")


def test_mul_with_zero():
    check(14, "0*5+3\n", "3")


def test_mixed_long():
    # 9-9+9*9: max = (9-9)+9*9 = 81
    check(14, "9-9+9*9\n", "81")


def _all_values(expr):
    if len(expr) == 1:
        return {int(expr)}
    results = set()
    for i in range(1, len(expr), 2):
        lefts = _all_values(expr[:i])
        rights = _all_values(expr[i + 1:])
        op = expr[i]
        for a in lefts:
            for b in rights:
                if op == "+":
                    results.add(a + b)
                elif op == "-":
                    results.add(a - b)
                else:
                    results.add(a * b)
    return results


def test_stress_random_small():
    random.seed(14)
    for trial in range(30):
        n_ops = random.randint(0, 6)
        digits = [str(random.randint(0, 9)) for _ in range(n_ops + 1)]
        ops = [random.choice("+-*") for _ in range(n_ops)]
        expr = "".join(d + o for d, o in zip(digits, ops)) + digits[-1]

        expected = max(_all_values(expr))
        got = int(check(14, expr + "\n"))

        assert got == expected, (
            f"trial #{trial}: expr={expr}\n"
            f"expected={expected}, got={got}"
        )
