"""Print the Cloudstep Software order report."""

from business_rules import (
    calculate_license_total,
    format_license_line,
    gets_trainer,
    largest_license,
    needs_contract_review,
    total_licensed,
)

orders = [
    {"company": "Pine Books", "seat_price": 40.00, "seats": 5, "education": False},
    {"company": "Quarry School", "seat_price": 35.00, "seats": 12, "education": True},
    {"company": "Redwood Cargo", "seat_price": 45.00, "seats": 60, "education": False},
    {"company": "Summit College", "seat_price": 50.00, "seats": 150, "education": True},
    {"company": "Tidal Health", "seat_price": 55.00, "seats": 100, "education": False},
    {"company": "Upland Farms", "seat_price": 60.00, "seats": 24, "education": False},
    {"company": "Vega Dental", "seat_price": 30.00, "seats": 25, "education": True},
    {"company": "Willow Law", "seat_price": 400.00, "seats": 9, "education": False},
]


def main() -> None:
    """Print one line per order and the summary lines."""
    print("Cloudstep Software - Order Report")

    order_count = 0
    review_count = 0
    trainer_count = 0
    for order in orders:
        total = calculate_license_total(
            order["seat_price"], order["seats"], order["education"]
        )
        contract_review = needs_contract_review(total)
        trainer = gets_trainer(order["seats"], total)
        print(format_license_line(order["company"], total, contract_review, trainer))

        order_count = order_count + 1
        if contract_review:
            review_count = review_count + 1
        if trainer:
            trainer_count = trainer_count + 1

    grand_total = total_licensed(orders)
    average = grand_total / order_count

    print(f"Orders: {order_count}")
    print(f"Total licensed: ${grand_total:.2f}")
    print(f"Average license total: ${average:.2f}")
    print(f"Largest license total: {largest_license(orders)}")
    print(f"Contract reviews needed: {review_count}")
    print(f"Trainers assigned: {trainer_count}")


if __name__ == "__main__":
    main()