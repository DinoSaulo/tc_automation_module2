#language: en
Feature: Validate the data returned by searches in ICMC-USP

    '''I as a user want to see the professors quantities
    of the ICMC-USP in the site of the university'''

    Scenario: Check the number of professors in a given department
        Given I am on ICMC-USPs Professors page
        When I select the option "Departamento de Ciências de Computação" in the department filter
        Then I see "24" professors of the department