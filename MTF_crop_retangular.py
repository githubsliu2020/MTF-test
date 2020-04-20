# -*- coding: utf-8 -*-
"""Created on Sun Feb  2 11:19:39 2020
@author: sliu10
"""
#coding = utf-8
#======================================================================================================
#文件说明:
#使用OpenCv——python设置图像的ROI区域
#======================================================================================================

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
#       由于OpenCv中,imread()函数读进来的图片,其本质上就是一个三维的数组,这个NumPy中的三维数组是一致的,所以设置图片的
#   ROI区域的问题,就转换成数组的切片问题,在Python中,数组就是一个列表序列,所以使用列表的切片就可以完成ROI区域的设置
#======================================================================================================
import os                                         #導入OS系統模組
import numpy as np                                #导入python中的数值分析,矩阵运算的程序库模組
import cv2                                        #导入OpenCv程序库模組
        
#===讀取檔案=====
def read_file(filename) :
    srcImg = cv2.imread(filename)                         #将图片加载到内存    
    #cv2.namedWindow("[srcImg]",cv2.WINDOW_AUTOSIZE)            #创建显示窗口


# ====设置ROI区域的高度========================================
def ROI_size()
    h = 20                          
    w = 40 
    #===== UCT,CT,LCT,UC_L,UC_R,LC_L,LC_R======

    #Celestia  x1=830 x2=860 x3=860 x4=100 x5=1800 x6=310 x7=1560  y1=370 y2=680 y3=880 y4=350 y5=330 y6=820 y7=830
    #Kaptivo x1=1010 x2=980 x3=970 x4=300 x5=1710 x6=470 x7=1470 y1=290 y2=550 y3=700 y4=300 y5=280 y6=685 7=710
    #Celestia dewarp 
    x1=840 
    x2=850 
    x3=850 
    x4=130 
    x5=1660 
    x6=330
    x7=1450 

    y1=320 
    y2=560 
    y3=760 
    y4=320 
    y5=310 
    y6=760 
    y7=780

#======设置ROI擷取区域的宽度======================================

def img_roi()
    for i in range(len(x)):


    img_roi1        = srcImg[y1:y1+h,x1:x1+w] 
    cv2.imwrite('img/11_1080P_1.bmp',img_roi1)
      

    img_roi2        = srcImg[y2:y2+h,x2:x2+w] 
    cv2.imwrite('img/11_1080P_2.bmp',img_roi2)


    img_roi3        = srcImg[y3:y3+h,x3:x3+w] 
    cv2.imwrite('img/11_1080P_3.bmp',img_roi3)


    img_roi4        = srcImg[y4:y4+h,x4:x4+w] 
    cv2.imwrite('img/11_1080P_4.bmp',img_roi4)


    img_roi5        = srcImg[y5:y5+h,x5:x5+w] 
    cv2.imwrite('img/11_1080P_5.bmp',img_roi5)


    img_roi6        = srcImg[y6:y6+h,x6:x6+w] 
    cv2.imwrite('img/11_1080P_6.bmp',img_roi6)


    img_roi7        = srcImg[y7:y7+h,x7:x7+w] 
    cv2.imwrite('img/11_1080P_7.bmp',img_roi7)


#====== #計算MTF=================================================
# gray[i] = cv2.imread('img/11_1080P_'+str(i)+'.bmp',cv2.IMREAD_GRAYSCALE) #轉成灰階圖
# cv2.imshow('MTF_'+str(i),gray[i])
# gray_avg[i]=np.mean(gray[i])   #取灰階圖的平均值
# gray_white[i]=gray[i].copy()   #複製灰階圖矩陣
# gray_white[gray_white[i] <gray_avg[i]]=0  #將複製的灰階矩陣中小於平均值的元素設為0

def MTF():
    gray1 = cv2.imread("img/11_1080P_1.bmp",cv2.IMREAD_GRAYSCALE) #灰度图
    gray2 = cv2.imread("img/11_1080P_2.bmp",cv2.IMREAD_GRAYSCALE) #灰度图
    gray3 = cv2.imread("img/11_1080P_3.bmp",cv2.IMREAD_GRAYSCALE) #灰度图
    gray4 = cv2.imread("img/11_1080P_4.bmp",cv2.IMREAD_GRAYSCALE) #灰度图
    gray5 = cv2.imread("img/11_1080P_5.bmp",cv2.IMREAD_GRAYSCALE) #灰度图
    gray6 = cv2.imread("img/11_1080P_6.bmp",cv2.IMREAD_GRAYSCALE) #灰度图
    gray7 = cv2.imread("img/11_1080P_7.bmp",cv2.IMREAD_GRAYSCALE) #灰度图


    #====================UCT=========================================================================
    cv2.imshow('MTF_1',gray1)
    g1=np.mean(gray1)                             #取灰度圖1的平均值
    g1_size=np.size(gray1)                        #計算灰階圖的總像素
    #g1_shape=np.shape(gray1)                     #計算灰階圖的維度
    gray1_rsp=gray1.reshape(1,g1_size)            #將灰度圖矩陣整形成一列n行的矩陣(n=總像素)
    g1_white=gray1_rsp.copy()                    #複製整形後的灰度圖1準備計算白色區域
    g1_white[g1_white < g1]=0                     #將複製的灰度圖白區灰階值小於平均的元素都設定為0         
    #g1_white[g1_white < 156]=0              
    g1_w_a= np.array(g1_white)                       #去除灰塗白區的0元素
    g1_w_b = np.array([0])
    g1_w_c = np.setdiff1d(g1_w_a,g1_w_b)
    g1_w=np.mean(g1_w_c)                           #取白區平均值

    g1_black=gray1_rsp.copy()                    #複製整形後的灰度圖1準備計算黑色區域
    g1_black[g1_black > g1]=0                     #將複製的灰度圖白區灰階值小於平均的元素都設定為0  
    #g1_black[g1_black > 100]=0                  
    g1_b_a= np.array(g1_black)                       #去除灰塗白區的0元素
    g1_b_b = np.array([0])
    g1_b_c = np.setdiff1d(g1_b_a,g1_b_b)
    g1_b=np.mean(g1_b_c)                           #取白區平均值
    g1_MTF=(g1_w-g1_b)/(g1_w+g1_b)                 #計算UCT的MTF
    UCT=format(g1_MTF, '0.2f')

    #====================CT=========================================================================
    cv2.imshow('MTF_2',gray2)
    g2=np.mean(gray2)                             #取灰度圖1的平均值
    g2_size=np.size(gray2)                        #計算灰階圖的總像素
    #g1_shape=np.shape(gray1)                     #計算灰階圖的維度
    gray2_rsp=gray2.reshape(1,g2_size)            #將灰度圖矩陣整形成一列n行的矩陣(n=總像素)
    g2_white=gray2_rsp.copy()                    #複製整形後的灰度圖1準備計算白色區域
    g2_white[g2_white < g2]=0                     #將複製的灰度圖白區灰階值小於平均的元素都設定為0         
    #g2_white[g2_white < 156]=0              
    g2_w_a= np.array(g2_white)                       #去除灰塗白區的0元素
    g2_w_b = np.array([0])
    g2_w_c = np.setdiff1d(g2_w_a,g2_w_b)
    g2_w=np.mean(g2_w_c)                           #取白區平均值

    g2_black=gray2_rsp.copy()                    #複製整形後的灰度圖1準備計算黑色區域
    g2_black[g2_black > g2]=0                     #將複製的灰度圖白區灰階值小於平均的元素都設定為0  
    #g2_black[g2_black > 100]=0                  
    g2_b_a= np.array(g2_black)                       #去除灰塗白區的0元素
    g2_b_b = np.array([0])
    g2_b_c = np.setdiff1d(g2_b_a,g2_b_b)
    g2_b=np.mean(g2_b_c)                           #取白區平均值
    g2_MTF=(g2_w-g2_b)/(g2_w+g2_b)                 #計算CT的MTF
    CT=format(g2_MTF, '0.2f')

    #====================LCT=========================================================================
    cv2.imshow('MTF_3',gray3)
    g3=np.mean(gray3)                             #取灰度圖1的平均值
    g3_size=np.size(gray3)                        #計算灰階圖的總像素
    #g1_shape=np.shape(gray1)                     #計算灰階圖的維度
    gray3_rsp=gray3.reshape(1,g3_size)            #將灰度圖矩陣整形成一列n行的矩陣(n=總像素)
    g3_white=gray3_rsp.copy()                    #複製整形後的灰度圖1準備計算白色區域
    g3_white[g3_white < g3]=0                     #將複製的灰度圖白區灰階值小於平均的元素都設定為0         
    #g3_white[g3_white < 156]=0              
    g3_w_a= np.array(g3_white)                       #去除灰塗白區的0元素
    g3_w_b = np.array([0])
    g3_w_c = np.setdiff1d(g3_w_a,g3_w_b)
    g3_w=np.mean(g3_w_c)                           #取白區平均值

    g3_black=gray3_rsp.copy()                    #複製整形後的灰度圖1準備計算黑色區域
    g3_black[g3_black > g3]=0                     #將複製的灰度圖白區灰階值小於平均的元素都設定為0  
    #g3_black[g3_black > 100]=0                  
    g3_b_a= np.array(g3_black)                       #去除灰塗白區的0元素
    g3_b_b = np.array([0])
    g3_b_c = np.setdiff1d(g3_b_a,g3_b_b)
    g3_b=np.mean(g3_b_c)                           #取白區平均值
    g3_MTF=(g3_w-g3_b)/(g3_w+g3_b)                 #計算LCT的MTF
    LCT=format(g3_MTF, '0.2f')

    #====================UC_L=========================================================================
    cv2.imshow('MTF_4',gray4)
    g4=np.mean(gray4)                             #取灰度圖1的平均值
    g4_size=np.size(gray4)                        #計算灰階圖的總像素
    #g1_shape=np.shape(gray1)                     #計算灰階圖的維度
    gray4_rsp=gray4.reshape(1,g4_size)            #將灰度圖矩陣整形成一列n行的矩陣(n=總像素)
    g4_white=gray4_rsp.copy()                    #複製整形後的灰度圖1準備計算白色區域
    g4_white[g4_white < g4]=0                     #將複製的灰度圖白區灰階值小於平均的元素都設定為0         
    #g4_white[g4_white < 156]=0              
    g4_w_a= np.array(g1_white)                       #去除灰塗白區的0元素
    g4_w_b = np.array([0])
    g4_w_c = np.setdiff1d(g4_w_a,g4_w_b)
    g4_w=np.mean(g4_w_c)                           #取白區平均值

    g4_black=gray4_rsp.copy()                    #複製整形後的灰度圖1準備計算黑色區域
    g4_black[g4_black > g4]=0                     #將複製的灰度圖白區灰階值小於平均的元素都設定為0  
    #g4_black[g4_black > 100]=0                  
    g4_b_a= np.array(g4_black)                       #去除灰塗白區的0元素
    g4_b_b = np.array([0])
    g4_b_c = np.setdiff1d(g4_b_a,g4_b_b)
    g4_b=np.mean(g4_b_c)                           #取白區平均值
    g4_MTF=(g4_w-g4_b)/(g4_w+g4_b)                 #計算UC_l的MTF
    UC_L=format(g4_MTF, '0.2f')

    #====================UC_R=========================================================================
    cv2.imshow('MTF_5',gray5)
    g5=np.mean(gray5)                             #取灰度圖1的平均值
    g5_size=np.size(gray5)                        #計算灰階圖的總像素
    #g1_shape=np.shape(gray1)                     #計算灰階圖的維度
    gray5_rsp=gray5.reshape(1,g5_size)            #將灰度圖矩陣整形成一列n行的矩陣(n=總像素)
    g5_white=gray5_rsp.copy()                    #複製整形後的灰度圖1準備計算白色區域
    g5_white[g5_white < g5]=0                     #將複製的灰度圖白區灰階值小於平均的元素都設定為0         
    #g5_white[g5_white < 156]=0              
    g5_w_a= np.array(g5_white)                       #去除灰塗白區的0元素
    g5_w_b = np.array([0])
    g5_w_c = np.setdiff1d(g5_w_a,g5_w_b)
    g5_w=np.mean(g5_w_c)                           #取白區平均值

    g5_black=gray5_rsp.copy()                    #複製整形後的灰度圖1準備計算黑色區域
    g5_black[g5_black > g5]=0                     #將複製的灰度圖白區灰階值小於平均的元素都設定為0  
    #g5_black[g5_black > 100]=0                  
    g5_b_a= np.array(g5_black)                       #去除灰塗白區的0元素
    g5_b_b = np.array([0])
    g5_b_c = np.setdiff1d(g5_b_a,g5_b_b)
    g5_b=np.mean(g5_b_c)                           #取白區平均值
    g5_MTF=(g5_w-g5_b)/(g5_w+g5_b)                 #計算UC_l的MTF
    UC_R=format(g5_MTF, '0.2f')

    #====================LC_L=========================================================================
    cv2.imshow('MTF_6',gray6)
    g6=np.mean(gray6)                             #取灰度圖1的平均值
    g6_size=np.size(gray6)                        #計算灰階圖的總像素
    #g1_shape=np.shape(gray1)                     #計算灰階圖的維度
    gray6_rsp=gray6.reshape(1,g6_size)            #將灰度圖矩陣整形成一列n行的矩陣(n=總像素)
    g6_white=gray6_rsp.copy()                    #複製整形後的灰度圖1準備計算白色區域
    g6_white[g6_white < g6]=0                     #將複製的灰度圖白區灰階值小於平均的元素都設定為0         
    #g6_white[g6_white < 156]=0              
    g6_w_a= np.array(g6_white)                       #去除灰塗白區的0元素
    g6_w_b = np.array([0])
    g6_w_c = np.setdiff1d(g6_w_a,g6_w_b)
    g6_w=np.mean(g6_w_c)                           #取白區平均值

    g6_black=gray6_rsp.copy()                    #複製整形後的灰度圖1準備計算黑色區域
    g6_black[g6_black > g6]=0                     #將複製的灰度圖白區灰階值小於平均的元素都設定為0  
    #g6_black[g6_black > 100]=0                  
    g6_b_a= np.array(g6_black)                       #去除灰塗白區的0元素
    g6_b_b = np.array([0])
    g6_b_c = np.setdiff1d(g6_b_a,g6_b_b)
    g6_b=np.mean(g6_b_c)                           #取白區平均值
    g6_MTF=(g6_w-g6_b)/(g6_w+g6_b)                 #計算UC_l的MTF
    LC_L=format(g6_MTF, '0.2f')

    #====================LC_R=========================================================================
    cv2.imshow('MTF_7',gray7)
    g7=np.mean(gray7)                             #取灰度圖1的平均值
    g7_size=np.size(gray7)                        #計算灰階圖的總像素
    #g1_shape=np.shape(gray1)                     #計算灰階圖的維度
    gray7_rsp=gray7.reshape(1,g7_size)            #將灰度圖矩陣整形成一列n行的矩陣(n=總像素)
    g7_white=gray7_rsp.copy()                    #複製整形後的灰度圖1準備計算白色區域
    g7_white[g7_white < g7]=0                     #將複製的灰度圖白區灰階值小於平均的元素都設定為0         
    #g7_white[g7_white < 156]=0              
    g7_w_a= np.array(g7_white)                       #去除灰塗白區的0元素
    g7_w_b = np.array([0])
    g7_w_c = np.setdiff1d(g7_w_a,g7_w_b)
    g7_w=np.mean(g7_w_c)                           #取白區平均值

    g7_black=gray7_rsp.copy()                    #複製整形後的灰度圖1準備計算黑色區域
    g7_black[g7_black > g7]=0                     #將複製的灰度圖白區灰階值小於平均的元素都設定為0  
    #g7_black[g7_black > 100]=0                  
    g7_b_a= np.array(g7_black)                       #去除灰塗白區的0元素
    g7_b_b = np.array([0])
    g7_b_c = np.setdiff1d(g7_b_a,g7_b_b)
    g7_b=np.mean(g7_b_c)                           #取白區平均值
    g7_MTF=(g7_w-g7_b)/(g7_w+g7_b)                 #計算UC_l的MTF
    LC_R=format(g7_MTF, '0.2f')

    print(g1_MTF)
    print(g2_MTF)
    print(g3_MTF)
    print(g4_MTF)
    print(g5_MTF)
    print(g6_MTF)
    print(g7_MTF)

#=======设置ROI顯示区域的大小======================================

def ROI_display():
    cv2.rectangle(srcImg, (x1,y1), (x1+w,y1+h), (0, 0, 255), 2)   # srcImg => 图片数据; #(x,y) => (最左,最上) 是个tuple;# (x+w,y+h) => [最右,最下] 是个tuple;# (0, 0, 255) => rgb 颜色; # 3 => 粗细程度
    cv2.rectangle(srcImg, (x2,y2), (x2+w,y2+h), (0, 0, 255), 2)
    cv2.rectangle(srcImg, (x3,y3), (x3+w,y3+h), (0, 0, 255), 2)
    cv2.rectangle(srcImg, (x4,y4), (x4+w,y4+h), (0, 0, 255), 2)
    cv2.rectangle(srcImg, (x5,y5), (x5+w,y5+h), (0, 0, 255), 2)
    cv2.rectangle(srcImg, (x6,y6), (x6+w,y6+h), (0, 0, 255), 2)
    cv2.rectangle(srcImg, (x7,y7), (x7+w,y7+h), (0, 0, 255), 2)
    # 'MTF_CT' => 需要显示的信息;
    # (x, y) => 给定一个元组 里面给定点坐标 x, y; 
    # cv2.FONT_HERSHEY_COMPLEX_SMALL => 模式;
    # 0.8 => 字体粗细; 
    # (0, 0, 255) => rgb 颜色;
    cv2.putText(srcImg, 'MTF_UCT='+str(UCT), (x1,y1+40), cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.8, (0, 255, 255))
    cv2.putText(srcImg, 'MTF_CT='+str(CT), (x2,y2+40), cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.8, (0, 255, 255))
    cv2.putText(srcImg, 'MTF_LCT='+str(LCT), (x3,y3+40), cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.8, (0, 255, 255))
    cv2.putText(srcImg, 'MTF_UC_L='+str(UC_L), (x4,y4+40), cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.8, (0, 255, 255))
    cv2.putText(srcImg, 'MTF_UC_R='+str(UC_R), (x5-100,y5+50), cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.8, (0, 255, 255))
    cv2.putText(srcImg, 'MTF_LC_L='+str(LC_L), (x6,y6+40), cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.8, (0, 255, 255))
    cv2.putText(srcImg, 'MTF_LC_R='+str(LC_R), (x7-100,y7+40), cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.8, (0, 255, 255))

# target_path => 保存路径
# img => 图片数据
path="img/11_1080P_0.bmp"
ss=cv2.imwrite(path, srcImg)
MTF_Im = cv2.imread("img/11_1080P_0.bmp", cv2.IMREAD_COLOR)
#cv.NamedWindow("MTF", cv.CV_WINDOW_AUTOSIZE)
#cv2.namedWindow(imgpath, 0);

MTF_Im = cv2.imread("img/11_1080P_0.bmp", cv2.IMREAD_COLOR)
MTF_Im = cv2.resize(MTF_Im, (1920, 1080))
cv2.namedWindow('MTF_ALL', cv2.WINDOW_NORMAL)    # 窗口大小可以改变
# cv2.namedWindow('result', cv2.WINDOW_AUTOSIZE)    # 窗口大小不可以改变
# cv2.namedWindow('result', cv2.WINDOW_FREERATIO)   # 窗口大小自适应比例
# cv2.namedWindow('result', cv2.WINDOW_KEEPRATIO)   # 窗口大小保持比例
# cv2.namedWindow('result', cv2.WINDOW_GUI_EXPANDED)    # 显示色彩变成暗色 ps.这个我没看出来有啥用。
cv2.imshow('MTF_ALL', MTF_Im)

# 按下空白鍵關閉所有視窗
cv2.waitKey(0)
# 关闭所有的窗口 
cv2.destroyAllWindows()

def main()
    filename ="img/11_1080P.bmp"
