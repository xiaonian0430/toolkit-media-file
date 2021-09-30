# encoding: utf-8
"""
@author: Xiao Nian
@contact: xiaonian030@163.com

@version: 1.0
@license: Apache Licence
@file: main.py
@time: 2021-04-25 13:00

"""
import xlrd
import json

if __name__ == "__main__":
    data = []
    dataIndex = -1
    cityIndex = -1
    workbook = xlrd.open_workbook(r'./area.xlsx')
    sheet1 = workbook.sheet_by_name('Sheet1')
    cols0 = sheet1.col_values(0)  # 获取第1列内容
    cols1 = sheet1.col_values(1)  # 获取第2列内容
    cols2 = sheet1.col_values(2)  # 获取第3列内容
    for index, area in enumerate(cols2):
        if area == '':
            continue
        if cols0[index] != '':
            dataIndex = dataIndex + 1
            cityIndex = -1
            dataItem = {
                "name": cols0[index],
                "city": []
            }
            data.append(dataItem)
        if cols1[index] != '':
            cityIndex = cityIndex + 1
            data[dataIndex]['city'].append({
                "name": cols1[index],
                "area": []
            })
        data[dataIndex]['city'][cityIndex]['area'].append(area)

    # 结果
    result = json.dumps(data, indent=4, ensure_ascii=False)
    with open("city.json", "w", encoding='utf-8') as fp:
        fp.write(result)
