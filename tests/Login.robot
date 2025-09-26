*** Settings ***
Library    SeleniumLibrary
Library    okw4robot.keywords.host.HostKeywords                 WITH NAME    Host
Library    okw4robot.keywords.app.AppKeywords                   WITH NAME    App
Library    okw4robot.keywords.widget_keywords.WidgetKeywords    WITH NAME    KW

# Suite Setup     Setup Login Test
# Suite Teardown  Close All Browsers

*** Variables ***
${LOGIN_HTML}   file:///C:/temp/login.html

*** Keywords ***
Setup Login Test
    Start Host     Chrome
    Start App      Chrome 
    Select Window  Chrome
    SetValue       URL       ${LOGIN_HTML}
    # ClickOn        Maximize Window
    Start App      web/TestAppOKW4Robot_WEB

*** Test Cases ***
Login OK
    Setup Login Test

    Select Window  LoginDialog
    SetValue       Benutzer     admin
    SetValue       Passwort     geheim
    ClickOn        OK
    VerifyValue    Status       Status: Angemeldet

    Stop Host

Login Abbruch
    Setup Login Test

    Select Window  LoginDialog
    ClickOn        Abbruch
    VerifyValue    Status       Status: Abgebrochen

    Stop Host

Widget Existenzprüfung
    Setup Login Test

    Select Window  LoginDialog
    VerifyExist    DoesNotExist    NO

    Stop Host

Chrome Zu Firefox Umschalten
    Start Host     Chrome
    Start App      Chrome
    Select Window  Chrome
    SetValue       URL    ${LOGIN_HTML}
    Stop Host

    Start Host     Firefox
    Start App      Firefox
    Select Window  Firefox
    SetValue       URL    ${LOGIN_HTML}
    Stop Host
