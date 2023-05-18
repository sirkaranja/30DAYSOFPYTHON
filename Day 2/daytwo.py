temperature = int(input("Temperature: "))
rain = input('Is it raining outside? (yes/no): ').lower()

if rain == 'no':
    if temperature < 50:
        print('Hi, consider wearing a coat, hat, scarf, and gloves')
    elif 50 <= temperature < 70:
        print('Wear a sweater or light jacket')
    elif temperature >= 70:
        print('Hi, consider wearing a t-shirt and shorts')
elif rain == 'yes':
    if 50 <= temperature < 70:
        print('Wearing a rain jacket and boots')
    elif temperature >= 70:
        print('Hi, consider wearing a rain jacket and boots')
