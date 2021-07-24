Vim�UnDo� �'���pb{+�2S�F���E�b�K5   %   H    @mock.patch("health_monitor.system.SystemHealthChecker._remedy_cmd")      E      
       
   
   
    ]/OK    _�                        %    ����                                                                                                                                                                                                                                                                                                                                                             ]e=     �         )      ,            {"memory_util_percent": "30.0"},5�_�                       (    ����                                                                                                                                                                                                                                                                                                                                                             ]e?     �         )      +            {"memory_util_percent": 30.0"},5�_�                       (    ����                                                                                                                                                                                                                                                                                                                                                             ]eA    �               )   	import os   #from unittest import TestCase, mock       5from health_monitor.system import SystemHealthChecker           (class TestSystemHealthChecker(TestCase):       def setUp(self):   ,        self.memory_percent_threshold = int(   9            os.environ["MINARY_MEMORY_PERCENT_THRESHOLD"]   	        )   9        self.system_health_checker = SystemHealthChecker(   *            {"memory_util_percent": 30.0},   *            self.memory_percent_threshold,               "some-command",   	        )       H    @mock.patch("health_monitor.system.SystemHealthChecker._remedy_cmd")   H    @mock.patch("health_monitor.system.SystemHealthChecker._is_healthy")   G    def test_check_system_info_healthy(self, mock_health, mock_remedy):   '        mock_health.return_value = True   *        self.system_health_checker.check()   ,        self.assertFalse(mock_remedy.called)       H    @mock.patch("health_monitor.system.SystemHealthChecker._remedy_cmd")   H    @mock.patch("health_monitor.system.SystemHealthChecker._is_healthy")   K    def test_check_system_info_not_healthy(self, mock_health, mock_remedy):   (        mock_health.return_value = False   *        self.system_health_checker.check()   +        self.assertTrue(mock_remedy.called)           def test_is_healthy(self):   A        self.assertTrue(self.system_health_checker._is_healthy())       "    def test_is_not_healthy(self):   4        system_health_checker = SystemHealthChecker(   ,            {"memory_util_percent": "90.0"},   *            self.memory_percent_threshold,               "some-command",   	        )   =        self.assertFalse(system_health_checker._is_healthy())5�_�                    #   )    ����                                                                                                                                                                                                                                                                                                                                                             ]eD     �   "   $   '      ,            {"memory_util_percent": "90.0"},5�_�                    #   $    ����                                                                                                                                                                                                                                                                                                                                                             ]eE     �   "   $   '      +            {"memory_util_percent": "90.0},5�_�                    #   $    ����                                                                                                                                                                                                                                                                                                                                                             ]eF    �               '   	import os   #from unittest import TestCase, mock       5from health_monitor.system import SystemHealthChecker           (class TestSystemHealthChecker(TestCase):       def setUp(self):   ,        self.memory_percent_threshold = int(   9            os.environ["MINARY_MEMORY_PERCENT_THRESHOLD"]   	        )   9        self.system_health_checker = SystemHealthChecker(   X            {"memory_util_percent": 30.0}, self.memory_percent_threshold, "some-command"   	        )       H    @mock.patch("health_monitor.system.SystemHealthChecker._remedy_cmd")   H    @mock.patch("health_monitor.system.SystemHealthChecker._is_healthy")   G    def test_check_system_info_healthy(self, mock_health, mock_remedy):   '        mock_health.return_value = True   *        self.system_health_checker.check()   ,        self.assertFalse(mock_remedy.called)       H    @mock.patch("health_monitor.system.SystemHealthChecker._remedy_cmd")   H    @mock.patch("health_monitor.system.SystemHealthChecker._is_healthy")   K    def test_check_system_info_not_healthy(self, mock_health, mock_remedy):   (        mock_health.return_value = False   *        self.system_health_checker.check()   +        self.assertTrue(mock_remedy.called)           def test_is_healthy(self):   A        self.assertTrue(self.system_health_checker._is_healthy())       "    def test_is_not_healthy(self):   4        system_health_checker = SystemHealthChecker(   *            {"memory_util_percent": 90.0},   *            self.memory_percent_threshold,               "some-command",   	        )   =        self.assertFalse(system_health_checker._is_healthy())5�_�                       <    ����                                                                                                                                                                                                                                                                                                                                                             ]/OA     �         %      H    @mock.patch("health_monitor.system.SystemHealthChecker._remedy_cmd")5�_�      	                 I    ����                                                                                                                                                                                                                                                                                                                                                             ]/OD     �         %      L    @mock.patch("health_monitor.system.SystemHealthChecker._run_remedy_cmd")5�_�      
           	      E    ����                                                                                                                                                                                                                                                                                                                                                             ]/OH     �         %      H    @mock.patch("health_monitor.system.SystemHealthChecker._remedy_cmd")5�_�   	               
      <    ����                                                                                                                                                                                                                                                                                                                                                             ]/OJ    �         %      L    @mock.patch("health_monitor.system.SystemHealthChecker._remedy_command")5��