import pandas as pd

pdf = pd.read_excel('../reestr_res_IB.xlsx')
# print()
# pdf.info()
pdf.rename(columns={
                    'Наименование_информационной_системы': 'sybsystem',
                    'Роль': 'role',
                    'Техническая_роль': 'tech_role',
                    'Интерфейс_выгрузки': 'interface_uploads',
                    'Форма_Выгрузки': 'form_uploads',
                    'Тип_аутентификации': 'type_auth',
                    'Тип_авторизации': 'type_auth_1',
                    'СЭД': 'SED',
                    'Приказ_ПЭ': 'prikaz',
                    'Уполномоченный_владелец_нформационного_ресурса_роли_от_бизнеса': 'owner_bis',
                    'Ответственное_лицо_от_бизнеса': 'responsible_person_bis',
                    'Уполномоченный_владелец_от_ИТ': 'owner_it',
                    'samaccountname2\n': 'samaccountname2',
                    'Ответственное_лицо_от_ИТ': 'responsible_person_it',
                    'Описание_информационного_ресурса_роли_в_информационной_системе': 'role_desc'
                }, inplace=True)
print()
subsystems = pd.DataFrame({'ID': pdf['ID'], 'subsystems': pdf['sybsystem']}).drop_duplicates()
subsystems.loc[subsystems['ID'].isna(), 'ID'] = 'ID9999'
subsystems_dict = {}
last_id = ''
count = 1
for row in subsystems.itertuples():
    if last_id != row[1]:

        count = 1
        last_id = row[1]
    if last_id not in subsystems_dict.keys():
        subsystems_dict[last_id] = {row[2]: f'{last_id}{str(count).zfill(4)}'}
    else:
        subsystems_dict[last_id].update({row[2]: f'{last_id}{str(count).zfill(4)}'})
    count += 1

# for col_name, data in subsystems.items():
#     if col_name == 'ID':
#         if last_id != col_name:
#             count = 1
#             last_id = col_name
#         new_id = f'{col_name}{str(count).zfill(4)}'
#         count += 1
for sybsystem in pdf['Наименование_информационной_системы'].unique():
    name = str(sybsystem).replace('\n', '')
