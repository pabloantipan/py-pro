def make_repeater_of(n):
    def repeater(string):
        assert type(string) == str, "Only strings please"
        return string * n

    return repeater


def make_division_by(n):
    assert type(n) == int, "Only integers not zero please"
    assert n != 0, "Cannot divide by zero"

    def division(number):
        assert type(number) == int, "Only integers please"
        return number / n

    return division


def run():
    rep_3 = make_repeater_of(3)
    print(rep_3("Hello"))

    div_4 = make_division_by(4)
    print(div_4(16))


if __name__ == "__main__":
    run()
