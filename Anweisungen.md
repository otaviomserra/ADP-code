# Einführung 

Dieser Code ist eine Fortsetzung von Benjamins Arbeit (die in das Neoception®-System integriert ist) und implementiert den digitalen Schatten des CiP.

Um zu vermeiden, dass die Codes zusammengeführt werden und mögliche Fehler entstehen, befindet sich der Code für den digitalen Schatten im Ordner [datenverarbeitung](datenverarbeitung).

Es wurden jedoch einige Änderungen am ursprünglichen Code vorgenommen, denn um die Daten aus der Fabrik zu erhalten, wurde der Ansatz verfolgt, die vom Neoception-System generierten "Logs" zu speichern und die Sensordaten durch Filtern dieser Nachricht zu extrahieren.

Der digitale Schatten wurde in zwei Teile aufgeteilt, der erste bezieht sich auf das Inventar und der zweite auf die Prozesse, wobei Klassen verwendet wurden, um die Funktionsweise beider und die Berechnung der jeweiligen Kennzahlen zu trennen. Beide Teile sind wieder in den Hauptcode der [Datenverarbeitung](datenverarbeitung/datenverarbeitung_main.py) integriert.

Für das Inventar findet die Hauptoperation in [InventoryDataDistribution](datenverarbeitung/InventarDataDistribution.py) statt und die Berechnung der Kennzahlen erfolgt in [calculate_inventory_kpis](datenverarbeitung/calculate_inventory_kpis.py). Was den Prozess betrifft, so befindet sich seine Hauptfunktion in [process_requests](datenverarbeitung/process_requests.py) und seine Kennzahlen in [calculate_process_kpis](datenverarbeitung/calculate_process_kpis.py). Ein äußerst wichtiger zusätzlicher Code ist [extra_process_logs](datenverarbeitung/extra_process_logs.py), der mit den manuellen Schaltflächen in den Exceldateien integriert ist.

Um den Code auszuführen, vergewissern Sie sich, dass alle [Anforderungen](#anforderungen) erfüllt sind, und befolgen Sie die Anweisungen im Abschnitt über die [Ausführung des Codes](#Anweisung-zur-Ausführung-des-Codes).

# Anforderungen
## System-Anforderungen
Dieser Code muss auf Windows laufen. Das Datenformat im System sollte English(UK) sein. Das geht darum, dass der digitale Knopf ein spezifisches Datenformat braucht.

## Python-Anforderungen

Folgende Python-Module sollten mithilfe von ```pip install package-name``` installiert werden, indem ```package-name``` ist:
- django-environ
- numpy
- pandas
- openpyxl
- watchdog
- subprocess
- multiprocessing
- xlwings
- pythoncom
- win32com
- datetime
- sys
- logging
- json
- csv

## PyCharm-Anforderungen
Wer PyCharm nicht hat, bitte die neueste Version von "PyCharm Community Edition" (kostenlos) herunterladen und installieren	 

### Umgebungsvariablen und Datei
Damit der Code mit Neoception ausgeführt werden kann, muss die Umgebungskonfiguration aktiviert werden, gehen Sie zu:
1. Klicken Sie auf "File"
2. Klicken Sie auf "Settings"
3. Klicken Sie auf "Plugins"
4. Installieren "EnvFile"

### Parallele Ausführung
Um mehrere Skripte direkt auf PyCharm laufen zu lassen, gehen Sie zu:
1. Klicken Sie auf "Run"
2. Klicken Sie auf "Edit configurations"
3. Wählen Sie die Skripte (main.py, datenverarbeitung_main.py und extra_process_logs.py)
4. Aktivieren Sie das Kontrollkästchen "Allow parallel run"

# Anweisung zur Ausführung des Codes
Es gibt drei Skripte, die gleichzeitig ausgeführt werden müssen:
- Zuerst muss [main.py](main.py) laufen. (Erkennt die Events aus der Fabrik)
- Dann muss [datenverarbeitung_main.py](datenverarbeitung/datenverarbeitung_main.py) laufen. (Verarbeitet die erkannten Events und berechnet Kennzahlen)
- Dann muss [extra_process_logs.py](datenverarbeitung/extra_process_logs.py) laufen. (Nimmt Prozessdaten aus dem Digitalen Knopf)

# Initialisierung des Digitalen Schattens
Dieser Prozess nutzt zwei Skripte: [initialize_inventory.py](datenverarbeitung/initialize_inventory.py) und [run_reinitialization.py](datenverarbeitung/run_reinitialization.py)
- Ersetzen Sie den gesamten Inhalt vom ["Werk"](Werk)-Ordner durch den Inhalt vom ["Werk clean"](Werk-clean).
- Gehen Sie zu dem Code in [initialize_inventory.py](datenverarbeitung/initialize_inventory.py) und ändern Sie die Anzahl von Kisten, die sich auf jede Linie in der Fabrik befinden.
- Lassen Sie [initialize_inventory.py](datenverarbeitung/initialize_inventory.py) laufen; das ist sehr schnell.
- Lassen Sie r[run_reinitialization.py](datenverarbeitung/run_reinitialization.py) für ein paar Sekunden laufen und dann unterbrechen Sie das Programm.
- Lassen Sie [datenverarbeitung_main.py](datenverarbeitung/datenverarbeitung_main.py) und [run_reinitialization.py](datenverarbeitung/run_reinitialization.py) gleichzeitig laufen.
- Die Initialisierung dauert ~10 Minuten. Sie erhalten eine Nachricht "Done." im Terminal von run_reinitialization.py, wenn die Initialisierung fertig ist.