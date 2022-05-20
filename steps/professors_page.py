from behave import given, when, then
from selenium.webdriver.common.by import By
import time
from hamcrest import *

# URL do site
base_url = "https://www.icmc.usp.br/pessoas/docentes"

# Variáveis com os elementos
input_cep_id = 'campoCEP'
btn_buscar_cep_css_selector = "input[value='buscar cep']"

@given(u'I am on ICMC-USPs Professors page')
def step_impl(context):
    context.web.get(base_url)

    #aceitar coockies
    context.web.find_element(By.CSS_SELECTOR, "div[class='btn btn-primary jb accept blue']").click()

@when(u'I select the option {department} in the department filter')
def step_impl(context, department):

    dept_value = ""

    if "Departamento de Ciências de Computação" in department:
        dept_value = "SCC"
    elif "Departamento de Matemática" in department:
        dept_value = "SMA"
    elif "Departamento de Matemática Aplicada e Estatística" in department:
        dept_value = "SME"
    elif "Departamento de Sistemas de Computação" in department:
        dept_value = "SSC"

    context.web.find_element(By.CSS_SELECTOR, "select[name='estsgl']").click()

    time.sleep(1)

    context.web.find_element(By.CSS_SELECTOR, "option[value='{}']".format(dept_value)).click()

    time.sleep(1)

    context.web.find_element(By.CSS_SELECTOR, "select[name='estsgl']").click()


@then(u'I see {expected_number_teachers} professors of the department')
def step_impl(context, expected_number_teachers):
    time.sleep(1)

    expected_number_teachers = int(expected_number_teachers.replace("\"", ""))

    # conta a quantidade de paginas
    # cada página tem 24 professores
    # qtd_profs = (24 * (num_pags - 1)) + qtd_profs_ultima_pagina
    # se tiver apenas uma página o numero de professores vai ser o que está na tela

    qtd_pags = len(context.web.find_elements(By.CSS_SELECTOR, "ul[class='pagination'] li")) - 2 #-2 devido aso botões de previous e next

    if qtd_pags == 1:
        qtd_profs = len(context.web.find_elements(By.CSS_SELECTOR, "div[class='row mostra_pessoas'] div[class='thumbnail']"))
    else:
        # clica no botão para ir para a ultima pagina
        context.web.find_element(By.XPATH, "//a[text()='»']").click()
        qtd_profs_last_page = len(context.web.find_elements(By.CSS_SELECTOR, "div[class='row mostra_pessoas'] div[class='thumbnail']"))

        qtd_profs = ((qtd_pags - 1) * 24)  + qtd_profs_last_page

    assert_that(qtd_profs, is_(expected_number_teachers), f"The "+ str(qtd_pags))
