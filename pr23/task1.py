from exporters import Exporter

NAME = "Kateryna"
SURNAME = "Katashynska"
GROUP = "IT-31"


def main():
    print(f"{NAME} {SURNAME}, {GROUP}")
    try:
        Exporter()
    except TypeError as error:
        print("error:", error)


if __name__ == "__main__":
    main()
