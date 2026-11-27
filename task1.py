
from exporters import Exporter


print("Перевірка абстрактного класу:")

try:
    Exporter()
except TypeError as error:
    print("error:", error)
