#noinspection CucumberUndefinedStep
Feature: Katalog
  # User story:
  # Som läsare vill jag kunna se alla böcker i katalogen med titel och författare, samt kunna markera eller avmarkera en bok som favorit via hjärtat, för att hålla koll på vilka böcker jag kanske vill läsa.

  Scenario: välja en bok som favorit

    Given jag är på startsidan
    When  jag klickar på hjärtat för "Ormar på ett plan: En Python-berättelse"
    Then  boken "Ormar på ett plan: En Python-berättelse" är markerad som favorit
