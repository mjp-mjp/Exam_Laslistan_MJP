#noinspection CucumberUndefinedStep
Feature: Katalog
  # User story:
  # Som läsare vill jag kunna välja böcker i katalogen som favoriter för att hålla koll på vilka böcker jag vill läsa.

  Scenario: välja en bok som favorit

    Given jag är på startsidan
    When  jag klickar på hjärtat för "Ormar på ett plan: En Python-berättelse"
    Then  boken "Ormar på ett plan: En Python-berättelse" är markerad som favorit
