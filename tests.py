import unittest
from conversions import (
    convertCelsiusToKelvin, convertCelsiusToFahrenheit,
    convertFahrenheitToCelsius, convertFahrenheitToKelvin,
    convertKelvinToCelsius, convertKelvinToFahrenheit
)
from conversions_refactored import convert, ConversionNotPossible

class TestConversions(unittest.TestCase):

    def test_convertCelsiusToKelvin(self):
        self.assertEqual(convertCelsiusToKelvin(0), 273.15)
        self.assertEqual(convertCelsiusToKelvin(100), 373.15)

    def test_convertCelsiusToFahrenheit(self):
        self.assertEqual(convertCelsiusToFahrenheit(0), 32)
        self.assertEqual(convertCelsiusToFahrenheit(100), 212)

    def test_convertFahrenheitToCelsius(self):
        self.assertEqual(convertFahrenheitToCelsius(32), 0)
        self.assertEqual(convertFahrenheitToCelsius(212), 100)

    def test_convertFahrenheitToKelvin(self):
        self.assertEqual(convertFahrenheitToKelvin(32), 273.15)
        self.assertEqual(convertFahrenheitToKelvin(212), 373.15)

    def test_convertKelvinToCelsius(self):
        self.assertEqual(convertKelvinToCelsius(273.15), 0)
        self.assertEqual(convertKelvinToCelsius(373.15), 100)

    def test_convertKelvinToFahrenheit(self):
        self.assertEqual(convertKelvinToFahrenheit(273.15), 32)
        self.assertEqual(convertKelvinToFahrenheit(373.15), 212)

    def test_general_conversion(self):
        self.assertEqual(convert("Celsius", "Kelvin", 0), 273.15)
        self.assertEqual(convert("Fahrenheit", "Celsius", 32), 0)
        self.assertEqual(convert("Kelvin", "Fahrenheit", 373.15), 212)

    def test_invalid_conversion(self):
        with self.assertRaises(ConversionNotPossible):
            convert("Celsius", "Miles", 100)  # Should raise error

# Run the tests
if __name__ == '__main__':
    unittest.main()

# test push
