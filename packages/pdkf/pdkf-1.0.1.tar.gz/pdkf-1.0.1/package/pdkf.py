def read_file(file_name, file_content):
    if file_name[-3:] == 'csv':
        data = pandas.read_csv(BytesIO(file_content))
        return data
    elif file_name[-4:] == 'json':
        json_list = json.loads(file_content.decode())
        data = pandas.DataFrame() 
        for item in json_list:
            if len(data) == 0:
                data = pandas.json_normalize(list(item.values())[0])
            else:
                data = pandas.concat([data, pandas.json_normalize(list(item.values())[0])], ignore_index = True)
        return data
    else:
        raise Exception(f'Wrong file format: {file_name}')
                

def read_pdkf(file):
    if file[-4:] != 'pdkf':
        raise Exception(f'Wrong file format')
    dataframe_dict = {}
    file_zip = ZipFile(file, 'r', allowZip64=True)
    try:
        for file_name in file_zip.namelist():
            if file_name[-4:] != 'meta':
                file_content = file_zip.read(file_name)
                dataframe_dict[file_name[:file_name.find('.')]] = read_file(file_name, file_content)
        for file_name in file_zip.namelist():
            if file_name[-4:] == 'meta':
                file_content = file_zip.read(file_name)
                data = json.loads(file_content.decode())
                for column, type in data.items():
                    dataframe_dict[file_name[:-5]][column] = dataframe_dict[file_name[:-5]][column].astype(type)
    finally:
        file_zip.close()
    return dataframe_dict