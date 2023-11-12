import requests


class Converter:
    def __init__(self, amount, from_, to):
        self.to = to.upper()
        self.amount = float(amount)
        self.from_ = from_.upper()

    def get_exchange_rate(self, base_currency, target_currency):
        api_url = f"https://api.exchangerate-api.com/v4/latest/{base_currency}"
        response = requests.get(api_url)
        data = response.json()
        
        if response.status_code == 200:
            rate = data['rates'].get(target_currency)
            if rate is not None:
                return rate
            else:
                pass
        else:
            return {"ok": False, "code": response.status_code}

    def convert(self):
        rate = self.get_exchange_rate(self.from_, self.to)
        
        if rate is not None:
            converted_amount = self.amount * rate
            return {"amount": self.amount, "from": self.from_, "converted_amount": converted_amount, "to": self.to}
        else:
            return None