*** Settings ***
Library  SeleniumLibrary
Test Setup      Open Browser  browser=headlessfirefox
Test Teardown	Close Browser

*** Variables ***
${browser}  chrome
${url}  https://rozetka.com.ua/ua/
${correctSearch}    AGM A9
${incorrectSearch}  jhvjhjhjhv

*** Test Cases ***
CorrectSearchTest
    [Tags]  maintainer=todynyuk
    open browser    ${url}   ${browser}
    maximize browser window
    set selenium speed  2seconds
    input text  xpath://input[@name='search']    ${correctSearch}
    click button    xpath://button[contains(@class, 'button_color_green')]
    Element Should Contain    xpath://h1[contains(@class, 'catalog-heading')]    ${correctSearch}   Page not contains search text
    Element Should Contain    xpath://span[@class='goods-tile__title'][1]    ${correctSearch}   Page not contains search text

IncorrectSearchTest
    [Tags]  maintainer=todynyuk
    open browser    ${url}   ${browser}
    input text  xpath://input[@name='search']  ${incorrectSearch}
    click button    xpath://button[contains(@class, 'button_color_green')]
    element should be enabled   xpath://span[@class='ng-star-inserted']
