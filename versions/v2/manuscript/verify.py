import json
from math import comb, factorial, isqrt


def prime(value):
    return value >= 2 and all(value % divisor for divisor in range(2, isqrt(value) + 1))


def inverse_coefficient(row, degree):
    if row == 0:
        return int(degree == 0)
    return comb(row + degree - 1, degree)


def coefficient_sum(row, degree, factorials):
    return sum(
        (factorials[degree] // index)
        * (2**index - 1)
        * inverse_coefficient(row, degree - index)
        for index in range(1, degree + 1)
    )


def recurrence_row(row, maximum):
    values = [0, 1]
    rising = row
    for degree in range(2, maximum + 1):
        values.append(
            (3 * (degree - 1) + row) * values[-1]
            - 2 * (degree - 1) * (degree - 2 + row) * values[-2]
            + rising
        )
        rising *= row + degree - 1
    return values[:maximum + 1]


def polynomial(degree):
    coefficients = [0] * degree
    for index in range(1, degree + 1):
        rising = [1]
        for shift in range(degree - index):
            updated = [0] * (len(rising) + 1)
            for power, value in enumerate(rising):
                updated[power] += shift * value
                updated[power + 1] += value
            rising = updated
        scale = comb(degree, index) * factorial(index - 1) * (2**index - 1)
        for power, value in enumerate(rising):
            coefficients[power] += scale * value
    return coefficients


def evaluate(coefficients, value):
    result = 0
    for coefficient in reversed(coefficients):
        result = result * value + coefficient
    return result


def require(condition, label):
    if not condition:
        raise ValueError(label)


def signed_inverse(row, degree):
    numerator = 1
    for shift in range(degree):
        numerator *= row + shift
    require(numerator % factorial(degree) == 0, 'integer binomial coefficient')
    return numerator // factorial(degree)


def parameter_sum(base, row, degree):
    return sum(
        (factorial(degree) // index) * (base**index - 1)
        * signed_inverse(row, degree - index)
        for index in range(1, degree + 1)
    )


def parameter_recurrence(base, row, maximum):
    values = [0, base - 1]
    rising = row
    for degree in range(2, maximum + 1):
        values.append(
            ((base + 1) * (degree - 1) + row) * values[-1]
            - base * (degree - 1) * (degree - 2 + row) * values[-2]
            + (base - 1) * rising
        )
        rising *= row + degree - 1
    return values


def lah_polynomial(degree, parameter):
    if degree == 0:
        return [1]
    return [factorial(degree) // factorial(index)
            * comb(degree + 2 * parameter - 1, degree - index)
            for index in range(degree + 1)]


def main():
    maximum_row = 30
    maximum_degree = 200
    factorials = [factorial(degree) for degree in range(maximum_degree + 1)]
    primes = [degree for degree in range(2, maximum_degree + 1) if prime(degree)]
    polys = {degree: polynomial(degree) for degree in range(1, 13)}
    for degree, coefficients in polys.items():
        require(len(coefficients) == degree and coefficients[-1] == degree
                and all(value >= 0 for value in coefficients),
                f'polynomial degree and positivity {degree}')
    cells = 0
    quotients = 0
    alternate_cases = 0
    homogeneous_cases = 0
    difference_cases = 0
    for row in range(maximum_row + 1):
        values = recurrence_row(row, maximum_degree)
        for degree in range(maximum_degree + 1):
            value = coefficient_sum(row, degree, factorials)
            require(value == values[degree], f'coefficient identity {row}, {degree}')
            if degree:
                require(value % degree == factorials[degree - 1] % degree,
                        f'alternate column residue {row}, {degree}')
                require(value % degree == factorials[degree - 1] * (2**degree - 1) % degree,
                        f'column residue {row}, {degree}')
                if degree == 4:
                    require(value % 4 == 2, f'exception {row}')
                else:
                    require((value % degree == 0) == (not prime(degree)),
                            f'divisibility {row}, {degree}')
            if degree in polys:
                require(evaluate(polys[degree], row) == value,
                        f'polynomial identity {row}, {degree}')
                require(evaluate(polys[degree], row + 1) - value
                        == (degree * evaluate(polys[degree - 1], row + 1)
                            if degree > 1 else 0),
                        f'finite difference {row}, {degree}')
                difference_cases += 1
            if degree:
                alternate = sum(
                    (comb(row + degree - 1, degree - index)
                     * (factorials[degree] // index))
                    for index in range(1, degree + 1)
                )
                require(alternate == value,
                        f'alternate binomial sum {row}, {degree}')
                alternate_cases += 1
            cells += 1
        for index in range(maximum_degree - 2):
            predicted = (
                (4 * index + 2 * row + 7) * values[index + 2]
                - (5 * index**2 + (6 * row + 12) * index
                   + row**2 + 8 * row + 7) * values[index + 1]
                + 2 * (index + 1) * (index + row + 1)
                * (index + row) * values[index]
            )
            require(values[index + 3] == predicted,
                    f'homogeneous recurrence {row}, {index}')
            homogeneous_cases += 1
        for index in primes:
            value = values[index]
            require(value % index == index - 1, f'prime residue {row}, {index}')
            integral = value % (index - 1) == 0
            expected = index not in (3, 5) or row % 2 == 0
            require(integral == expected, f'quotient integrality {row}, {index}')
            if integral:
                require((value // (index - 1)) % index == 1,
                        f'quotient residue {row}, {index}')
            quotients += 1
    expected_polys = [
        [1],
        [3, 2],
        [14, 12, 3],
        [90, 82, 30, 4],
        [744, 680, 285, 60, 5],
        [7560, 6788, 2985, 760, 105, 6],
        [91440, 80136, 35532, 9870, 1715, 168, 7],
        [1285200, 1098984, 482300, 138796, 27160, 3444, 252, 8],
        [20603520, 17227584, 7425492, 2152584, 447405, 65520, 6342, 360, 9],
    ]
    for index, expected in enumerate(expected_polys, start=1):
        require(polys[index] == expected, f'A355259 row {index - 1}')
    parameter_cells = 0
    parameter_prime_cases = 0
    negative_row_cases = 0
    for base in range(-3, 6):
        for row in range(-6, 7):
            values = parameter_recurrence(base, row, 24)
            for degree in range(25):
                value = parameter_sum(base, row, degree)
                if base == 2 and row == -1 and degree >= 2:
                    closed = (1 + 2**(degree - 1) * (degree - 2)) * factorial(degree - 2)
                    binomial = sum(
                        (factorial(degree) // (index + 2)) * comb(degree - 2, index)
                        for index in range(degree - 1)
                    )
                    require(value == closed == binomial,
                            f'negative row formulas {degree}')
                    negative_row_cases += 1
                require(value == values[degree],
                        f'parameter coefficient {base}, {row}, {degree}')
                if degree:
                    require(value % degree == factorial(degree - 1)
                            * (base**degree - 1) % degree,
                            f'parameter residue {base}, {row}, {degree}')
                    divides = (base % 2 != 0 if degree == 4 else
                               not prime(degree) or (base - 1) % degree == 0)
                    require((value % degree == 0) == divides,
                            f'parameter divisibility {base}, {row}, {degree}')
                if prime(degree):
                    require(value % degree == (1 - base) % degree,
                            f'parameter prime {base}, {row}, {degree}')
                    integral = (degree not in (3, 5) or base % 2 != 0
                                or row % 2 == 0)
                    require((value % (degree - 1) == 0) == integral,
                            f'parameter quotient {base}, {row}, {degree}')
                    if integral:
                        require((value // (degree - 1)) % degree
                                == (base - 1) % degree,
                                f'parameter quotient residue {base}, {row}, {degree}')
                    parameter_prime_cases += 1
                parameter_cells += 1
    lah_identity_cases = 0
    lah_congruence_cases = 0
    for parameter in range(6):
        for degree in range(44):
            coefficients = lah_polynomial(degree, parameter)
            image = sum(factorial(index - 1) * coefficients[index]
                        for index in range(1, degree + 1))
            require(image == coefficient_sum(2 * parameter, degree, factorials),
                    f'Lah identification {parameter}, {degree}')
            lah_identity_cases += 1
        for modulus in [2, 3, 5, 7, 11, 13, 17, 19]:
            for multiple in [1, 2]:
                for offset in range(5):
                    shift = multiple * modulus
                    left = lah_polynomial(offset + shift, parameter)
                    lower = lah_polynomial(offset, parameter)
                    for index, value in enumerate(left):
                        target = lower[index - shift] if index >= shift else 0
                        require((value - target) % modulus == 0,
                                f'Lah polynomial congruence {parameter}, {modulus}, {multiple}, {offset}, {index}')
                    lah_congruence_cases += 1
    print(json.dumps({
        'status': 'PASS',
        'arithmetic': 'exact integers',
        'rows': [0, maximum_row],
        'degrees': [0, maximum_degree],
        'coefficient_cells': cells,
        'prime_columns': primes,
        'prime_quotient_cases': quotients,
        'polynomial_identity_cases': (maximum_row + 1) * len(polys),
        'A355259_displayed_rows': len(expected_polys),
        'alternate_binomial_cases': alternate_cases,
        'homogeneous_recurrence_cases': homogeneous_cases,
        'finite_difference_cases': difference_cases,
        'integer_parameter_ranges': {'base': [-3, 5], 'row': [-6, 6], 'degree': [0, 24]},
        'integer_parameter_cells': parameter_cells,
        'integer_parameter_prime_cases': parameter_prime_cases,
        'A355258_formula_cases': negative_row_cases,
        'Lah_identification_cases': lah_identity_cases,
        'Lah_polynomial_congruence_cases': lah_congruence_cases,
        'checks': [
            'coefficient sum equals differential recurrence',
            'column residue and divisibility equivalence',
            'exceptional column four has residue two',
            'prime residue minus one',
            'exact prime quotient integrality and residue',
            'polynomial identities and published coefficient rows',
            'alternate binomial formula and homogeneous recurrence',
            'column finite difference identity',
            'integer parameter coefficient, divisibility and quotient formulas',
            'Lah identification and earlier polynomial congruence',
        ],
        'scope': 'finite checks; universal statements have written proofs in note.tex',
    }, indent=2))


if __name__ == '__main__':
    main()
