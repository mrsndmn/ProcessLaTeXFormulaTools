# -*- encoding: utf-8 -*-
# @Author: SWHL
# @Contact: liekkaskono@163.com
from process_formula import NormalizeFormula

normlizer = NormalizeFormula()


math_str = [
    ('\Delta z\sim1', '\Delta\\\\z\sim\\\\1'),

    ('1000', '1000'),
    ('\\nu t', '\\nu\\\\t'),
    # TODO numbers detokenization checkout!
    ('\\hskip 5mm', '\\hspace{5mm}'),
    ('\\left\\langle x\\right\\rangle', '\\left\\langle\\\\x\\right\\rangle'),
    ("\\underset { \\xi\\in \\Xi^0 } { \\max } \\ : f ( \\xi ) ", "\\max_{\\xi\\in \\Xi^{0}}\ \\\\:\\\\f( \\xi) "),
    ('\\sqrt T', '\\sqrt\\\\T'),
    ("\\sum_i^n i = \\frac{n(n+1)}{2}", "\\sum_{i}^{n}i=\\frac{n(n+1)}{2}"),
    ('\lim_{x\\to\\\\0} \\frac{1}{x} = \infty', '\lim_{x\\to\\\\0}\\frac{1}{x}=\infty'),
    ('x\\to\\\\0', 'x\\to\\\\0'),
    ('\\ \\rm', '\\ \\mathrm{}'),
    ('\\textrm { PXP }', '\\textrm{PXP}'),
    ('ball~wrt', 'ball~\\\\wrt'),
    ('\\log p', '\\log\\\\p'),
    ('\\dots', '\\dots'),
    ('\\notin', '\\notin'),
    ('x \\notin T', 'x\\notin\\\\T'),
    ('T_ { \epsilon }', 'T_{\epsilon}'),
    ('tractrix', 'tractrix'),
    ('\\text { tractrix }', '\\text{tractrix}'),
    ('\mathcal { F }', '\mathcal\\\\F'),

]

# math_str = math_str[:1]

errors = 0

for latex_in, expected_output in math_str:
    normalized_out = normlizer(latex_in)[0]
    # print("normalized_out", normalized_out)
    if normalized_out.strip() != expected_output.strip():
        errors += 1
        print(f"expected_output: {expected_output}")
        print(f"normalized_out:  {normalized_out}")
        print("-"*10)

print(f"errors {errors}")