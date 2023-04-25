from PyQt5 import QtCore 
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtCore import QTimer 

# from Utils import opencv_engine


class video_controller(object):
    def __init__(self, videoinfo, ui, end_choose_interrupt_frame = -1):
        self.ui = ui
        self.end_choose_interrupt_frame = end_choose_interrupt_frame    # default: end_choose_interrupt_frame為0(一開始可不用傳入東西)
        self.qpixmap_fix_width = 800                                    # 16x9 = 1920x1080 = 1280x720 = 800x450
        self.qpixmap_fix_height = 450
        self.current_frame_no = 0
        self.videoplayer_state = "pause"
        self.init_video_info(videoinfo=videoinfo)
        self.set_video_player()

    def init_video_info(self, videoinfo):
        self.vc = videoinfo["vc"]
        self.video_name = videoinfo["video_name"]
        self.video_fps = videoinfo["fps"]
        self.video_total_frame_count = videoinfo["frame_count"]
        self.video_width = videoinfo["width"]
        self.video_height = videoinfo["height"]

        self.ui.slider_videoframe.setRange(0, self.video_total_frame_count-1)
        self.ui.slider_videoframe.valueChanged.connect(self.get_slider_value)

    def set_video_player(self):
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer_timeout) # when timeout, do run one
        self.timer.start(1) # but if CPU can not decode as fast as fps, we set 1 (need decode time)
        # 但如果CPU跑很慢(比幀率慢), default就是1


    def set_current_frame_no(self, frame_no):
        self.vc.set(1, frame_no) # bottleneck

    def get_next_frame(self):
        ret, frame = self.vc.read()
        self.ui.label_frameinfo.setText(f"frame number: {self.current_frame_no}/{self.video_total_frame_count}")
        self.set_slider_value()
        return frame

    def update_label_frame(self, frame):       
        bytesPerline = 3 * self.video_width
        qimg = QImage(frame, self.video_width, self.video_height, bytesPerline, QImage.Format_RGB888).rgbSwapped()
        self.qpixmap = QPixmap.fromImage(qimg)

        if self.qpixmap.width()/16 >= self.qpixmap.height()/9: # like 1600/16 > 90/9, height is shorter, align width
            self.qpixmap = self.qpixmap.scaledToWidth(self.qpixmap_fix_width)
        else: # like 1600/16 < 9000/9, width is shorter, align height
            self.qpixmap = self.qpixmap.scaledToHeight(self.qpixmap_fix_height)
        self.ui.label_videoplayer.setPixmap(self.qpixmap)
        self.ui.label_videoplayer.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter) # Center


    def play(self):
        self.videoplayer_state = "play"

    def stop(self):
        self.videoplayer_state = "stop"

    def pause(self):
        self.videoplayer_state = "pause"
    
    def forward(self):
        self.videoplayer_state = "forward"

    def rewind(self):
        self.videoplayer_state = "rewind"

    def timer_timeout(self):
        if (self.videoplayer_state == "play"):
            ### 若已經播映完畢
            if self.current_frame_no >= self.video_total_frame_count-1:
                self.videoplayer_state = "stop"
                self.current_frame_no = 0  # 從頭開始replay
                self.set_current_frame_no(self.current_frame_no)
            ### 若遇到選擇的interrupt結束時
            elif self.current_frame_no == int(self.end_choose_interrupt_frame):
                self.videoplayer_state = "pause"
                self.current_frame_no = self.end_choose_interrupt_frame
                self.set_current_frame_no(self.current_frame_no)
                self.end_choose_interrupt_frame = -1 # 結束此次interrupt選取->將end_choose_interrupt_frame reset
            ### 若播映中
            else:
                self.current_frame_no += 1

        if (self.videoplayer_state == "stop"):
            self.current_frame_no = 0
            self.set_current_frame_no(self.current_frame_no)

        if (self.videoplayer_state == "pause"):
            self.current_frame_no = self.current_frame_no
            self.set_current_frame_no(self.current_frame_no)

        if self.videoplayer_state == "forward":
            self.videoplayer_state = "play"
            self.current_frame_no += self.video_fps*5
            if self.current_frame_no >= self.video_total_frame_count-1: # 往前 若已經超過總幀數的話
                self.current_frame_no = self.video_total_frame_count-1 # 停在最後面
            self.set_current_frame_no(self.current_frame_no)
            

        if self.videoplayer_state == "rewind":
            self.videoplayer_state = "play"
            self.current_frame_no -= self.video_fps*5
            if self.current_frame_no < 0: # 往後 若已經小於第一幀的話
                self.current_frame_no = 0
            self.set_current_frame_no(self.current_frame_no)

        frame = self.get_next_frame()
        self.update_label_frame(frame)

    def get_slider_value(self):
        self.current_frame_no = self.ui.slider_videoframe.value()
        self.set_current_frame_no(self.current_frame_no)

    def set_slider_value(self):
        self.ui.slider_videoframe.setValue(self.current_frame_no)
