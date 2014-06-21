'''
Created on 2014-6-19
@author: Administrator
'''
import cv2.cv as cv
import tesseract
import os;
appContent = {'imagevalidateerror':1, 'requesterror':2, 'neterror':3, 'apperror':4}

def getImageText(path="validateimage/imageValidate"):
    try:
        api = tesseract.TessBaseAPI()
        api.Init(".","eng",tesseract.OEM_DEFAULT)
        image= cv.LoadImage(path, cv.CV_LOAD_IMAGE_GRAYSCALE);
        tesseract.SetCvImage(image,api)
        text=api.GetUTF8Text();
        return text;
    except Exception, e:
        print e;
        return '';
def getImageTextBuff(buff):
    try:
        imagefiledata = cv.CreateMatHeader(1, len(buff), cv.CV_8UC1)
        cv.SetData(imagefiledata, buff, len(buff))
        src = cv.DecodeImage(imagefiledata, cv.CV_LOAD_IMAGE_COLOR)
        api = tesseract.TessBaseAPI()
        api.Init(".","eng",tesseract.OEM_DEFAULT)
        tesseract.SetCvImage(src,api);
        text=api.GetUTF8Text();
        return text;
    except Exception, e:
        print e;
        return '';

def saveImageFile(buff, savePath, filename):
    file = None;
    try:
        if not savePath.endswith(os.sep):
            savePath += os.sep;
        if not os.path.exists(savePath):
            os.mkdir(savePath);
        fullfilname = savePath + filename
        if os.path.isfile(fullfilname):
            os.remove(fullfilname)
        file = open(fullfilname, "wb");
        file.write(buff);
        return True;
    except Exception, e:
        print e;
        return False
    finally:
        if file:
            file.close();

#print getImageText();