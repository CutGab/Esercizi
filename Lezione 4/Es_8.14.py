manufacturer = (input("Insert their manufacturer: "))

model_name = (input("Insert their model: "))

def build_profile(manufacturer: str, model_name: str):
    
    car: dict = {}
    
    car["Manufacturer"] = manufacturer
    
    car["Model Name"] = model_name

    return car

print(build_profile(model_name, manufacturer))