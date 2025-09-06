# ✨ Übersicht der Host- und App-Schlüsselwörter (OKW4Robot)

Diese Seite bietet eine strukturierte Übersicht aller aktuell unterstützten **Host- und App-Schlüsselwörter** des OKW4Robot-Frameworks, gruppiert nach Anwendungsbereich. Die eigentliche Funktionalität wird durch die jeweiligen Adapter (z. B. Selenium) und die YAML-Objektlisten definiert.

## 🚀 Host-Schlüsselwörter
Diese Schlüsselwörter dienen der Initialisierung und Steuerung des Testhosts (z. B. Chrome, Firefox, Swing, ...).

| Keyword          | Beschreibung                                                                 |
|------------------|------------------------------------------------------------------------------|
| `Start Host`     | Initialisiert den Host auf Basis der YAML-Definition.                        |
| `Select Host`    | Überprüft, ob der gewünschte Host aktiv ist (Validierung).                |
| `Stop Host`      | Beendet den aktiven Host und setzt Kontext zurück.                            |

**Hinweis:**
Im OKW4Robot-Paket sind bereits vorbereitete Objektlisten für Chrome und Firefox enthalten:
- `Chrome.yaml`
- `Firefox.yaml`

Diese enthalten virtuelle Widgets wie `URL` oder `Maximize Window`, um den Browser gezielt zu steuern.

## 📄 App-Schlüsselwörter
Diese Schlüsselwörter laden die Applikationsmodelle (Objektlisten) und setzen den Kontext für die nachfolgenden Widget-Schlüsselwörter.

| Keyword           | Beschreibung                                                                                     |
|-------------------|--------------------------------------------------------------------------------------------------|
| `Start App`       | Lädt die App-Objektliste aus YAML (z. B. `web/Login.yaml`) und initialisiert den Anwendungskontext. |
| `Select App`      | Aktiviert eine bereits gestartete App erneut (Kontextwechsel z. B. nach Parallelstarts).         |
| `Stop App`        | Beendet den Anwendungskontext und setzt Fensterkontext zurück.                                   |
| `Select Window`   | Wählt ein Fenster oder virtuelles Widget innerhalb der App für den folgenden Testschritt.         |

## 🔗 Beispiel für Chrome/Firefox-Umschaltung
```robotframework
*** Settings ***
Library    okw4robot.keywords.host.HostKeywords
Library    okw4robot.keywords.app.AppKeywords
Library    okw4robot.keywords.widget_keywords.WidgetKeywords

*** Variables ***
${LOGIN_HTML}    file:///C:/temp/login.html

*** Test Cases ***
Login mit Chrome
    Start Host    Chrome
    Start App     Chrome
    Select Window Chrome
    SetValue      URL     ${LOGIN_HTML}
    ClickOn       Maximize Window
    Start App     web/TestAppOKW4Robot_WEB
    Select Window LoginDialog
    SetValue      Benutzer    admin
    SetValue      Passwort    geheim
    ClickOn       OK
    VerifyValue   Status      Status: Angemeldet
    Stop App
    Stop Host

Login mit Firefox
    Start Host    Firefox
    Start App     Firefox
    Select Window Firefox
    SetValue      URL     ${LOGIN_HTML}
    ClickOn       Maximize Window
    Start App     web/TestAppOKW4Robot_WEB
    Select Window LoginDialog
    SetValue      Benutzer    admin
    SetValue      Passwort    geheim
    ClickOn       OK
    VerifyValue   Status      Status: Angemeldet
    Stop App
    Stop Host
```

---
Für weitere Details siehe auch:
- [`docs/keywords_host_app.md`](keywords_host_app.md) – ausführliche Beschreibung mit Beispielen
- [`docs/context.md`](context.md) – Kontextverwaltung von Adapter, App, Fenster

