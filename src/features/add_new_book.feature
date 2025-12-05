# U1
# Som en användare
# vill jag lägga till nya böcker i listan
# så att jag kan lägga till mina egna böcker

  Feature: Lägg till en nya böcker
    Scenario Outline:
      Given användaren är på startsidan
      When användaren trycker på knappen "Lägg till bok"
      Then "Lägg till ny bok" knappen går inte att trycka på med tomma textfält
      And  användaren skriver in "<titel>" och "<forfattare>" i text fälten
      And användaren trycker på "Lägg till ny bok"
      Then Titel och Författare fälten töms
      Then användaren trycker på knappen "Katalog"
      And En ny bok som heter "<titel>" av "<forfattare>" har lagts till sist i Katalogen

      Examples:
      |     titel      | forfattare  |
      |Sagan om ringen|  J.R.R      |
      |Världens mat   | En känd kock|

      Scenario:
