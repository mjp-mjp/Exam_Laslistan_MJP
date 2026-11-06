# Svar på teorifrågor

## 1. Vad är skillnaden mellan enhetstest, integrationstest, regressionstest och prestandatest?

**Enhetstest** testar en del av systemet helt isolerat, tex en enskild metod, för att se att just den logiken fungerar oberoende av resten. I mitt projekt testar jag addBook och toggleFavorite var för sig.

**Integrationstest** testar att flera delar fungerar tillsammans och skickar data rätt mellan sig. I mitt projekt testar jag att en bok som läggs till i BookStore och markeras som favorit också hamnar i FavoriteBooks.

**Regressionstest** ska säkerställa att det som redan fungerar inte går sönder när ny kod läggs till eller ändras. Det behöver inte vara nya tester, utan de enhets- och integrationstester som redan finns blir regressionstester när de körs om och om igen, tex i CI vid varje push.

**Prestandatest** mäter hur snabbt och stabilt systemet är under belastning, tex responstid, körtid och hur mycket minne/CPU det drar när det kommer många användare eller stora datamängder.

## 2. Beskriv hur det går till när man arbetar med TDD.

I TDD skriver man testet innan koden. Först skriver man ett test för något som inte finns än och kör det, då blir det rött (red). Det här gör man också för att vara säker på att testet faktiskt kan misslyckas och fungerar som det ska. Sen skriver man så lite kod som möjligt för att testet ska bli grönt (green), och här gör det inget om koden är lite ful så länge det bara fungerar. Därefter städar man upp koden (refactor), både den vanliga koden och testkoden, och kör testerna igen för att se att de fortfarande är gröna och att inget gick sönder när man städade. Sen börjar man om med nästa test.

I mitt projekt gjorde jag så med BookStore och FavoriteBooks, tex skrev jag först ett test för addBook som blev rött då metoden inte fanns, och sen skrev jag metoden så att testet blev grönt. Fördelen är att all kod har tester från början och att man bara skriver den kod som faktiskt behövs.

## 3. Beskriv hur BDD skiljer sig från TDD.

BDD är en vidareutveckling av TDD, så i båda skriver man testerna innan koden. TDD är mer för utvecklare då testerna skrivs i kod och testar enskilda metoder. I BDD beskriver man istället hur systemet ska bete sig för användaren, dvs med meningar på nästan vanligt språk, i Gherkin med Given, When och Then. Då kan alla i projektet, tex beställare/kund, testare och utvecklare, förstå testerna och vara med och ta fram dem. Fokus blir mer på vad som ger nytta för användaren än på hur koden ser ut.

I mitt projekt använde jag TDD med pytest för BookStore och FavoriteBooks, och BDD med behave för webbsidan där varje user story har en feature-fil.

## 4. Vilka sorters tester skulle du vilja använda för en webbsida som liknar Läslistan?

För backend skulle jag använda enhetstester med TDD då det går snabbt att testa varje metod för sig och fel hittas tidigt, samt integrationstester för att se att klasserna fungerar tillsammans, tex att en bok som markeras som favorit också hamnar i favoritlistan.

För frontend skulle jag använda BDD med behave och Playwright (E2E) då det testar hela flödet såsom användaren klickar runt på sidan, och features går att läsa även för beställaren. Jag skulle inte bara testa att något går att göra utan även att det går att ångra, tex att avmarkera en favorit och att boken då försvinner från Mina böcker.

Alla tester skulle köras i CI vid varje push så att de blir regressionstester, dvs att inget som redan fungerar går sönder när sidan byggs ut (dela listor, quiz, diskussioner). Får sidan många användare så behövs även prestandatester.

Utöver det automatiserade skulle jag även testa manuellt, för man ramlar alltid över saker som inte finns i en checklista eller ett i förväg uttänkt testfall.
