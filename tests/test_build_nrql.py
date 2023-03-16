from newrelic_grep.nrgrep import build_nrql, get_timezone

timezone = get_timezone()


def test_1() -> None:
    pattern = "pat"
    expect = "SELECT * FROM Log WHERE message LIKE '%pat%' LIMIT MAX SINCE 3 DAYS AGO"

    nrql = build_nrql(pattern, None, None)

    assert nrql == expect


def test_percent() -> None:
    pattern = "%%%"
    expect = "SELECT * FROM Log WHERE message LIKE '%\\%\\%\\%%' LIMIT MAX SINCE 3 DAYS AGO"

    nrql = build_nrql(pattern, None, None)

    assert nrql == expect


def test_single_quote() -> None:
    pattern = "'''"
    expect = "SELECT * FROM Log WHERE message LIKE '%\\'\\'\\'%' LIMIT MAX SINCE 3 DAYS AGO"

    nrql = build_nrql(pattern, None, None)

    assert nrql == expect


def test_double_quote() -> None:
    pattern = '"""'
    expect = '''SELECT * FROM Log WHERE message LIKE '%"""%' LIMIT MAX SINCE 3 DAYS AGO'''

    nrql = build_nrql(pattern, None, None)

    assert nrql == expect


def test_backslash() -> None:
    pattern = "\\"
    expect = "SELECT * FROM Log WHERE message LIKE '%\\\\%' LIMIT MAX SINCE 3 DAYS AGO"

    nrql = build_nrql(pattern, None, None)

    assert nrql == expect


def test_since_full() -> None:
    pattern = "pat"
    since = "20230315123456"
    expect = f"SELECT * FROM Log WHERE message LIKE '%pat%' LIMIT MAX SINCE '2023-03-15 12:34:56 {timezone}'"

    nrql = build_nrql(pattern, since, None)

    assert nrql == expect


def test_since_no_sec() -> None:
    pattern = "pat"
    since = "202303151234"
    expect = f"SELECT * FROM Log WHERE message LIKE '%pat%' LIMIT MAX SINCE '2023-03-15 12:34:00 {timezone}'"

    nrql = build_nrql(pattern, since, None)

    assert nrql == expect


def test_since_no_min() -> None:
    pattern = "pat"
    since = "2023031512"
    expect = f"SELECT * FROM Log WHERE message LIKE '%pat%' LIMIT MAX SINCE '2023-03-15 12:00:00 {timezone}'"

    nrql = build_nrql(pattern, since, None)

    assert nrql == expect


def test_since_no_hour() -> None:
    pattern = "pat"
    since = "20230315"
    expect = f"SELECT * FROM Log WHERE message LIKE '%pat%' LIMIT MAX SINCE '2023-03-15 00:00:00 {timezone}'"

    nrql = build_nrql(pattern, since, None)

    assert nrql == expect


def test_since_no_day() -> None:
    pattern = "pat"
    since = "202303"
    expect = f"SELECT * FROM Log WHERE message LIKE '%pat%' LIMIT MAX SINCE '2023-03-01 00:00:00 {timezone}'"

    nrql = build_nrql(pattern, since, None)

    assert nrql == expect


def test_since_no_month() -> None:
    pattern = "pat"
    since = "2023"
    expect = f"SELECT * FROM Log WHERE message LIKE '%pat%' LIMIT MAX SINCE '2023-01-01 00:00:00 {timezone}'"

    nrql = build_nrql(pattern, since, None)

    assert nrql == expect


def test_until_full() -> None:
    pattern = "pat"
    until = "20230315123456"
    expect = f"SELECT * FROM Log WHERE message LIKE '%pat%' LIMIT MAX SINCE 3 DAYS AGO UNTIL '2023-03-15 12:34:56 {timezone}'"

    nrql = build_nrql(pattern, None, until)

    assert nrql == expect


def test_until_no_sec() -> None:
    pattern = "pat"
    until = "202303151234"
    expect = f"SELECT * FROM Log WHERE message LIKE '%pat%' LIMIT MAX SINCE 3 DAYS AGO UNTIL '2023-03-15 12:34:00 {timezone}'"

    nrql = build_nrql(pattern, None, until)

    assert nrql == expect


def test_until_no_min() -> None:
    pattern = "pat"
    until = "2023031512"
    expect = f"SELECT * FROM Log WHERE message LIKE '%pat%' LIMIT MAX SINCE 3 DAYS AGO UNTIL '2023-03-15 12:00:00 {timezone}'"

    nrql = build_nrql(pattern, None, until)

    assert nrql == expect


def test_until_no_hour() -> None:
    pattern = "pat"
    until = "20230315"
    expect = f"SELECT * FROM Log WHERE message LIKE '%pat%' LIMIT MAX SINCE 3 DAYS AGO UNTIL '2023-03-15 00:00:00 {timezone}'"

    nrql = build_nrql(pattern, None, until)

    assert nrql == expect


def test_until_no_day() -> None:
    pattern = "pat"
    until = "202303"
    expect = f"SELECT * FROM Log WHERE message LIKE '%pat%' LIMIT MAX SINCE 3 DAYS AGO UNTIL '2023-03-01 00:00:00 {timezone}'"

    nrql = build_nrql(pattern, None, until)

    assert nrql == expect


def test_until_no_month() -> None:
    pattern = "pat"
    until = "2023"
    expect = f"SELECT * FROM Log WHERE message LIKE '%pat%' LIMIT MAX SINCE 3 DAYS AGO UNTIL '2023-01-01 00:00:00 {timezone}'"

    nrql = build_nrql(pattern, None, until)

    assert nrql == expect


def test_regex() -> None:
    pattern = "pat"
    expect = "SELECT * FROM Log WHERE message RLIKE r'.*pat.*' LIMIT MAX SINCE 3 DAYS AGO"

    nrql = build_nrql(pattern, regex=True)

    assert nrql == expect


def test_regex_percent() -> None:
    pattern = "%%%"
    expect = "SELECT * FROM Log WHERE message RLIKE r'.*%%%.*' LIMIT MAX SINCE 3 DAYS AGO"

    nrql = build_nrql(pattern, regex=True)

    assert nrql == expect


def test_regex_single_quote() -> None:
    pattern = "'''"
    expect = "SELECT * FROM Log WHERE message RLIKE r'.*\\'\\'\\'.*' LIMIT MAX SINCE 3 DAYS AGO"

    nrql = build_nrql(pattern, regex=True)

    assert nrql == expect


def test_regex_double_quote() -> None:
    pattern = '"""'
    expect = '''SELECT * FROM Log WHERE message RLIKE r'.*""".*' LIMIT MAX SINCE 3 DAYS AGO'''

    nrql = build_nrql(pattern, regex=True)

    assert nrql == expect


def test_regex_backslash() -> None:
    pattern = "\\"
    expect = "SELECT * FROM Log WHERE message RLIKE r'.*\\\\.*' LIMIT MAX SINCE 3 DAYS AGO"

    nrql = build_nrql(pattern, regex=True)

    assert nrql == expect


def test_regex_start() -> None:
    pattern = "^pat"
    expect = "SELECT * FROM Log WHERE message RLIKE r'^pat.*' LIMIT MAX SINCE 3 DAYS AGO"

    nrql = build_nrql(pattern, regex=True)

    assert nrql == expect


def test_regex_end() -> None:
    pattern = "pat$"
    expect = "SELECT * FROM Log WHERE message RLIKE r'.*pat$' LIMIT MAX SINCE 3 DAYS AGO"

    nrql = build_nrql(pattern, regex=True)

    assert nrql == expect


def test_attribute_condition() -> None:
    pattern = "pat"
    attrs = ["hostname:myhost"]
    expect = "SELECT * FROM Log WHERE message LIKE '%pat%' AND hostname='myhost' LIMIT MAX SINCE 3 DAYS AGO"

    nrql = build_nrql(pattern, conditions=attrs)

    assert nrql == expect


def test_attribute_two_conditions() -> None:
    pattern = "pat"
    attrs = ["hostname:myhost", "param:value"]
    expect = "SELECT * FROM Log WHERE message LIKE '%pat%' AND hostname='myhost' AND param='value' LIMIT MAX SINCE 3 DAYS AGO"

    nrql = build_nrql(pattern, conditions=attrs)

    assert nrql == expect


def test_attribute_condition_percent() -> None:
    pattern = "pat"
    attrs = ["hostname:%%%"]
    expect = "SELECT * FROM Log WHERE message LIKE '%pat%' AND hostname='%%%' LIMIT MAX SINCE 3 DAYS AGO"

    nrql = build_nrql(pattern, conditions=attrs)

    assert nrql == expect


def test_attribute_condition_single_quote() -> None:
    pattern = "pat"
    attrs = ["hostname:'''"]
    expect = "SELECT * FROM Log WHERE message LIKE '%pat%' AND hostname='\\'\\'\\'' LIMIT MAX SINCE 3 DAYS AGO"

    nrql = build_nrql(pattern, conditions=attrs)

    assert nrql == expect


def test_attribute_condition_double_quote() -> None:
    pattern = "pat"
    attrs = ['hostname:"""']
    expect = '''SELECT * FROM Log WHERE message LIKE '%pat%' AND hostname='"""' LIMIT MAX SINCE 3 DAYS AGO'''

    nrql = build_nrql(pattern, conditions=attrs)

    assert nrql == expect


def test_attribute_condition_backslash() -> None:
    pattern = "pat"
    attrs = ["hostname:\\"]
    expect = "SELECT * FROM Log WHERE message LIKE '%pat%' AND hostname='\\\\' LIMIT MAX SINCE 3 DAYS AGO"

    nrql = build_nrql(pattern, conditions=attrs)

    assert nrql == expect


def test_limit() -> None:
    pattern = "pat"
    limit = 41
    expect = "SELECT * FROM Log WHERE message LIKE '%pat%' LIMIT 41 SINCE 3 DAYS AGO"

    nrql = build_nrql(pattern, limit=limit)

    assert nrql == expect
