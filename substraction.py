def subtrahiere(x, y):
    """
    Diese Funktion nimmt zwei Zahlen als Argumente entgegen und gibt die Differenz zurück.

    Parameter:
    - x (float oder int): Die erste Zahl.
    - y (float oder int): Die zweite Zahl.

    Rückgabe:
    float oder int: Die Differenz von x und y.
    """
    differenz = x - y
    return differenz

def dividiere(x, y):
    """
    Diese Funktion nimmt zwei Zahlen als Argumente entgegen und gibt das Quotient zurück.

    Parameter:
    - x (float oder int): Der Dividend.
    - y (float oder int): Der Divisor. Muss von Null verschieden sein.

    Rückgabe:
    float oder int: Das Ergebnis der Division von x durch y.
    """
    if y != 0:
        quotient = x / y
        return quotient
    else:
        raise ValueError("Der Divisor (y) darf nicht Null sein.")