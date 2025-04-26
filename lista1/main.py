from interfejs import Zadanie, ZadaniePriorytetowe, ZadanieRegularne, ManagerZadan

def interfejs():
    manager = ManagerZadan()

    while True:
        print("\nMenu:")
        print("1. Dodaj zadanie")
        print("2. Usuń zadanie")
        print("3. Oznacz jako wykonane")
        print("4. Edytuj zadanie")
        print("5. Wyświetl zadania")
        print("6. Wyjście")
        wybor = input("Wybierz opcję: ")

        if wybor == "1":
            tytul = input("Tytuł: ")
            opis = input("Opis: ")
            termin = input("Termin wykonania (YYYY-MM-DD): ")
            typ = input("Priorytetowe (P) / Regularne (R) / Zwykłe (Z): ").upper()

            if typ == "P":
                priorytet = int(input("Priorytet (1-5): "))
                zadanie = ZadaniePriorytetowe(tytul, opis, termin, priorytet)
            elif typ == "R":
                powtarzalnosc = input("Powtarzalność (codziennie, tygodniowo, miesięcznie): ")
                zadanie = ZadanieRegularne(tytul, opis, termin, powtarzalnosc)
            else:
                zadanie = Zadanie(tytul, opis, termin)

            manager.dodaj_zadanie(zadanie)

        elif wybor == "2":
            tytul = input("Podaj tytuł zadania do usunięcia: ")
            zadanie = next((z for z in manager.zadania if z.tytul == tytul), None)
            if zadanie in manager:
                manager.usun_zadanie(zadanie)
                print("Zadanie usunięte.")
            else:
                print("Nie znaleziono zadania.")

        elif wybor == "3":
            tytul = input("Podaj tytuł zadania do oznaczenia jako wykonane: ")
            zadanie = next((z for z in manager.zadania if z.tytul == tytul), None)
            if zadanie in manager:
                manager.oznacz_jako_wykonane(zadanie)
                print("Zadanie oznaczone jako wykonane.")
            else:
                print("Nie znaleziono zadania.")

        elif wybor == "4":
            tytul = input("Podaj tytuł zadania do edycji: ")
            zadanie = next((z for z in manager.zadania if z.tytul == tytul), None)
            if zadanie in manager:
                nowy_tytul = input("Nowy tytuł: ")
                nowy_opis = input("Nowy opis: ")
                nowy_termin = input("Nowy termin (YYYY-MM-DD): ")
                manager.edytuj_zadanie(zadanie, nowy_tytul, nowy_opis, nowy_termin)
                print("Zadanie zaktualizowane.")
            else:
                print("Nie znaleziono zadania.")

        elif wybor == "5":
            manager.wyswietl_zadania()

        elif wybor == "6":
            print("Zamykanie aplikacji...")
            break

        else:
            print("Nieprawidłowa opcja, spróbuj ponownie.")


if __name__ == "__main__":
    interfejs()
