# Programowanie w architekturze klient-serwer, semestr letni 22/23

## IDE i VCS
Warunki, w jakich projekt powinien działać poprawnie:

1. Pycharm 2023.1 połączony z kontem na GitHubie + Python3.9
2. Po włączeniu PyCharma otwieramy projekt z GitHuba:
   1. Opcja "Get from VCS"
      ![setup01](/docs/img/setup01.png?raw=true)
   2. Wybór repozytorium i lokalnego katalogu:
      - URL: https://github.com/trashhpanda/klient-serwer
      - Directory: według uznania
      - na koniec klikamy "Clone"
      ![setup02](/docs/img/setup02.png?raw=true)
3. Dodajemy środowisko wirtualne i interpreter:
   1. Pycharm -> Settings -> Project: [nazwa projektu] -> Python interpreter
   2. Dalej żeby dodać odpowiedni interpreter wybieramy "Add local interpreter..."
      ![setup03](/docs/img/setup03.png?raw=true)
   3. Wyskakuje okno z wyborem środowiska wirtualnego
      - Zostawiamy Virtualenv
      - Wybieramy opcję "New"
      - Location: lokalizacja projektu u nas na komputerze (Directory z punktu 2.2.) z końcówką /venv/ (powinno być automatycznie)
      - Base interpreter: lokalizacja gdzie jest na komputerze interpreter Pythona
      - klikamy OK
      ![setup04](/docs/img/setup04.png?raw=true)
   4. Teraz powinien się wyświetlać interpreter i jego lokalizacja w projekcie oraz zainstalowane pakiety. Klikamy "OK".
      ![setup05](/docs/img/setup05.png?raw=true)


## Instalacja pakietów

1. W PyCharmie otwieramy Terminal
   ![setup06](/docs/img/setup06.png?raw=true)
2. Aktualizujemy/instalujemy pip (`pip install --upgrade pip`)
3. Instalujemy wymagane pakiety poleceniem `pip install -r requirements.txt`
