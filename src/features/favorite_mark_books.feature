# U2
# Som en användare
# vill jag favoritmarkera böcker se dem i en separat lista
# så att jag kan lättare hålla koll på de böcker jag är intresserad av

  Feature: Favoritmarkera böcker
    Scenario:
      Given användaren är på startsidan
      When användaren trycker på knappen "Mina böcker"
      Then texten "När du valt, kommer dina favoritböcker att visas här." syns på sidan
      Then användaren trycker på knappen "Katalog"
      Then användaren trycker på hjärtikonen för "Min katt är min chef"
      Then användaren trycker på hjärtikonen för "Jag trodde det var tisdag"
      When användaren trycker på knappen "Mina böcker"
      Then texten "När du valt, kommer dina favoritböcker att visas här." syns inte på sidan
      Then en lista med böckerna "Min katt är min chef" och "Jag trodde det var tisdag" syns på sidan