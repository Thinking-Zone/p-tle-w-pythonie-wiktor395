# Program do rozwiązania zadania
for i in range(1, 51):  # Iterujemy po liczbach od 1 do 50 (włącznie)
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")  # Jeśli liczba jest podzielna zarówno przez 3, jak i przez 5
    elif i % 3 == 0:
        print("Fizz")  # Jeśli liczba jest podzielna przez 3
    elif i % 5 == 0:
        print("Buzz")  # Jeśli liczba jest podzielna przez 5
    else:
        print(i)  # W przeciwnym razie wypisujemy liczbę
