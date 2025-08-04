
*** Variables ***
${list1} 1, 2, 3, 4,5,
${MY_VARIABLE}
*** Test Cases ***
Test case 1
    [Tags]  test1
    LOG TO CONSOLE    "This is a Test message"
    LOG TO CONSOLE    ${MY_VARIABLE}


