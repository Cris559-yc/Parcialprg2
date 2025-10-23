
from faker import Faker

fake = Faker()

print("=== 10 tarjetas de crédito (ficticias) ===")
for i in range(10):
    print(f"\nTarjeta #{i+1}")
    print(fake.credit_card_full())
    print("-" * 40)
