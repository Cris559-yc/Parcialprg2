
from faker import Faker

fake = Faker("es_ES")

print("10 nombres completos")
for i in range(10):
    print(f"{i+1}. {fake.name()}")
