
from faker import Faker

fake = Faker()

print("10 usuarios y URLs")
for i in range(10):
    usuario = fake.user_name()
    url = fake.url()
    print(f"{i+1}. Usuario: {usuario}  |  URL: {url}")
