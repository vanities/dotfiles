Vim�UnDo� `��?�.}���5���8s}���<�UA>LX�v��   B   )from .models import Wallet, WalletPrivate                             [��    _�                     A        ����                                                                                                                                                                                                                                                                                                                            A           H           V        [���     �   @   A          $class WalletPrivateAdmin(BaseAdmin):       $    list_display = ('pk', 'wallet',)       exclude = ('data',)       5    def get_readonly_fields(self, request, obj=None):           return ('wallet',)    5�_�                    A        ����                                                                                                                                                                                                                                                                                                                            A           A           V        [���     �   @   A           5�_�                    C        ����                                                                                                                                                                                                                                                                                                                            A           A           V        [���    �   B   C          6admin.site.register(WalletPrivate, WalletPrivateAdmin)5�_�                            ����                                                                                                                                                                                                                                                                                                                            A           A           V        [��    �         B      )from .models import Wallet, WalletPrivate5��