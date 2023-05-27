from PyQt5 import QtWidgets, QtGui, QtCore
from Ui_Result import Ui_MainWindow
import MenuController
from Utils import judge, compute, opencv_engine, image
import cv2 as cv
 

class Result_controller(QtWidgets.QMainWindow):
    def __init__(self, oneday_dir):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint | QtCore.Qt.WindowCloseButtonHint)
        self.setup_control()

        self.oneday_dir = oneday_dir
        self.show_result()
        self.ui.button_remove_interrupt.setDisabled(True)

        qimage = image.show_image_on_label("./image/ins1.png")
        self.ui.label_cute_image.setPixmap(qimage)
        self.ui.label_cute_image.lower()

        qimage = image.show_image_on_label("./image/background1.png")
        self.ui.label_background.setPixmap(qimage)
        self.ui.label_background.lower()
        op = QtWidgets.QGraphicsOpacityEffect()
        op.setOpacity(0.4)
        self.ui.label_background.setGraphicsEffect(op)

    ### 將每個button連上對應的event
    def setup_control(self):
        self.ui.list_widget_interrupt.itemDoubleClicked.connect(self.show_interrupt_clip) # 雙擊interrupt時，跳出此段畫面
        self.ui.list_widget_interrupt.itemClicked.connect(self.choose_remove_interrupt) # 單擊interrupt時，選取起來準備刪除
        self.ui.button_remove_interrupt.clicked.connect(self.remove_interrupt)
        self.ui.comboBox_choose_video.currentIndexChanged.connect(self.change_list_widget)

        self.ui.button_back_menu.clicked.connect(self.back_menu)


    def show_result(self):
        ##### Step1. print result to UI #####
        ## 最上面的大數據
        self.ui.label_performance.setText(self.oneday_dir.oneday_performance)
        self.ui.label_performance_text.setText("中斷次數評分:   ")
        self.ui.label_efficiency.setText(self.oneday_dir.oneday_efficiency)
        self.ui.label_efficeiency_text.setText("效率評分:   ")
        ## 次要的小數據
        self.ui.label_surgery_time.setText("總手術時間:   " + str(round(self.oneday_dir.oneday_total_time/60, 1)) + " 分鐘")
        self.ui.label_total_interrupt_time.setText("總中斷時間:   " + str(round(self.oneday_dir.oneday_interrupt_time/60, 1))  + " 分鐘")
        self.ui.label_interrupt_times.setText("總中斷次數:   " + str(self.oneday_dir.oneday_interrupt_count) + " 次")
        self.ui.label_ratio.setText("中斷時間佔整個手術時間的比例:   " + str(self.oneday_dir.oneday_ratio) + " %")
        self.ui.label_unit_interrupt_counts.setText("平均每九分鐘的中斷次數:   " + str(self.oneday_dir.oneday_unit_interrupt_counts) + " 次")

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
        self.ui.button_remove_interrupt.setDisabled(False)


    def remove_interrupt(self):
        # 刪除list widget的item
        remove_item = self.ui.list_widget_interrupt.takeItem(self.remove_item_index)
        self.ui.list_widget_interrupt.removeItemWidget(remove_item)

        # 刪除excel裡的row(大影片interrupt)
        self.oneday_dir.delete_excel_row(self.choose_video_file, self.remove_item_index)

        # 刪除小影片interrupt
        self.choose_video_file.delete_interrupt(self.remove_item_index)

        # 更改目前UI的顯示!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        self.ui.label_total_interrupt_time.setText("總中斷時間:   " + str(round(self.oneday_dir.oneday_interrupt_time/60, 1))  + " 分鐘")
        self.ui.label_interrupt_times.setText("總中斷次數:   " + str(self.oneday_dir.oneday_interrupt_count) + " 次")
        self.ui.label_ratio.setText("中斷時間佔整個手術時間的比例:   " + str(self.oneday_dir.oneday_ratio) + " %")
        self.ui.label_unit_interrupt_counts.setText("平均每九分鐘的中斷次數:   " + str(self.oneday_dir.oneday_unit_interrupt_counts) + " 次")
        self.ui.label_performance.setText(self.oneday_dir.oneday_performance)
        self.ui.label_performance_text.setText("中斷次數評分:   ")
        self.ui.label_efficiency.setText(self.oneday_dir.oneday_efficiency)
        self.ui.label_efficeiency_text.setText("效率評分:   ")

        self.ui.button_remove_interrupt.setDisabled(True)
        

    def back_menu(self):
        self.hide()
        self.result_window = MenuController.Menu_controller()
        self.result_window.show()