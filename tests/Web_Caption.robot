*** Settings ***
Library    SeleniumLibrary
Library    okw4robot.keywords.host.HostKeywords                 WITH NAME    Host
Library    okw4robot.keywords.app.AppKeywords                   WITH NAME    App
Library    okw4robot.keywords.caption_keywords.CaptionKeywords  WITH NAME    CAP
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
    PAR.SetOKWParameter    TimeOutVerifyCaption    10
    SetValue       URL         ${FILE_URL}
    Start App      web/WidgetsDemo

Teardown Widgets Demo
    Stop Host

*** Test Cases ***
Verify Button Caption
    Setup Widgets Demo
    Select Window   WidgetsDemo
    CAP.VerifyCaption      OK      OK
    Teardown Widgets Demo

Memorize And Log Caption
    Setup Widgets Demo
    Select Window   WidgetsDemo
    CAP.MemorizeCaption    OK      OkCaption
    CAP.LogCaption         OK
    Teardown Widgets Demo
