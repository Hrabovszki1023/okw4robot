# Web Keyword × Widget Matrix (Selenium)

Diese Matrix ist transponiert: Schlüsselwörter als Zeilen, Widgets als Spalten. Ein Häkchen (✔) bedeutet implementiert; leere Felder sind (derzeit) nicht implementiert. Gilt für den Web‑Adapter (Selenium).

| Keyword                    | Button | TextField | MultilineField | Label | CheckBox | ComboBox | RadioList | ListBox |
|---------------------------|:------:|:---------:|:--------------:|:-----:|:--------:|:--------:|:---------:|:-------:|
| ClickOn                   |   ✔    |     ✔     |       ✔        |       |    ✔     |          |           |         |
| DoubleClickOn             |   ✔    |           |                |       |          |          |           |         |
| SetValue                  |        |     ✔     |       ✔        |       |    ✔     |    ✔     |           |         |
| Select                    |        |           |                |       |          |    ✔     |     ✔     |    ✔    |
| TypeKey                   |        |           |                |       |          |          |           |         |
| VerifyValue               |        |     ✔     |       ✔        |   ✔   |    ✔     |    ✔     |     ✔     |    ✔    |
| VerifyValueWCM            |        |     ✔     |       ✔        |   ✔   |          |          |           |         |
| VerifyValueREGX           |        |     ✔     |       ✔        |   ✔   |          |          |           |         |
| VerifyExist               |   ✔    |     ✔     |       ✔        |   ✔   |    ✔     |    ✔     |     ✔     |    ✔    |
| LogValue                  |        |     ✔     |       ✔        |   ✔   |    ✔     |    ✔     |           |    ✔    |
| MemorizeValue             |        |     ✔     |       ✔        |   ✔   |    ✔     |    ✔     |           |    ✔    |
| VerifyPlaceholder         |        |     ✔     |       ✔        |       |          |    ✔     |           |         |
| VerifyPlaceholderWCM      |        |     ✔     |       ✔        |       |          |    ✔     |           |         |
| VerifyPlaceholderREGX     |        |     ✔     |       ✔        |       |          |    ✔     |           |         |

Hinweise
- VerifyExist: generisch für alle Widgets über `BaseWidget.okw_verify_exist()` (Adapter: `element_exists`).
- TypeKey: Auf Widget‑Ebene nicht implementiert. Das Keyword unterstützt jedoch das Literal `$DELETE` und löscht Inhalte bei textbasierten Widgets (über den Keyword‑Handler), ohne `okw_type_key` zu benötigen.
- Placeholder: Sinnvoll für TextField, MultilineField und input‑basierte ComboBoxen; bei nativen `<select>` ist der Placeholder in der Regel leer.

Verweise
- Adapter: `src/okw4robot/adapters/selenium_web.py`
- Widgets: `src/okw4robot/widgets/common/*`
- Keywords (Allgemein): `src/okw4robot/keywords/widget_keywords.py`
- Placeholder‑Keywords: `src/okw4robot/keywords/placeholder_keywords.py`
