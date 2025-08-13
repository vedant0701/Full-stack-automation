Feature: This is to test the UI functionality of our project

Scenario: Login to the sauce demo page
Given the user is on the login page
When The user logins with username 'standard_user' and password 'secret_sauce'
Then the user logins and is on the homepage

Scenario: User add a few products to the cart
When user add 'Sauce Labs Backpack' into the cart
When user add 'Sauce Labs Bike Light' into the cart
Then the user goes to the cart
