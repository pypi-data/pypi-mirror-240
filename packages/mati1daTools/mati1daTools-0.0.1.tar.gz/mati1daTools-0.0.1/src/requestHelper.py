import requests
import time


def requestSend(url,method = 'GET',data=None,json_data = None,header = None):
    try:
        if method == 'GET':
            response = requests.get(url, headers=header)
        elif method == 'POST':
            response = requests.post(url, data=data, json=json_data, headers=header)
        elif method == 'PUT':
            response = requests.put(url, data=data, json=json_data, headers=header)
        elif method =="GET_FILE":
            response = requests.get(url, headers=header)
            if str(response.status_code)=="200":
                return response
        else:
            raise ValueError("Unsupported HTTP method:不支持的请求方式")
        
        if str(response.status_code) =="200":
            response_json = response.json()
            if str(response_json['code'])=="0":
                return response_json['data']
            else:
                print("code:{},data:{},msg:{}".format(response_json['code'],response_json['data'],response_json['msg']))
                return False
        else:
            print("接口返回代码异常：{}".format(response.status_code))
            return False
        
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None
    

def internship_requestSend(url,method = 'GET',data=None,json_data = None,header = None):
    time.sleep(1)
    try:
        if method == 'GET':
            response = requests.get(url, headers=header)
        elif method == 'POST':
            response = requests.post(url, data=data, json=json_data, headers=header)
        elif method == 'PUT':
            response = requests.put(url, data=data, json=json_data, headers=header)
        elif method =="GET_FILE":
            response = requests.get(url, headers=header)
            if str(response.status_code)=="200":
                 return response_json['data']
        else:
            raise ValueError("Unsupported HTTP method:不支持的请求方式")
        
        if str(response.status_code) =="200":
            response_json = response.json()
            if str(response_json['code'])=="200":
                return response_json['data']
            else:
                print(response_json['error_code'])
                return False
        else:
            print("接口返回代码异常：{}".format(response.status_code))
            print(response)
            return False
        
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None
    