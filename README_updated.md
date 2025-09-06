# OKW4Robot

Treiber-unabhängige Keyword-Architektur für das [Robot Framework](https://robotframework.org/).

Dieses Projekt ermöglicht es, mit einem einheitlichen Satz von Schlüsselwörtern Tests gegen verschiedene GUI-Technologien (Web, Swing etc.) durchzuführen.

---

## 🔍 Dokumentation

| Thema                             | Datei                                              |
|----------------------------------|-----------------------------------------------------|
| Kontext-Verwaltung                | [docs/context.md](docs/context.md)                 |
| Host- und App-Schlüsselwörter     | [docs/keywords_host_app.md](docs/keywords_host_app.md) |
| Übersicht: Schlüsselwörter Host & App | [docs/keywords_host_app_overview.md](docs/keywords_host_app_overview.md) |


## 📍 Dokumentation

| Thema | Datei |
|-------|-------|
| Kontext-Verwaltung: Wie Adapter und Applikationen ausgewählt werden | [docs/context.md](docs/context.md) |
| Parameter der Objektlisten für JavaRPC (Host, App, Port, JAR etc.) | [docs/docs_host_app_config.md](docs/docs_host_app_config.md) |
| Trennung von Host und App – Konzept und Begründung | [docs/docs_host_app_trennung.md](docs/docs_host_app_trennung.md) |
| Neue Schlüsselwörter: Start/Stop Host & App, Select Host & App | [docs/keywords_host_app.md](docs/keywords_host_app.md) |
| Übersichtstabelle: Host- und App-Schlüsselwörter | [docs/keywords_host_app_uebersicht.md](docs/keywords_host_app_uebersicht.md) |
| Struktur und Zweck der wichtigsten Python-Module | [docs/modules.md](docs/modules.md) |


---

## 🚀 Erste Schritte

```bash
pip install -e .
```

```robot
*** Settings ***
Library    okw4robot.keywords.app.AppKeywords
Library    okw4robot.keywords.host.HostKeywords
Library    okw4robot.keywords.widget_keywords.WidgetKeywords
```

---

## 📁 Projektstruktur

```
OKW4Robot/
├── src/okw4robot/
│   ├── keywords/
│   ├── runtime/
│   ├── locators/
│   └── ...
├── tests/
├── docs/
│   ├── context.md
│   ├── modules.md
│   ├── keywords_host_app.md
│   └── keywords_host_app_overview.md
└── README.md

```

---

© 2025 Zoltán Hrabovszki – OpenKeyWord / OKW4Robot