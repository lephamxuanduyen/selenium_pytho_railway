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
