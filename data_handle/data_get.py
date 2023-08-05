import os
import sys
import re
import time
import dataset_handle


# 返回值为字典

def top_idle_handle(line_str):
    obj_key = re.findall("CPU:", line_str)
    if len(obj_key) != 0:
        obj_data = re.findall("\d+", line_str)
        if len(obj_data) != 7:
            return None
        else:
            data = {}
            data["idle"] = obj_data[3]
            return data
    else:
        return None


def top_processes_cpu_handle(line_str):
    return None


def procrank_processes_ram_handle(line_str):
    return None

def top_single_process_handle(line_str, process):
    p = str(line_str)
    p1 = str(process)
    obj_key = re.findall(p1, line_str)
    if len(obj_key) != 0:
        obj_data = re.findall("\d+", line_str)
        # print(obj_data)
        if len(obj_data) < 4:
            return None
        else:
            data = {}
            data[process] = obj_data[4]
            return data
    else:
        return None

def free_ram_handle(line_str):
    p = str(line_str)
    if p.find("-/+ buffers/cache:") != -1:
        obj_data = re.findall("\d+", line_str)
        if len(obj_data) != 2:
            return None
        else:
            data = {}
            data["free"] = obj_data[1]
            return data
    else:
        return None


parsing_once_str_list = {
    "top_idle": top_idle_handle,
    "top_process_cpu": top_processes_cpu_handle,
    "procrank_process_ram": procrank_processes_ram_handle,
    "free_ram": free_ram_handle
}

############################## 数据处理##################################


def get_free_table(file_path):
    t = dataset_handle.Table_drawing(1, "free")
    with open(file_path, 'r') as f:
        for line in f.readlines():
            data = free_ram_handle(line)
            if data != None:
                # print(data["free"])
                t.table_drawing_get_data(data["free"])
    t.table_drawing_finish()


def get_cpu_idle_table(file_path):
    t = dataset_handle.Table_drawing(1, "cpu idle")
    with open(file_path, 'r') as f:
        for line in f.readlines():
            data = top_idle_handle(line)
            if data != None:
                # print(data)
                t.table_drawing_get_data(data["idle"])
    t.table_drawing_finish()


def get_cpu_consumption_table(file_path,process):
    proc = "%s 进程消耗" % (process)
    t = dataset_handle.Table_drawing(1, proc)
    with open(file_path, 'r') as f:
        for line in f.readlines():
            data = top_single_process_handle(line,process)
            if data != None:
                # print(data)
                t.table_drawing_get_data(int(data[process]))
    t.table_drawing_finish()

# 获取top中idle的平均值


def get_match_str_datas(file_path):
    num = 0
    total_data = 0
    with open(file_path, 'r') as f:
        for line in f.readlines():
            data = top_idle_handle(line)
            if data != None:
                total_data = total_data+int(data['idle'])
                num = num+1
    print(total_data)
    print(num)
    print(total_data/num)

# 获取单个进程的cpu消耗
def get_single_proc_cpu_consum(file_path, process):
    num = 0
    total_data = 0
    with open(file_path, 'r') as f:
        for line in f.readlines():
            data = top_single_process_handle(line, process)
            if data != None:
                total_data = total_data+int(data[process])
                num = num+1
    print(total_data)
    print(num)
    print(total_data/num)


# get_match_str_datas("640_480_2.log")
# get_match_str_datas("320_240_3.log")
# get_match_str_datas("test5.log")
get_single_proc_cpu_consum("test5.log","h2642yuv")
# get_match_str_from_file("352_288_1.log",need_matched_str)
# get_free_table("352_288_4.log")
# get_cpu_idle_table("352_288_5.log")
get_cpu_consumption_table("test5.log","h2642yuv")
