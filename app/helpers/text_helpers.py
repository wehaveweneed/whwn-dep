import re


def strip_non_alphanumeric(input):
    pattern = re.compile('[\W_]+')
    return pattern.sub('', input)
