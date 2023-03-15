# https://leetcode.com/problems/convert-the-temperature/

celsius = 36.50


def convert_temp(celsius):
    lst = []
    kelvin = 273.15
    lst.append(celsius + kelvin)
    lst.append(celsius * 1.80 + 32.00)

    return lst

print(convert_temp(celsius))
