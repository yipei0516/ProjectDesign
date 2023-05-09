from PyQt5 import QtWidgets, QtGui, QtCore
from UI import Ui_MainWindow
from Directory import Directory
from File import Video_File
from Utils import judge, compute, opencv_engine, image
from VideoController import video_controller
from Plot import Plot
import cv2 as cv 
import os
from playsound import playsound
 

class MainWindow_controller(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setup_control()
        self.ui.button_start_judge.setDisabled(True)
        self.ui.button_check_result.setDisabled(True)

    ### 將每個button連上對應的event
    def setup_control(self):
        # TODO
        self.ui.button_choose_video.clicked.connect(self.clicked_choose_video)
        self.ui.button_start_judge.clicked.connect(self.clicked_start_judge)
        self.ui.button_check_result.clicked.connect(self.show_result)
        self.ui.list_widget_interrupt.itemDoubleClicked.connect(self.show_interrupt_clip) # 雙擊interrupt時，跳出此段畫面
        self.ui.list_widget_interrupt.itemClicked.connect(self.choose_remove_interrupt) # 單擊interrupt時，選取起來準備刪除
        self.ui.button_remove_interrupt.clicked.connect(self.remove_interrupt)


        self.ui.comboBox_choose_video.currentIndexChanged.connect(self.change_list_widget)

        self.ui.button_plot_result.clicked.connect(self.clicked_button_plot_result)
        

    def clicked_choose_video(self):
        ##### Step1. 選取資料夾 #####
        dir_path = QtWidgets.QFileDialog.getExistingDirectory()
        dir_name = os.path.basename(dir_path)
        self.oneday_dir = Directory(dirpath=dir_path, dirname=dir_name)

        ##### Step2. 確認是否直接關掉選取畫面 #####
        # 直接關掉選擇資料夾畫面 #
        if dir_path == '':
            pass
        # 已選取某個資料夾!! #
        else:
            ##### Step3. 先做Directory的部分-> 找出全部的video(小檔案) #####
            all_file_name = os.listdir(dir_path)
            oneday_video_name = []
            for file in all_file_name:
                if os.path.splitext(file)[1] == ".mp4": # 若是影片檔才能當作一個file
                    # 1. 先新增成多個video_file檔
                    filepath = dir_path + "/" + file
                    filename = os.path.splitext(file)[0]
                    video_file = Video_File(filepath=filepath, filename=filename)
                    self.oneday_dir.video_file_list.append(video_file)
                    self.oneday_dir.video_count += 1
                    self.oneday_dir.oneday_total_time += round(video_file.videoinfo['frame_count']/video_file.videoinfo['fps'], 1) # 記錄總影片時長(in seconds)

                    # 2. 再準備待會要檢查有沒有重複偵測的部分
                    oneday_video_name.append(filename)

            ##### Step4. 確認資料夾是否選對(有無包含mp4檔) #####
            # 沒有含mp4檔案 #
            if self.oneday_dir.video_count == 0:
                mbox = QtWidgets.QMessageBox(self.ui.centralwidget)
                mbox.setIcon(QtWidgets.QMessageBox.Warning)
                mbox.setText("資料夾 {0} 未包含影片檔案，請重新選擇資料夾".format(dir_name))
                mbox.exec()
                pass
            # 有含mp4檔案 #
            else:
                ##### Step5. 確認是否偵測過此資料夾! #####
                # 工作表內已含有此天的手術偵測紀錄 #
                if dir_name in self.oneday_dir.wb.sheetnames: 
                    repeated_sheet = self.oneday_dir.wb[dir_name]
                    mbox = QtWidgets.QMessageBox(self.ui.centralwidget) # 跳出警告訊息
                    mbox.setIcon(QtWidgets.QMessageBox.Warning)
                    mbox.setText("你已經測試過 {0} 的手術，是否要重新測試?".format(dir_name))
                    mbox.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No) # 添加三顆按鈕
                    mbox.setDefaultButton(QtWidgets.QMessageBox.No) # 設定預設按鈕
                    ret = mbox.exec()
                    if ret == QtWidgets.QMessageBox.Yes:
                        # 刪除前一個judge的結果
                        self.oneday_dir.wb.remove_sheet(repeated_sheet)
                        self.oneday_dir.wb.save('Result.xlsx')
                        self.ui.button_start_judge.setDisabled(False)
                        self.ui.button_check_result.setDisabled(True)
                    elif ret == QtWidgets.QMessageBox.No:
                        # 跳出上次的結果
                        self.oneday_dir.oneday_interrupt_count = int(repeated_sheet['B'+str(repeated_sheet.max_row-4)].value)
                        self.oneday_dir.oneday_interrupt_time = compute.normal_time_to_seconds(repeated_sheet['B'+str(repeated_sheet.max_row-3)].value)
                        self.oneday_dir.oneday_performance = repeated_sheet['B'+str(repeated_sheet.max_row-1)].value
                        self.oneday_dir.oneday_efficiency = repeated_sheet['B'+str(repeated_sheet.max_row)].value
                        A_col = repeated_sheet['A']
                        start_time = repeated_sheet['B']
                        end_time = repeated_sheet['C']
                        video_index = 0
                        for i in range(2, len(A_col)): # 跳過第一行
                            if A_col[i].value == '手術總中斷次數':
                                break
                            elif video_index < self.oneday_dir.video_count and A_col[i].value == oneday_video_name[video_index]:
                                video_file = self.oneday_dir.video_file_list[video_index]
                                video_index += 1
                            elif (A_col[i].value is not None) and (A_col[i].value != 'No interrupt') :
                                interrupt_info = {}
                                interrupt_info["start_time"] = compute.normal_time_to_seconds(start_time[i].value)
                                interrupt_info["end_time"] = compute.normal_time_to_seconds(end_time[i].value)
                                video_file.revised_interrupt_list.append(interrupt_info)
                                video_file.total_revised_interrupt_count += 1
                        self.ui.button_start_judge.setDisabled(True)
                        self.ui.button_check_result.setDisabled(False)
                # 工作表內未含有此天的手術偵測紀錄 #
                else:
                    self.ui.button_start_judge.setDisabled(False)
                    self.ui.button_check_result.setDisabled(True)

                # 為了可能重複偵測->全部reset
                self.ui.label_video_name.setText("資料夾名稱:   " + dir_name)
                self.ui.label_done.setVisible(False)
                self.ui.label_performance.setText("")
                self.ui.label_performance_text.setText("中斷次數評分:   尚未進行偵測")
                self.ui.label_efficiency.setText("")
                self.ui.label_efficeiency_text.setText("效率評分:   尚未進行偵測")
                self.ui.label_surgery_time.setText("總手術時間:   尚未進行偵測")
                self.ui.label_total_interrupt_time.setText("總中斷時間:   尚未進行偵測")
                self.ui.label_interrupt_times.setText("總中斷次數:   尚未進行偵測")
                self.ui.label_ratio.setText("中斷時間佔比:   尚未進行偵測")
                self.ui.label_efficeiency_text.setText("單位時間中斷次數:   尚未進行偵測")
                

    
    ### Start Judge
    def clicked_start_judge(self):
        finish_judge = True # 是否正確結束judge
        for video in self.oneday_dir.video_file_list:
            ##### Step1. start judge #####
            finish_judge = judge.start_judge(file=video)
            if finish_judge == False: # 非正確結束
                break
            judge.revise_interrupt(file=video)


            ##### Step2. write result to file #####
            # video.write_result_to_file()

        if finish_judge == True: # 正確結束
            ##### Step3. 評估performance #####
            self.oneday_dir.oneday_performance = judge.performance(oneday_dir=self.oneday_dir)
            self.oneday_dir.oneday_efficiency = judge.performance_eff(oneday_dir=self.oneday_dir)


            ##### Step4. write result to excel #####
            self.oneday_dir.write_result_to_excel()


            ##### Step5. 結束Judge後的提示 #####
            qimage = image.show_image_on_label("./image/FINISH.jpg")
            self.ui.label_done.setPixmap(qimage)
            playsound('./sound/done.mp3')

            self.ui.button_start_judge.setDisabled(True)
            self.ui.button_check_result.setDisabled(False)
        
        else: # 未正確結束
            mbox = QtWidgets.QMessageBox(self.ui.centralwidget)
            mbox.setIcon(QtWidgets.QMessageBox.Warning)
            mbox.setText("資料夾 {0} 未正確結束，請重新選擇資料夾或者重新偵測此資料夾".format(self.oneday_dir.dirname))
            mbox.exec()

    def show_result(self):
        ##### Step1. print result to UI #####
        self.ui.label_interrupt_times.setText("總中斷次數:   " + str(self.oneday_dir.oneday_interrupt_count))
        self.ui.label_performance.setText(self.oneday_dir.oneday_performance)
        self.ui.label_performance_text.setText("中斷次數評分:   ")
        self.ui.label_efficiency.setText(self.oneday_dir.oneday_efficiency)
        self.ui.label_efficeiency_text.setText("效率評分:   ")
        ##### Step2. show all interrupt #####
        self.ui.comboBox_choose_video.clear()
        for video_file in self.oneday_dir.video_file_list:
            self.ui.comboBox_choose_video.addItem(video_file.filename)

    def change_list_widget(self):
        ##### Step1. check現在是哪一個video #####
        index = self.ui.comboBox_choose_video.currentIndex()
        self.ui.list_widget_interrupt.clear() # 清空listwidget

        ##### Step2. show result in list widget #####
        self.choose_video_file = self.oneday_dir.video_file_list[index]
        for i in range(self.choose_video_file.total_revised_interrupt_count):
            start_normal_time = compute.get_normal_time_info(time_in_seconds=self.choose_video_file.revised_interrupt_list[i]["start_time"])
            start_time_name = compute.get_excel_str(normal_time=start_normal_time)

            end_normal_time = compute.get_normal_time_info(time_in_seconds=self.choose_video_file.revised_interrupt_list[i]["end_time"])
            end_time_name = compute.get_excel_str(normal_time=end_normal_time)

            self.ui.list_widget_interrupt.addItem("Interrupt" + str(i+1) + ". " + start_time_name + " - " + end_time_name)
    
    def show_interrupt_clip(self):
        ##### Step1. 取出選取到的interrupt 
        item_index = self.ui.list_widget_interrupt.currentRow()

        videoinfo = opencv_engine.get_video_info(self.choose_video_file.filepath) # 因為每一次要播放的地方不一樣，Judge時已把原本的vc release掉，所以每次show都重新get_video_info
        vc = videoinfo["vc"]
        fps = videoinfo["fps"]
        
        start_choose_frame = compute.seconds_to_frame_num(time_in_seconds=self.choose_video_file.revised_interrupt_list[item_index]['start_time'], fps=fps) 
        end_choose_frame = compute.seconds_to_frame_num(time_in_seconds=self.choose_video_file.revised_interrupt_list[item_index]['end_time'], fps=fps)

        ##### Step2. 播映interrupt開始的地方
        frame_diff = end_choose_frame - start_choose_frame
        count_frame = 0

        
        vc.set(cv.CAP_PROP_POS_FRAMES, start_choose_frame - fps*1) #往前1秒開始播放
        while True:
            count_frame += 1
            ret, frame = vc.read()             # 讀取影片的每一幀
            if not ret:
                print("Cannot receive frame")   # 如果讀取錯誤，印出訊息
                break
            cv.imshow('Interrupy fragment', frame)     # 如果讀取成功，顯示該幀的畫面
            if cv.waitKey(int(1000/fps)) == ord('q') or count_frame == int(frame_diff + fps*1): # 往後1秒結束(變成int才能偵測幀數)
                break
        
        vc.release()
        cv.destroyAllWindows()                 # 結束所有視窗
        

    def choose_remove_interrupt(self):
        self.remove_item_index = self.ui.list_widget_interrupt.currentRow()


    def remove_interrupt(self):
        # 刪除list widget的item
        remove_item = self.ui.list_widget_interrupt.takeItem(self.remove_item_index)
        self.ui.list_widget_interrupt.removeItemWidget(remove_item)

        # 刪除excel裡的row
        self.oneday_dir.delete_excel_row(self.choose_video_file, self.remove_item_index)

        # 更改目前UI的顯示!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        self.ui.label_total_interrupt_time.setText("總中斷時間:   " + str(self.oneday_dir.oneday_interrupt_time))
        self.ui.label_interrupt_times.setText("總中斷次數:   " + str(self.oneday_dir.oneday_interrupt_count))
        


    def clicked_button_plot_result(self):
        self.plotObject = Plot(ui=self.ui)

        has_FiveDaysData = self.plotObject.judge_fiveDays()
        if(has_FiveDaysData == True):
            self.plotObject.load_currentFiveDaysData()
        else:
            self.ui.plot_label1.setText("尚未集滿5天手術資料!")
            self.ui.plot_label2.setText("尚未集滿5天手術資料!")
            self.ui.plot_label3.setText("尚未集滿5天手術資料!")
            self.ui.plot_label4.setText("尚未集滿5天手術資料!")
