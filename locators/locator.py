class Base:
    tab_menu = "//div[@id=\"menu\"]//li//a[span[text()='%s']]"
    welcome_mes = "//div[@id='banner']//strong"
    mes_problem_acc = "//div[@id='content']/p[contains(@class, 'message error') and following-sibling::form]"
    welcome_user_message = "//div[@id='banner']//strong"
    message_problem_account = "//div[@id='content']/p[contains(@class, 'message error') and following-sibling::form]"
    paragraph = "//p[contains(text(),'%s')]"

class Login:
    emailTxb = "//form//input[@id='username']"
    pwdtxb = "//form//input[@id='password']"
    loginBtn = "//form//input[@type='submit']"

class MailPage:
    cbx_scramble_address = "//label[text()=' Scramble Address']"
    email = "//span[@id='email-widget']"
    mail_domain = "//div[@id='guerrilla_mail']//select"
    email_confirm = "//tbody[@id='email_list']//tr[td[text()='%s']]"
    link_confirm = "//div[@class='email_body']//a"
    mail_name_btn = "//div[@id='guerrilla_mail']//span[@id='inbox-id']"
    mail_name_txb = "//div[@id='guerrilla_mail']//span[@id='inbox-id']/input[@type='text']"
    set_btn = "//div[@id='guerrilla_mail']//span[@id='inbox-id']/button[text()='Set']"
    mail_domain_select = "//div[@id='guerrilla_mail']//select"
    cbx_mail_confirm = "//tbody[@id='email_list']//tr[td[text()='%s']]//input"
    delete_mail_btn = "//input[@value='Delete']"
    link_back_to_inbox = "//div[@class='email_page']//a[@id='back_to_inbox_link']"

class Register:
    email_txb = "//input[@id='email']"
    passwword_txb = "//input[@id='password']"
    confirm_pwd_txb = "//input[@id='confirmPassword']"
    pid_txb = "//input[@id='pid']"
    register_btn = "//input[@type='submit']"
    message_invalid_pwd = "//form//label[preceding-sibling::input[@id='password']]"
    message_invalid_pid = "//form//label[preceding-sibling::input[@id='pid']]"
    message_register_succ = "//div[@id='content']/p"

class BookTicket:
    txb = "//select[@name='%s']"
    submit_form_btn = "//input[@type='submit']"
    info_book_ticket_succ = "//table//td[count(//th[text()='%s']/preceding-sibling::th) + 1]"
    message = "//div[@id='content']/h1"
    mes_book_ticket_succ = "//div[@id='content']/h1"
    total = "//td[count(//tr//th[text()='Total Price']/preceding-sibling::th)+1]"

class MyTicket:
    cancel_btn = "//input[contains(@onclick, 'Delete')]"
    total = "//table[@class='MyTable']//tr[td[text()='%s' and following-sibling::td[text()='%s' and following-sibling::td[text()='%s' and following-sibling::td[text()='%s' and following-sibling::td[text()='%s']]]]]]//td[count(//tr/th[text()='Total Price']/preceding-sibling::th)+1]"
    filter_depart_station = "//select[@name='FilterDpStation']"
    filter_date = "//input[@name='FilterDpDate']"
    filter_apply_btn = "//input[@type='submit' and @value='Apply filter']"
    departs = "//table[@class='MyTable']//td[count(//table[@class='MyTable']//tr/th[text()='Depart Station']/preceding-sibling::th) + 1]"
    date = "//table[@class='MyTable']//td[count(//table[@class='MyTable']//tr/th[text()='Depart Date']/preceding-sibling::th) + 1]"
