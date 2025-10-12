*** Settings ***
Library    SeleniumLibrary
Library    okw4robot.keywords.host.HostKeywords                 WITH NAME    Host
Library    okw4robot.keywords.app.AppKeywords                   WITH NAME    App
Library    okw4robot.keywords.widget_keywords.WidgetKeywords    WITH NAME    KW

*** Variables ***
${DEMO_FILE}    docs/examples/widgets_demo.html

*** Keywords ***
Setup Widgets Demo
    Start Host     Chrome
    Start App      Chrome
    Select Window  Chrome
    ${FILE_URL}=   Evaluate    __import__('pathlib').Path('${DEMO_FILE}').resolve().as_uri()
    KW.SetValue    URL         ${FILE_URL}
    Start App      web/WidgetsDemo

Teardown Widgets Demo
    Stop Host

*** Test Cases ***
Exists YES And NO
    Setup Widgets Demo
    Select Window   WidgetsDemo
    KW.VerifyExist   Name         YES
    KW.ExecuteJS    document.querySelector('[data-testid="ta-anmerkung"]').remove();
    KW.VerifyExist   Anmerkung    NO
    Teardown Widgets Demo


