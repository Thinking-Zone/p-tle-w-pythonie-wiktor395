suma = 0  # Zmienna do przechowywania sumy

# Iterujemy tylko po liczbach nieparzystych
for i in range(1, 101, 2):  # range(1, 101, 2) - zaczynamy od 1, idziemy do 100, krok 2
    suma += i  # Dodajemy każdą liczbę nieparzystą do sumy

# Wyświetlamy wynik
print("Suma liczb nieparzystych od 1 do 100 wynosi:", suma)
