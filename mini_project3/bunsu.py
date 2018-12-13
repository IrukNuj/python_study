from fractions import Fraction
import math

def add(add1, add2):
    mixed_fraction_1 = (Fraction(add1[2], add1[3]) + add1[1]) * add1[0]
    mixed_fraction_2 = (Fraction(add2[2], add2[3]) + add2[1]) * add2[0]

    added_fraction = mixed_fraction_1 + mixed_fraction_2

    added_fraction, plus_minus_sign = decision_posi_nega(added_fraction)

    coefficient_num = added_fraction.numerator // added_fraction.denominator


    numerator_num = added_fraction.numerator - coefficient_num * added_fraction.denominator
    denominator_num = added_fraction.denominator

    return (plus_minus_sign, coefficient_num, numerator_num, denominator_num)

def sub(sub1, sub2):
    mixed_fraction_1 = (Fraction(sub1[2], sub1[3]) + sub1[1]) * sub1[0]
    mixed_fraction_2 = (Fraction(sub2[2], sub2[3]) + sub2[1]) * sub2[0]

    added_fraction = mixed_fraction_1 - mixed_fraction_2

    added_fraction, plus_minus_sign = decision_posi_nega(added_fraction)

    coefficient_num = added_fraction.numerator // added_fraction.denominator

    numerator_num = added_fraction.numerator - coefficient_num * added_fraction.denominator
    denominator_num = added_fraction.denominator

    return (plus_minus_sign, coefficient_num, numerator_num, denominator_num)

def mul(mul1, mul2):
    mixed_fraction_1 = (Fraction(mul1[2], mul1[3]) + mul1[1]) * mul1[0]
    mixed_fraction_2 = (Fraction(mul2[2], mul2[3]) + mul2[1]) * mul2[0]

    added_fraction = mixed_fraction_1 * mixed_fraction_2

    added_fraction, plus_minus_sign = decision_posi_nega(added_fraction)

    coefficient_num = added_fraction.numerator // added_fraction.denominator

    numerator_num = added_fraction.numerator - coefficient_num * added_fraction.denominator
    denominator_num = added_fraction.denominator

    return (plus_minus_sign, coefficient_num, numerator_num, denominator_num)

def div(div1, div2):
    mixed_fraction_1 = (Fraction(div1[2], div1[3]) + div1[1]) * div1[0]
    mixed_fraction_2 = (Fraction(div2[2], div2[3]) + div2[1]) * div2[0]

    added_fraction = mixed_fraction_1 / mixed_fraction_2

    added_fraction, plus_minus_sign = decision_posi_nega(added_fraction)

    coefficient_num = added_fraction.numerator // added_fraction.denominator

    numerator_num = added_fraction.numerator - coefficient_num * added_fraction.denominator
    denominator_num = added_fraction.denominator

    return (plus_minus_sign, coefficient_num, numerator_num, denominator_num)

def decision_posi_nega(added_fraction):
    if added_fraction < 0:
        plus_minus_sign = -1
        added_fraction *= -1
    else:
        plus_minus_sign = 1

    return added_fraction, plus_minus_sign

def gcd(num1, num2):
    return math.gcd(num1, num2)
