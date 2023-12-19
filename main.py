import csv

class Clients:
    type_decice = {
        'tablet':'планшета',
        'desktop':'персонального компьютера',
        'laptop':'ноутбука',
        'mobile':'мобильного устройства'
    }
    gender_type = {
        'female':'женского пола',
        'male':'мужского пола'
    }

    def __init__(self, name, gender, age, device, browser, summ, region):
        self.name = name
        self.gender = Clients.gender_type.get(gender)
        self.age = age
        self.device = Clients.type_decice.get(device)
        self.browser = browser
        self.summ = summ
        self.region = region

    
    def get_template_row(self):
        return f'Пользователь {self.name} {self.gender},{self.age} лет совершил покупку на {self.summ} у.е. с {self.device} c браузера {self.browser}. Регион, из которого совершалась покупка: {self.region}'

with open('clients.txt', 'w') as output_file:
    with open("web_clients_correct.csv") as input_file:
        for p_data in csv.reader(input_file):
            print("ROW")
            print(p_data)
            output_file.write(Clients(p_data[0], p_data[3], p_data[4], p_data[1], p_data[2], p_data[5], p_data[6]).get_template_row() + '\n')