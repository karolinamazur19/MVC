// Inicjalizacja budowniczego aplikacji (Builder), który konfiguruje hosta, 
// serwer Kestrel oraz domyślne ustawienia (np. czytanie pliku appsettings.json).
var builder = WebApplication.CreateBuilder(args);

// --- SEKCJA USŁUG (Dependency Injection) ---

// Dodanie usług niezbędnych do obsługi Kontrolerów wraz z Widokami (Razor Views).
// To tutaj system rejestruje mechanizmy routingu oraz silnik renderujący widoki (.cshtml).
builder.Services.AddControllersWithViews();

// Zbudowanie instancji aplikacji (App) na podstawie skonfigurowanych wcześniej usług.
var app = builder.Build();

// --- SEKCJA POTOKU ŻĄDAŃ (Middleware Pipeline) ---

// Konfiguracja obsługi błędów i bezpieczeństwa dla środowisk innych niż deweloperskie (np. Produkcja).
if (!app.Environment.IsDevelopment())
{
    // W razie nieobsłużonego błędu przekierowuje użytkownika do kontrolera Home i akcji Error.
    app.UseExceptionHandler("/Home/Error");
    
    // Włącza mechanizm HSTS (HTTP Strict Transport Security), wymuszający bezpieczne połączenia.
    app.UseHsts();
}

// Middleware wymuszający przekierowanie z protokołu HTTP na bezpieczny HTTPS.
app.UseHttpsRedirection();

// Mechanizm analizujący adres URL i dopasowujący go do odpowiednich tras (Route).
app.UseRouting();

// Middleware obsługujący uprawnienia użytkowników (wymagane przed wywołaniem kontrolerów).
app.UseAuthorization();

// Obsługa nowych mechanizmów optymalizacji zasobów statycznych (dostępne w nowszych wersjach .NET).
app.MapStaticAssets();

// Definicja domyślnej trasy routingu. 
// Jeśli użytkownik wejdzie na stronę główną, system domyślnie szuka kontrolera 'Home' i akcji 'Index'.
// {id?} oznacza, że parametr identyfikatora jest opcjonalny.
app.MapControllerRoute(
    name: "default",
    pattern: "{controller=Home}/{action=Index}/{id?}")
    .WithStaticAssets();

// Uruchomienie aplikacji i rozpoczęcie nasłuchiwania na nadchodzące żądania HTTP.
app.Run();
