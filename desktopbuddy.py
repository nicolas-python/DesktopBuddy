import subprocess                   #Damit kann das Python-Programm mit andere Programmen arbeiten und diese starten
from pathlib import Path            #ist ein Python-Modul zur Arbeit mit Dateipfaden

#speicherort der aktuellen Python-Datei ermitteln
project_folder = Path(__file__).parent              #path = dateipfade erstellen und bearbeiten

#Pfad zur Godot-Anwendung
godot_application = project_folder / "build" / "DesktopBuddy.exe"   #erstellt den vollständigen Pfad zur exportierten Godot-Anwendung im build-Ordner

#starten
subprocess.Popen([str(godot_application)])                  #startet das angegebene Programm
