def test_abs1():
    assert abs(-42) == 42, "Должно быть абсолютное значение числа(целое)"

def test_abs2():
    assert abs(-42) == -42, "Должно быть абсолютное значение числа(целое)"
    # self.assertEqual(a, b, msg="Значения разные")