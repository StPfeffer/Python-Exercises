class Person():
    def __init__(self, name: str, address: str):
        self.name = name
        self.address = address
    
    def __str__(self) -> str:
        return f"{self.name}, {self.address}"


def main() -> None:
    person = Person(name="Mateus", address="Avenida Minas Gerais")
    print(person)


if __name__ == "__main__":
    main()