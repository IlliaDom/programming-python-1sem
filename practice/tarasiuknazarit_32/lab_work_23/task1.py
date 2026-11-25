from exporters import Exporter

try:
    Exporter()
except TypeError as error:
    print("error:", error)
