Vim�UnDo� ���A�����b�|T��[Aw��m=��-                                      \�hP    _�                              ����                                                                                                                                                                                                                                                                                                                                                             \�hO    �                  import uuid   import secrets   import string           class GrinWallet:       def __init__(self):   E        address = 'grin+{}@coinmine.com'.format(uuid.uuid4().hex[:8])   *        password = ''.join(secrets.choice(   G            string.ascii_uppercase + string.digits) for _ in range(24))   *        self.wallet = {'Address': address,   1                       'Pool Password': password}           def get_dict(self):           return self.wallet5��