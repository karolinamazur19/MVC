
<!DOCTYPE html>
<html lang="pl">
<head>
    <meta charset="UTF-8">
    <style>
        @page {
            size: A4;
            margin: 20mm;
            background-color: #ffffff;
        }
        body {
            font-family: 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
            line-height: 1.6;
            color: #333;
            margin: 0;
            padding: 0;
        }
        .header-banner {
            background-color: #0078d4;
            color: white;
            padding: 20px;
            border-radius: 8px;
            margin-bottom: 20px;
        }
        h1 { margin: 0; font-size: 22pt; }
        h2 { 
            color: #0078d4; 
            border-bottom: 2px solid #0078d4; 
            padding-bottom: 5px; 
            margin-top: 25px;
            font-size: 16pt;
        }
        h3 { color: #444; font-size: 13pt; margin-top: 15px; }
        code {
            background-color: #f4f4f4;
            padding: 2px 5px;
            border-radius: 4px;
            font-family: 'Consolas', monospace;
            font-size: 10pt;
        }
        .code-block {
            background-color: #2d2d2d;
            color: #f8f8f2;
            padding: 15px;
            border-radius: 6px;
            font-family: 'Consolas', monospace;
            white-space: pre-wrap;
            margin: 10px 0;
            font-size: 10pt;
        }
        .feature-list {
            list-style-type: none;
            padding: 0;
        }
        .feature-list li {
            margin-bottom: 10px;
            padding-left: 25px;
            position: relative;
        }
        .feature-list li::before {
            content: '✔';
            position: absolute;
            left: 0;
            color: #28a745;
            font-weight: bold;
        }
        .footer {
            margin-top: 30px;
            font-size: 9pt;
            color: #777;
            text-align: center;
            border-top: 1px solid #eee;
            padding-top: 10px;
        }
    </style>
</head>
<body>
    <div class="header-banner">
        <h1>Projekt: Cyfrowa Biblioteka</h1>
        <p>System zarządzania zasobami bibliotecznymi w architekturze ASP.NET Core MVC</p>
    </div>

    <h2>1. Opis Projektu</h2>
    <p>
        Aplikacja "Cyfrowa Biblioteka" to w pełni funkcjonalny system CRUD stworzony w technologii .NET. 
        Projekt demonstruje praktyczne zastosowanie wzorca architektonicznego <strong>Model-View-Controller (MVC)</strong> 
        oraz mechanizmów walidacji i filtrowania danych.
    </p>

    <h2>2. Wykorzystany Wzorzec Architektoniczny</h2>
    <p>Projekt ściśle rozdziela odpowiedzialność na trzy warstwy:</p>
    <ul>
        <li><strong>Model:</strong> Klasa <code>Book</code> definiująca strukturę danych i reguły walidacji.</li>
        <li><strong>View:</strong> Widoki Razor wykorzystujące Bootstrap do estetycznej prezentacji danych.</li>
        <li><strong>Controller:</strong> <code>BooksController</code> zarządzający logiką biznesową i przepływem żądań.</li>
    </ul>

    <h2>3. Funkcjonalności (Pełny CRUD)</h2>
    <ul class="feature-list">
        <li><strong>Create (Dodawanie):</strong> Formularz z walidacją pól (tytuł, autor, rok).</li>
        <li><strong>Read (Odczyt):</strong> Dynamiczna lista książek z responsywną tabelą.</li>
        <li><strong>Update (Edycja):</strong> Możliwość aktualizacji danych istniejących rekordów.</li>
        <li><strong>Delete (Usuwanie):</strong> Bezpieczne usuwanie pozycji z potwierdzeniem JavaScript.</li>
        <li><strong>Filtrowanie:</strong> Zaawansowana wyszukiwarka po tytule i autorze (Case-Insensitive).</li>
    </ul>

    <h2>4. Instrukcja Uruchomienia</h2>
    <h3>Wymagania:</h3>
    <p>Zainstalowane środowisko <code>.NET SDK 8.0</code> (lub nowsze).</p>
    
    <h3>Kroki:</h3>
    <ol>
        <li>Otwórz folder projektu w terminalu.</li>
        <li>Uruchom komendę budującą i startującą serwer:
            <div class="code-block">dotnet run</div>
        </li>
        <li>Aplikacja będzie dostępna pod adresem: 
            <code>http://localhost:5076/Books</code>
        </li>
    </ol>

    <h2>5. Zastosowane Technologie</h2>
    <ul>
        <li>ASP.NET Core MVC</li>
        <li>Entity Framework Core (InMemory/Static Collection)</li>
        <li>Bootstrap 5.x</li>
        <li>jQuery Validation (Walidacja po stronie klienta)</li>
    </ul>

    <div class="footer">
        Projekt zaliczeniowy - 2024. Wykonany zgodnie z wytycznymi dokumentacji projektowej.
    </div>
</body>
</html>
