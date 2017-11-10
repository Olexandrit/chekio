def friendly_number(number, base=1000, decimals=0, suffix='',
                    powers=['', 'k', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y']):
    """
    Format a number as friendly text, using common suffixes.
    """

    if number < base:
        print("number= ", number)
        return str(number)

    index_power = 0
    while number > base:
        index_power += 1
        number = number / base

    print("decimals= ", decimals)

    if decimals > 0:
        number = round(number, decimals)
    else:
        number = int(number)

    number = str(number) + powers[index_power] + suffix

    print("number= ", number)
    return str(number)


if __name__ == '__main__':
    # assert friendly_number(102) == '102', '102'
    # assert friendly_number(10240) == '10k', '10k'
    # assert friendly_number(12341234, decimals=1) == '12.3M', '12.3M'
    assert friendly_number(12461, decimals=1) == '12.5k', '12.5k'
    # assert friendly_number(1024000000, base=1024, suffix='iB') == '976MiB', '976MiB'
    # assert friendly_number(12000000, decimals=3) == '12.000M', '12.000M'
