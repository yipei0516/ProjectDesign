import cv2 as cv
import os
import re
from PIL import Image, ImageQt
from PyQt5.QtGui import QImage, QPixmap

class opencv_engine(object):

    @staticmethod
    def get_video_info(video_path): 
        videoinfo = {} # !!!!! dictionary !!!!!
        vc = cv.VideoCapture(video_path)
        videoinfo["vc"] = vc    # 影片片段
        basename = os.path.basename(video_path)
        filename = os.path.splitext(basename)[0]                                    # 只取出檔案名字([1]為副檔名)
        videoinfo["video_name"] = filename
        videoinfo["fps"] = vc.get(cv.CAP_PROP_FPS) # 影片幀率
        videoinfo["frame_count"] = int(vc.get(cv.CAP_PROP_FRAME_COUNT)) # 影片總幀數
        videoinfo["width"] = int(vc.get(cv.CAP_PROP_FRAME_WIDTH))
        videoinfo["height"] = int(vc.get(cv.CAP_PROP_FRAME_HEIGHT))
        return videoinfo
    
    def release_video(cap):
        if cap is None:
            return
        else:
            cap.release()
            return
        
class compute(object):
    def get_normal_time_info(time_in_seconds):
        normal_time = {}
        normal_time["minute"] = (int)(time_in_seconds/60)
        normal_time["second"] = (int)(round(time_in_seconds - 60*normal_time["minute"], 0))
        return normal_time
    
    def get_frame_num(time_in_normal_time, fps):
        time_in_seconds = time_in_normal_time["minute"]*60 + time_in_normal_time["second"]
        frame_num = time_in_seconds * fps
        return frame_num
    
    def get_excel_str(normal_time):
        normal_time_str = str(normal_time["minute"]).zfill(2) + ": " + str(normal_time["second"]).zfill(2)
        return normal_time_str
    
    def normal_time_to_seconds(time_in_normal_time):
        interrupt_info = re.findall(r"\d+", str(time_in_normal_time))
        minute = int(interrupt_info[0])
        second = int(interrupt_info[1])
        time_in_seconds = minute*60 + second
        return time_in_seconds
    
    def seconds_to_frame_num(time_in_seconds, fps):
        frame_num = time_in_seconds * fps
        return frame_num
        
        
    

class judge(object):
    def start_judge(file):
        cap = file.videoinfo["vc"]
        fps = file.videoinfo["fps"]
        finish_judge = True
        ## parameter setting ##
        limit = 20      # count_frame的上限 = fake_count的上限 = 20

        ## init ##
        frame_no = 0
        valid_element = 59*4

        count_frame = 0                
        interrupt_flag = False
        tmp_flag = False
        tmp_count_frame = 0
        end_flag = False
        count_flag = False

        candidate_index = 0
        
        ## start judge ##
        while True:
            # reset 
            r_dominate_pixels = 0
            gb_dominate_pixels = 0

            ret, frame = cap.read()            # 讀取影片的每一幀
            if not ret:
                print("Cannot receive frame")       # 如果讀取錯誤，印出訊息
                break

            cv.imshow('BGRValue', frame)            # 如果讀取成功，顯示該幀的畫面

            
            image = cv.resize(frame, (32, 18))
            b,g,r = cv.split(image)

            for i in range(18):
                for j in range(6,26):
                    bgr_value_str = "[%4d" % b[i,j] + "%4d" % g[i,j] + "%4d] " % r[i,j]

            for i in range(18):
                for j in range(6,26):
                    # judge pixel who domiante
                    # if(b[i, j] == r[i, j]) or (g[i, j] == r[i, j]):         # 排除白、黑、灰(r[]=g[]=b[])
                    #     valid_element = valid_element - 1
                    # else:
                    #     if(r[i, j] > b[i, j]) or (r[i, j] > g[i, j]):
                    #         r_dominate_pixels += 1
                    #     else:
                    #         gb_dominate_pixels += 1
                    bg_max = max(b[i, j], g[i, j])
                    average = ((int)(b[i, j]) + (int)(g[i, j]) + (int)(r[i, j])) / 3
                    if(abs(average - (int)(r[i, j])) < 12 and abs(average - (int)(b[i, j])) < 12 and abs(average - (int)(g[i, j])) < 12):
                        pass
                    elif(r[i, j] > bg_max):
                        r_dominate_pixels += 1
                    else:
                        gb_dominate_pixels += 1
            
            if(gb_dominate_pixels >= r_dominate_pixels) :    # 在鼻孔外面
                count_flag = True
                count_frame += 1
                if(tmp_flag == True):
                    tmp_flag = False
                    tmp_count_frame = 0
            else:                       # 在鼻孔裡面
                if(count_flag == True):
                    if(tmp_flag == True) and (tmp_count_frame < 20):
                        tmp_count_frame += 1
                        count_frame += 1
                    elif(tmp_flag == True) and (tmp_count_frame >= 20):
                        if(count_frame - tmp_count_frame >= 8):
                            end_flag = True
                        else:
                            count_frame = 0
                        tmp_flag = False
                        count_flag = False
                    elif(tmp_flag == False) and (count_frame >= 8):
                        tmp_flag = True
                        tmp_count_frame += 1
                        count_frame += 1
                    else:
                        tmp_flag = False
                        tmp_count_frame = 0
                        count_frame = 0
                        count_flag = False

            # 如果連續30偵判斷在鼻外  -->  手術中斷
            if(count_frame >= 30):
                interrupt_flag = True
            else:
                interrupt_flag = False

            ## 記錄interrupt頭、尾時間點 
            # 記錄interrupt開始、結束時間點   --> 只記錄interrupt_flag從false變true的瞬間
            if end_flag == True:
                end_flag = False
                file.total_interrupt_count += 1
                interrupt_info = {} # dictionary
                interrupt_info["start_frame"] = frame_no - count_frame
                interrupt_info["end_frame"] = frame_no - tmp_count_frame
                interrupt_info["start_time"] = round((frame_no - count_frame)/fps, 1)
                interrupt_info["end_time"] = round((frame_no - tmp_count_frame)/fps, 1)
                interrupt_info["label"] = 'A'
                file.interrupt_list.append(interrupt_info) # 加入interrupt list中
                candidate_index += 1
                count_frame = 0
            
            if(tmp_flag == False):
                tmp_count_frame = 0

            frame_no += 1
            if cv.waitKey(1) == ord('q'):      # 每一毫秒更新一次，直到按下 q 結束
                finish_judge = False # 若手動關掉則刪除此次紀錄
                break
        
        cap.release()
        cv.destroyAllWindows()                  # 結束所有視窗

        return finish_judge

        
    def revise_interrupt(file):

        interrupt_info = {} # dictionary
        first_BLabel_record = False

        if file.total_interrupt_count == 0:
            return
        
        elif file.total_interrupt_count == 1:
            file.revised_interrupt_list.append(file.interrupt_list[0])
            file.total_revised_interrupt_count += 1
            return
        

        for i in range(1, file.total_interrupt_count):
            p1 = i-1
            p2 = i

            if(file.interrupt_list[p2]['start_frame'] - file.interrupt_list[p1]['end_frame'] <= 100):
                if(first_BLabel_record == False):
                    interrupt_info["start_frame"] = file.interrupt_list[p1]["start_frame"]
                    interrupt_info["start_time"] = file.interrupt_list[p1]["start_time"]
                    interrupt_info["label"] = 'B'
                    first_BLabel_record = True

                    file.interrupt_list[p1]['label'] = 'B'

                interrupt_info["end_frame"] = file.interrupt_list[p2]["end_frame"]
                interrupt_info["end_time"] = file.interrupt_list[p2]["end_time"]
                file.interrupt_list[p2]['label'] = 'B'

                if(p2 == file.total_interrupt_count-1):
                    file.total_revised_interrupt_count += 1
                    file.revised_interrupt_list.append(interrupt_info)

            else:
                if not interrupt_info:                  #if(interrupt_info == NULL)     --> A的interrupt 
                    file.total_revised_interrupt_count += 1
                    interrupt_info = file.interrupt_list[p1]
                    file.revised_interrupt_list.append(interrupt_info)

                else:                                   #if(interrupt_info != NULL)     --> 最後一個B收尾
                    file.total_revised_interrupt_count += 1
                    file.revised_interrupt_list.append(interrupt_info)
                
                interrupt_info = {}      # 幫下一個interrupt清空interrupt_info變數
                first_BLabel_record = False


                if(p2 == file.total_interrupt_count-1):
                    file.total_revised_interrupt_count += 1
                    interrupt_info = file.interrupt_list[p2]
                    file.revised_interrupt_list.append(interrupt_info)

    def get_score(oneday_dir):
        oneday_interrupt_count = oneday_dir.oneday_interrupt_count
        oneday_total_time = oneday_dir.oneday_total_time

        score = round(oneday_interrupt_count/(oneday_total_time/60/9), 2)
        print("SCORE = " + str(score))
        return score


    def performance(oneday_dir):
        oneday_interrupt_count = oneday_dir.oneday_interrupt_count
        oneday_total_time = oneday_dir.oneday_total_time

        score = oneday_interrupt_count/(oneday_total_time/60/9)
        performance = '-'
        if 0 <= score < 1:
            performance = 'A+'
        elif 1 <= score < 3:
            performance = 'A'
        elif 3 <= score < 4:
            performance = 'A-'
        elif 4 <= score < 5:
            performance = 'B+'
        elif 5 <= score < 7:
            performance = 'B'
        elif 7 <= score < 8:
            performance = 'B-'
        elif 8 <= score < 9:
            performance = 'C+'
        elif 9 <= score < 11:
            performance = 'C'
        elif 11 <= score < 12:
            performance = 'C-'
        elif 12 <= score:
            performance = 'D'

        return performance
    
    def performance_eff(oneday_dir):

        score = round(oneday_dir.oneday_interrupt_time / oneday_dir.oneday_total_time, 3) * 100
        performance = '-'
        if 0 <= score < 6:
            performance = 'A'
        elif 6 <= score < 12:
            performance = 'B'
        elif 12 <= score < 18:
            performance = 'C'
        elif 18 <= score:
            performance = 'D'

        return performance
    
class image(object):
    def show_image_on_label(filepath):
        img = Image.open(filepath)
        qimg = ImageQt.toqimage(img)
        height, width = img.size
        canvas = QPixmap(width,height).fromImage(qimg)
        return canvas
