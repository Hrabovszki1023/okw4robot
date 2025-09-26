*** Settings ***
Library    SeleniumLibrary
Library    okw4robot.keywords.host.HostKeywords                 WITH NAME    Host
Library    okw4robot.keywords.app.AppKeywords                   WITH NAME    App
Library    okw4robot.keywords.widget_keywords.WidgetKeywords    WITH NAME    KW
Library    okw4robot.keywords.placeholder_keywords.PlaceholderKeywords    WITH NAME    PH

*** Variables ***
${DEMO_FILE}    docs/examples/widgets_demo.html

*** Keywords ***
Setup Widgets Demo
    [Documentation]    Start Chrome, open demo HTML, load WidgetsDemo locators
    Start Host     Chrome
    Start App      Chrome
    Select Window  Chrome
    ${FILE_URL}=   Evaluate    __import__('pathlib').Path('${DEMO_FILE}').resolve().as_uri()
    SetValue       URL         ${FILE_URL}
    Start App      web/WidgetsDemo

Teardown Widgets Demo
    Stop Host

*** Test Cases ***
TextField Set And Verify
    Setup Widgets Demo
    Select Window   WidgetsDemo
    SetValue        Name        Mustermann
    SetValue        Vorname     Max
    VerifyValue     Name        Mustermann
    VerifyValue     Vorname     Max
    Teardown Widgets Demo

MultilineField Set And Verify
    Setup Widgets Demo
    Select Window   WidgetsDemo
    SetValue        Anmerkung   Mehrzeilige Eingabe\nmit zwei Zeilen
    VerifyValue     Anmerkung   Mehrzeilige Eingabe\nmit zwei Zeilen
    Teardown Widgets Demo

CheckBox Checked And Unchecked
    Setup Widgets Demo
    Select Window   WidgetsDemo
    SetValue        Verheiratet     Checked
    VerifyValue     Verheiratet     Checked
    SetValue        Verheiratet     Unchecked
    VerifyValue     Verheiratet     Unchecked
    Teardown Widgets Demo

RadioList Select And Verify
    Setup Widgets Demo
    Select Window   WidgetsDemo
    Select          Zahlungsmethode     paypal
    VerifyValue     Zahlungsmethode     paypal
    Teardown Widgets Demo

ComboBox Set And Verify
    Setup Widgets Demo
    Select Window   WidgetsDemo
    # Beide Varianten sind möglich: SetValue oder Select
    SetValue        Geschlecht      Männlich
    VerifyValue     Geschlecht      Männlich
    Select          Geschlecht      Weiblich
    VerifyValue     Geschlecht      Weiblich
    Teardown Widgets Demo

OK Aggregates Values In Status
    Setup Widgets Demo
    Select Window   WidgetsDemo
    SetValue        Name        Mustermann
    SetValue        Vorname     Max
    SetValue        Anmerkung   Hallo Welt
    SetValue        Verheiratet    Checked
    Select          Zahlungsmethode  sepa
    Select          Geschlecht   Divers
    ClickOn         OK
    # Das Status-Label enthält mehrere Zeilen. Wir prüfen mit Wildcards auf Teilinhalt.
    VerifyValueWCM  Status      *"Name" = "Mustermann"*
    VerifyValueWCM  Status      *"Vorname" = "Max"*
    VerifyValueWCM  Status      *"Verheiratet" = "Checked"*
    Teardown Widgets Demo

VerifyExist On Status
    Setup Widgets Demo
    Select Window   WidgetsDemo
    VerifyExist     Status    YES
    Teardown Widgets Demo

$IGNORE Behavior: SetValue Does Nothing
    Setup Widgets Demo
    Select Window   WidgetsDemo
    SetValue        Name        Before
    SetValue        Name        $IGNORE
    VerifyValue     Name        Before
    Teardown Widgets Demo

$IGNORE Behavior: Select Does Nothing
    Setup Widgets Demo
    Select Window   WidgetsDemo
    SetValue        Geschlecht   Männlich
    Select          Geschlecht   $IGNORE
    VerifyValue     Geschlecht   Männlich
    Teardown Widgets Demo

$IGNORE Behavior: TypeKey Does Nothing
    Setup Widgets Demo
    Select Window   WidgetsDemo
    SetValue        Name        SomeText
    TypeKey         Name        $IGNORE
    VerifyValue     Name        SomeText
    Teardown Widgets Demo

$IGNORE Behavior: VerifyValue Is Skipped
    Setup Widgets Demo
    Select Window   WidgetsDemo
    SetValue        Name        SkipCheck
    VerifyValue     Name        $IGNORE
    # If not ignored, above would assert; reaching here means it was skipped.
    Teardown Widgets Demo

$IGNORE Behavior: VerifyValueWCM/REGX Are Skipped
    Setup Widgets Demo
    Select Window   WidgetsDemo
    SetValue        Name        Any
    VerifyValueWCM  Name        $IGNORE
    VerifyValueREGX  Name        $IGNORE
    Teardown Widgets Demo

EMPTY And DELETE Semantics
    Setup Widgets Demo
    Select Window   WidgetsDemo
    SetValue        Name        ToDelete
    TypeKey         Name        $DELETE
    VerifyValue     Name        ${EMPTY}
    SetValue        Anmerkung   ${EMPTY}
    VerifyValue     Anmerkung   ${EMPTY}
    Teardown Widgets Demo

Placeholders On Inputs
    Setup Widgets Demo
    Select Window   WidgetsDemo
    VerifyPlaceholder      Name         Nachname
    VerifyPlaceholderWCM   Vorname      *name*
    VerifyPlaceholderREGX  Anmerkung    ^Mehrzeilige\\s+Eingabe.*
    Teardown Widgets Demo

Memorize And Reuse In Multiline
    Setup Widgets Demo
    Select Window   WidgetsDemo
    SetValue        Name        Alice
    MemorizeValue   Name        Name
    SetValue        Anmerkung   Gemerkter wert : ${Name}
    VerifyValue     Anmerkung   Gemerkter wert : Alice
    Teardown Widgets Demo
