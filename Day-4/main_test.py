# So you can execute the file with python to test the file
from main import *
import pytest
if __name__ == "__main__":
    import subprocess
    # use -k <string> to only run tests which contain the provided string
    subprocess.run('pytest')
    exit()


def test_convert_value_to_int():
    assert convert_value_to_int('2000')   == 2000
    assert convert_value_to_int('-2000')  == -2000
    assert convert_value_to_int('2000d')  == None
    assert convert_value_to_int(' 2000 ') == 2000


def test_convert_passport_value_to_int():
    passport = { 'byr': '2000' }
    assert convert_passport_value_to_int('byr', passport) == True
    assert passport == { 'byr': 2000 }

    passport = { 'byr': '2000d' }
    assert convert_passport_value_to_int('byr', passport) == False
    assert passport == { 'byr': '2000d' }

def test_validate_value_between():
    key = 'byr'
    passport = { key: '2000' }
    assert validate_value_between(passport, key, 1900, 2100) == True

    passport = { key: '1900' }
    assert validate_value_between(passport, key, 1900, 2100) == True
    passport = { key: '2100' }
    assert validate_value_between(passport, key, 1900, 2100) == True

    passport = { key: '1899' }
    assert validate_value_between(passport, key, 1900, 2100) == False
    passport = { key: '2101' }
    assert validate_value_between(passport, key, 1900, 2100) == False

    passport = { key: '2000abc' }
    assert validate_value_between(passport, key, 1900, 2100) == False

    passport = { key: '2000' }
    assert validate_value_between(passport, key, 1900, 2100, 4) == True
    passport = { key: '02000' }
    assert validate_value_between(passport, key, 1900, 2100, 4) == False

def test_validate_height():
    met = 'metric'
    imp = 'imperial'

    passport = { met: '180cm', imp: '65in' }
    assert validate_height(passport, met, (160, 190), (60, 70)) == True
    assert validate_height(passport, imp, (160, 190), (60, 70)) == True

    passport = { met: '100cm', imp: '10in' }
    assert validate_height(passport, met, (160, 190), (60, 70)) == False
    assert validate_height(passport, imp, (160, 190), (60, 70)) == False

    passport = { met: '200cm', imp: '100in' }
    assert validate_height(passport, met, (160, 190), (60, 70)) == False
    assert validate_height(passport, imp, (160, 190), (60, 70)) == False

    passport = { met: '200', imp: '100din' }
    assert validate_height(passport, met, (160, 190), (60, 70)) == False
    assert validate_height(passport, imp, (160, 190), (60, 70)) == False

def test_validate_hair_color():
    passport = { 'hcl': '#123456' }
    assert validate_hair_color(passport, 'hcl') == True
    passport = { 'hcl': '#6789ab' }
    assert validate_hair_color(passport, 'hcl') == True
    passport = { 'hcl': '#cdefff' }
    assert validate_hair_color(passport, 'hcl') == True

    passport = { 'hcl': '#12345g' }
    assert validate_hair_color(passport, 'hcl') == False

    passport = { 'hcl': '#1234567' }
    assert validate_hair_color(passport, 'hcl') == False
    passport = { 'hcl': '#1234' }
    assert validate_hair_color(passport, 'hcl') == False
    passport = { 'hcl': '1234567' }
    assert validate_hair_color(passport, 'hcl') == False
