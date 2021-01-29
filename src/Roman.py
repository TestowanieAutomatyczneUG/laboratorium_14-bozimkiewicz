class Roman:
    def roman(self, number):
        letters = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
        numbers = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        roman_number = ''
        i = 0
        while number > 0:
            for _ in range(number // numbers[i]):
                roman_number += letters[i]
                number -= numbers[i]
            i += 1
        return roman_number
