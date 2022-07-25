from winreg import HKEY_LOCAL_MACHINE


list_elements = [2, 3, 5, 8, 4, 9]

result_list = [index for index in list_elements if (index % 2) == 0]

print(result_list)

r_list = [index for index in list_elements if (index % 3 )== 0]

print(r_list)