def is_line(line1, line2):
    try:
        float(line1) and float(line2)
        return False
    except ValueError:
        return True

def comparison(line1, line2):
    if is_line(line1, line2):
        if line1 == line2:
            return 1
        elif len(line1) > len(line2):
            return 2
        elif line2 == 'learn':
            return 3
    else:
        return 0

if __name__ == "__main__":
    print(comparison(1254,0.327))
    print(comparison('merci', 'merci'))
    print(comparison('checkingline1','line2'))
    print(comparison('you','learn'))
    print(comparison('no','result'))