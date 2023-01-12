from models import Record, Phone, Adress, Email
import connect


def look_up_DB (text):

    records = Record.objects()
    for r in records:
        dict_record = r.to_mongo().to_dict()
        record_name = dict_record['name']

        if record_name.lower().find(text.lower()) >= 0:
            print(
                f'Looked up text was found in next statement: "{record_name}" in record: "{record_name}"')

        for key, value in dict_record.items():
            if key == 'emails' or key == 'adresses' or key == 'phones':

                if value:
                    #print(key, value)

                    for inner_dict in value: # value - list

                        dict_value = inner_dict['name']
                        if dict_value.lower().find(text.lower()) >= 0:
                            print(
                                f'Looked up text was found in next statement: "{dict_value}" in record: "{record_name}"')


def add_records_DB(name, phone):
    phone = Phone(name=phone)

    Record(name=name, phones=[phone, ]).save()



def change_phone_DB(name, new_phone):
    phone = Phone(name=new_phone)
    record = Record.objects(name=name)
    record.update(phones=[phone, ])


def add_phone_DB(name, phone):

    phone_add = Phone(name=phone)
    record = Record.objects(name=name)

    #for r in record:
    #    print(r.to_mongo().to_dict())

    record.update_one(push__phones=phone_add)

def del_phone_DB(name, phone):

    phone_del = Phone(name=phone)
    record = Record.objects(name=name)

    #for r in record:
    #    print(r.to_mongo().to_dict())

    record.update_one(pull__phones=phone_del)




def del_rec_DB(name):

    record = Record.objects(name=name)
    record.delete()

def add_email_DB(name, email):

    email_add = Email(name=email)
    record = Record.objects(name=name)

    # for r in record:
    #    print(r.to_mongo().to_dict())

    record.update_one(push__emails=email_add)

def change_email_DB(name, new_email):

    email = Email(name=new_email)
    record = Record.objects(name=name)
    record.update(emails=[email, ])

def add_adress_DB(name, adress):

    adress_add = Adress(name=adress)
    record = Record.objects(name=name)

    record.update_one(push__adresses=adress_add)


def change_adress_DB(name, new_adress):

    adress = Adress(name=new_adress)
    record = Record.objects(name=name)
    record.update(adresses=[adress, ])


if __name__ == '__main__':
    #add_records_DB('Serhii', '111111111')
    #add_records_DB('Andrii', '888888888')
    change_phone_DB('Serhii', '2111111111')
    #add_phone_DB('Serhii', '2222222222')
    #del_phone_DB('Andrii', '2222222222')
    #del_rec_DB('Bobo')
    #add_email_DB('Andrii', '1@1.1')
    #change_email_DB('Andrii', '2@2.2')
    #add_adress_DB('Andrii', 'Vinica')
    #change_adress_DB('Andrii', 'Lviv')
    look_up_DB ('an')
