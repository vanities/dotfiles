Vim�UnDo� 2���=O�g�_�&���R�6Թ9�t
3���r   \           except:   G         
       
   
   
    \e��    _�                            ����                                                                                                                                                                                                                                                                                                                                                             \e�P     �      Z   4    �         4    �          3    5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             \e�R     �                  5�_�                    Y        ����                                                                                                                                                                                                                                                                                                                            Y          �          V       \e�V    �   X   Y       3   7from django.utils.translation import ugettext_lazy as _       >from rest_framework.authentication import (BaseAuthentication,   D                                           get_authorization_header)   %from rest_framework import exceptions       4from coinmine.authenticator.models import MinerToken           3class MinerTokenAuthentication(BaseAuthentication):       model = MinerToken           keyword = 'Token'       model = None           def get_model(self):   "        if self.model is not None:               return self.model           return MinerToken       ,    def authenticate_credentials(self, key):            model = self.get_model()           try:   F            token = model.objects.select_related('miner').get(key=key)   "        except model.DoesNotExist:   F            raise exceptions.AuthenticationFailed(_('Invalid token.'))       #        return (token.miner, token)       $    def authenticate(self, request):   8        auth = get_authorization_header(request).split()       H        if not auth or auth[0].lower() != self.keyword.lower().encode():               return None               if len(auth) == 1:   E            msg = _('Invalid token header. No credentials provided.')   6            raise exceptions.AuthenticationFailed(msg)           elif len(auth) > 2:   T            msg = _('Invalid token header. Token string should not contain spaces.')   6            raise exceptions.AuthenticationFailed(msg)               try:   $            token = auth[1].decode()           except UnicodeError:   `            msg = _('Invalid token header. Token string should not contain invalid characters.')   6            raise exceptions.AuthenticationFailed(msg)   3        return self.authenticate_credentials(token)       +    def authenticate_header(self, request):           return self.keyword5�_�                    ,   2    ����                                                                                                                                                                                                                                                                                                                            Y          Y          V       \e�a    �   +   .   X      Q            raise exceptions.AuthenticationFailed(_('User inactive or deleted.'))5�_�                    <   /    ����                                                                                                                                                                                                                                                                                                                            Z          Z          V       \e�v    �   ;   >   Y      X                msg = _('Invalid token header. Token string should not contain spaces.')5�_�                    C   /    ����                                                                                                                                                                                                                                                                                                                            [          [          V       \e�|     �   B   E   Z      d                msg = _('Invalid token header. Token string should not contain invalid characters.')5�_�                    O   /    ����                                                                                                                                                                                                                                                                                                                            \          \          V       \e��     �   N   Q   [      X                msg = _('Invalid token header. Token string should not contain spaces.')5�_�      	              V   /    ����                                                                                                                                                                                                                                                                                                                            ]          ]          V       \e��    �   U   X   \      d                msg = _('Invalid token header. Token string should not contain invalid characters.')5�_�      
           	   [        ����                                                                                                                                                                                                                                                                                                                            ^          ^          V       \e��    �   Z   [           5�_�   	               
   G       ����                                                                                                                                                                                                                                                                                                                            ]          ]          V       \e��    �   F   H   \              except:5��