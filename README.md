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
1. UI：看能不能好幾個video file同時測
2. 匯入excel的資料還沒改（分成兩部分：known & unknown）$
3. 最後美觀再說
@