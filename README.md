# 目前做完的：
1. 可以選取要看的interrupt讓video跳到中斷開始的地方
2. 暫停、開始、從頭開始
3. 滑桿
4. 分成幾個.py檔：
    - Start.py：程式開始的地方
    - Controller.py：控制整個UI
    - VideoController.py：控制影片播放器的地方（右半邊）
    - File.py：放有關於讀進來的video file的Class（一個file可以創一個class）
        * 放置一個video會需要用的參數(filename、interrupt_count)
        * 寫入.txt file的function、寫入excel的function
    - Utils.py：放置一些會用到的function
    - UI.py：UI


# 需要再做的：
1. 不能夠按q停止judge
2. code偏醜


# Code大略描述
- Start.py:         程式開始的地方
- Controller.py:    控制整個UI
- Directory.py:     放置一整個(一天)的手術的資訊
    * video_file_list - Video_file Class(在File.py裡)的list
    * wb - excel檔案
    * oneday_interrupt_count - 一個手術的總中斷次數
    * write_result_to_excel - 一個手術寫成一個工作表
- File.py:          每一個video file(一天中的一小片段), 一個class
    * interrupt_count - 一個小片段的手術中斷次數
- Utils.py:         放置一些計算用到function
    * opencv_engine class : 取得影片資訊
    * compute.py : 計算時間變化等等...
    * judge class : 偵測中斷時所需function
- UI.py：UI

# 安裝
- conda install openpyxl
- pip install playsound
- 根據此網址更改playsound檔案: https://blog.csdn.net/jasonwu93/article/details/121475106 

# 注意
- 最後注意UI上顯示圖片的路徑