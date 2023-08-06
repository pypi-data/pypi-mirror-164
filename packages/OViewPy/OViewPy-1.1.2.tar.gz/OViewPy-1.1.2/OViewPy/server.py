import string
import requests
import threading
import time

from numpy import number
from progress.spinner import Spinner
from OViewPy.varstruct import VarStruct


class Server:
    def __init__(self, url) -> None:
        self.__serverURL = url
        self.__wmtsURL = url + "/wmts?"
        self.__wmsURL = url + "/wms?"
        self.__docmdURL = url + "/DoCmd?cmd="
        header = {
            "Content-Type": "application/json"
        }
        response = requests.get(
            url=self.__docmdURL + "GetServerInfo",
            headers=header,
            timeout=100000
        )
        if response.status_code == 200:
            jsonStr = response.json()
            self.__version = jsonStr["FullVersion"]
        else:
            self.__version = None

    @property
    def version(self) -> string:
        return self.__version

    @property
    def wmsURL(self) -> string:
        return self.__wmsURL

    @property
    def wmtsURL(self) -> string:
        return self.__wmtsURL

    @property
    def docmdURL(self) -> string:
        return self.__docmdURL

    @property
    def serverURL(self) -> string:
        return self.__serverURL

    def DoCommand(self, command: string, parm: VarStruct, ret: VarStruct, timeOut=100000) -> bool:
        header = {
            "Content-Type": "application/json"
        }
        if(parm != None):
            data = parm.ToJson()
        else:
            data = ""
        url = self.__docmdURL + command
        response = requests.post(
            url=url, headers=header, data=data, timeout=timeOut)
        if response.status_code == 200:
            jsonStr = response.text
            ret.FromJson(jsonStr)
            return True
        else:
            jsonStr = response.text
            print(jsonStr)
            raise SystemError('Server Error')

    def getLayerList(self):
        parm = VarStruct()
        ret = VarStruct()
        self.DoCommand(command="GetAll2DLayerInfo", parm=parm, ret=ret)
        retDict = ret.ToDict()
        if retDict["success"]:
            return retDict["ret"]
        else:
            return retDict

    def getOViewLayerList(self):
        parm = VarStruct()
        ret = VarStruct()
        self.DoCommand(command="GetAll3DLayerInfo", parm=parm, ret=ret)
        retDict = ret.ToDict()
        if retDict["success"]:
            return retDict["ret"]
        else:
            return retDict

    def deleteLayer(self, layerName: string = None):
        if layerName == None:
            return False
        parm = VarStruct()
        ret = VarStruct()
        parm.Set("layername", layerName)
        self.DoCommand(command="Delete2DLayer", parm=parm, ret=ret)
        retDict = ret.ToDict()
        if retDict["success"]:
            return True
        else:
            return False

    def deleteOViewLayer(self, layerName: string = None):
        if layerName == None:
            return False
        parm = VarStruct()
        ret = VarStruct()
        parm.Set("layername", layerName)
        self.DoCommand(command="Delete3DLayer", parm=parm, ret=ret)
        retDict = ret.ToDict()
        if retDict["success"]:
            return True
        else:
            return False

    def saveImageToServer(self, imageFilePath: string, layerName: string, epsg: int = 4326):
        parm = VarStruct()
        parm.Set("imageFilePath", imageFilePath)
        parm.Set("outputFilePath", imageFilePath + ".tif")
        parm.Set("layerName", layerName)
        parm.Set("epsg", epsg)
        ret = VarStruct()
        spinner = Spinner('Loading ')
        docmdThread = threading.Thread(
            target=self.DoCommand, args=("Image2RasterLayer", parm, ret,))
        docmdThread.start()

        def loadingAnimate():
            while docmdThread.is_alive():
                time.sleep(0.1)
                spinner.next()
            spinner.finish()
        t = threading.Thread(target=loadingAnimate)
        t.start()
        docmdThread.join()
        print("Done！")
        return

    def saveVectorFileToServer(self, VectorFilePath: string, layerName: string, epsg: number = 4326):
        parm = VarStruct()
        parm.Set("sourceUrl", VectorFilePath)
        parm.Set("layerName", layerName)
        parm.Set("epsg", epsg)
        ret = VarStruct()
        spinner = Spinner('Loading ')
        docmdThread = threading.Thread(
            target=self.DoCommand, args=("VectorFile2VectorrLayer", parm, ret,))
        docmdThread.start()

        def loadingAnimate():
            while docmdThread.is_alive():
                time.sleep(0.1)
                spinner.next()
            spinner.finish()
        t = threading.Thread(target=loadingAnimate)
        t.start()
        docmdThread.join()
        print("Done！")
        return
