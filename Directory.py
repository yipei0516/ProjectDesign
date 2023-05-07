import numpy as np
import openpyxl
import os
from Utils import compute

class Directory:
    def __init__(self, dirpath, dirname):
        self.dirpath = dirpath
        self.dirname = dirname

        self.video_count = 0

        self.oneday_interrupt_count = 0
        self.video_file_list = []
        self.oneday_interrupt_time = 0

        self.wb = openpyxl.load_workbook('Result.xlsx')
        

    
    def write_result_to_excel(self): ## write result to excel ##
        self.ws = self.wb.create_sheet(self.dirname)
        self.ws['A1'] = self.dirname
        self.ws['B1'] = 'Start Time'
        self.ws['C1'] = 'End Time'

        ##### 1. 印出revised interrupt #####
        for video in self.video_file_list:
            data = ['', '', '']
            self.ws.append(data)

            data = [video.filename, '', '']
            self.ws.append(data)

            if video.total_revised_interrupt_count == 0:
                data = ['No interrupt', '', '']
                self.ws.append(data)

            for i in range(video.total_revised_interrupt_count):
                interrupt_name = 'Interrupt#' + str(i+1)
                interrupt = video.revised_interrupt_list[i]
                
                ##### interrupt start #####
                start_normal_time = compute.get_normal_time_info(time_in_seconds=interrupt["start_time"])
                start_time_name = compute.get_excel_str(normal_time=start_normal_time)

                ##### interrupt end #####
                end_normal_time = compute.get_normal_time_info(time_in_seconds=interrupt["end_time"])
                end_time_name = compute.get_excel_str(normal_time=end_normal_time)

                ##### interrupt time (中斷長度) #####
                self.oneday_interrupt_time += interrupt["end_time"] - interrupt["start_time"]

                ##### interrupt count (中斷次數) #####
                self.oneday_interrupt_count += 1

                # 加入row
                data = [interrupt_name, start_time_name, end_time_name]
                self.ws.append(data)

        for i in range(2):
            self.ws.append(['', '', ''])

        ##### 2. 印出手術總中斷次數 #####
        total_interrupt_number_name = str(self.oneday_interrupt_count)

        data = ['總手術中斷次數', total_interrupt_number_name, '']
        self.ws.append(data)

        ##### 3. 印出手術總中斷時長 #####
        total_normal_time = compute.get_normal_time_info(time_in_seconds=self.oneday_interrupt_time)
        total_time_name = compute.get_excel_str(normal_time=total_normal_time)

        data = ['總手術中斷時間', total_time_name, '']
        self.ws.append(data)

        ##### 4. 印出手術總時長 #####
        total_normal_time = compute.get_normal_time_info(time_in_seconds=self.oneday_interrupt_time)
        total_time_name = compute.get_excel_str(normal_time=total_normal_time)

        data = ['總手術中斷時間', total_time_name, '']
        self.ws.append(data)

        self.wb.save(filename='Result.xlsx')


    def delete_excel_row(self, choose_video_file, remove_interrupt_index):
        video_file_name = self.ws['A']

        row_num = 0
        for name in video_file_name:
            row_num += 1
            if name.value == choose_video_file.filename:
                self.ws.delete_rows(row_num + remove_interrupt_index + 1) #excel第一列為1(非index)
                break

        
        self.oneday_interrupt_count -= 1
        self.oneday_interrupt_time -= (choose_video_file.revised_interrupt_list[remove_interrupt_index]["end_time"] - choose_video_file.revised_interrupt_list[remove_interrupt_index]["start_time"])
        total_normal_time = compute.get_normal_time_info(time_in_seconds=self.oneday_interrupt_time)
        total_time_name = compute.get_excel_str(normal_time=total_normal_time)
        row = self.oneday_interrupt_count + 3 + 1 # 3行不重要的資訊
        self.ws['B'+str(self.ws.max_row-1)].value = self.oneday_interrupt_count
        self.ws['B'+str(self.ws.max_row)].value = total_time_name
        self.wb.save(filename='Result.xlsx')
        