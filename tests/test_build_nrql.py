from newrelic_grep.nrgrep import build_nrql

def test_1()-> None:
    pattern = "pat"
    expect = "SELECT * FROM Log WHERE message LIKE '%pat%' LIMIT MAX SINCE 3 DAYS AGO"

    nrql = build_nrql(pattern, None, None)

    assert nrql == expect

def test_percent()-> None:
    pattern = "%%%"
    expect = "SELECT * FROM Log WHERE message LIKE '%\\%\\%\\%%' LIMIT MAX SINCE 3 DAYS AGO"

    nrql = build_nrql(pattern, None, None)

    assert nrql == expect

def test_single_quote()-> None:
    pattern = "'''"
    expect = "SELECT * FROM Log WHERE message LIKE '%\\'\\'\\'%' LIMIT MAX SINCE 3 DAYS AGO"

    nrql = build_nrql(pattern, None, None)

    assert nrql == expect

def test_since_full()-> None:
    pattern = "pat"
    since = "20230315123456"
    expect = "SELECT * FROM Log WHERE message LIKE '%pat%' LIMIT MAX SINCE '2023-03-15 12:34:56 +0900'"

    nrql = build_nrql(pattern, since, None)

    assert nrql == expect

def test_since_no_sec()-> None:
    pattern = "pat"
    since = "202303151234"
    expect = "SELECT * FROM Log WHERE message LIKE '%pat%' LIMIT MAX SINCE '2023-03-15 12:34:00 +0900'"

    nrql = build_nrql(pattern, since, None)

    assert nrql == expect

def test_since_no_min()-> None:
    pattern = "pat"
    since = "2023031512"
    expect = "SELECT * FROM Log WHERE message LIKE '%pat%' LIMIT MAX SINCE '2023-03-15 12:00:00 +0900'"

    nrql = build_nrql(pattern, since, None)

    assert nrql == expect

def test_since_no_hour()-> None:
    pattern = "pat"
    since = "20230315"
    expect = "SELECT * FROM Log WHERE message LIKE '%pat%' LIMIT MAX SINCE '2023-03-15 00:00:00 +0900'"

    nrql = build_nrql(pattern, since, None)

    assert nrql == expect

def test_since_no_day()-> None:
    pattern = "pat"
    since = "202303"
    expect = "SELECT * FROM Log WHERE message LIKE '%pat%' LIMIT MAX SINCE '2023-03-01 00:00:00 +0900'"

    nrql = build_nrql(pattern, since, None)

    assert nrql == expect

def test_since_no_month()-> None:
    pattern = "pat"
    since = "2023"
    expect = "SELECT * FROM Log WHERE message LIKE '%pat%' LIMIT MAX SINCE '2023-01-01 00:00:00 +0900'"

    nrql = build_nrql(pattern, since, None)

    assert nrql == expect

def test_until_full()-> None:
    pattern = "pat"
    until = "20230315123456"
    expect = "SELECT * FROM Log WHERE message LIKE '%pat%' LIMIT MAX SINCE 3 DAYS AGO UNTIL '2023-03-15 12:34:56 +0900'"

    nrql = build_nrql(pattern, None, until)

    assert nrql == expect

def test_until_no_sec()-> None:
    pattern = "pat"
    until = "202303151234"
    expect = "SELECT * FROM Log WHERE message LIKE '%pat%' LIMIT MAX SINCE 3 DAYS AGO UNTIL '2023-03-15 12:34:00 +0900'"

    nrql = build_nrql(pattern, None, until)

    assert nrql == expect

def test_until_no_min()-> None:
    pattern = "pat"
    until = "2023031512"
    expect = "SELECT * FROM Log WHERE message LIKE '%pat%' LIMIT MAX SINCE 3 DAYS AGO UNTIL '2023-03-15 12:00:00 +0900'"

    nrql = build_nrql(pattern, None, until)

    assert nrql == expect

def test_until_no_hour()-> None:
    pattern = "pat"
    until = "20230315"
    expect = "SELECT * FROM Log WHERE message LIKE '%pat%' LIMIT MAX SINCE 3 DAYS AGO UNTIL '2023-03-15 00:00:00 +0900'"

    nrql = build_nrql(pattern, None, until)

    assert nrql == expect

def test_until_no_day()-> None:
    pattern = "pat"
    until = "202303"
    expect = "SELECT * FROM Log WHERE message LIKE '%pat%' LIMIT MAX SINCE 3 DAYS AGO UNTIL '2023-03-01 00:00:00 +0900'"

    nrql = build_nrql(pattern, None, until)

    assert nrql == expect

def test_until_no_month()-> None:
    pattern = "pat"
    until = "2023"
    expect = "SELECT * FROM Log WHERE message LIKE '%pat%' LIMIT MAX SINCE 3 DAYS AGO UNTIL '2023-01-01 00:00:00 +0900'"

    nrql = build_nrql(pattern, None, until)

    assert nrql == expect

def test_regex()-> None:
    pattern = "pat"
    expect = "SELECT * FROM Log WHERE message RLIKE r'pat' LIMIT MAX SINCE 3 DAYS AGO"

    nrql = build_nrql(pattern, regex=True)

    assert nrql == expect

def test_regex_percent()-> None:
    pattern = "%%%"
    expect = "SELECT * FROM Log WHERE message RLIKE r'%%%' LIMIT MAX SINCE 3 DAYS AGO"

    nrql = build_nrql(pattern, regex=True)

    assert nrql == expect

def test_regex_single_quote()-> None:
    pattern = "'''"
    expect = "SELECT * FROM Log WHERE message RLIKE r'\\'\\'\\'' LIMIT MAX SINCE 3 DAYS AGO"

    nrql = build_nrql(pattern, regex=True)

    assert nrql == expect
