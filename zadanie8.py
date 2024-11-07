# Inicjalizujemy licznik odpowiedzi "nie"
nie_count = 0

# Pętla, która pyta użytkownika, aż odpowie "tak"
while True:
    user_input = input("Czy pada? (Odpowiedz 'tak', 'nie' lub 'nie wiem'): ").lower()

    # Sprawdzamy odpowiedź
    if user_input == "tak":
        print(f"Zakończono. Liczba odpowiedzi 'nie': {nie_count}")
        break  # Kończymy pętlę, gdy użytkownik odpowie "tak"
    elif user_input == "nie":
        nie_count += 1  # Zwiększamy licznik odpowiedzi "nie"
    elif user_input == "nie wiem":
        print("To wyjdź na zewnątrz i się dowiedz.")
    else:
        print("Nie rozumiem odpowiedzi. Proszę odpowiedzieć 'tak', 'nie' lub 'nie wiem'.")
