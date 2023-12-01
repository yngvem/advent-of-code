from pathlib import Path


DIGITS = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4", 
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
    "zero": "0",
}
REVERSED_DIGITS = {key[::-1]: value for key, value in DIGITS.items()}


def extract_leading_number(input_: str, digit_map: dict[str, str]) -> str:
    """Extracts leading number if possible
    
    >>> extract_leading_number('7løh', DIGITS)
    '7'
    >>> extract_leading_number('twofgxh', DIGITS)
    '2'
    >>> extract_leading_number('7løh', REVERSED_DIGITS)
    '7'
    >>> extract_leading_number('owtfgxh', REVERSED_DIGITS)
    '2'
    """
    
    if input_[0].isdigit():
        return input_[0]
    
    for key, value in digit_map.items():
        if input_.startswith(key):
            return value


def get_calibration_value(calibration_line: str) -> int:
    """
    >>> get_calibration_value('1abc2')
    12
    >>> get_calibration_value('pqr3stu8vwx')
    38
    >>> get_calibration_value('a1b2c3d4e5f')
    15
    >>> get_calibration_value('treb7uchet')
    77
    >>> get_calibration_value('two1nine')
    29
    >>> get_calibration_value('eightwothree')
    83
    >>> get_calibration_value('abcone2threexyz')
    13
    >>> get_calibration_value('xtwone3four')
    24
    >>> get_calibration_value('4nineeightseven2')
    42
    >>> get_calibration_value('zoneight234')
    14
    >>> get_calibration_value('7pqrstsixteen')
    76

    """
    line_length = len(calibration_line)

    for offset in range(line_length):
        first_digit = extract_leading_number(calibration_line[offset:], DIGITS)
        if first_digit is not None:
            break
    
    for i in range(line_length):
        offset = -(1 + i)
        last_digit = extract_leading_number(calibration_line[offset::-1], REVERSED_DIGITS)
        if last_digit is not None:
            break
    
    return int(first_digit + last_digit)


def get_total_calibration_value(calibration_document: str) -> int:
    """ Gets calibration value from document

    >>> document = '''1abc2
    ... pqr3stu8vwx
    ... a1b2c3d4e5f
    ... treb7uchet'''
    >>> get_total_calibration_value(document)
    142

    >>> document = '''two1nine
    ... eightwothree
    ... abcone2threexyz
    ... xtwone3four
    ... 4nineeightseven2
    ... zoneight234
    ... 7pqrstsixteen'''
    >>> get_total_calibration_value(document)
    281
    """
    return sum((get_calibration_value(line) for line in calibration_document.splitlines()))


if __name__ == "__main__":
    with open(Path(__file__).parent / "data/input") as f:
        calibration_document = f.read()
    print(get_total_calibration_value(calibration_document))
