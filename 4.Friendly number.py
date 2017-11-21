from decimal import Decimal


def friendly_number(number, base=1000, decimals=0, suffix='',
                    powers=['', 'k', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y']):
    number = Decimal(number)
    power = 0
    while abs(number) >= base and power < len(powers) - 1:
        power += 1
        number /= base
    number = round(number, decimals) if decimals else int(number)

    result = '{:.{dec}f}{}{}'.format(number, powers[power], suffix, dec=decimals)
    print(result)
    return result

if __name__ == '__main__':
    assert friendly_number(102) == '102', '102'
    assert friendly_number(10240) == '10k', '10k'
    assert friendly_number(12341234, decimals=1) == '12.3M', '12.3M'
    assert friendly_number(12461, decimals=1) == '12.5k', '12.5k'
    assert friendly_number(1024000000, base=1024, suffix='iB') == '976MiB', '976MiB'
    assert friendly_number(12000000, decimals=3) == '12.000M', '12.000M'
    assert friendly_number(102, decimals=2) == '102.00', '102.00'
