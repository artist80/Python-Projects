def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

def celsius_to_kelvin(celsius):
    kelvin = celsius + 273.15
    return kelvin

def kelvin_to_celsius(kelvin):
    celsius = kelvin - 273.15
    return celsius

def fahrenheit_to_kelvin(fahrenheit):
    celsius = fahrenheit_to_celsius(fahrenheit)
    kelvin = celsius_to_kelvin(celsius)
    return kelvin

def kelvin_to_fahrenheit(kelvin):
    celsius = kelvin_to_celsius(kelvin)
    fahrenheit = celsius_to_fahrenheit(celsius)
    return fahrenheit

def main():
    print("Welcome to the Temperature Calculator!")
    print("Choose the operation you want to perform:")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")
    print("4. Kelvin to Celsius")
    print("5. Fahrenheit to Kelvin")
    print("6. Kelvin to Fahrenheit")
    
    choice = input("Enter your choice (1/2/3/4/5/6): ")
    
    if choice == '1':
        celsius = float(input("Enter temperature in Celsius: "))
        print(f"{celsius} Celsius = {celsius_to_fahrenheit(celsius)} Fahrenheit")
    elif choice == '2':
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        print(f"{fahrenheit} Fahrenheit = {fahrenheit_to_celsius(fahrenheit)} Celsius")
    elif choice == '3':
        celsius = float(input("Enter temperature in Celsius: "))
        print(f"{celsius} Celsius = {celsius_to_kelvin(celsius)} Kelvin")
    elif choice == '4':
        kelvin = float(input("Enter temperature in Kelvin: "))
        print(f"{kelvin} Kelvin = {kelvin_to_celsius(kelvin)} Celsius")
    elif choice == '5':
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        print(f"{fahrenheit} Fahrenheit = {fahrenheit_to_kelvin(fahrenheit)} Kelvin")
    elif choice == '6':
        kelvin = float(input("Enter temperature in Kelvin: "))
        print(f"{kelvin} Kelvin = {kelvin_to_fahrenheit(kelvin)} Fahrenheit")
    else:
        print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
