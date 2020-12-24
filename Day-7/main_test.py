# So you can execute the file with python to test the file
if __name__ == "__main__":
    import subprocess
    # use -k <string> to only run tests which contain the provided string
    subprocess.run('pytest')
    exit()

from main import *
import pytest

def test_parse_bag_data_form_string():
    # normal bag
    string = 'light red bags contain 1 bright white bag, 2 muted yellow bags.'
    expected =  ('light red', [(1, 'bright white'), (2, 'muted yellow')])
    assert parse_bag_data_form_string(string) == expected

    string = 'bright white bags contain 1 shiny gold bag.'
    expected =  ('bright white', [(1, 'shiny gold')])
    assert parse_bag_data_form_string(string) == expected

    # only one or more than two words for color
    string = 'red bags contain 1 white bag, 2 muted dark yellow bags.'
    expected =  ('red', [(1, 'white'), (2, 'muted dark yellow')])
    assert parse_bag_data_form_string(string) == expected

    # empty bag
    string = 'faded blue bags contain no other bags.'
    expected =  ('faded blue', [])
    assert parse_bag_data_form_string(string) == expected
