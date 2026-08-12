def celsius_to_fahrenheit(c):
    calcf = (c * 9/5) + 32
    return calcf
answer = celsius_to_fahrenheit(0)
print(f"0°C = {answer:.1f}°F")
answer1 = celsius_to_fahrenheit(100)
print(f"100°C = {answer1:.1f}°F")


def fahrenheit_to_celsius(f):
    calcc = (f - 32) * 5/9
    return calcc
answer2 = fahrenheit_to_celsius(72)
print(f"72°F = {answer2:.1f}°C")
