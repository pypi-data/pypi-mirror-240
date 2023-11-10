# -*- coding: UTF-8 -*-
# pip install opencv-python
import pyuc
from pyuc.py_api_b import PyApiB
from PIL import Image,ImageFilter
from pyuc.py_recg.imgU import ImgU
import os
if PyApiB.tryImportModule("aircv", installName="aircv"):
    import aircv as ac
if PyApiB.tryImportModule("cv2", installName="opencv-python"):
    import cv2
if PyApiB.tryImportModule("pytesseract", installName="pytesseract"):
    import pytesseract 
    # https://digi.bib.uni-mannheim.de/tesseract/tesseract-ocr-w64-setup-5.3.3.20231005.exe
    # tesseract --list-langs 
    # 训练下载：https://github.com/nguyenq/jTessBoxEditor/releases/tag/


class TesseractU(PyApiB):
    """
    文字识别相关工具
    """
    @staticmethod
    def produce(key=None):
        return PyApiB._produce(key, __class__)

    def image_to_num(self,imgU:ImgU, lang="eng", config="--psm 7 -c tessedit_char_whitelist=0123456789."):
        return pytesseract.image_to_string(imgU.getPilImg(),lang=lang,config=config)

    def image_to_num_by_folder(self, imgU:ImgU, folderPath:str):
        """ 单行 """
        # https://zhuanlan.zhihu.com/p/365202405
        files = os.listdir(folderPath)
        charH, charW = 10, 6
        # print(files)
        temps = {}
        for ff in files:
            temps[ff[:-4]] = cv2.resize(cv2.imread(f'{folderPath}/{ff}', cv2.IMREAD_GRAYSCALE),(charW, charH))
        # charH, charW = list(temps.values())[0].shape
        # charH, charW = 10, 6
        # print(charW, charH)

        contours = cv2.findContours(imgU.getNpImg(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)[0]
        result = []
        
        for cnt in contours:
            [x,y,w,h] = cv2.boundingRect(cnt)
            # 按照高度筛选
            if charH+6 > h > charH-3:
                result.append([x,y,w,h])

        result.sort(key=lambda x:x[0])
        if len(result) == 0:
            return ""
        # print(result)
        # 过滤和添加可能为空格或小数点的方格
        # result = [[3, 2, 5, 10], [9, 2, 6, 9], [16, 2, 6, 9], [23, 2, 6, 9],[29, 2, 6, 9], [35, 2, 6, 10]]
        newResult = [result[0]]
        for iii in range(1,len(result)):
            if result[iii][0]-result[iii-1][0] < charW>>1:
                # 矩离太近了不要了
                pass
            elif result[iii][0]-result[iii-1][0] < charW+(charW>>1):
                newResult.append(result[iii])
            else:
                # 超距离了，应该是个.
                newResult.append([0,0,0,0])
                newResult.append(result[iii])
        result = newResult

        tttt = ""
        zzz = 0
        for x, y, w, h in result:    
            if x==0 and y==0 and w==0 and h==0:
                tttt += "."
                continue
            digit = cv2.resize(imgU.getNpImg()[y:y+h, x:x+w], (charW, charH))
            
            zzz+=1
            res = []
            for key in temps:
                # TODO 改为计算相同的数量比
                res.append((key, self.sim(digit, temps[key])))
            res.sort(key=lambda x:x[1])
            # print(res)
            # print(str(f"{res[-1][0]}"))
            tttt+=str(f"{res[-1][0]}")
        # print(tttt)
        if tttt.count(".")>1:
            return tttt[:-2].replace(".","") + tttt[-2:]
        return tttt
    

    def sim(self, src1, src2):
        score = cv2.matchTemplate(src1, src2, cv2.TM_CCORR_NORMED)
        return score[0]

