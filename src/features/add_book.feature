#noinspection CucumberUndefinedStep
Feature: Lägg till bok
  # User story:
  # Som läsare vill jag kunna lägga till en bok som saknas i katalogen för att kunna välja den som favorit.

  Scenario: lägga till en ny bok

    Given jag är på startsidan
    When  jag går till Lägg till bok
    And   jag skriver in titeln "Min nya bok"
    And   jag skriver in författaren "Okänd Författare"
    And   jag klickar på Lägg till ny bok
    And   jag går till Katalog
    Then  boken "Min nya bok" finns i katalogen
    