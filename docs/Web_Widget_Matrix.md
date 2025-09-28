## 1. Aktionen ohne Eingabewert
Kurzbeschreibung: Aktionen, die keine Werte übergeben bekommen (z. B. Klicks).

| Keyword        | Button | TextField | MultilineField | Label | CheckBox | ComboBox | RadioList | ListBox |
|----------------|:------:|:---------:|:--------------:|:-----:|:--------:|:--------:|:---------:|:-------:|
| ClickOn        |   ✔    |     ✔     |       ✔        |       |    ✔     |          |           |         |
| DoubleClickOn  |   ✔    |           |                |       |          |          |           |         |
| SetFocus       |   ✔    |     ✔     |       ✔        |   ✔   |    ✔     |    ✔     |     ✔     |    ✔    |

## 2. Aktionen mit Eingabewert
Kurzbeschreibung: Aktionen, die einen Wert/Parameter benötigen (Eingaben, Auswahlen).

| Keyword   | Button | TextField | MultilineField | Label | CheckBox | ComboBox | RadioList | ListBox |
|-----------|:------:|:---------:|:--------------:|:-----:|:--------:|:--------:|:---------:|:-------:|
| SetValue  |        |     ✔     |       ✔        |       |    ✔     |    ✔     |           |         |
| Select    |        |           |                |       |          |    ✔     |     ✔     |    ✔    |
| TypeKey   |        |     ✔     |       ✔        |       |          |    ✔     |           |         |

## 3. Verify (wartend, mit Timeout)
Kurzbeschreibung: Prüfungen, die bis zum Sollzustand oder Timeout warten.

| Keyword                  | Button | TextField | MultilineField | Label | CheckBox | ComboBox | RadioList | ListBox |
|--------------------------|:------:|:---------:|:--------------:|:-----:|:--------:|:--------:|:---------:|:-------:|
| VerifyValue              |        |     ✔     |       ✔        |   ✔   |    ✔     |    ✔     |     ✔     |    ✔    |
| VerifyValueWCM           |        |     ✔     |       ✔        |   ✔   |          |          |           |         |
| VerifyValueREGX          |        |     ✔     |       ✔        |   ✔   |          |          |           |         |
| VerifyPlaceholder        |        |     ✔     |       ✔        |       |          |    ✔     |           |         |
| VerifyPlaceholderWCM     |        |     ✔     |       ✔        |       |          |    ✔     |           |         |
| VerifyPlaceholderREGX    |        |     ✔     |       ✔        |       |          |    ✔     |           |         |
| VerifyTooltip            |   ✔    |     ✔     |       ✔        |   ✔   |    ✔     |    ✔     |     ✔     |    ✔    |
| VerifyTooltipWCM         |   ✔    |     ✔     |       ✔        |   ✔   |    ✔     |    ✔     |     ✔     |    ✔    |
| VerifyTooltipREGX        |   ✔    |     ✔     |       ✔        |   ✔   |    ✔     |    ✔     |     ✔     |    ✔    |
| VerifyLabel              |   ✔    |     ✔     |       ✔        |   ✔   |    ✔     |    ✔     |     ✔     |    ✔    |
| VerifyLabelWCM           |   ✔    |     ✔     |       ✔        |   ✔   |    ✔     |    ✔     |     ✔     |    ✔    |
| VerifyLabelREGX          |   ✔    |     ✔     |       ✔        |   ✔   |    ✔     |    ✔     |     ✔     |    ✔    |
| VerifyCaption            |   ✔    |           |                |   ✔   |          |          |           |         |
| VerifyCaptionWCM         |   ✔    |           |                |   ✔   |          |          |           |         |
| VerifyCaptionREGX        |   ✔    |           |                |   ✔   |          |          |           |         |
| VerifyAttribute          |   ✔    |     ✔     |       ✔        |   ✔   |    ✔     |    ✔     |     ✔     |    ✔    |
| VerifyAttributeWCM       |   ✔    |     ✔     |       ✔        |   ✔   |    ✔     |    ✔     |     ✔     |    ✔    |
| VerifyAttributeREGX      |   ✔    |     ✔     |       ✔        |   ✔   |    ✔     |    ✔     |     ✔     |    ✔    |
| VerifyExist (generisch)  |   ✔    |     ✔     |       ✔        |   ✔   |    ✔     |    ✔     |     ✔     |    ✔    |
| VerifyHasFocus           |   ✔    |     ✔     |       ✔        |   ✔   |    ✔     |    ✔     |     ✔     |    ✔    |

## 4. Memorize
Kurzbeschreibung: Liest Werte/Attribute und speichert sie in Robot‑Variablen.

| Keyword            | Button | TextField | MultilineField | Label | CheckBox | ComboBox | RadioList | ListBox |
|--------------------|:------:|:---------:|:--------------:|:-----:|:--------:|:--------:|:---------:|:-------:|
| MemorizeValue      |        |     ✔     |       ✔        |   ✔   |    ✔     |    ✔     |           |    ✔    |
| MemorizeTooltip    |   ✔    |     ✔     |       ✔        |   ✔   |    ✔     |    ✔     |     ✔     |    ✔    |
| MemorizeLabel      |   ✔    |     ✔     |       ✔        |   ✔   |    ✔     |    ✔     |     ✔     |    ✔    |
| MemorizeCaption    |   ✔    |           |                |   ✔   |          |          |           |         |
| MemorizeAttribute  |   ✔    |     ✔     |       ✔        |   ✔   |    ✔     |    ✔     |     ✔     |    ✔    |

## 5. Log
Kurzbeschreibung: Loggt die aktuellen Werte/Attribute für Diagnosezwecke.

| Keyword       | Button | TextField | MultilineField | Label | CheckBox | ComboBox | RadioList | ListBox |
|---------------|:------:|:---------:|:--------------:|:-----:|:--------:|:--------:|:---------:|:-------:|
| LogValue      |        |     ✔     |       ✔        |   ✔   |    ✔     |    ✔     |           |    ✔    |
| LogTooltip    |   ✔    |     ✔     |       ✔        |   ✔   |    ✔     |    ✔     |     ✔     |    ✔    |
| LogLabel      |   ✔    |     ✔     |       ✔        |   ✔   |    ✔     |    ✔     |     ✔     |    ✔    |
| LogCaption    |   ✔    |           |                |   ✔   |          |          |           |         |
| LogAttribute  |   ✔    |     ✔     |       ✔        |   ✔   |    ✔     |    ✔     |     ✔     |    ✔    |

Hinweise
- VerifyExist: generisch für alle Widgets über `BaseWidget.okw_verify_exist()` (Adapter: `element_exists`).
- TypeKey: Auf Widget‑Ebene nicht implementiert. Das Keyword unterstützt jedoch das Literal `$DELETE` und löscht Inhalte bei textbasierten Widgets (über den Keyword‑Handler), ohne `okw_type_key` zu benötigen.
- Placeholder: Sinnvoll für TextField, MultilineField und input‑basierte ComboBoxen; bei nativen `<select>` ist der Placeholder in der Regel leer.
- Tooltip: Technisch für alle Widgets möglich (liest `title`/`aria-label`), Sinn je nach Element.
 - Label: Ermittelt Beschriftung über `aria-labelledby` / `<label for=…>` / `aria-label` / Fallback Text.
 - Caption: Sichtbarer Text des Elements selbst (nicht die Feldbeschriftung und nicht der Value‑Inhalt).
- Label: Ermittelt Beschriftung über `aria-labelledby` / `<label for=…>` / `aria-label` / Fallback Text.
- Caption: Sichtbarer Text des Elements selbst (nicht die Feldbeschriftung und nicht der Value‑Inhalt).

Verweise
- Adapter: `src/okw4robot/adapters/selenium_web.py`
- Widgets: `src/okw4robot/widgets/common/*`
- Keywords (Allgemein): `src/okw4robot/keywords/widget_keywords.py`
- Placeholder‑Keywords: `src/okw4robot/keywords/placeholder_keywords.py`
- Tooltip‑Keywords: `src/okw4robot/keywords/tooltip_keywords.py`
- Label‑Keywords: `src/okw4robot/keywords/label_keywords.py`
- Caption‑Keywords: `src/okw4robot/keywords/caption_keywords.py`
- Attribute‑Keywords: `src/okw4robot/keywords/attribute_keywords.py`
