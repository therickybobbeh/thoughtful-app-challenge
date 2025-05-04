def sort(width, height, length, mass, limit_size=1000000, limit_mass=20):
    """
    Sorts the given dimensions and mass based on predefined limits.
    
    Parameters:
    width (float): The width of the object in cm.
    height (float): The height of the object in cm.
    length (float): The length of the object in cm.
    mass (float): The mass of the object in kilograms.
    limit_size (float): The volume limit in cm³ (default is 1,000,000 cm³).
    limit_mass (float): The mass limit in kilograms (default is 20 kg).
    
    Returns:
    str: "STANDARD" if the object is standard, "SPECIAL" if it is special, and "REJECTED" if it is rejected.
    """
    volume = width * height * length
    if volume >= limit_size and mass <= limit_mass:
        return "STANDARD"
    elif (volume >= limit_size and mass > limit_mass) or (volume < limit_size and mass > limit_mass):
        return "SPECIAL"
    else:
        return "REJECTED"

def main():
    print("Enter the dimensions (width, height, length in cm) and mass (in kg) of the object:")
    try:
        width = float(input("Width (cm): "))
        height = float(input("Height (cm): "))
        length = float(input("Length (cm): "))
        mass = float(input("Mass (kg): "))
        result = sort(width, height, length, mass)
        print(f"The object is classified as: {result}")
    except ValueError:
        print("Invalid input. Please enter numeric values for dimensions and mass.")

if __name__ == "__main__":
    main()
