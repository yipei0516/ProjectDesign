import cv2 as cv
import os

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

class judge(object):

    def start_judge(file, cap):
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
            file.resultFile.write("Now Frame: " + str(frame_no) + "\n")

            for i in range(18):
                for j in range(6,26):
                    bgr_value_str = "[%4d" % b[i,j] + "%4d" % g[i,j] + "%4d] " % r[i,j]
                    file.resultFile.write(bgr_value_str)
                file.resultFile.write("\n")

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
                    if(r[i, j] > bg_max):
                        file.resultFile.write("[  r ] ")
                        r_dominate_pixels += 1
                    elif(abs(average - (int)(r[i, j])) < 12 and abs(average - (int)(b[i, j])) < 12 and abs(average - (int)(g[i, j])) < 12):
                        file.resultFile.write("[  s ] ")
                    else:
                        file.resultFile.write("[ gb ] ")
                        gb_dominate_pixels += 1
                file.resultFile.write("\n")
            
            file.resultFile.write("r_dominate_pixels = " + str(r_dominate_pixels) + "\n")
            file.resultFile.write("gb_dominate_pixels = " + str(gb_dominate_pixels) + "\n")

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
                        if(count_frame - tmp_count_frame >= 10):
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

            file.resultFile.write("tmp_flag = " + str(tmp_flag) + "\n")
            file.resultFile.write("tmp_count_frame = " + str(tmp_count_frame) + "\n")
            file.resultFile.write("count_flag = " + str(count_flag) + "\n")
            file.resultFile.write("count_frame = " + str(count_frame) + "\n")
            file.resultFile.write("end_flag = " + str(end_flag) + "\n")
            file.resultFile.write("\n")
            
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
                interrupt_info["start_time"] = round((frame_no - count_frame)/27.25, 1)
                interrupt_info["end_time"] = round((frame_no - tmp_count_frame)/27.25, 1)
                file.interrupt_list.append(interrupt_info) # 加入interrupt list中
                # file.startFrame[candidate_index] = frame_no - count_frame
                # file.endFrame[candidate_index] = frame_no - tmp_count_frame
                # file.startTime[candidate_index] = round((frame_no - count_frame)/27.25, 1)
                # file.endTime[candidate_index] = round((frame_no - tmp_count_frame)/27.25, 1)
                candidate_index += 1
                count_frame = 0
            
            if(tmp_flag == False):
                tmp_count_frame = 0

            frame_no += 1
            if cv.waitKey(1) == ord('q'):      # 每一毫秒更新一次，直到按下 q 結束
                break
        
        # !!!!! 目前為了後續檢查interrupt所以不能release !!!!!
        cap.release()                    # 所有作業都完成後，釋放資源
        cv.destroyAllWindows()                  # 結束所有視窗
        
