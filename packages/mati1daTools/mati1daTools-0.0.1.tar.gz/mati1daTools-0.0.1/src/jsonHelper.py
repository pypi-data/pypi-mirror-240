
import json
class jsonHelper:


    @staticmethod
    def writeJson(data,filename):
        with open(filename,'w',encoding='utf-8') as file:
            json.dump(data,file,ensure_ascii=False)

    @staticmethod
    def readJson(filename):
        with open(filename,'r',encoding='utf-8') as file:
            meta = json.load(file)
        return meta