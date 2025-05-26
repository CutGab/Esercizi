def describe_city (name: str, country: str = "Italy"):
    print(f"{name} is in {country}")


describe_city("Milan")

describe_city("Rome")

describe_city("Tokyo", "Japan")