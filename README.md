# Programowanie w architekturze klient-serwer, semestr letni 22/23

## Dokumentacja do projektu

W miarę możliwości wszystko idzie do folderu "docs", najbardziej aktualna wersja na branchu `main`.

##### W części 2 (27 kwietnia) oddajemy:
- szkielet bazy danych (utworzone modele w Django):  api->`models.py`
- diagramy przypadków użycia: docs->`diagram-use-case.pdf`
- definicje endpointów: docs->`endpointy.md`
- poziomy dostępu: docs->`poziomy_dostepu.txt`

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


## Brawo!!!
Po wpisaniu `python manage.py runserver` w terminalu powino coś działać w przeglądarce :D


## Co dalej?
Jak mamy wszystko zainstalowane/zaktualizowane to można póki co pobawić się panelem admina (jak ma się superusera).
Po odpaleniu serwera wystarczy wpisać adres z terminala w przeglądarce i na końcu dodać `/admin/`.


## Aktualizacja requirements.txt
Jeśli zainstalujemy pakiety, których nie było wcześniej w projekcie i chcemy ułatwić innym robotę, należy zrobić to:

1. Jednorazowo w terminalu wewnątrz środowiska wirtualnego projektu: `pip install pipreqs`
2. Jednorazowo w terminalu wewnątrz środowiska wirtualnego projektu: `pip install pip-tools`
3. Za każdym razem przed commitem: `pipreqs --savepath=requirements.in && pip-compile`

Dzięki temu każdy pobierając nowe wersje plików może użyć polecenia `pip install -r requirements.txt` i nie musi szukać brakujących pakietów :)