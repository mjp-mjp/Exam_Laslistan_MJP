# Examination

Examination Testverktyg, TAP VT26D av Marie J Parming (MJP).

## Om projektet

Läslistan är en webbsida där man kan välja ut sina favoriter från en katalog med böcker, eller lägga till nya. I projektet har jag testat både backend i Python samt den befintliga webbsidan https://tap-vt26-testautomatisering.github.io/exam/

## Vad jag har testat

**Backend (pytest)**
- Enhetstester för `BookStore.addBook`, `BookStore.toggleFavorite`, `FavoriteBooks.add` och `FavoriteBooks.remove`, samt att en favorit går att avmarkera igen.
- Integrationstest för att en bok från `BookStore` som markeras som favorit hamnar i `FavoriteBooks`.

**Frontend (behave + Playwright)**
- Katalog: att man kan markera en bok som favorit.
- Lägg till bok: att en ny bok med titel och författare hamnar i katalogen.
- Mina böcker: att en favoritmarkerad bok syns i listan.

User stories finns i [STORIES.md](STORIES.md) och svar på teorifrågorna i [ANSWERS.md](ANSWERS.md).

Alla tester körs automatiskt med GitHub Actions vid push till main (headless).

## Starta projektet

För att starta mitt projekt behöver man Python 3.14. Skriv följande commandline i terminalen, medan man står i projektets rotmapp.

Skapa och aktivera en virtuell miljö (Windows):

```commandline
python -m venv .venv
.venv\Scripts\activate
```

Installera paketen och webbläsaren:

```commandline
pip install -r requirements.txt
playwright install chromium
```

Kör testerna:

```commandline
pytest
behave
```

## Vad jag har gjort

Samtliga G-krav (A–E) är genomförda.

| G-krav | Status |
|--------|--------|
| A      | ✅ |
| B      | ✅ |
| C      | ✅ |
| D      | ✅ |
| E      | ✅ |