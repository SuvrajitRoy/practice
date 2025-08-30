class CurrencyConverter:
    
#class attribute, base value dollar
    exchange_rates = {
        'USD': 1.0,       #base value
        'BDT': 121.99,
        'EUR': 0.88,
        'GBP': 0.74,
        'INR': 85.11,
        'JPY': 142.76,
        'NZD': 1.666,
        'AUD': 1.541,
        'PKR': 281.982,
        'MYR': 4.218
    }
    
 #instance attribute
    def __init__(self, amount, from_currency, to_currency):
       
        self.amount = amount
        self.from_currency = from_currency.upper()
        self.to_currency = to_currency.upper()
      

 #instance method handle coversion
    def convert(self):
        
        if self.from_currency not in CurrencyConverter.exchange_rates or \
        self.to_currency not in CurrencyConverter.exchange_rates:
            return "Invalid currency not in out system"
            
        base_amount = self.amount/ CurrencyConverter.exchange_rates[self.from_currency]
            
        converted_amount = base_amount* CurrencyConverter.exchange_rates[self.to_currency]
        return round (converted_amount, 2) 
            
    #(Currency, new rate)
    @classmethod
    def update_rate(cls,currency, new_rate):
        cls.exchange_rates[currency] = new_rate

    @staticmethod #helper
    def is_valid_currency(code):
        return code.upper() in CurrencyConverter.exchange_rates
    

class Logger:
    #instance method converter CurrencyConverter object 
    def log(self, user, converter):
        result = converter.convert()
        print(f"Record: {user} converted {converter.amount} {converter.from_currency} -> {result} {converter.to_currency}")


# CurrencyConverter.update_rate("BDT", "130")

if __name__== "__main__":
    amount = float(input("Enter amount: "))
    from_curr = input("Enter your currency: ")
    to_curr = input("Enter your desired currency in which you want to convert: ")
    user = input("Enter your Name: ")

     #Object created
    converter = CurrencyConverter(amount, from_curr, to_curr)   

    if not CurrencyConverter.is_valid_currency(from_curr) or not CurrencyConverter.is_valid_currency(to_curr):
        print("Invalid currency we don't have that currency")

    else:
        logger_obj = Logger()
        logger_obj.log(user, converter)

