# -*- coding: utf-8 -*-
"""
Created on Thu April  13 00:47:56 2020

@author: sunny_liu
"""
#清除記憶體:
def clear():
    for key, value in globals().items():
        if callable(value) or value.__class__.__name__ == "module":
            continue
        del globals()[key]
        

# 排除系统内建函数
def __clear_env(): 
     
    for key in globals().keys(): 
        
        if not key.startswith("__"): 
                     
            globals().pop(key) 
 
#========================================================================================================
#模块说明:
#   由于OpenCv中,imread()函数读进来的图片,其本质上就是一个三维的数组,这个NumPy中的三维数组是一致的,所以设置图片的
#   ROI区域的问题,就转换成数组的切片问题,在Python中,数组就是一个列表序列,所以使用列表的切片就可以完成ROI区域的设置
#======================================================================================================

import os                                                                      #導入OS系統模組
import cv2                                                                     #导入OpenCv程序库模組
import numpy as np                                                             #导入python中的数值分析,矩阵运算的程序库模組
import csv                                                                     #導入csv程式庫模組

#=====起始:建立MTF.csv==============================================
def create_csv(MTF_path):
    with open(MTF_path,'w', newline='' ,encoding='utf-8') as f:                 #沒有的話建立MTF.csv在指定路徑MTF_path下
        f.write('#srcImg,UCT,CT,LCT,UC-L,UC-R,LC-L,LC-R\n')                     #寫入文件內文標題
        csv.writer(f)  
        print('進入起始:建立MTF.csv')
    return                                                                      #注意return的階層必須為def次一層,否則不會印出標題

#====功能一:讀取目錄並修改檔名另存資料夾==============================
def read_directory(read_path):                                                  #建立功能一:讀取資料夾路徑並導入参数(此處為放置目標路徑read_path)
    path = 'C:/Users/sunny/Desktop/Jspider/T2/ROI/'                             #创建文件路径
    i = 0                                                                       #設置循環計數器i
    for filename in os.listdir(read_path):                                      #listdir( )這個function會找遍傳進去的路徑底下的所有檔案
        if filename.endswith(".jpg"):                                           #找出自己要的檔案(此處為結尾.bmp的檔案)                         
            print('進入功能一:找到檔案',filename)                                 #找到檔案後通知以確認有讀取到的顯示訊息
            i = i + 1                                                           #讀取檔案計數增加1次
            img = cv2.imread(read_path + '/' + filename)                        #讀取目標圖片絕對路徑下的檔案名稱
            cv2.imwrite('C:/Users/sunny/Desktop/Jspider/T2/IMG' + '/' +'src_Img'+'%d.bmp'%i , img)  #重新序列檔案名稱後寫入新路徑    
            folder_name = path + 'step' + str(i)                                         #重新序列檔案順便建立相應的ROI資料夾
            if not os.path.isdir(folder_name):                                  #檢查是否有相應序號的資料夾
                   os.mkdir(folder_name)                                        #沒有的話則建立資料夾
            print('進入功能一:找建立資料夾step:',i)
        else:                                                                   #如果檢查已經沒有以.bmp結尾的檔案存在則進行以下步驟
            continue                                                            #跳出迴圈
    return                                                                      #回到主程式main() 此處注意return的位置需在for對齊位置


#======功能二:设置ROI擷取区域的宽度高度並存入擷取圖==============================

def scrImg_directory(srcImg_path,roi_path,img_count):
    srcImg = cv2.imread(srcImg_path + '/' + 'src_Img'+'%d.bmp'%img_count)       #打開srcImg_path下的來源圖檔srcImg
    print('打開來源圖檔:' ,'src_Img'+'%d.bmp'%img_count)              
    h,w = (20,40)                                                               #設置ROI高寬
    x=[860 ,870 ,883 ,160 ,1660 ,350 ,1450]                                     #設置UCT,CT,LCT,UC_L,UC_R,LC_L,LC_R的ROI座標
    y=[380 ,745 ,1030 ,390 ,380 ,1010 ,1030]

    j = 0                         
    for j in range(len(x)):                                                     #產生ROI座標的截圖
        img_roi = srcImg[y[j]:y[j]+h ,x[j]:x[j]+w] 
        cv2.imwrite(roi_path + '/' + 'img_roi'+'%d.bmp'%j ,img_roi)
        print('進入功能二:存入分析圖:','img_roi'+'%d.bmp'%j)    
        j=j+1
     
    return img_roi
 
    
#=======功能三:計算MTF==========================================================
 
def MTF_cal(roi_path ,img_count):
    MTF_row = []
    h = 0
    for gray_img in os.listdir(roi_path): 
        gray_img = roi_path + '/' + 'img_roi'+'%d.bmp'%h       
        gray1 = cv2.imread(gray_img ,cv2.IMREAD_GRAYSCALE)                      #將讀入的ROI截圖依序改成灰度图
        print('進入功能三:讀入ROI目標圖片',gray_img)
        h = h + 1
        cv2.namedWindow('img_roi' ,cv2.WINDOW_AUTOSIZE)                         # 窗口大小可以改变
        cv2.imshow('img_roi' ,gray1)   
        cv2.waitKey(50)   # 0代表一直等待按下空白鍵才關閉所有視窗，括号里的数字代表等待多长时间(单位ms)
        cv2.destroyAllWindows()  # 关闭所有的窗口 
        
        g1 = np.mean(gray1)                            #取灰度圖1的平均值
        g1_size = np.size(gray1)                       #計算灰階圖的總像素
        #g1_shape=np.shape(gray1)                      #計算灰階圖的維度
        gray1_rsp=gray1.reshape(1,g1_size)             #將灰度圖矩陣整形成一列n行的矩陣(n=總像素)
        g1_white=gray1_rsp.copy()                      #複製整形後的灰度圖1準備計算白色區域
        g1_white[g1_white < g1]=0                      #將複製的灰度圖白區灰階值小於平均的元素都設定為0         
        g1_w_a= np.array(g1_white)                     #去除灰階塗白區的0元素
        g1_w_b = np.array([0])                         #挑出矩陣有0值得索引值
        g1_w_c = np.setdiff1d(g1_w_a,g1_w_b)           #將矩陣重新去掉0值後重新排列成一維矩陣
        g1_w=np.mean(g1_w_c)                           #取白區平均值
        g1_black=gray1_rsp.copy()                      #複製整形後的灰度圖1準備計算黑色區域
        g1_black[g1_black > g1]=0                      #將複製的灰度圖白區灰階值小於平均的元素都設定為0                 
        g1_b_a= np.array(g1_black)                     #去除灰階塗白區的0元素
        g1_b_b = np.array([0])
        g1_b_c = np.setdiff1d(g1_b_a,g1_b_b)
        g1_b=np.mean(g1_b_c)                           #取白區平均值
        g1_MTF=(g1_w-g1_b)/(g1_w+g1_b)                 #計算UCT的MTF  
        MTF_data=format(g1_MTF, '0.3f')                     #取小數點下三位數        
        MTF_row.append(MTF_data)
    print ('得值MTF:',MTF_row)
    MTF_row.insert(0, img_count)
    print ("增加一行索引值 : ", MTF_row)
    return MTF_row 
  
#=========功能四:寫入MTF數據於MTF.csv文件中==============
def write_file(MTF_path ,MTF_file ,img_count):
    datas = MTF_file
    with open('C:/Users/sunny/Desktop/Jspider/T2/MTF.csv', 'a', newline='') as csvfile:
        writer  = csv.writer(csvfile)
        for row in datas:
            writer.writerow(row)
    
     
#===主程式=======================

      
def main():
    
    #read_Img =[]                                                               #把資料內的檔名建立清待
    #count_read = 0                                                             #建立計數器
    read_path = 'C:/Users/sunny/Desktop/Jspider/T2'                             #读取目標圖文件夹的绝对路径（不能有中文名称）
    MTF_path = 'C:/Users/sunny/Desktop/Jspider/T2/MTF.csv'                      #預設MTF.csv資料文件路徑
    if os.path.isfile(MTF_path):                                                #檢查模組下的路徑是否有MTF.csv檔案存在
        print('找到檔案:MTF.csv')                                                #有的話列印出檔案名稱
    else:                                                                       #沒有的話進入起始功能:確認並建立MTF.csv
        create_csv(MTF_path)
       
    read_directory(read_path)                                                   #進入功能一:讀取目錄並重新序列檔名另存於新路徑
    srcImg_path = 'C:/Users/sunny/Desktop/Jspider/T2/IMG'                       #序列檔名後的图片資料夾路徑
    path = 'C:/Users/sunny/Desktop/Jspider/T2/ROI/'                             #创建文件路径
    num = len([name for name in os.listdir(srcImg_path) if os.path.isfile(os.path.join(srcImg_path, name))]) #統計srcImg_path資料夾下的檔案數量 
                                                                                #如統計資料夾數量，用 os.path.isdir(path)做判斷語句。                                         
    MTF_file = []
    s = 0
    for s in range(num) :                                                      #以scrImg檔案數量來決定要建立幾個ROI存檔的資料夾數(目前10~14個取樣步數)
        img_count = s + 1
        s = s + 1
        roi_path = path + 'step' + str(s)                                                #将擷取後的ROI區域圖片加载到指定路徑内存
        print ('打開路徑:' + roi_path)                                           #印出讀取的ROI資料夾序號確認存在
        scrImg_directory(srcImg_path ,roi_path ,img_count)                      #進入功能二:设置ROI擷取区域的宽度高度並存入擷取圖                                                                                                              
        MTF=MTF_cal(roi_path ,img_count)
        MTF_file.append(MTF)                                                   #進入功能三:計算每一張圖片的七個MTF數據   
    write_file(MTF_path ,MTF_file ,img_count)
main()