
from faker import Faker

fake = Faker("es_ES")

print("=== 10 direcciones ===")
for i in range(10):
    direccion = fake.address().replace("\n", ", ")
    print(f"{i+1}. {direccion}")
