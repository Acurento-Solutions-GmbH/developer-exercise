<p align="center"><img src="docs/banner.de.svg" alt="Acurento · Developer Exercise · Kleine Änderung. Klare Entscheidungen." width="960"></p>

<p align="center"><a href="README.md">English</a> · <strong>Deutsch</strong></p>

<p align="center"><strong>60 Minuten Aufgabe · 45 Minuten Gespräch · KI ausdrücklich erlaubt</strong><br>Python ohne zusätzliche Pakete · Keine juristischen Vorkenntnisse erforderlich</p>

---

## Willkommen bei Acurento

Wir entwickeln Software, die komplexe Arbeit verständlich macht. Unsere Rechtskataster-Plattform hilft Unternehmen und Berater:innen, relevante regulatorische Änderungen zu erkennen und zu bearbeiten.

Diese kleine Aufgabe zeigt einen Ausschnitt davon. Uns interessiert, wie Sie vorhandenen Code verstehen, Entscheidungen treffen und Ergebnisse überprüfen. Eine begründete, unvollständige Lösung ist willkommen. Zusätzliche Features oder besonders aufwendige Dokumentation bringen keine Extrapunkte.

## Die Aufgabe

> „Bei einem Kunden fehlt die Anlagenkapazität. Trotzdem zeigt das System **nicht betroffen**. Können wir dieser Einschätzung vertrauen?“

Übernehmen Sie das kleine bestehende Programm in diesem Repository. Untersuchen Sie die Rückmeldung, verbessern Sie die Bewertung und ergänzen Sie aussagekräftige Tests.

Das Ergebnis soll für jeden Kunden eine dieser Einschätzungen liefern:

| Status | Bedeutung |
|---|---|
| `affected` | Die vorliegenden Daten belegen, dass die Regel zutrifft. |
| `not_affected` | Die vorliegenden Daten belegen, dass die Regel nicht zutrifft. |
| `needs_review` | Die vorliegenden Daten reichen für eine Entscheidung nicht aus. |

Jede Einschätzung braucht eine kurze, für Berater:innen verständliche **Begründung anhand der verfügbaren Daten**. Bei Prüfbedarf soll erkennbar sein, welche Information fehlt.

### Die gesamte Fachregel

Die fiktive Regel **DEMO-001** betrifft Anlagen des Typs **F-01** mit einer Kapazität von **mindestens 5 Tonnen pro Stunde**. Alle anderen Anlagentypen sind von dieser Regel nicht betroffen.

- Jeder Kunde hat in dieser Aufgabe genau eine Anlage mit bekanntem Typ.
- Eine Kapazität ist eine nichtnegative Zahl in Tonnen pro Stunde. `0` ist ein gültiger, bekannter Wert.
- `null` oder ein fehlendes Feld `capacity_t_h` bedeutet **unbekannt**.
- Alle übrigen Felder sind vorhanden und korrekt. Die Eingaben sind gültiges JSON.
- Alle Angaben beziehen sich auf denselben Zeitpunkt. Weitere Gesetze oder Ausnahmen gibt es für diese Aufgabe nicht.

**Regel, Unternehmen und Daten sind vollständig fiktiv.** Bitte ausschließlich diese Fachregel verwenden; externe Rechtsrecherche ist nicht nötig. Die Einschätzung ist ein Hinweis für einen Review und kein allgemeines Compliance-Urteil über einen Kunden.

### Umfang

Verbessern Sie die bestehende Funktion und ihre Begründungen. Die dokumentierten Statuswerte sowie Kunden- und Regel-IDs sollen in der Ausgabe erhalten bleiben. Sie können den Code nach Bedarf umstrukturieren.

Eine Weboberfläche, Datenbank, API, Deployment oder ein LLM zur Laufzeit sind nicht Teil der Aufgabe. Auch ein allgemeines Regelwerk oder eine vollständige Eingabevalidierung ist nicht erforderlich.

## In zwei Minuten starten

Voraussetzung: **Python 3.10 oder neuer**, keine weiteren Pakete oder Zugangsdaten.

```bash
git clone https://github.com/Acurento-Solutions-GmbH/developer-exercise.git
cd developer-exercise
python3 -m relevance
python3 -m unittest discover -s tests -v
```

Unter Windows können Sie `python3` durch `py -3` ersetzen. Alternativ: oben **Code → Download ZIP**, entpacken und die Befehle im entpackten Ordner ausführen.

Das Programm schreibt JSON auf die Standardausgabe. Eigene Eingaben und eine gespeicherte Ausgabe sind ebenfalls möglich:

```bash
python3 -m relevance --customers data/customers.json --rule data/rule.json
python3 -m relevance > result.json
```

Die vorhandenen Tests prüfen nur zwei bekannte Fälle und die ausführbare Schnittstelle. **Grüne Tests bedeuten hier ausdrücklich nicht, dass die gemeldete Schwäche behoben ist.**

| Datei | Wofür sie da ist |
|---|---|
| [`relevance/assessment.py`](relevance/assessment.py) | Bestehende Bewertungslogik – hier starten |
| [`data/rule.json`](data/rule.json) | Die fiktive Regel als Daten |
| [`data/customers.json`](data/customers.json) | Drei synthetische Kundenprofile |
| [`tests/test_assessment.py`](tests/test_assessment.py) | Erste Tests zum Ergänzen |
| [`HANDOVER.de.md`](HANDOVER.de.md) | Vorlage für Ihre kurze Übergabe |

Python ist unser Vorschlag. Falls Sie sich in einer anderen Sprache deutlich besser ausdrücken können, dürfen Sie dieselbe Schnittstelle und dieselben Daten verwenden. Dokumentieren Sie dann einen einfachen Start- und Testbefehl; Framework-Auswahl wird nicht bewertet.

## Zeit und Werkzeuge

**Bitte nach insgesamt 60 Minuten stoppen**, auch wenn etwas fehlt. Lesen, Umsetzung, Tests und Übergabe zählen dazu. Als Orientierung: 10 Minuten verstehen, 30 Minuten ändern, 10 Minuten überprüfen, 10 Minuten übergeben. Falls die lokale Einrichtung blockiert, melden Sie sich bei Ihrer Kontaktperson; Installationsprobleme sollen die Aufgabe nicht bestimmen.

KI-Assistenten, Coding-Agents, Autovervollständigung und Dokumentation sind ausdrücklich erlaubt – auch für die gesamte Implementierung. Entscheidend ist, dass Sie das Ergebnis nachvollziehen und prüfen können. Arbeiten ohne KI ist ebenso willkommen. Falls Sie KI nutzen möchten und keinen Zugang haben, melden Sie sich vor Beginn bei Ihrer Kontaktperson, damit wir einen vergleichbaren Zugang organisieren können.

Notieren Sie kurz, welche Werkzeuge Sie genutzt haben und wie Sie wichtige Ergebnisse überprüft haben. Ein vollständiger Chatverlauf oder eine Bildschirmaufnahme ist nicht erforderlich. Sie müssen weder einen KI-Fehler finden noch eine künstliche Geschichte über abgelehnte Vorschläge erzählen.

## Abgabe

Senden Sie Ihrer bisherigen Acurento-Kontaktperson **eine ZIP-Datei** mit Ihrer Lösung oder einen Link zu einem **separaten privaten Repository**. Den benötigten GitHub-Zugang stimmen Sie mit dieser Person ab. Für ein privates Repository verwenden Sie eine eigene Kopie; ein Fork dieses öffentlichen Repositorys lässt sich nicht privat machen.

Bitte keine Lösung als öffentlichen Pull Request, Issue oder öffentlichen Fork einreichen, damit die Aufgabe für andere Kandidat:innen nutzbar bleibt.

Die Abgabe enthält:

1. Ihren Code und Ihre Tests mit funktionierenden Start- und Testbefehlen.
2. Eine ausgefüllte Übergabevorlage: [`HANDOVER.de.md`](HANDOVER.de.md), **höchstens 300 Wörter** insgesamt.

Die JSON-Ausgabe dürfen Sie ergänzen; sie ist kein Pflicht-Deliverable. Deutsch oder Englisch sind gleichermaßen willkommen. Bitte keine Zugangsdaten oder echten Kundendaten beilegen. Ihre Einreichung dient der Bewerbung und ist keine beauftragte Produktionsarbeit.

## Das anschließende Gespräch

Wenn wir nach der Durchsicht gemeinsam weitergehen, planen wir **45 Minuten**:

| Dauer | Inhalt |
|---|---|
| 10 Minuten | Ihre Lösung vorführen und einen Fall durch den Code verfolgen |
| 10 Minuten | Eine Entscheidung und die dazugehörige Überprüfung besprechen |
| 20 Minuten | Gemeinsam eine kleine neue Anforderung bearbeiten |
| 5 Minuten | Was würden Sie freigeben, was als Nächstes verbessern? |

---

<p align="center">Acurento · Software für nachvollziehbare Entscheidungen</p>
