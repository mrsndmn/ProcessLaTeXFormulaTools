# -*- encoding: utf-8 -*-
# @Author: SWHL
# @Contact: liekkaskono@163.com
from process_formula import NormalizeFormula

normlizer = NormalizeFormula()


math_str = [
    ('x\\to\\\\0', 'x\\to\\\\0'),
    ('\lim_{x\\to\\\\0} \\frac{1}{x} = \infty', '\lim_{x\\to 0}\\frac{1}{x}=\infty'),
    ("\\sum_i^n i = \\frac{n(n+1)}{2}", "\\sum_{i}^{n} i = \\frac{n(n+1)}{2}"),
]

errors = 0

for latex_in, expected_output in math_str:
    normalized_out = normlizer(latex_in)[0]
    print("normalized_out", normalized_out)
    if normalized_out != expected_output:
        errors += 1
        print(f"expected_output: {expected_output}, normalized_out: {normalized_out}")

print(f"errors {errors}")