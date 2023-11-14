import requests;

print("- Crypto Checking Application -");

while True:
    crypto = input("Enter the name of crypto (bitcoin): ").lower();
    currency = input("Enter the currency: ").lower();

    def get_crypto_price(coin):
        url = f'https://api.coingecko.com/api/v3/simple/price?ids={coin}&vs_currencies={currency}';
        try:
            response = requests.get(url);
        except:
            raise ValueError("Could not get a url!");
        data = response.json();
        if coin in data:
            return data[coin][currency];
        else:
            return None;
    
    price = get_crypto_price(crypto);
    if price is not None:
        print(f"Current course {crypto.capitalize()}: {price} {currency.upper()}");
    else:
        print("Sorry, you crypto is not find of not available!");
    exit = input("Enter anything to exit: ");
    if exit.isalpha() or exit.isdigit() is True:
        break;