from exporters import Exporter


if __name__ == "__main__":
    try:
        Exporter()
    except TypeError as error:
        print("error:", error)
