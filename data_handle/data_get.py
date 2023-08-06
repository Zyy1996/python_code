import os
import sys
import re
import time
import dataset_handle
from single_line_handle import Line_str_handle



# def get_free_table(file_path):
#     total_data = {}
#     with open(file_path, 'r') as f:
#         for line in f.readlines():
#             data = Line_str_handle.free_ram_handle(line)
#             if data is not None:
#                 print(data["free"])
                # t.table_drawing_get_data(data["free"])
    # t.table_drawing_finish()

def get_cpu_idle_table(file_path,proc:list):
    proc_data = {}
    proc_data["CPU"] = []
    time_num:int = 0
    for key in proc:
        proc_data[key] = []
    with open(file_path, 'r') as f:
        for line in f.readlines():
            data = Line_str_handle.top_idle_handle(line)
            if data is not None:
                # print(time_num)
                proc_data['CPU'].append(100-int(data["idle"]))
                for key in proc:
                    proc_data[key].append(0)
                time_num = time_num + 1
                continue
            for proc_index in proc:
                data = Line_str_handle.top_single_process_handle(line,proc_index)
                if data is not None:
                    # print(data)
                    proc_data[proc_index][time_num-1] = int(data[proc_index])
                    break
        # print(proc_data)
        tab = dataset_handle.Polt_draw(0,"CPU消耗",proc_data)
        tab.show()


# def get_cpu_consumption_table(file_path,process):
#     proc = "%s 进程消耗" % (process)
#     t = dataset_handle.Table_drawing(1, proc)
#     with open(file_path, 'r') as f:
#         for line in f.readlines():
#             data = top_single_process_handle(line,process)
#             if data != None:
#                 # print(data)
#                 t.table_drawing_get_data(int(data[process]))
#     t.table_drawing_finish()

# # 获取top中idle的平均值


# def get_match_str_datas(file_path):
#     num = 0
#     total_data = 0
#     with open(file_path, 'r') as f:
#         for line in f.readlines():
#             data = top_idle_handle(line)
#             if data != None:
#                 total_data = total_data+int(data['idle'])
#                 num = num+1
#     print(total_data)
#     print(num)
#     print(total_data/num)

# # 获取单个进程的cpu消耗
# def get_single_proc_cpu_consum(file_path, process):
#     num = 0
#     total_data = 0
#     with open(file_path, 'r') as f:
#         for line in f.readlines():
#             data = top_single_process_handle(line, process)
#             if data != None:
#                 total_data = total_data+int(data[process])
#                 num = num+1
#     print(total_data)
#     print(num)
#     print(total_data/num)

get_cpu_idle_table("352_288.log",["iot_video_ipc_test","imi_ali"])
# get_match_str_datas("640_480_2.log")
# get_match_str_datas("320_240_3.log")
# get_match_str_datas("test5.log")
# get_single_proc_cpu_consum("test5.log","h2642yuv")
# get_match_str_from_file("352_288_1.log",need_matched_str)
# get_free_table("352_288_4.log")
# get_cpu_idle_table("352_288_5.log")
# get_cpu_consumption_table("test5.log","h2642yuv")
