import numpy as np
import openpyxl
import os
from Utils import opencv_engine

class Video_File:
    def __init__(self, filepath, filename):
        self.filepath = filepath

        self.filename = filename

        self.total_interrupt_count = 0
        self.interrupt_list = []

        self.total_revised_interrupt_count = 0
        self.revised_interrupt_list = []

        self.total_interrupt_time = 0

        self.total_time = 0

        self.videoinfo = opencv_engine.get_video_info(video_path=filepath)
        # list裡面為的東西為dictionary(包含：start time、end time等等)
        # interrupt_list = [ 第一個interrupt_info, 第二個interrupt_info, 第三個interrupt_info .....]
        # interrupt_list[0] = interrupt_info = {
        #     "start_frame" : interrupt開始的frame(int)
        #     "end_frame"   : interrupt結束的frame(int)
        #     "start_time"  : interrupt開始的time(in seconds)
        #     "end_time"    : interrupt結束的time(in seconds)
        #     "label"       : interrupt label --> A類表簡單可分類；B類表待確認類
        # }  ### 見Utils.py judge


    def delete_interrupt(self, remove_index):
        self.total_revised_interrupt_count -= 1
        del self.revised_interrupt_list[remove_index]