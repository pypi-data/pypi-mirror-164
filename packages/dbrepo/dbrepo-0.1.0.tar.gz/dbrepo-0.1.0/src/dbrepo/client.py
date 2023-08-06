import json
import regex as re
import requests as rq
from dbrepo.constants import DBREPO_TEST_INSTANCE
from dbrepo.error import InvalidIdentifier
from dbrepo.query import Query
import pandas as pd


class Container:
    
    def __init__(self, **kwargs) -> None:
        self.dict = kwargs
        self.fetch_meta()

    def fetch_meta(self):
        url = f'{self.endpoint}/container'
        res = rq.get(url, verify=False)




class Client:

    def __init__(self, username : str = None, password : str = None, url : str = DBREPO_TEST_INSTANCE) -> None:
        self.url = url
        self.endpoint = f'{self.url}/api'
        self.__auth(username, password)
        # self.fetch_meta()


    def __auth(self, username : str, password : str) -> None:

        url = f'{self.endpoint}/auth'
        json = { 'username' : username, 'password' : password }

        res = rq.post(url, json=json, verify=False)
        json = res.json()
        self.token = self.__validate_auth_res(json)
        self.token = 'Bearer ' + self.token


    def __validate_auth_res(self, res: dict) -> str:

        if 'error' in res or 'token' not in res:
            if res['status'] == 401:
                raise ValueError('Authentication failed - username or password are wrong')
            else:
                raise ValueError('Authentication failed')

        return res['token']

    # def fetch_meta(self):

    #     url = f'{self.endpoint}/container'
    #     res = rq.get(url, verify=False)
    #     self.container = { c['id'] : Container(**c) for c in res.json()}
    #     {}

    #     # print(pd.DataFrame(res.json()))

    def fetch_database_info(self,cid,dbid) -> dict:

        url = f'{self.endpoint}/container/{cid}/database/{dbid}/table'
        res = rq.get(url, headers=self.__header(), verify=False)
        data = res.json()
        df = pd.DataFrame(data)

        return df

    def generate_table_in_database(self, cid, dbid, name, desc, columns):

        url = f'{self.endpoint}/container/{cid}/database/{dbid}/table'
        body = {
            'name': name,
            'description': desc,
            'columns': columns
        }
        
        rq.post(url, headers=self.__header(), json=body, verify=False)

    def query_by_pid(self, pid) -> Query:

        if isinstance(pid,str) and not pid.isnumeric():
            result = re.search('.*/pid/(.*)', pid)
            if result == None:
                raise InvalidIdentifier(
                    f"Could not resolve pid '{pid}'. Please provide a correct pid like '{self.url}/pid/12345' or '12345'"
                    )
            pid = result.group(1)

        url = f'{self.endpoint}/pid/{pid}'

        res = rq.get(url, headers=self.__header(), verify=False)
        data = res.json()

        return self.query(data['cid'], data['dbid'], data['qid'])


    def query(self, cid: int, dbid: int, qid: int) -> Query:

        url = f'{self.endpoint}/container/{cid}/database/{dbid}/query/{qid}'

        res = rq.put(url, headers=self.__header(), verify=False)
        data = res.json()
        df = pd.DataFrame(data['result'])
        
        return df

    def query_by_statement(self, cid: int, dbid: int, statement : str) -> Query:

        url = f'{self.endpoint}/container/{cid}/database/{dbid}/query'
        json = {'statement' : statement}
        
        res = rq.put(url, headers=self.__header(), json=json, verify=False)
        data = res.json()
        df = pd.DataFrame(data['result'])

        return df

    def __header(self):
        return {'Authorization': self.token}


    def add_data_table(self, cid: int, dbid: int, tid: int, df: pd.DataFrame):

        url = f'{self.endpoint}/container/{cid}/database/{dbid}/table/{tid}/data'
        for index, row in df.iterrows():
            json = {'data': row.to_dict()}   
            res = rq.post(url, headers=self.__header(), json=json, verify=False)

client = Client(username='jtaha',password='pw',url='http://s125.dl.hpc.tuwien.ac.at')
columns = [{
            "name": x,
            "type": y,
            "null_allowed": True,
            "primary_key": False,
            "check_expression": None,
            "foreign_key": None,
            "references": None,
            "unique": False
        } for x,y in zip(['a','b','c'],['number','decimal','string'])]
client.generate_table_in_database(1,1,'test','test_desc',columns=columns)