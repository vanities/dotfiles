Vim�UnDo� <6����BUĝϜ�kQl������'@I�      #from unittest import TestCase, mock                                 \� �    _�                             ����                                                                                                                                                                                                                                                                                                                                                             \��     �                �             5�_�                       ,    ����                                                                                                                                                                                                                                                                                                                                                             \��     �               .    def test_hostname_addition_on_error(self):5�_�                       6    ����                                                                                                                                                                                                                                                                                                                                                             \��     �               9    def test_hostname_addition_on_error(self, mock_port):5�_�                       6    ����                                                                                                                                                                                                                                                                                                                                                             \��     �                             �               5�_�                       +    ����                                                                                                                                                                                                                                                                                                                                                             \��    �                  	import os   import unittest        from utils import CoinmineLogger           $class TestLogger(unittest.TestCase):       maxDiff = None           def setUp(self):   .        os.environ["SHORT_UUID"] = "SOME_UUID"   .        self.logger = CoinmineLogger(__name__)            @mock.patch('requests.post')   9    def test_hostname_addition_on_error(self, mock_post):   ;        with self.assertLogs(__name__, "ERROR") as context:   )            self.logger.error("some-log")   W            self.assertEqual("ERROR:test_logger:SOME_UUID some-log", context.output[0])   -            self.assertTrue(mock_post.called)5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             \��     �               import unittest5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             \��     �               import unittest5�_�      	                     ����                                                                                                                                                                                                                                                                                                                                                             \��    �               from unittest5�_�      
           	          ����                                                                                                                                                                                                                                                                                                                                                             \��    �               $class TestLogger(unittest.TestCase):5�_�   	              
          ����                                                                                                                                                                                                                                                                                                                                                             \�    �                    @mock.patch("requests.post")5�_�   
                    )    ����                                                                                                                                                                                                                                                                                                                                                             \�7    �               +    @mock.patch("sentry_sdk.capture_event")5�_�                       ,    ����                                                                                                                                                                                                                                                                                                                                                             \��     �               /    @mock.patch("sentry_sdk.capture_exception")5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             \��    �                   @mock.patch("logging.n")5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             \�^     �                    @mock.patch("logging.error")5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             \�i    �               '    @mock.patch("CoinmineLogger.error")5�_�                      +    ����                                                                                                                                                                                                                                                                                                                                                             \�j     �               -    @mock.patch("utils.CoinmineLogger.error")5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             \��     �                   @mock.patch("sentry")5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             \��   	 �                   @mock.patch("sentry.init")5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             \� �     �             �             5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             \� �     �             �             5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             \� �     �               .        os.environ["SHORT_UUID"] = "SOME_UUID"5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             \� �     �               .        os.environ["SHORT_UUID"] = "SOME_UUID"5�_�                       ,    ����                                                                                                                                                                                                                                                                                                                                                             \� �     �               <        os.environ["MINARY_SENTRY_PUBLIC_KEY"] = "SOME_UUID"5�_�                       2    ����                                                                                                                                                                                                                                                                                                                                                             \� �     �               <        os.environ["MINARY_SENTRY_PROJECT_ID"] = "SOME_UUID"5�_�                       2    ����                                                                                                                                                                                                                                                                                                                                                             \� �   
 �               <        os.environ["MINARY_SENTRY_PUBLIC_KEY"] = "SOME_UUID"5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             \� �     �                "    @mock.patch("sentry_sdk.init")5�_�                       ,    ����                                                                                                                                                                                                                                                                                                                                                             \� �     �               9    def test_hostname_addition_on_error(self, mock_post):5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             \� �    �                -            self.assertTrue(mock_post.called)5�_�                             ����                                                                                                                                                                                                                                                                                                                                                             \� �    �               #from unittest import TestCase, mock5�_�                      -    ����                                                                                                                                                                                                                                                                                                                                                             \�N     �               :        with self.assertLogs(__name__, "WARN") as context:5�_�                       ,    ����                                                                                                                                                                                                                                                                                                                                                             \�Q     �               ;        with self.assertLogs(__name__, "DEBUG") as context:5�_�                        #    ����                                                                                                                                                                                                                                                                                                                                                             \�W     �               R            self.assertEqual(":test_logger:SOME_UUID some-log", context.output[0])5��