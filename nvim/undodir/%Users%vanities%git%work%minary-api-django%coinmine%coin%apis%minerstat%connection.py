Vim�UnDo� 88���~�������jy�T�g��6`�F/0�      class Connection:                             ^j��    _�                            ����                                                                                                                                                                                                                                                                                                                                       *          V       ^j��     �                    0    def post(url_path, data=None, headers=None):           response = None   6        url = "{}{}".format(Connection.HOST, url_path)               try:   E            response = requests.post(url, data=data, headers=headers)   '            response.raise_for_status()               except HTTPError:   E            logger.warning("FAILURE {}".format(make_error_message()))                except RequestException:   O            logger.error("FAILURE {} url={}".format(make_error_message(), url))               return response5�_�                            ����                                                                                                                                                                                                                                                                                                                                                 V       ^j��     �   
                     def get_html(url_path):           response = None   6        url = "{}{}".format(Connection.HOST, url_path)               try:   (            response = requests.get(url)   '            response.raise_for_status()               except HTTPError:   E            logger.warning("FAILURE {}".format(make_error_message()))                except RequestException:   O            logger.error("FAILURE {} url={}".format(make_error_message(), url))               return response5�_�                           ����                                                                                                                                                                                                                                                                                                                                                 V       ^j��     �         
    �         
    5�_�                            ����                                                                                                                                                                                                                                                                                                                                                  V        ^j��     �                 import requests   ;from requests.exceptions import RequestException, HTTPError   ,from celery.utils.log import get_task_logger   4from coinmine.worker.utils import make_error_message       "logger = get_task_logger(__name__)5�_�                            ����                                                                                                                                                                                                                                                                                                                                                  V        ^j��     �                 5�_�                           ����                                                                                                                                                                                                                                                                                                                                                  V        ^j��     �               class Connection:5�_�                            ����                                                                                                                                                                                                                                                                                                                                                  V        ^j��    �                  =from coinmine.coin.apis.base_connection import BaseConnection       !class Connection(BaseConnection):   "    HOST = "https://minerstat.com"5�_�                             ����                                                                                                                                                                                                                                                                                                                                                 V       ^j��     �      +        5��