import os
import sys
import re
import time
import dataset_handle

'''
正则表达式规则
-?\d+\.\d+|-?\d+ : 获取小数,整数
'''

class Line_str_handle():
    def __init__(self) -> None:
        pass

    @classmethod
    def top_idle_handle(cls, line_str):
        obj_key = re.findall("CPU:", line_str)
        if len(obj_key) != 0:
            obj_data = re.findall("-?\d+\.\d+|-?\d+", line_str)
            # print(obj_data)
            if len(obj_data) != 7:
                return None
            else:
                data = {"idle": obj_data[3]}
                return data
        else:
            return None

    @classmethod
    def procrank_processes_ram_handle(cls, line_str):
        return None

    @classmethod
    def top_single_process_handle(cls, line_str, process):
        p = str(line_str)
        p1 = str(process)
        obj_key = re.findall(p1, line_str)
        if len(obj_key) != 0:
            obj_data = re.findall("-?\d+\.\d+|-?\d+", line_str)
            # print(obj_data)
            if len(obj_data) < 4:
                return None
            else:
                data = {process: obj_data[4]}
                return data
        else:
            return None

    @classmethod
    def free_ram_handle(cls, line_str):
        p = str(line_str)
        if p.find("-/+ buffers/cache:") != -1:
            obj_data = re.findall("-?\d+\.\d+|-?\d+", line_str)
            if len(obj_data) != 2:
                return None
            else:
                data = {"free": obj_data[1]}
                return data
        else:
            return None

    @classmethod
    def top_processes_cpu_handle(cls, line_str):
        obj_key = re.findall("imilab_app",line_str)
        # print("1")
        if len(line_str) != 0:
            # print("12")
            obj_data = re.findall("-?\d+\.\d+|-?\d+",line_str)
            print(obj_data)
        return obj_data

# a = Line_str_handle.top_processes_cpu_handle("imilab_app-121.123112asdfasf123,1231231.33--sdfs 2323 2323 32.2 1.2.3.")
