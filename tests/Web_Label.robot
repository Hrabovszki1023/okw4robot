*** Settings ***
Library    SeleniumLibrary
Library    okw4robot.keywords.host.HostKeywords                 WITH NAME    Host
Library    okw4robot.keywords.app.AppKeywords                   WITH NAME    App
Library    okw4robot.keywords.label_keywords.LabelKeywords      WITH NAME    LAB
Library    okw4robot.keywords.widget_keywords.WidgetKeywords    WITH NAME    KW
Library    okw4robot.keywords.params.ParamsKeywords             WITH NAME    PAR

*** Variables ***
${DEMO_FILE}    docs/examples/widgets_demo.html

*** Keywords ***
Setup Widgets Demo
    Start Host     Chrome
    Start App      Chrome
    Select Window  Chrome
    ${FILE_URL}=   Evaluate    __import__('pathlib').Path('${DEMO_FILE}').resolve().as_uri()
    PAR.SetOKWParameter    TimeOutVerifyLabel    10
    PAR.SetOKWParameter    TimeOutVerifyValue    10
    SetValue       URL         ${FILE_URL}
    Start App      web/WidgetsDemo

Teardown Widgets Demo
    Stop Host

*** Test Cases ***
Verify Labels For Form Controls
    Setup Widgets Demo
    Select Window   WidgetsDemo
    LAB.VerifyLabel        Name            Name
    LAB.VerifyLabel        Vorname         Vorname
    LAB.VerifyLabel        Anmerkung       Anmerkung
    LAB.VerifyLabel        Verheiratet     Verheiratet
    LAB.VerifyLabel        Geschlecht      Geschlecht
    Teardown Widgets Demo

Label Wildcard And Regex
    Setup Widgets Demo
    Select Window   WidgetsDemo
    LAB.VerifyLabelWCM     Verheiratet     *heirat*
    LAB.VerifyLabelREGX    Geschlecht      ^Geschl.*
    Teardown Widgets Demo

Memorize And Log Label
    Setup Widgets Demo
    Select Window   WidgetsDemo
    LAB.MemorizeLabel      Name        NameLabel
    LAB.LogLabel           Name
    # Verwendung: ${NameLabel}
    Teardown Widgets Demo
