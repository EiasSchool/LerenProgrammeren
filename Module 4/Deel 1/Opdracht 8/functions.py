# Controleert of een getal een priemgetal is.
def is_prime(number:int) -> bool:
    # als number klijner of gelijk aan 1 krijg je false
    if number <= 1:
        return False
    
    # als number is gelijk aan 2 krijg je true
    if number == 2:
        return True
    
    # geeft false als het getal deelbaar is door 2 behalve 2 zelf
    if number % 2 == 0:
        return False
    
    # controleert deelbaarheid vanaf 3 tot number met stappen van 2
    max_divisor = int(number**0.5) + 1
    for d in range(3, max_divisor, 2):
        if number % d == 0:
            return False
    
    # retourneert True als het getal nergens door gedeeld kon worden
    return True
def get_primes_up_to(n: int) -> list:
    """Geeft een lijst met alle priemgetallen tot en met n."""
    primes = []
    for num in range(2, n + 1):
        if is_prime(num):
            primes.append(num)
    return primes

def get_first_n_primes(n: int) -> list:
    """Geeft een lijst met de eerste n priemgetallen."""
    primes = []
    num = 2
    while len(primes) < n:
        if is_prime(num):
            primes.append(num)
        num += 1
    return primes

def get_primes_between(a: int, b: int) -> list:
    """Geeft een lijst met priemgetallen tussen a en b."""
    primes = []
    for num in range(a, b + 1):
        if is_prime(num):
            primes.append(num)
    return primes
