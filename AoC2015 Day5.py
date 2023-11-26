import re

file = open("Day5 input.txt", "r")
lines = file.readlines()
file.close()


def check_nice_string(s):
    vowel_regex = r"(?:.*[aeiou]){3,}"
    double_regex = r"(.)\1"
    disallowed_regex = r"ab|cd|pq|xy"

    has_three_vowels = re.search(vowel_regex, s)
    has_double_letter = re.search(double_regex, s)
    has_disallowed = re.search(disallowed_regex, s)

    return has_three_vowels and has_double_letter and not has_disallowed


counter = 0
for line in lines:
    bool = check_nice_string(line)
    if bool:
        counter += 1

print(counter)


def check_nice_string2(s):
    pair_twice_regex = r"(..).*\1"
    repeat_with_one_between_regex = r"(.).\1"

    has_pair_twice = re.search(pair_twice_regex, s) is not None
    has_repeat_with_one_between = re.search(repeat_with_one_between_regex, s) is not None

    return has_pair_twice and has_repeat_with_one_between


counter = 0
for line in lines:
    bool = check_nice_string2(line)
    if bool:
        counter += 1

print(counter)
