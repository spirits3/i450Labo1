class StringCalculator:
    def add(string_numbers):
        if ";" in string_numbers and not(any(c.isalpha() for c in string_numbers)): 
            numbers = string_numbers.split(";")
            sum_numbers = sum([int(value) for value in numbers if int(value) < 1000])
        else : 
            try: 
                sum_numbers = int(string_numbers)
            except ValueError:
                sum_numbers = 0
        
        return sum_numbers