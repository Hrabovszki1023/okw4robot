# 🧭 Keyword-Referenz: Host- & App-Keywords

Diese Anleitung beschreibt die Verwendung der OKW4Robot-Schlüsselwörter für Host- und App-Steuerung. Sie bilden das Fundament für alle Testfälle: Ohne aktiven Host (Treiber) und geladene App (Objektlisten-YAML) können keine Widgets angesprochen werden.

---

## 🔌 Host-Keywords

### `Start Host    <HostName>`
Lädt und initialisiert den Treiber für die Host-Umgebung (z. B. `Chrome`, `Firefox`). Erwartet wird eine passende Objektlisten-YAML in:

```
# Beispiel: Chrome
src/okw4robot/locators/Chrome.yaml
```

Diese YAML muss enthalten:
```yaml
Chrome:
  __self__:
    class: okw4robot.adapters.selenium_web.SeleniumWebAdapter
    browser: chrome
```

🔄 Diese Methode startet **noch nicht automatisch den Browser**, sondern stellt nur den Treiber bereit.

---

### `Select Host    <HostName>`
Wechselt in einen zuvor gestarteten Host-Kontext. Dies ist sinnvoll, wenn mehrere Hosts parallel verwendet werden (z. B. Browser-Vergleich).

✅ Wirft Fehler, wenn der gewünschte Host nicht aktiv ist.

---

### `Stop Host`
Beendet den aktuellen Treiber (z. B. schließt den Browser) und löscht alle App- und Fensterkontexte.

---

## 🧱 App-Keywords

### `Start App    <AppName>`
Lädt eine **Objektlisten-YAML** für eine Anwendung. Der Pfad wird wie folgt interpretiert:

- `Start App    TestApp` → `locators/TestApp.yaml`
- `Start App    web/TestApp` → `locators/web/TestApp.yaml`

Beispiel:
```yaml
TestApp:
  LoginDialog:
    Benutzer:
      class: okw4robot.widgets.web.TextField
      locator: { css: '[data-testid="Benutzer"]' }
```

☝️ Voraussetzung: Ein Host muss zuvor gestartet worden sein.

---

### `Select Window    <WindowName>`
Aktiviert ein Fenster oder ein virtuelles Widget aus dem App-Modell. Erst nach Auswahl eines Fensters kann auf darunterliegende Widgets zugegriffen werden.

Beispiel:
```
Select Window    LoginDialog
```

---

### `Stop App`
Beendet den aktuellen Anwendungskontext (Modell, Fenster, Name).

---

## 🧪 Beispiel: Browser wechseln (Chrome vs. Firefox)

```robotframework
*** Settings ***
Library    okw4robot.keywords.host.HostKeywords
Library    okw4robot.keywords.app.AppKeywords
Library    okw4robot.keywords.widget_keywords.WidgetKeywords

*** Test Cases ***
Login mit Chrome
    Start Host           Chrome
    Start App            Chrome
    Select Window        Chrome
    SetValue             URL      file:///C:/temp/login.html
    ClickOn              Maximize Window
    Start App            web/TestAppOKW4Robot_WEB
    Select Window        LoginDialog
    SetValue             Benutzer     admin
    Stop App
    Stop Host

Login mit Firefox
    Start Host           Firefox
    Start App            Firefox
    Select Window        Firefox
    SetValue             URL      file:///C:/temp/login.html
    ClickOn              Maximize Window
    Start App            web/TestAppOKW4Robot_WEB
    Select Window        LoginDialog
    SetValue             Benutzer     admin
    Stop App
    Stop Host
```

---

## 📌 Hinweise

- Das `Select Window` funktioniert sowohl für "echte" Fenster als auch für virtuelle Objekte (z. B. `URL`, `Maximize Window` bei Browsern).
- Wird `Start Host` erneut aufgerufen, werden App und Fenster-Kontext automatisch zurückgesetzt.
- Alle Fehler wie "kein Host aktiv", "Fenster nicht gefunden" oder "Widget nicht definiert" werden klar protokolliert (inkl. Stacktrace, falls aktiviert).

---

> 📂 Du findest die zugehörigen YAMLs in `locators/` (Projekt) oder `src/okw4robot/locators/` (Framework-Vorgaben).

> 🧩 Für eine Liste aller verfügbaren Widget-Keywords siehe `docs/keywords_widget.md` (folgt).

