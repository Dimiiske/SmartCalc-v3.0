import pytest
import ctypes

def result_c(input_string):
    calc_lib = ctypes.CDLL('./libcalc.so')
    calc_lib.result_c.argtypes = [ctypes.c_char_p, ctypes.POINTER(ctypes.c_int)]
    calc_lib.result_c.restype = ctypes.c_double
    error_code = ctypes.c_int()
    result = calc_lib.result_c(input_string.encode('utf-8'), ctypes.byref(error_code))
    return result

def test_calc_0():
    error = 1
    my_res = result_c("sin(30) + 2 * 3 - (5 - 1)")
    origin = 1.011968375907
    assert abs(my_res - origin) < 1e-7

def test_calc_1():
    error = 1
    my_res = result_c("2 + 2.2")
    origin = 4.2
    assert abs(my_res - origin) < 1e-7

def test_calc_2():
    error = 1
    my_res = result_c("sin(cos(2^3))")
    origin = -0.1449871
    assert abs(my_res - origin) < 1e-7

def test_calc_3():
    error = 1
    my_res = result_c("sin(cos(2^3)")
    origin = 0
    assert abs(my_res - origin) < 1e-7

def test_calc_4():
    error = 1
    my_res = result_c("sqrt(4.12)+asin(0)")
    origin = 2.029778313
    assert abs(my_res - origin) < 1e-7

def test_calc_5():
    error = 1
    my_res = result_c("55 + 3 / 2")
    origin = 56.5
    assert abs(my_res - origin) < 1e-7

def test_calc_6():
    error = 1
    my_res = result_c("atan(0.5422 / 23.12) + tan(0.256) + log(2.21)")
    origin = 0.6295825
    assert abs(my_res - origin) < 1e-7

def test_calc_7():
    error = 1
    my_res = result_c("12 + (cos(23.12 + sin(12.12 - cos(2.21 / 12))))")
    origin = 11.00962042178
    assert abs(my_res - origin) < 1e-7

def test_calc_8():
    error = 1
    my_res = result_c("tan(3.14159/2)")
    origin = 753695.9951408089
    assert abs(my_res - origin) < 1e-7

def test_calc_9():
    error = 1
    my_res = result_c("-3--4")
    origin = 1
    assert abs(my_res - origin) < 1e-7

def test_calc_10():
    error = 1
    my_res = result_c(".")
    origin = 0
    assert abs(my_res - origin) < 1e-7

def test_calc_11():
    error = 1
    my_res = result_c("acos()")
    origin = 0
    assert abs(my_res - origin) < 1e-7

def test_calc_12():
    error = 1
    my_res = result_c("sin(3.14159/2)*2.231^3-acos(0.123)")
    origin = 9.65700833938
    assert abs(my_res - origin) < 1e-7

def test_calc_13():
    error = 1
    my_res = result_c("5^2+25/5*6")
    origin = 55
    assert abs(my_res - origin) < 1e-7

def test_calc_14():
    error = 1
    my_res = result_c("10mod5")
    origin = 0
    assert abs(my_res - origin) < 1e-7

def test_calc_15():
    error = 1
    my_res = result_c("sqrt(15)")
    origin = 3.8729833
    assert abs(my_res - origin) < 1e-7

def test_calc_16():
    error = 1
    my_res = result_c("ln(2.718281828459045)")
    origin = 0.99999999
    assert abs(my_res - origin) < 1e-7

def test_calc_17():
    error = 1
    my_res = result_c("0*3 + sin(-55)")
    origin = 0.9997551
    assert abs(my_res - origin) < 1e-7

def test_calc_18():
    error = 1
    my_res = result_c("0*3 + sin(-55)")
    origin = 0.9997551
    assert abs(my_res - origin) < 1e-7

def test_calc_19():
    error = 1
    my_res = result_c("acos(-1) + 53542/4555 + (22+1.511)")
    origin = 38.407148087
    assert abs(my_res - origin) < 1e-7

def test_calc_20():
    error = 1
    my_res = result_c("asin(-1)")
    origin = -1.5707963
    assert abs(my_res - origin) < 1e-7

def test_calc_21():
    error = 1
    my_res = result_c("khreh")
    origin = 0
    assert abs(my_res - origin) < 1e-7

def test_calc_22():
    error = 1
    my_res = result_c("656566")
    origin = 656566
    assert abs(my_res - origin) < 1e-7

def test_calc_23():
    error = 1
    my_res = result_c("sin(22) / cos(22) + (5^2 + 3.5 - 1 * 5)")
    origin = 23.50885165
    assert abs(my_res - origin) < 1e-7

def test_calc_24():
    error = 1
    my_res = result_c("log(10) + ln(5) / sqrt(5)")
    origin = 1.7197625
    assert abs(my_res - origin) < 1e-7

def test_calc_25():
    error = 1
    my_res = result_c("75 + atan(-5)")
    origin = 73.6265993
    assert abs(my_res - origin) < 1e-7

def test_calc_26():
    error = 1
    my_res = result_c("3*2*2*2*2*2*")
    origin = 0
    assert abs(my_res - origin) < 1e-7

def test_calc_27():
    error = 1
    my_res = result_c("7.5.5.5")
    origin = 0
    assert abs(my_res - origin) < 1e-7

def test_calc_28():
    error = 1
    my_res = result_c("+7.5")
    origin = 7.5
    assert abs(my_res - origin) < 1e-7

def test_calc_29():
    error = 1
    my_res = result_c("sqrp(30)")
    origin = 0
    assert abs(my_res - origin) < 1e-7

def test_calc_30():
    error = 1
    my_res = result_c("mod")
    origin = 0
    assert abs(my_res - origin) < 1e-7

def test_calc_31():
    error = 1
    my_res = result_c("5 mod 0")
    origin = 0
    assert abs(my_res - origin) < 1e-7

def test_calc_32():
    error = 1
    my_res = result_c("5 / 0")
    origin = 0
    assert abs(my_res - origin) < 1e-7

def test_calc_33():
    error = 1
    my_res = result_c("-")
    origin = 0
    assert abs(my_res - origin) < 1e-7

def test_calc_34():
    error = 1
    my_res = result_c("cos(.)")
    origin = 0
    assert abs(my_res - origin) < 1e-7

def test_calc_35():
    error = 1
    my_res = result_c("5^")
    origin = 0
    assert abs(my_res - origin) < 1e-7

def test_calc_36():
    error = 1
    my_res = result_c("5 modd 3")
    origin = 0
    assert abs(my_res - origin) < 1e-7

# gcc -shared -fPIC -o libcalc.so s21_calc.c