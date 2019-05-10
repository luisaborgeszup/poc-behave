Feature: Account Withdraw

   Feature Description

Scenario Outline: Account withdraw of an account without enough money
    Given an account with a total of money equals to R$ 50
    When the account owner attempts to makes a withdraw of R$ <amount>
    Then the follow message <message> should appear

    Examples:
    | amount |     message      |
    | 60     | not enough money |
    | 70     | not enough money |


Scenario Outline: Account withdraw of an account with enough money
    Given an account with a total of money equals to R$ 50
    When the account owner attempts to makes a withdraw of R$ <amount>
    Then the follow message <message> should appear

    Examples:
    | amount |     message         |
    | 30     | operation completed |
    | 50     | operation completed |


Scenario Outline: Account deposit
    Given an account with a total of money equals to R$ 50
    When the account owner attempts to makes a deposit of R$ <amount>
    Then the current total of money should be <current_total>

    Examples:
    | amount |     current_total    |
    | 30     |        80            |
    | 50     |        100           |
