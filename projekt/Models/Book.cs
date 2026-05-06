using System.ComponentModel;
using System.ComponentModel.DataAnnotations;

namespace MvcLibrary.Models;

// Klasa modelu reprezentująca książkę w systemie
public class Book
{
    // Unikalny identyfikator książki, potrzebny do edycji i usuwania
    public int Id { get; set; }

    [Required(ErrorMessage = "Tytuł jest wymagany")]
    [DisplayName("Tytuł")]
    public string Title { get; set; }

    [Required(ErrorMessage = "Autor jest wymagany")]
    [DisplayName("Autor")]
    public string Author { get; set; }

    [Required(ErrorMessage = "Rok wydania jest wymagany")]
    [DisplayName("Rok wydania")]
    [Range(1000, 2100, ErrorMessage = "Podaj poprawny rok (między 1000 a 2100)")]
    public int ReleaseYear { get; set; }
}