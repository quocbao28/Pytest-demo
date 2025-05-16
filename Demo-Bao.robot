*** Settings ***
Suite Setup       Open Browser To Guru Site
Suite Teardown    Close Browser
Library           SeleniumLibrary
Library           Collections
Library           FakerLibrary

*** Variables ***
${BASE_URL}       https://demo.guru99.com/
${LOGIN_URL}      https://demo.guru99.com/V1/index.php
${BROWSER}        Firefox
${Delay}          30s
${emailField}     input[name='emailid']

*** Test Cases ***
Register And Login With Generated Credentials
    ${random_email}=    Fake Email
    Input Email And Get Credentials    ${random_email}
    Go To Login Page
    Login With Retrieved Credentials

*** Keywords ***
Open Browser To Guru Site
    Open Browser    ${BASE_URL}    ${BROWSER}
    sleep    ${Delay}
    Wait Until Element Is Visible    css:input[name=emailid]

Fake Email
    ${email}=    FakerLibrary.Email
    RETURN    ${email}

Input Email And Get Credentials
    [Arguments]    ${email}
    Wait Until Page Contains Element    css:input[name=emailid]
    Input Text    css:input[name=emailid]    ${email}
    Click Button    css:input[name=btnLogin]
    Wait Until Page Contains    User ID
    ${user_id}=    Get Text    xpath:(//td[text()='User ID :']/../td)[2]
    ${password}=    Get Text    xpath:(//td[text()='Password :']/../td)[2]
    Set Suite Variable    ${USER_ID}    ${user_id}
    Set Suite Variable    ${PASSWORD}    ${password}

Go To Login Page
    Go To    ${LOGIN_URL}
    sleep    ${Delay}
    Wait Until Page Contains Element    css:input[name=uid]

Login With Retrieved Credentials
    Input Text    css:input[name=uid]    ${USER_ID}
    Input Text    css:input[name=password]    ${PASSWORD}
    Click Button    css:input[name=btnLogin]
    Wait Until Page Contains    Gtpl Bank
