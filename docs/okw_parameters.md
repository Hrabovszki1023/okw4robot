# OKW Parameter und Timeouts

Diese Seite dokumentiert konfigurierbare OKW‑Parameter (Timeouts, Ignore‑Regel) und zeigt, wie sie gesetzt werden.

---

## Übersicht der Parameter

- ${OKW_TIMEOUT_VERIFY_VALUE}
  - Zweck: Timeout für VerifyValue, VerifyValueWCM, VerifyValueREGX
  - Typ: Sekunden (Zahl) oder Robot‑Zeitformat (z. B. `10s`, `1 min`)
  - Default: 10

- ${OKW_TIMEOUT_VERIFY_PLACEHOLDER}
  - Zweck: Timeout für VerifyPlaceholder, VerifyPlaceholderWCM, VerifyPlaceholderREGX
  - Typ: Sekunden oder Robot‑Zeitformat
  - Default: 10

- ${OKW_TIMEOUT_VERIFY_TOOLTIP}
  - Zweck: Timeout für VerifyTooltip, VerifyTooltipWCM, VerifyTooltipREGX
  - Typ: Sekunden oder Robot‑Zeitformat
  - Default: 10

- ${OKW_IGNORE_EMPTY}
  - Zweck: Leere Werte global ignorieren (No‑Op) für Set/Select/TypeKey/VerifyValue*
  - Typ: YES/NO (TRUE/FALSE/1/0 werden akzeptiert)
  - Default: NO

---

## Setzen per Keyword

- Library: `okw4robot.keywords.params.ParamsKeywords`
- Keyword: `SetOKWParameter  <Name>  <Wert>`
  - Unterstützte Namen (case‑insensitive):
    - `TimeOutVerifyValue` → `${OKW_TIMEOUT_VERIFY_VALUE}`
    - `TimeOutVerifyPlaceholder` → `${OKW_TIMEOUT_VERIFY_PLACEHOLDER}`
    - `TimeOutVerifyTooltip` → `${OKW_TIMEOUT_VERIFY_TOOLTIP}`
  - Wert: Zahl (Sekunden) oder Robot‑Zeitstring (`10s`, `1 min`)
  - Scope: Suite‑Variable

Beispiele:
```robotframework
*** Settings ***
Library    okw4robot.keywords.params.ParamsKeywords    WITH NAME    PAR

*** Test Cases ***
Setze Timeouts
    PAR.SetOKWParameter    TimeOutVerifyValue         20
    PAR.SetOKWParameter    TimeOutVerifyPlaceholder   8
    PAR.SetOKWParameter    TimeOutVerifyTooltip       15s
```

---

## Setzen per Variables‑Section

Alternativ können die Variablen direkt gesetzt werden:
```robotframework
*** Variables ***
${OKW_TIMEOUT_VERIFY_VALUE}         20
${OKW_TIMEOUT_VERIFY_PLACEHOLDER}   8
${OKW_TIMEOUT_VERIFY_TOOLTIP}       15s
${OKW_IGNORE_EMPTY}                 NO
```

Hinweise:
- Zahlen werden als Sekunden interpretiert; Zeitstrings werden per `convert_time` umgerechnet.
- Verify‑Keywords warten bis zum ersten passenden Zustand oder bis zum Timeout und schlagen sonst mit dem zuletzt gelesenen Wert fehl.

---

## Betroffene Keywords

- VerifyValue, VerifyValueWCM, VerifyValueREGX → `${OKW_TIMEOUT_VERIFY_VALUE}`
- VerifyPlaceholder, VerifyPlaceholderWCM, VerifyPlaceholderREGX → `${OKW_TIMEOUT_VERIFY_PLACEHOLDER}`
- VerifyTooltip, VerifyTooltipWCM, VerifyTooltipREGX → `${OKW_TIMEOUT_VERIFY_TOOLTIP}`

Ignore‑Regel (No‑Op):
- `$IGNORE` wird immer ignoriert.
- Leere Werte (`""`, Whitespaces) nur wenn `${OKW_IGNORE_EMPTY}=YES`.
