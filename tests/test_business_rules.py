from business_rules import (
    calculate_license_cost,
    calculate_license_total,
    format_license_line,
    get_seat_discount,
    gets_trainer,
    largest_license,
    needs_contract_review,
    total_licensed,
)


# Rule 1: license cost
def test_license_cost_is_price_times_seats():
    assert round(calculate_license_cost(40.00, 5), 2) == 200.00


# Rule 2: first tier (10 seats)
def test_discount_is_zero_at_9_seats():
    assert get_seat_discount(9) == 0.0


def test_discount_is_7_percent_at_10_seats():
    assert get_seat_discount(10) == 0.07


# Rule 2: second tier (50 seats), education customer
def test_discount_is_7_percent_at_49_seats_education():
    assert get_seat_discount(49, education=True) == 0.07


def test_discount_is_16_percent_at_50_seats_education():
    assert get_seat_discount(50, education=True) == 0.16


# Rule 3: 16% only for education
def test_discount_is_7_percent_at_50_seats_not_education():
    assert get_seat_discount(50) == 0.07


def test_education_changes_license_total():
    assert round(calculate_license_total(50.00, 150, education=True), 2) == 6300.00
    assert round(calculate_license_total(50.00, 150), 2) == 6975.00


# Rule 4: onboarding fee limit ($400)
def test_fee_added_when_discounted_cost_is_exactly_400():
    assert round(calculate_license_total(400.00, 1), 2) == 460.00


def test_no_fee_when_discounted_cost_is_400_01():
    assert round(calculate_license_total(400.01, 1), 2) == 400.01


def test_license_total_applies_7_percent_discount():
    assert round(calculate_license_total(45.00, 60), 2) == 2511.00


# Rule 5: contract review limit ($5,000)
def test_no_contract_review_at_exactly_5000():
    assert needs_contract_review(5000.00) is False


def test_contract_review_at_5000_01():
    assert needs_contract_review(5000.01) is True


# Rule 6: trainer seat limit (25 seats), total kept low
def test_trainer_at_25_seats_with_low_total():
    assert gets_trainer(25, 100.00) is True


def test_no_trainer_at_24_seats_with_low_total():
    assert gets_trainer(24, 100.00) is False


# Rule 6: trainer total limit ($3,000), seats kept low
def test_no_trainer_at_exactly_3000_with_few_seats():
    assert gets_trainer(1, 3000.00) is False


def test_trainer_at_3000_01_with_few_seats():
    assert gets_trainer(1, 3000.01) is True


# total_licensed
def test_total_licensed_adds_two_orders():
    orders = [
        {"company": "Pine Books", "seat_price": 40.00, "seats": 5, "education": False},
        {"company": "Quarry School", "seat_price": 35.00, "seats": 12, "education": True},
    ]
    assert round(total_licensed(orders), 2) == 710.60


def test_total_licensed_empty_list_is_zero():
    assert round(total_licensed([]), 2) == 0.00


# largest_license
def test_largest_license_finds_biggest_order():
    orders = [
        {"company": "Pine Books", "seat_price": 40.00, "seats": 5, "education": False},
        {"company": "Willow Law", "seat_price": 400.00, "seats": 9, "education": False},
    ]
    assert largest_license(orders) == "Willow Law"


def test_largest_license_tie_returns_first():
    orders = [
        {"company": "First Co", "seat_price": 100.00, "seats": 5, "education": False},
        {"company": "Second Co", "seat_price": 100.00, "seats": 5, "education": False},
    ]
    assert largest_license(orders) == "First Co"


def test_largest_license_empty_list_returns_empty_string():
    assert largest_license([]) == ""


# format_license_line
def test_format_line_with_no_and_no():
    line = format_license_line("Pine Books", 260.00, False, False)
    assert line == "Pine Books: $260.00 | contract review: no | trainer: no"


def test_format_line_with_yes_and_yes():
    line = format_license_line("Summit College", 6300.00, True, True)
    assert line == "Summit College: $6300.00 | contract review: yes | trainer: yes"


def test_format_line_shows_two_decimal_places():
    line = format_license_line("Upland Farms", 1339.2, False, False)
    assert line == "Upland Farms: $1339.20 | contract review: no | trainer: no"