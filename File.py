import numpy as np
import openpyxl
import os

class Video_File:
    def __init__(self, filepath, filename , cap):
        self.filepath = filepath
        self.filename = filename
        self.cap = cap
        self.total_interrupt_count = 0

        self.interrupt_list = [] 
        # list裡面為的東西為dictionary(包含：start time、end time等等)
        # interrupt_list = [ 第一個interrupt_info, 第二個interrupt_info, 第三個interrupt_info .....]
        # interrupt_list[0] = interrupt_info = {
        #     "start_frame" : interrupt開始的frame(int)
        #     "end_frame"   : interrupt結束的frame(int)
        #     "start_time"  : interrupt開始的time(in seconds)
        #     "end_time"    : interrupt結束的time(in seconds)
        # }  ### 見Utils.py judge
        
        # self.interrupts_frame = []  # 裡面裝的是pair(interrupt開始的frame, interrupt結束的frame)
        # self.interrupts_time = []   # 裡面裝的是pair(interrupt開始的time, interrupt結束的time)

        # self.startFrame = []
        # self.startFrame = [0 for i in range(100)]
        # self.startTime = []
        # self.startTime = [0 for i in range(100)]
        # self.endFrame= []
        # self.endFrame = [0 for i in range(100)]
        # self.endTime = []
        # self.endTime = [0 for i in range(100)]
        

    def write_result_to_file(self): ## write result to file ##
        basename = os.path.basename(self.filepath)
        self.filename = os.path.splitext(basename)[0]
        print("basename", basename)
        print("filename", self.filename)
        fileStr = self.filename + ".txt"
        resultFile = open(fileStr, "w")
        resultFile.write("Video Num:  " + self.filename + "\n")
        resultFile.write("Total interrupt count: " + str(self.total_interrupt_count) + "\n")
        resultFile.write("Interrupt Record Frame and Time: \n")

        for i in range(self.total_interrupt_count):
            start_minute = 0
            start_second = 0
            start_minute = (int)(self.interrupt_list[i]["start_time"]/60)
            start_second = (round(self.interrupt_list[i]["start_time"] - 60*start_minute, 0))
            end_minute = 0
            end_second = 0
            end_minute = (int)(self.interrupt_list[i]["end_time"]/60)
            end_second = (round(self.interrupt_list[i]["end_time"] - 60*end_minute, 0))

            resultFile.write("\tInterrupt#" + str(i) + "\t\t" + str(self.interrupt_list[i]["start_time"]) + 
                             "\t\t(" + str(start_minute) + ": " + str(start_second) + ")" + 
                             "\t\t" + str(self.interrupt_list[i]["end_time"]) +
                             "\t\t(" + str(end_minute) + ": " + str(end_second) + ")\n")

    def write_result_to_excel(self): ## write result to excel ##
        
        name = self.filename
        wb = openpyxl.load_workbook('./Result.xlsx')
        ws1 = wb.create_sheet(name)
        ws1['A1'].value = name
        ws1['B1'].value = 'Start Frame #'
        ws1['C1'].value = 'Start Time'
        ws1['D1'].value = 'End Frame #'
        ws1['E1'].value = 'End Time'

        for i in range(self.total_interrupt_count):
            interrupt_name = 'Interrupt#' + str(i)
            
            ##### interrupt start #####
            start_minute = (int)(self.interrupt_list[i]["start_time"]/60)
            start_second = (round(self.interrupt_list[i]["start_time"] - 60*start_minute, 0))
            start_time_name = str(start_minute) + ": " + str(start_second)
            start_frame_name = str(self.interrupt_list[i]["start_frame"])

            ##### interrupt end #####
            end_minute = (int)(self.interrupt_list[i]["end_time"]/60)
            end_second = (round(self.interrupt_list[i]["end_time"] - 60*end_minute, 0))
            end_time_name = str(end_minute) + ": " + str(end_second)
            end_frame_name = str(self.interrupt_list[i]["end_frame"])

            data = [interrupt_name, start_frame_name, start_time_name, end_frame_name, end_time_name]
            ws1.append(data)

        wb.save('./Result.xlsx')
