Vim�UnDo� !�gW��)�tB���I�ٱ������<W��3�   &   D        wallet = Wallet.objects.create(owner=miner.owner, coin=coin)      C      C       C   C   C    [D�!    _�                            ����                                                                                                                                                                                                                                                                                                                                                             [DAi     �      	   "      <            Wallet.objects.get(owner=miner.owner, coin=coin)5�_�                    
       ����                                                                                                                                                                                                                                                                                                                                                             [DAn    �   	      "      -            WalletService.create(miner, coin)5�_�                       	    ����                                                                                                                                                                                                                                                                                                                                                             [D��     �         "              #coins = {5�_�                       	    ����                                                                                                                                                                                                                                                                                                                                                             [D��     �         "              #    'eth'5�_�                       	    ����                                                                                                                                                                                                                                                                                                                                                             [D��     �         "      
        #}5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             [D��     �         "                  'eth'5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             [D��     �         "                  'data'5�_�      	                     ����                                                                                                                                                                                                                                                                                                                                                             [D��     �         "                  'data}5�_�      
           	          ����                                                                                                                                                                                                                                                                                                                                                             [D�     �         "              return {}5�_�   	              
          ����                                                                                                                                                                                                                                                                                                                                                             [D�    �         "              return {'Address'}5�_�   
                   6    ����                                                                                                                                                                                                                                                                                                                                                             [D�@     �         #       �         "    5�_�                       1    ����                                                                                                                                                                                                                                                                                                                                                             [D�P     �         #      1from coinmine.scripts.wallet_generator.genaddress5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             [D�\     �         #          def generate_wallet(coin):5�_�                       #    ����                                                                                                                                                                                                                                                                                                                                                             [D�s     �         $      #        if coin.short_name == 'eth'5�_�                       H    ����                                                                                                                                                                                                                                                                                                                                                             [D�}     �         %      Hfrom coinmine.scripts.wallet_generator.genaddress import WalletGenerator5�_�                       ?    ����                                                                                                                                                                                                                                                                                                                                                             [Dɹ     �         %      Hfrom coinmine.scripts.wallet_generator.genaddress import WalletGenerator5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             [D��     �         %                  wallet = 5�_�                       I    ����                                                                                                                                                                                                                                                                                                                                                             [D��     �         %      Ifrom coinmine.scripts.wallet_generator.genaddress import AddressGenerator5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             [D��     �         %                  wallet = 5�_�                       0    ����                                                                                                                                                                                                                                                                                                                                                             [D��     �         %      0            wallet = ag.generate_ethereum_wallet5�_�                       2    ����                                                                                                                                                                                                                                                                                                                                                             [D��     �         %      =            wallet = ag.generate_ethereum_wallet().get_dict()5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             [D��     �                $            return wallet.get_dict()5�_�                    !        ����                                                                                                                                                                                                                                                                                                                                                             [D��     �   !   #   %    �   !   "   %    5�_�                    "       ����                                                                                                                                                                                                                                                                                                                                                             [D��     �   !   #   &      $            return wallet.get_dict()5�_�                       1    ����                                                                                                                                                                                                                                                                                                                                                V       [D��     �         &    �         &    5�_�                       1    ����                                                                                                                                                                                                                                                                                                                                                V       [D��     �      !   (    �         (    5�_�                        1    ����                                                                                                                                                                                                                                                                                                                                                V       [D��     �       #   *    �       !   *    5�_�                    "   1    ����                                                                                                                                                                                                                                                                                                                                                V       [D��     �   "   %   ,    �   "   #   ,    5�_�                    $   1    ����                                                                                                                                                                                                                                                                                                                                                V       [D�     �   $   '   .    �   $   %   .    5�_�                        "    ����                                                                                                                                                                                                                                                                                                                                                V       [D�     �         0      $        if coin.short_name == 'eth':5�_�      !                  )    ����                                                                                                                                                                                                                                                                                                                                                V       [D�     �         0      2            wallet = ag.generate_ethereum_wallet()5�_�       "           !      "    ����                                                                                                                                                                                                                                                                                                                                                V       [D�     �          0      $        if coin.short_name == 'eth':5�_�   !   #           "       *    ����                                                                                                                                                                                                                                                                                                                                                V       [D�     �      !   0      2            wallet = ag.generate_ethereum_wallet()5�_�   "   $           #   !   "    ����                                                                                                                                                                                                                                                                                                                                                V       [D�     �       "   0      $        if coin.short_name == 'eth':5�_�   #   %           $   "   )    ����                                                                                                                                                                                                                                                                                                                                                V       [D�H     �   !   #   0      2            wallet = ag.generate_ethereum_wallet()5�_�   $   &           %   #   "    ����                                                                                                                                                                                                                                                                                                                                                V       [D�K     �   "   $   0      $        if coin.short_name == 'eth':5�_�   %   '           &   $   )    ����                                                                                                                                                                                                                                                                                                                                                V       [D�O     �   #   %   0      2            wallet = ag.generate_ethereum_wallet()5�_�   &   (           '   %   "    ����                                                                                                                                                                                                                                                                                                                                                V       [D�S     �   $   &   0      $        if coin.short_name == 'eth':5�_�   '   )           (   &   )    ����                                                                                                                                                                                                                                                                                                                                                V       [D�V     �   %   '   0      2            wallet = ag.generate_ethereum_wallet()5�_�   (   *           )   $   $    ����                                                                                                                                                                                                                                                                                                                                                V       [D�^     �   #   %   0      -            wallet = ag.generate_zcl_wallet()5�_�   )   +           *   '       ����                                                                                                                                                                                                                                                                                                                                                V       [D�h     �   &   '          "        return {'Address' : 'asd'}5�_�   *   ,           +   '        ����                                                                                                                                                                                                                                                                                                                            '          )          V       [D�k     �   &   '                  coins = {               'eth'   	        }5�_�   +   -           ,   )        ����                                                                                                                                                                                                                                                                                                                            )           ,           V        [D�m    �   (   )                  #try           #    print('trying')           #except:           #    print('error')5�_�   ,   .           -          ����                                                                                                                                                                                                                                                                                                                            )           )           V        [D�B     �         (      2            wallet = ag.generate_ethereum_wallet()5�_�   -   0           .          ����                                                                                                                                                                                                                                                                                                                            )           )           V        [D�F     �         (      0            wallet = ag.generate_monero_wallet()5�_�   .   1   /       0           ����                                                                                                                                                                                                                                                                                                                            )           )           V        [D�K     �      !   (      :            wallet = ag.generate_ethereum_classic_wallet()5�_�   0   2           1   "       ����                                                                                                                                                                                                                                                                                                                            )           )           V        [D�M     �   !   #   (      /            wallet = ag.generate_zcash_wallet()5�_�   1   3           2   $       ����                                                                                                                                                                                                                                                                                                                            )           )           V        [D�O     �   #   %   (      2            wallet = ag.generate_zclassic_wallet()5�_�   2   4           3   &       ����                                                                                                                                                                                                                                                                                                                            )           )           V        [D�P    �   %   '   (      1            wallet = ag.generate_zencash_wallet()5�_�   3   5           4          ����                                                                                                                                                                                                                                                                                                                            )           )           V        [D�j     �         (      4            wallet = ag().generate_ethereum_wallet()5�_�   4   6           5   (       ����                                                                                                                                                                                                                                                                                                                            )           )           V        [D�o     �   '   (                   return wallet.get_dict()5�_�   5   7           6   '        ����                                                                                                                                                                                                                                                                                                                            (           (           V        [D�p     �   &   '           5�_�   6   8           7          ����                                                                                                                                                                                                                                                                                                                            '           '           V        [D�t     �         &      2            wallet = ag().generate_monero_wallet()5�_�   7   9           8           ����                                                                                                                                                                                                                                                                                                                            '           '           V        [D�y     �      !   &      <            wallet = ag().generate_ethereum_classic_wallet()5�_�   8   :           9   "       ����                                                                                                                                                                                                                                                                                                                            '           '           V        [D�|     �   !   #   &      1            wallet = ag().generate_zcash_wallet()5�_�   9   ;           :   $       ����                                                                                                                                                                                                                                                                                                                            '           '           V        [D�~     �   #   %   &      4            wallet = ag().generate_zclassic_wallet()5�_�   :   <           ;   &       ����                                                                                                                                                                                                                                                                                                                            '           '           V        [D�    �   %   '          3            wallet = ag().generate_zencash_wallet()5�_�   ;   ?           <          ����                                                                                                                                                                                                                                                                                                                            '           '           V        [D�)     �         &    �         &    5�_�   <   A   =       ?          ����                                                                                                                                                                                                                                                                                                                            (           (           V        [D��     �                <        wallet_secrets = WalletService.generate_wallet(coin)5�_�   ?   B   @       A           ����                                                                                                                                                                                                                                                                                                                            '           '           V        [D��     �         &    5�_�   A   C           B           ����                                                                                                                                                                                                                                                                                                                            (           (           V        [D��     �                 5�_�   B               C      C    ����                                                                                                                                                                                                                                                                                                                            '           '           V        [D�     �         &      D        wallet = Wallet.objects.create(owner=miner.owner, coin=coin)5�_�   ?           A   @           ����                                                                                                                                                                                                                                                                                                                            (           (           V        [D��     �         &       5�_�   <   >       ?   =      C    ����                                                                                                                                                                                                                                                                                                                            (           (           V        [D�9     �         '      O        wallet = Wallet.objects.create(owner=miner.owner, coin=coin, address=])5�_�   =               >      N    ����                                                                                                                                                                                                                                                                                                                            (           (           V        [D�@     �         '      g        wallet = Wallet.objects.create(owner=miner.owner, coin=coin, address=wallet_secrets['Address'])5�_�   .           0   /           ����                                                                                                                                                                                                                                                                                                                            )           )           V        [D�I     �      !   (      <            wallet = a()g.generate_ethereum_classic_wallet()5�_�   
                    6    ����                                                                                                                                                                                                                                                                                                                                                             [D�>     �         "    �          "      ?from coinmine.wallet.models import Wallet, WalletPrivatbitcoine5��