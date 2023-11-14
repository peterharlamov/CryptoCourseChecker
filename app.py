import requests;

print("- Crypto Checking Application -");

while True:
    repeats = int(input("Select a count of cypto tokens you want to check: "))
    all_crypto_tokens = []
    for i in range(repeats):
        crypto = input("Enter the name of crypto (bitcoin): ").lower();
        all_crypto_tokens.append(crypto);
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
    
    for i in range(repeats):
        price = get_crypto_price(all_crypto_tokens[i]);
        if price is not None:
            print(f"Current course {all_crypto_tokens[i].capitalize()}: {price} {currency.upper()}");
        else:
            print("Sorry, you crypto is not find of not available!");
    exit = input("Enter anything to exit: ");
    if exit.isalpha() or exit.isdigit() is True:
        break;