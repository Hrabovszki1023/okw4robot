# OKW4Robot

Treiber-unabhängige Keyword-Architektur für das [Robot Framework](https://robotframework.org/).

Dieses Projekt ermöglicht es, mit einem einheitlichen Satz von Schlüsselwörtern Tests gegen verschiedene GUI-Technologien (Web, Swing etc.) durchzuführen.

---

## Dokumentation


- Docs-Übersicht: [docs/README.md](docs/README.md)
- Common Widgets (Web): [docs/widgets_common.md](docs/widgets_common.md)
- ComboBox & ListBox: [docs/widgets_combobox_listbox.md](docs/widgets_combobox_listbox.md)
- Keyword × Widget Matrix (Web, Selenium): [docs/Web_Widget_Matrix.md](docs/Web_Widget_Matrix.md)
- Ignore-Regel (, , ): [docs/keywords_ignore_rule.md](docs/keywords_ignore_rule.md)
- Placeholder-Keywords: [docs/keywords_placeholder.md](docs/keywords_placeholder.md)

---

## Erste Schritte

```bash
pip install -e .


```robot
*** Settings ***
Library    okw4robot.keywords.app.AppKeywords
Library    okw4robot.keywords.host.HostKeywords
Library    okw4robot.keywords.widget_keywords.WidgetKeywords
```

---

## Projektstruktur

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
- Tooltip-Keywords: [docs/keywords_tooltip.md](docs/keywords_tooltip.md)
- OKW Parameter und Timeouts: [docs/okw_parameters.md](docs/okw_parameters.md)
