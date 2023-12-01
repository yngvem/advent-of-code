from pathlib import Path


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
    """

    for character in calibration_line:
        if character.isdigit():
            first_digit = character
            break

    for character in reversed(calibration_line):
        if character.isdigit():
            last_digit = character
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
    """
    return sum((get_calibration_value(line) for line in calibration_document.splitlines()))


if __name__ == "__main__":
    with open(Path(__file__).parent / "data/input") as f:
        calibration_document = f.read()
    print(get_total_calibration_value(calibration_document))
