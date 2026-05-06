# Projekt: Cyfrowa Biblioteka - System Zarządzania Księgozbiorem

## 1. Opis Projektu
Aplikacja "Cyfrowa Biblioteka" to system webowy stworzony w technologii **ASP.NET Core 8.0 MVC**. Projekt realizuje pełną funkcjonalność zarządzania zasobami bibliotecznymi (CRUD) i został zaprojektowany z myślą o przejrzystości kodu oraz łatwości obsługi.

## 2. Funkcjonalności
* **Lista Książek (Read):** Przeglądanie wszystkich pozycji w responsywnej tabeli z wykorzystaniem Bootstrap 5.
* **Dodawanie (Create):** Intuicyjny formularz umożliwiający wprowadzanie nowych książek do bazy.
* **Edycja (Update):** Możliwość modyfikacji danych istniejących rekordów.
* **Usuwanie (Delete):** Bezpieczne usuwanie pozycji z mechanizmem potwierdzenia akcji.
* **Wyszukiwarka:** Funkcja filtrowania listy po tytule oraz autorze (niezależna od wielkości liter).
* **Walidacja:** Pełna walidacja danych wejściowych (np. wymagane pola, zakres roku wydania) działająca po stronie serwera i klienta.

## 3. Architektura MVC
Projekt ściśle realizuje wzorzec **Model-View-Controller**:
* **Model (`Models/Book.cs`):** Definiuje strukturę danych i reguły poprawności (atrybuty DataAnnotations).
* **View (`Views/Books/`):** Warstwa prezentacji wykorzystująca silnik Razor oraz Bootstrap do budowy interfejsu użytkownika.
* **Controller (`Controllers/BooksController.cs`):** Zarządza logiką biznesową, odbiera żądania użytkownika i koordynuje przepływ danych między modelem a widokiem.

## 4. Instrukcja Uruchomienia
Aby uruchomić projekt lokalnie, należy posiadać zainstalowane środowisko .NET 8 SDK.

1. Otwórz folder projektu w terminalu lub Visual Studio Code.
2. Przywróć zależności:
   ```bash
   dotnet restore
