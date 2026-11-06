#noinspection CucumberUndefinedStep
Feature: Mina böcker
  # User story:
  # Som läsare vill jag kunna se vilka böcker jag markerat som favorit, i en lista för att enkelt hitta en bok att läsa härnäst.

  Scenario: en favoritbok syns i Mina böcker listan

    Given jag är på startsidan
    When  jag klickar på hjärtat för "Ormar på ett plan: En Python-berättelse"
    And   jag går till Mina böcker fliken genom att klicka på fliken
    Then  boken "Ormar på ett plan: En Python-berättelse" syns under fliken Mina böcker