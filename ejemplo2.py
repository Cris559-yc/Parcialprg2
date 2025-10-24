
from faker import Faker

fake = Faker()

print("10 correos electrónicos")
for i in range(10):
    print(f"{i+1}. {fake.email()}")
