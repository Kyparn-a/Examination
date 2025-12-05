# U3
# Som en användare
# vill jag kunna ta bort min favoritmarkering från böcker
# så att jag kan ta bort de böcker som jag inte längre är intresserad av från min favoritlista
  
  Feature: Ta bort böcker från favorit listan
    Scenario Outline:
      Given användaren är på startsidan
      When användaren trycker på knappen "Lägg till bok"
      Then användaren skriver in "<titel>" och "<forfattare>" i text fälten
      And användaren trycker på "Lägg till ny bok"
      Then användaren trycker på knappen "Katalog"
      Then användaren trycker på hjärtikonen för "<titel>"
      And användaren trycker på hjärtikonen för "Min katt är min chef"
      When användaren trycker på knappen "Mina böcker"
      Then en lista med böckerna "Min katt är min chef" och "<titel>" syns på sidan
      Then användaren trycker på knappen "Katalog"
      Then användaren tar bort på hjärtikonen för "<titel>"
      When användaren trycker på knappen "Mina böcker"
      Then boken "<titel>" har tagits bort från favorit listan

    Examples:
      |     titel      | forfattare  |
      |The one ring    |  J.R.R      |