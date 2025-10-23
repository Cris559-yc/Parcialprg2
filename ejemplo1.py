
from faker import Faker

fake = Faker("jp_JP")

print("=== 10 nombres completos ===")
for i in range(10):
    print(f"{i+1}. {fake.name()}")
