Vim�UnDo� �b���/�m( ���U� [���]�gk�	D�   "   mport subprocess                              ^)�F    _�                             ����                                                                                                                                                                                                                                                                                                                                                             ^)�@     �                   5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             ^)�C     �                mport subprocess5�_�                             ����                                                                                                                                                                                                                                                                                                                                                             ^)�E    �                  import subprocess   import json   	import os       %class TestSecrets(unittest.TestCase):       def setUp(self):           self.maxDiff = None   3        os.environ["SECRET1_KEY"] = "secret1_value"   3        os.environ["SECRET2_KEY"] = "secret2_value"   Y        self.input_json = '{"version": "1.0", "secrets": ["secret1_key", "secret2_key"]}'           def test_secrets(self):            expected_output_json = (               '{'   I            '  "secret1_key": {"value": "secret1_value", "error": null},'   H            '  "secret2_key": {"value": "secret2_value", "error": null}'               '}'   	        )           proc = subprocess.run(   C                "echo '{}' | ./secrets.py".format(self.input_json),                   shell=True,   #                capture_output=True   	        )   *        output_json = proc.stdout.decode()           print(output_json)       W        self.assertDictEqual(json.loads(output_json), json.loads(expected_output_json))       if __name__ == '__main__':       unittest.main()5��