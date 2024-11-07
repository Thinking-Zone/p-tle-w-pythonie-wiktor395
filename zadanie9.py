# Pętla szukająca pierwszej liczby podzielnej przez 7 w przedziale od 1 do 100
for i in range(1, 101):  # range(1, 101) generuje liczby od 1 do 100
    if i % 7 == 0:  # Sprawdzamy, czy liczba jest podzielna przez 7
        print(f"Pierwsza liczba podzielna przez 7 to: {i}")
        break  # Zatrzymujemy pętlę po znalezieniu pierwszej liczby
