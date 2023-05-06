import numpy as np
import openpyxl
import os
from Utils import compute

class Video_File:
    def __init__(self, filepath, filename):
        self.filepath = filepath

        self.filename = filename

        self.total_interrupt_count = 0
        self.interrupt_list = []

        self.total_revised_interrupt_count = 0
        self.revised_interrupt_list = []

        self.total_interrupt_time = 0
        # list裡面為的東西為dictionary(包含：start time、end time等等)
        # interrupt_list = [ 第一個interrupt_info, 第二個interrupt_info, 第三個interrupt_info .....]
        # interrupt_list[0] = interrupt_info = {
        #     "start_frame" : interrupt開始的frame(int)
        #     "end_frame"   : interrupt結束的frame(int)
        #     "start_time"  : interrupt開始的time(in seconds)
        #     "end_time"    : interrupt結束的time(in seconds)
        #     "label"       : interrupt label --> A類表簡單可分類；B類表待確認類
        # }  ### 見Utils.py judge


    def write_result_to_excel(self, wb, wb_name): ## write result to excel ##
        # wb = openpyxl.load_workbook(one_day_wb)
        name = self.filename
        ws1 = wb.create_sheet(name)

        ws1['A1'].value = name
        ws1['B1'].value = 'Start Frame #'
        ws1['C1'].value = 'Start Time'
        ws1['D1'].value = 'End Frame #'
        ws1['E1'].value = 'End Time'
        ws1['F1'].value = 'Label'

        ##### 1. 印出revised interrupt #####
        for i in range(self.total_revised_interrupt_count):
            interrupt_name = 'Interrupt#' + str(i)
            
            ##### interrupt start #####
            start_frame_name = str(self.revised_interrupt_list[i]["start_frame"])
            start_normal_time = compute.get_normal_time_info(time_in_seconds=self.revised_interrupt_list[i]["start_time"])
            start_time_name = compute.get_excel_str(normal_time=start_normal_time)

            ##### interrupt end #####
            end_frame_name = str(self.revised_interrupt_list[i]["end_frame"])
            end_normal_time = compute.get_normal_time_info(time_in_seconds=self.revised_interrupt_list[i]["end_time"])
            end_time_name = compute.get_excel_str(normal_time=end_normal_time)

            ##### label #####
            label_name = self.revised_interrupt_list[i]["label"]
            
            ##### interrupt time (中斷長度) #####
            self.total_interrupt_time += self.revised_interrupt_list[i]["end_time"] - self.revised_interrupt_list[i]["start_time"]

            # 加入row
            data = [interrupt_name, start_frame_name, start_time_name, end_frame_name, end_time_name, label_name]
            ws1.append(data)

        for i in range(2):
            ws1.append(['', '', '', '', '', ''])

        ##### 2. 印出手術總中斷次數 #####
        total_interrupt_number_name = str(self.total_revised_interrupt_count)

        data = ['總手術中段次數', total_interrupt_number_name, '', '', '', '']
        ws1.append(data)

        ##### 3. 印出手術總中斷時長 #####
        total_normal_time = compute.get_normal_time_info(time_in_seconds=self.total_interrupt_time)
        total_time_name = compute.get_excel_str(normal_time=total_normal_time)

        data = ['總手術中段時間', total_time_name, '', '', '', '']
        ws1.append(data)

        wb.save(filename=wb_name+'.xlsx')


    def delete_excel_row(self, wb, wb_name, remove_interrupt_index):
        ws = wb[self.filename]
        ws.delete_rows(remove_interrupt_index+2) # excel第一列為1(非index)
        self.total_revised_interrupt_count -= 1
        self.total_interrupt_time -= (self.revised_interrupt_list[remove_interrupt_index]["end_time"] - self.revised_interrupt_list[remove_interrupt_index]["start_time"])
        total_normal_time = compute.get_normal_time_info(time_in_seconds=self.total_interrupt_time)
        total_time_name = compute.get_excel_str(normal_time=total_normal_time)
        row = self.total_revised_interrupt_count + 3 + 1 # 3行不重要的資訊
        ws['B'+str(row)].value = self.total_revised_interrupt_count
        ws['B'+str(row+1)].value = total_time_name
        wb.save(filename=wb_name+'.xlsx')
        