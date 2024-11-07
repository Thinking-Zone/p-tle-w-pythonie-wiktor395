import random  # Importujemy moduł random

# Losujemy, czy pada deszcz
weather = random.choice(["Pada", "Nie pada"])  # Losowo wybiera "Pada" lub "Nie pada"

# Pętla, która pyta użytkownika, dopóki nie zgadnie poprawnie
while True:
    user_input = input("Czy pada deszcz? (Odpowiedz 'Pada' lub 'Nie pada'): ")

    # Sprawdzamy, czy odpowiedź użytkownika jest poprawna
    if user_input == weather:
        print("Brawo! Zgadłeś!")
        break  # Kończymy pętlę, jeśli odpowiedź jest poprawna
    else:
        print("Nie zgadłeś. Spróbuj ponownie!")
