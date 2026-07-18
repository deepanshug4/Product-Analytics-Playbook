"""
Generate all synthetic datasets for the Product Analytics Playbook.
"""

from pathlib import Path

from generators.orders import generate_orders
from generators.restaurants import generate_restaurants
from generators.sessions import generate_sessions
from generators.users import generate_users


OUTPUT_DIR = Path("data/synthetic")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def main():

    print("🚀 Generating QuickBite datasets...\n")

    users = generate_users()
    print(f"✓ Users: {len(users):,}")

    restaurants = generate_restaurants()
    print(f"✓ Restaurants: {len(restaurants):,}")

    sessions = generate_sessions(
        users,
        restaurants,
        n_sessions=100000,
    )
    print(f"✓ Sessions: {len(sessions):,}")

    orders = generate_orders(sessions)
    print(f"✓ Orders: {len(orders):,}")

    users.to_csv(
        OUTPUT_DIR / "users_v1.csv",
        index=False,
    )

    restaurants.to_csv(
        OUTPUT_DIR / "restaurants_v1.csv",
        index=False,
    )

    sessions.to_csv(
        OUTPUT_DIR / "sessions_v1.csv",
        index=False,
    )

    orders.to_csv(
        OUTPUT_DIR / "orders_v1.csv",
        index=False,
    )

    print("\n✅ All datasets saved to data/synthetic/")


if __name__ == "__main__":
    main()
