'''
Author       : mati1da
Date         : 2023-08-29 16:16:58
LastEditors  : mati1da
LastEditTime : 2023-10-07 11:33:30
Description  : 
'''
import csv

def write_to_csv(filename, data):
    """
    将数据写入CSV文件

    Args:
        filename (str): 要写入的文件名
        data (list): 要写入的数据，每个元素应为一个包含字段值的列表
    """
    with open(filename, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        for row in data:
            csvwriter.writerow(row)
    
    print(f"数据已成功写入到 {filename}")

def read_csv_file(filename):
    """
    读取CSV文件并返回包含数据的列表

    Args:
        filename (str): 要读取的CSV文件名

    Returns:
        list: 包含CSV文件数据的列表
    """
    data = []
    with open(filename, 'r',encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            data.append(row)
    return data

