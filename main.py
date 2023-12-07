try:
    with open("purchase_log.txt", "r", encoding="utf-8", errors= None) as file:
        dict_file = {}

        for line in file:
            data = line
            print(line)
            data = data.rstrip().lstrip('{').rstrip('}')
            data_pair = data.split(",")
            left_pair = data_pair[0].split(":")
            key_left_pair = left_pair[0].lstrip('"').rstrip('"')
            value_left_pair = left_pair[1].lstrip(' "').rstrip('"')

            data = data.rstrip().lstrip('{').rstrip('}')
            right_pair = data_pair[1].split(":")
            key_right_pair = right_pair[0].lstrip(' "').rstrip('"')
            value_right_pair = right_pair[1].lstrip(' "').rstrip('"')
            dict_file.update({value_left_pair: value_right_pair})

        print("dict_file")
        print(dict_file)

except Exception as ex:
    print('Error')