# OKW4Robot

Treiber-unabhängige Keyword-Architektur für das [Robot Framework](https://robotframework.org/).

Dieses Projekt ermöglicht es, mit einem einheitlichen Satz von Schlüsselwörtern Tests gegen verschiedene GUI-Technologien (Web, Swing etc.) durchzuführen.

---

## 🔍 Dokumentation

| Thema                              | Datei                                                | Beschreibung |
|-----------------------------------|-------------------------------------------------------|--------------|
| Kontext-Verwaltung                 | [docs/context.md](docs/context.md)                   | Verwaltet den aktiven Host, die App und das fokussierte Widget zur Laufzeit |
| Host- und App-Schlüsselwörter      | [docs/keywords_host_app.md](docs/keywords_host_app.md) | Detaillierte Beschreibung der Schlüsselwörter `Start Host`, `Stop Host`, `Select Host`, `Start App`, `Stop App`, `Select App` |
| Übersicht: Host & App Keywords     | [docs/keywords_host_app_overview.md](docs/keywords_host_app_overview.md) | Tabelle aller Host- und App-bezogenen Keywords mit Funktion |
| Host-Konfiguration JavaRPC         | [docs/host_config_javarpc.md](docs/host_config_javarpc.md) | Beschreibung aller YAML-Parameter für JavaRPC-Hosts und deren Anwendungen |
| Teststrategie GUI-Export           | [docs/test_strategy_gui_export.md](docs/test_strategy_gui_export.md) | Strategie zur Verwendung des JavaRPC-Servers für GUI-Inspektion und Objektlisten-Export |

---

## 🚀 Erste Schritte

```bash
pip install -e .


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
│   ├── keywords_host_app.md
│   ├── keywords_host_app_overview.md
│   ├── host_config_javarpc.md
│   └── test_strategy_gui_export.md
└── README.md

```

---

© 2025 Zoltán Hrabovszki – OpenKeyWord / OKW4Robot