# # Декораторы
#
# from datetime import datetime
#
# def time_it(name):
#     print('Name:', name)
#     def outer(function):
#         def inner(*args):
#              start = datetime.now()
#              result = function(*args)
#              print(datetime.now() - start)
#              return result
#         return inner
#     return outer
#
# @time_it('generator_1')
# def generator_1(num):
#     lst = []
#     for i in range(num):
#         if i % 2 == 0:
#             lst.append(i)
#     return lst
#
# # по сути равнозначные варианты, но первый достаточен:
# # l1 = generator_1(10**4)
# # print(l1)
#
# # l2 = time_it(generator_1)(10**4)
# # print(l2)
#
# w = time_it('generator_1')(generator_1)(100)
# print(w)


# MySQL

import yaml
import mysql.connector as connector

class MyConnector:
    def __init__(self, connection_name):
        try:
            with open('db_params.yaml') as file:
                params = yaml.safe_load(file)
                params_name = params[connection_name]
                self._url = str(params_name['url'])
                self._port = str(params_name['port'])
                self._db = str(params_name['database'])
                self._user = str(params_name['user'])
                self._password = str(params_name['password'])
        except yaml.YAMLError as ex:
            print('ERROR {}'.format(ex))
        except KeyError as ex:
            print('ERROR {}'.format(ex))

        self._connection = None
        self._cursor = None
        self._connection_name = None
        self._connection_type = ''

    def __run_script(self, script):
        self._cursor.execute(script)

    def select(self, script):
        try:
            self.__run_script(script)
            return self._cursor.fetchall()
        except Exception as ex:
            print('ERROR {}'.format(ex))
            return None

    def create(self, script):
        try:
            self.__run_script(script)
        except Exception as ex:
            print('ERROR {}'.format(ex))

    def insert(self, script):
        try:
            self.__run_script(script)
        except Exception as ex:
            print('ERROR {}'.format(ex))

    def update(self, script):
        try:
            self.__run_script(script)
        except Exception as ex:
            print('ERROR {}'.format(ex))

    def exec(self, script):
        try:
            self.__run_script(script)
        except Exception as ex:
            print('ERROR {}'.format(ex))

    def call(self, proc_name, args):
        try:
            if args is None or len(args) == 0:
                self._cursor.callproc(proc_name)
            else:
                self._cursor.callproc(proc_name, args)
        except Exception as ex:
            print('ERROR {}'.format(ex))

    def close(self):
        self._cursor.close()
        self._cursor = None
        self._connection.close()
        self._connection = None
        print('Connection was closed')

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

class MySqlConnector(MyConnector):
    def __init__(self, connection_name):
        super(MySqlConnector, self).__init__(connection_name)
    def open(self):
        try:
            self._connection = connector.connect(
                user = self._user,
                password = self._password,
                host = self._url
            )
            self._connection.autocommit = True
            self._cursor = self._connection.cursor()
            self._connection_type = 'MySQL'
            print('Connection was open')
        except Exception as ex:
            print('ERROR {}'.format(ex))
            print('Connection wasn\'t open')

    def __enter__(self):
        self.open()
        return self