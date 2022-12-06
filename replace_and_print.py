def replace_and_print(name, *args):
    name = name.__name__.replace("_", " ").capitalize() + ";"
    print('Имя функции:', name, ' аргумент(ы) функции:', *args, end='\n\n')


def open_browser(browser_name):
    replace_and_print(open_browser, browser_name)


def go_to_company_name_homepage(page_url):
    replace_and_print(go_to_company_name_homepage, page_url)


def find_registration_button_on_login_page(page_url, button_text):
    replace_and_print(find_registration_button_on_login_page, page_url, button_text)


open_browser('Chrome')
go_to_company_name_homepage('https://qa.guru/')
find_registration_button_on_login_page('URL', 'Login')
