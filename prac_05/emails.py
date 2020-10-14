email_dict = {}
email = input('Email : ')
while email != '':
    coded_name = email.split('@')
    list_name = "".join([word for word in coded_name[0] if not word.isdigit()]).split('.')
    name = " ".join(list_name).title()

    bool_name = input(str('is your name {}? (Y/n) '.format(name)))

    if bool_name == 'y' or bool_name == '':
        name = " ".join(list_name).title()
    else:
        name = input('Name: ')

    email_dict.update({name: email})
    email = input('Email : ')

for name, email in email_dict.items():
    print("{} ({})".format(name, email))


