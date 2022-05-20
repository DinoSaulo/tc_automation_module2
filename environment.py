from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def before_all(context):
	context.web = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

	context.web.maximize_window()

def after_step(context, step):
	print()

def after_all(context):
	context.web.quit()