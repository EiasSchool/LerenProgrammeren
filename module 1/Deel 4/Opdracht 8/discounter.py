from test_lib import test, report

month_discount_brands = 'Vespa,Kymco,Yamama'
MONTH_DISCOUNT_PERC = 10
def calc_discount(price: float, brand: str, month_discount_brands: str) -> float:
    discount_brands = month_discount_brands.split(',')
    if brand in discount_brands:
        discount = (price * MONTH_DISCOUNT_PERC) / 100
        return round(discount, 2)
    else:
        return 0.0
    
test_gegevens = [
    (150.00, 'Vespa', 'Vespa,Kymco,Yamama', 15.00),
    (1500.00, 'Kymco', 'Vespa,Kymco,Yamama', 150.00),
    (2000.00, 'LOL', 'Vespa,Kymco,Yamama', 0.00),
    (3000.00, 'Yamama', 'Vespa,Kymco,Yamama', 300.00),
    (4000.00, 'Honda', 'Vespa,Kymco,Yamama', 0.00)
]

for price, brand, discount_brands, expected_discount in test_gegevens:
    calculated_discount = calc_discount(price, brand, discount_brands)
    name = f'test price: {price}, brand: {brand}'

    test(name, expected_discount, calculated_discount)

report()