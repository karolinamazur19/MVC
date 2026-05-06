using Microsoft.AspNetCore.Mvc;
using MvcLibrary.Models;
using System;
using System.Collections.Generic;
using System.Linq;

namespace MvcLibrary.Controllers;

// Kontroler zarządza przepływem danych między Modelem a Widokiem
public class BooksController : Controller
{
    private static List<Book> _books = new List<Book>();

    // Wyświetla listę i obsługuje wyszukiwanie (funkcja na wyższą ocenę)
    public IActionResult Index(string searchString)
    {
        var books = _books.AsEnumerable();
        if (!string.IsNullOrEmpty(searchString))
        {
            books = books.Where(b => (b.Title != null && b.Title.Contains(searchString, StringComparison.OrdinalIgnoreCase)) 
                                  || (b.Author != null && b.Author.Contains(searchString, StringComparison.OrdinalIgnoreCase)));
        }
        return View(books.ToList());
    }

    // Wyświetla formularz tworzenia
    public IActionResult Create() => View();

    // Zapisuje nową książkę po walidacji (ModelState.IsValid)
    [HttpPost]
    [ValidateAntiForgeryToken]
    public IActionResult Create(Book book)
    {
        if (ModelState.IsValid)
        {
            book.Id = _books.Any() ? _books.Max(b => b.Id) + 1 : 1;
            _books.Add(book);
            return RedirectToAction(nameof(Index));
        }
        return View(book);
    }

    // Pobiera dane do edycji (część pełnego CRUD)
    public IActionResult Edit(int id)
    {
        var book = _books.FirstOrDefault(b => b.Id == id);
        if (book == null) return NotFound();
        return View(book);
    }

    // Zapisuje zmiany w istniejącej książce
    [HttpPost]
    [ValidateAntiForgeryToken]
    public IActionResult Edit(int id, Book book)
    {
        if (id != book.Id) return NotFound();
        if (ModelState.IsValid)
        {
            var existingBook = _books.FirstOrDefault(b => b.Id == id);
            if (existingBook != null)
            {
                existingBook.Title = book.Title;
                existingBook.Author = book.Author;
                existingBook.ReleaseYear = book.ReleaseYear;
            }
            return RedirectToAction(nameof(Index));
        }
        return View(book);
    }

    // Usuwa książkę z listy
    [HttpPost]
    [ValidateAntiForgeryToken]
    public IActionResult Delete(int id)
    {
        var book = _books.FirstOrDefault(b => b.Id == id);
        if (book != null) _books.Remove(book);
        return RedirectToAction(nameof(Index));
    }
}