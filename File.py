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

        self.resultFile = open(self.filename + ".txt", "w")
        self.wb = openpyxl.load_workbook('Result.xlsx')
        self.wb_2 = openpyxl.load_workbook('Original_Result.xlsx')




    def write_result_to_file(self): ## write result to file ##
        self.resultFile.write("Video Num:  " + self.filename + "\n")
        self.resultFile.write("Total interrupt count: " + str(self.total_interrupt_count) + "\n")
        self.resultFile.write("Interrupt Record Frame and Time: \n")

        for i in range(self.total_interrupt_count):
            start_normal_time = compute.get_normal_time_info(time_in_seconds=self.interrupt_list[i]["start_time"])
            end_normal_time = compute.get_normal_time_info(time_in_seconds=self.interrupt_list[i]["end_time"])

            self.resultFile.write("\tInterrupt#" + str(i) + 
                             "\t\t" + str(self.interrupt_list[i]["start_frame"]) + 
                             "\t\t(" + str(start_normal_time["minute"]).zfill(2) + ": " + str(start_normal_time["second"]).zfill(2) + ")" + 
                             "\t\t" + str(self.interrupt_list[i]["end_frame"]) +
                             "\t\t(" + str(end_normal_time["minute"]).zfill(2) + ": " + str(end_normal_time["second"]).zfill(2) + ")\n")
            
        self.resultFile.close()


    def write_result_to_excel(self): ## write result to excel ##
        
        name = self.filename
        ws1 = self.wb.create_sheet(name)

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
            start_time_name = str(start_normal_time["minute"]).zfill(2) + ": " + str(start_normal_time["second"]).zfill(2)

            ##### interrupt end #####
            end_frame_name = str(self.revised_interrupt_list[i]["end_frame"])
            end_normal_time = compute.get_normal_time_info(time_in_seconds=self.revised_interrupt_list[i]["end_time"])
            end_time_name = str(end_normal_time["minute"]).zfill(2) + ": " + str(end_normal_time["second"]).zfill(2)

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
        total_time_name = str(total_normal_time["minute"]).zfill(2) + ": " + str(total_normal_time["second"]).zfill(2)

        data = ['總手術中段時間', total_time_name, '', '', '', '']
        ws1.append(data)

        self.wb.save('Result.xlsx')


        ##### 4. 印出原本 interrupt #####
        ws2 = self.wb_2.create_sheet(name)
        ws2['A1'].value = name
        ws2['B1'].value = 'Start Frame #'
        ws2['C1'].value = 'Start Time'
        ws2['D1'].value = 'End Frame #'
        ws2['E1'].value = 'End Time'
        ws2['F1'].value = 'Label'
        
        for i in range(self.total_interrupt_count):
            interrupt_name = 'Interrupt#' + str(i)
            
            ##### interrupt start #####
            start_frame_name = str(self.interrupt_list[i]["start_frame"])
            start_normal_time = compute.get_normal_time_info(time_in_seconds=self.interrupt_list[i]["start_time"])
            start_time_name = str(start_normal_time["minute"]).zfill(2) + ": " + str(start_normal_time["second"]).zfill(2)

            ##### interrupt end #####
            end_frame_name = str(self.interrupt_list[i]["end_frame"])
            end_normal_time = compute.get_normal_time_info(time_in_seconds=self.interrupt_list[i]["end_time"])
            end_time_name = str(end_normal_time["minute"]).zfill(2) + ": " + str(end_normal_time["second"]).zfill(2)

            ##### label #####
            label_name = self.interrupt_list[i]["label"]
            
            data = [interrupt_name, start_frame_name, start_time_name, end_frame_name, end_time_name, label_name]
            ws2.append(data)

        self.wb_2.save('Original_Result.xlsx')


    def delete_excel_row(self, remove_interrupt_index):
        ws = self.wb[self.filename]
        ws.delete_rows(remove_interrupt_index+2) # excel第一列為1(非index)
        self.wb.save('Result.xlsx')
        