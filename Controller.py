from PyQt5 import QtWidgets, QtGui, QtCore
from UI import Ui_MainWindow
from File import Video_File
from Utils import judge, compute, opencv_engine
from VideoController import video_controller
import cv2 as cv 
import os
import re

class MainWindow_controller(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setup_control()

    ### 將每個button連上對應的event
    def setup_control(self):
        # TODO
        self.ui.button_choose_video.clicked.connect(self.clicked_choose_video)
        self.ui.button_start_judge.clicked.connect(self.clicked_start_judge)
        self.ui.button_check_result.clicked.connect(self.show_video)
        self.ui.list_widget_interrupt.itemDoubleClicked.connect(self.interrupt_choose) # 選取interrupt時

    
    ### load video into FileDialog
    def clicked_choose_video(self):
        filepath, filetype = QtWidgets.QFileDialog.getOpenFileName()
        
        videoinfo = opencv_engine.get_video_info(filepath)
        self.vc = videoinfo["vc"]
        self.video_fps = videoinfo["fps"]
        self.video_total_frame_count = videoinfo["frame_count"]
        self.video_width = videoinfo["width"]
        self.video_height = videoinfo["height"]

        if not self.vc.isOpened():
            print("Cannot open camera")
            exit()
        basename = os.path.basename(filepath)
        filename = os.path.splitext(basename)[0]                                    # 只取出檔案名字([1]為副檔名)
        self.ui.label_video_name.setText("Video Name:   " + filename)
        
        self.video_file = Video_File(filepath=filepath, filename=filename) # 創一個Video_File class叫做file!!!!!!!!!!!!!
        

    
    ### Start Judge
    def clicked_start_judge(self):
        
        ##### Step1. start judge #####
        judge.start_judge(file=self.video_file, cap=self.vc)

        ##### Step2. write result to file #####
        self.video_file.write_result_to_file()    

        ##### Step3. write result to excel #####
        self.video_file.write_result_to_excel()   
            
        ##### Step4. print result to UI #####
        # record interrupt times, wrong judge times, accuracy
        self.wrongJudgeTimes = 0        # 目前沒這個資訊
        self.accuracy = 0               # 有了total_interrupt_count跟wrongJudgeTimes就可算accuracy
        self.ui.label_interrupt_times.setText("Interrupt Times:   " + str(self.video_file.total_interrupt_count))
        self.ui.label_wrong_judge_times.setText("Wrong Judge Times:   " + str(self.wrongJudgeTimes))
        self.ui.label_accuracy.setText("Accuracy:   " + str(self.accuracy))



    ### 按下check result button後出現video player
    def show_video(self):

        ##### Step1. show result in list widget #####
        # 將interrupt frame加入list widget裡
        for i in range(self.video_file.total_interrupt_count):
            start_normal_time = compute.get_normal_time_info(time_in_seconds=self.video_file.interrupt_list[i]["start_time"])
            start_time_name = str(start_normal_time["minute"]).zfill(2) + ": " + str(start_normal_time["second"]).zfill(2)

            end_normal_time = compute.get_normal_time_info(time_in_seconds=self.video_file.interrupt_list[i]["end_time"])
            end_time_name = str(end_normal_time["minute"]).zfill(2) + ": " + str(end_normal_time["second"]).zfill(2)

            self.ui.list_widget_interrupt.addItem(start_time_name + " - " + end_time_name)
            # list widget內item的形式為: 3270 - 3295

        ##### Step2. show video in video player #####
        self.video_path = self.video_file.filepath
        self.video_controller = video_controller(video_path=self.video_path, ui=self.ui)
        self.ui.button_play.clicked.connect(self.video_controller.play) # connect to function()
        self.ui.button_stop.clicked.connect(self.video_controller.stop)
        self.ui.button_pause.clicked.connect(self.video_controller.pause)
        self.ui.button_forward.clicked.connect(self.video_controller.forward)
        self.ui.button_rewind.clicked.connect(self.video_controller.rewind)
    
    def interrupt_choose(self):

        ##### Step1. 取出選取到的interrupt
        item = self.ui.list_widget_interrupt.currentItem().text()
        choose_frame = re.findall(r"\d+", item) # 從string中抓出數字的部分
            # choose_frame = [
            #     start interrupt minute,
            #     start interrupt second,
            #     end interrupt minute,
            #     end interrupt second,
            # ]

        start_normal_time = {}
        start_normal_time["minute"] = int(choose_frame[0])
        start_normal_time["second"] = int(choose_frame[1])
        start_choose_frame = compute.get_frame_num(start_normal_time, self.video_fps)

        end_normal_time = {}
        end_normal_time["minute"] = int(choose_frame[2])
        end_normal_time["second"] = int(choose_frame[3])
        end_choose_frame = compute.get_frame_num(end_normal_time, self.video_fps)

        ##### Step2. 播映interrupt開始的地方
        self.video_controller.pause()   # 先讓影片不播映->按下play再開始
        self.video_controller.current_frame_no = start_choose_frame
        # self.video_controller.set_current_frame_no(self.video_controller.current_frame_no)
        # frame = self.video_controller.get_next_frame()
        # self.video_controller.update_label_frame(frame)

        ##### Step3. 暫停interrupt結束的地方
        self.video_controller.end_choose_interrupt_frame = end_choose_frame
        # 因為video要從play狀態變成pause狀態所以得將end_choose_interrupt_frame傳入video_controller

