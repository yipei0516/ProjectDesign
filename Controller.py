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
        self.first_file = True

    ### 將每個button連上對應的event
    def setup_control(self):
        # TODO
        self.ui.button_choose_video.clicked.connect(self.clicked_choose_video)
        self.ui.button_start_judge.clicked.connect(self.clicked_start_judge)
        self.ui.button_check_result.clicked.connect(self.show_result)
        self.ui.list_widget_interrupt.itemDoubleClicked.connect(self.show_interrupt_clip) # 雙擊interrupt時，跳出此段畫面
        self.ui.list_widget_interrupt.itemClicked.connect(self.choose_remove_interrupt) # 單擊interrupt時，選取起來準備刪除
        self.ui.button_remove_interrupt.clicked.connect(self.remove_interrupt)
    
        

    ### load video into FileDialog
    def clicked_choose_video(self):

        filepath, filetype = QtWidgets.QFileDialog.getOpenFileName()

        if self.first_file: ## 第一次進入
            self.first_file = False
        else: ## 非第一次進入
            opencv_engine.release_video(self.vc)

        self.videoinfo = opencv_engine.get_video_info(filepath)
        self.vc = self.videoinfo["vc"]
        self.video_filename = self.videoinfo["video_name"]
        self.video_fps = self.videoinfo["fps"]

        if not self.vc.isOpened():
            print("Cannot open camera")
            exit()

        self.ui.label_video_name.setText("Video Name:   " + self.video_filename)
        
        self.video_file = Video_File(filepath=filepath, filename=self.video_filename) # 創一個Video_File class叫做file!!!!!!!!!!!!!
        

    
    ### Start Judge
    def clicked_start_judge(self):
        
        ##### Step1. start judge #####
        judge.start_judge(file=self.video_file, cap=self.vc, fps=self.video_fps)
        judge.revise_interrupt(file=self.video_file)

        ##### Step2. write result to file #####
        self.video_file.write_result_to_file()    

        ##### Step3. write result to excel #####
        self.video_file.write_result_to_excel()  
            
        ##### Step4. print result to UI #####
        # record interrupt times, wrong judge times, accuracy
        self.wrongJudgeTimes = 0        # 目前沒這個資訊
        self.accuracy = 0               # 有了total_interrupt_count跟wrongJudgeTimes就可算accuracy
        self.ui.label_interrupt_times.setText("Interrupt Times:   " + str(self.video_file.total_revised_interrupt_count))



    def show_result(self):

        ##### Step1. show result in list widget #####
        # 將interrupt frame加入list widget裡
        for i in range(self.video_file.total_revised_interrupt_count):
            start_normal_time = compute.get_normal_time_info(time_in_seconds=self.video_file.revised_interrupt_list[i]["start_time"])
            start_time_name = str(start_normal_time["minute"]).zfill(2) + ": " + str(start_normal_time["second"]).zfill(2)

            end_normal_time = compute.get_normal_time_info(time_in_seconds=self.video_file.revised_interrupt_list[i]["end_time"])
            end_time_name = str(end_normal_time["minute"]).zfill(2) + ": " + str(end_normal_time["second"]).zfill(2)

            self.ui.list_widget_interrupt.addItem( "Interrupt" + str(i+1) + ". " + start_time_name + " - " + end_time_name)
            # list widget內item的形式為: 3270 - 3295


        ##### Step2. show video in video player #####
        # self.video_controller = video_controller(videoinfo=self.videoinfo, ui=self.ui)
        # self.video_controller.pause()
        # self.ui.button_play.clicked.connect(self.video_controller.play) # connect to function()
        # self.ui.button_stop.clicked.connect(self.video_controller.stop)
        # self.ui.button_pause.clicked.connect(self.video_controller.pause)
        # self.ui.button_forward.clicked.connect(self.video_controller.forward)
        # self.ui.button_rewind.clicked.connect(self.video_controller.rewind)
    
    def show_interrupt_clip(self):
        ##### Step1. 取出選取到的interrupt 
        item_index = self.ui.list_widget_interrupt.currentRow()

        start_choose_frame = self.video_file.revised_interrupt_list[item_index]['start_frame']
        end_choose_frame = self.video_file.revised_interrupt_list[item_index]['end_frame']

        ##### Step2. 播映interrupt開始的地方
        frame_diff = end_choose_frame - start_choose_frame
        count_frame = 0

        ### 直接show ver ###
        self.vc.set(cv.CAP_PROP_POS_FRAMES, start_choose_frame - self.video_fps*1) #往前1秒開始播放
        while True:
            count_frame += 1
            ret, frame = self.vc.read()             # 讀取影片的每一幀
            if not ret:
                print("Cannot receive frame")   # 如果讀取錯誤，印出訊息
                break
            cv.imshow('Interrupy fragment', frame)     # 如果讀取成功，顯示該幀的畫面
            if cv.waitKey(int(1000/self.video_fps)) == ord('q') or count_frame == int(frame_diff + self.video_fps*1): # 往後1秒結束(變成int才能偵測幀數)
                break
        cv.destroyAllWindows()                 # 結束所有視窗
        
        ### video player ver ###
        # self.video_controller.current_frame_no = start_choose_frame
        # self.video_controller.end_choose_interrupt_frame = end_choose_frame # 因為video要從play狀態變成pause狀態所以得將end_choose_interrupt_frame傳入video_controller
        

    def choose_remove_interrupt(self):
        self.remove_item_index = self.ui.list_widget_interrupt.currentRow()


    def remove_interrupt(self):
        # 刪除list widget的item
        remove_item = self.ui.list_widget_interrupt.takeItem(self.remove_item_index)
        self.ui.list_widget_interrupt.removeItemWidget(remove_item)

        # 刪除excel裡的row
        self.video_file.delete_excel_row(self.remove_item_index)

