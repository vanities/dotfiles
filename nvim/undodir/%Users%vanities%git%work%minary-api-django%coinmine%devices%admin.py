Vim�UnDo� ��M��ST���rX�� ��R�3	��S�:�A   q       list_filter = ("active",)   A         -       -   -   -    ]�K    _�                     '        ����                                                                                                                                                                                                                                                                                                                                                             ]�l     �   '   )   Y              �   '   )   X    5�_�                    =       ����                                                                                                                                                                                                                                                                                                                                                             ]�u     �   =   @   Z              �   =   ?   Y    5�_�                    ?       ����                                                                                                                                                                                                                                                                                                                                                             ]�{     �   >   A   [          def active(self, obj)5�_�                    @       ����                                                                                                                                                                                                                                                                                                                                                             ]钆    �               \   import logging    from django.contrib import admin   from django import forms   %from django.db.models import Prefetch   3from simple_history.admin import SimpleHistoryAdmin        from .models import SupportMiner   )from coinmine.wallet.models import Wallet           $logger = logging.getLogger(__name__)           +class FilteredWalletsForm(forms.ModelForm):   (    def __init__(self, *args, **kwargs):   B        super(FilteredWalletsForm, self).__init__(*args, **kwargs)           try:   C            self.fields["wallet"].queryset = Wallet.objects.filter(   )                owner=self.instance.owner   $            ).select_related("coin")   L            self.fields["wallet"].label_from_instance = lambda obj: obj.coin           except Exception as e:   =            # when creating new config, doesn't crash the app   E            logger.error("uh oh something went wrong e={}".format(e))           class Meta:   #        labels = {"wallet": "Coin"}           @admin.register(SupportMiner)   ,class SupportMinerAdmin(SimpleHistoryAdmin):       list_display = (           "short_uuid",           "nickname",           "owner",           "coin",           "amount_mined",           "amount_mined_in_usd",           "case_version",           "active"           "created",       )           list_per_page = 50       =    list_select_related = ("wallet", "wallet__coin", "owner")       3    search_fields = ("nickname", "owner__username")       #    history_list_display = ["coin"]           raw_id_fields = ("owner",)       $    def get_queryset(self, request):   R        return super().get_queryset(request).prefetch_related(Prefetch("credits"))           def coin(self, obj):           try:   "            return obj.wallet.coin           except Exception:               return None           def active(self, obj):           return obj.active            def amount_mined(self, obj):           try:   >            return obj.credits.get(coin__name=obj.coin).amount           except Exception:               return 0       '    def amount_mined_in_usd(self, obj):           try:   T            return "${:,.2f}".format(obj.credits.get(coin__name=obj.coin).usd_value)           except Exception:   *            return "${:,.2f}".format(0.00)       5    def save_model(self, request, obj, form, change):           if not change:   2            owner = form.cleaned_data.get("owner")   %            # set default to ethereum   P            obj.wallet = Wallet.objects.get(owner=owner, coin__short_name="eth")   M        super(SupportMinerAdmin, self).save_model(request, obj, form, change)       (    def add_view(self, *args, **kwargs):   7        self.exclude = ("wallet", "uuid", "short_uuid")   0        return super().add_view(*args, **kwargs)       +    def change_view(self, *args, **kwargs):   '        self.form = FilteredWalletsForm   >        self.readonly_fields = ("owner", "uuid", "short_uuid")   3        return super().change_view(*args, **kwargs)5�_�                    >        ����                                                                                                                                                                                                                                                                                                                            >           ?           V        ]钍     �   =   >              def active(self, obj):           return obj.active5�_�                    >        ����                                                                                                                                                                                                                                                                                                                            >           >           V        ]钍    �   =   >           5�_�                    (       ����                                                                                                                                                                                                                                                                                                                            >           >           V        ]钻    �   '   *   X              "active" "created",5�_�      	              Y       ����                                                                                                                                                                                                                                                                                                                            ?           ?           V        ]�>    �   Z            �   Z            �   Y            5�_�      
           	   Y        ����                                                                                                                                                                                                                                                                                                                            [          [          V       ]�a     �   Y   \   \          �   Y   [   [    5�_�   	              
   [       ����                                                                                                                                                                                                                                                                                                                            ]          ]          V       ]�d     �   Z   \   ]          def active(self)5�_�   
                 [       ����                                                                                                                                                                                                                                                                                                                            ]          ]          V       ]�i     �   [   ]   ^              �   [   ]   ]    5�_�                    \       ����                                                                                                                                                                                                                                                                                                                            ^          ^          V       ]�p     �   [   ]   ^              return obj.actibe5�_�                    [       ����                                                                                                                                                                                                                                                                                                                            ^          ^          V       ]�r    �   Z   \   ^          def active(self):5�_�                    '       ����                                                                                                                                                                                                                                                                                                                                                             ]��     �   '   )   _              �   '   )   ^    5�_�                    (       ����                                                                                                                                                                                                                                                                                                                                                             ]��    �               _   import logging    from django.contrib import admin   from django import forms   %from django.db.models import Prefetch   3from simple_history.admin import SimpleHistoryAdmin        from .models import SupportMiner   )from coinmine.wallet.models import Wallet           $logger = logging.getLogger(__name__)           +class FilteredWalletsForm(forms.ModelForm):   (    def __init__(self, *args, **kwargs):   B        super(FilteredWalletsForm, self).__init__(*args, **kwargs)           try:   C            self.fields["wallet"].queryset = Wallet.objects.filter(   )                owner=self.instance.owner   $            ).select_related("coin")   L            self.fields["wallet"].label_from_instance = lambda obj: obj.coin           except Exception as e:   =            # when creating new config, doesn't crash the app   E            logger.error("uh oh something went wrong e={}".format(e))           class Meta:   #        labels = {"wallet": "Coin"}           @admin.register(SupportMiner)   ,class SupportMinerAdmin(SimpleHistoryAdmin):       list_display = (           "short_uuid",           "nickname",           "owner",           "coin",           "amount_mined",           "amount_mined_in_usd",           "case_version",           "lifetime"           "active",           "created",       )           list_per_page = 50       =    list_select_related = ("wallet", "wallet__coin", "owner")       3    search_fields = ("nickname", "owner__username")       #    history_list_display = ["coin"]           raw_id_fields = ("owner",)       $    def get_queryset(self, request):   R        return super().get_queryset(request).prefetch_related(Prefetch("credits"))           def coin(self, obj):           try:   "            return obj.wallet.coin           except Exception:               return None            def amount_mined(self, obj):           try:   >            return obj.credits.get(coin__name=obj.coin).amount           except Exception:               return 0       '    def amount_mined_in_usd(self, obj):           try:   T            return "${:,.2f}".format(obj.credits.get(coin__name=obj.coin).usd_value)           except Exception:   *            return "${:,.2f}".format(0.00)       5    def save_model(self, request, obj, form, change):           if not change:   2            owner = form.cleaned_data.get("owner")   %            # set default to ethereum   P            obj.wallet = Wallet.objects.get(owner=owner, coin__short_name="eth")   M        super(SupportMinerAdmin, self).save_model(request, obj, form, change)       (    def add_view(self, *args, **kwargs):   7        self.exclude = ("wallet", "uuid", "short_uuid")   0        return super().add_view(*args, **kwargs)       +    def change_view(self, *args, **kwargs):   '        self.form = FilteredWalletsForm   >        self.readonly_fields = ("owner", "uuid", "short_uuid")   3        return super().change_view(*args, **kwargs)           def active(self, obj):           return obj.active           active.boolean = True5�_�                    (       ����                                                                                                                                                                                                                                                                                                                                                             ]��     �   '   )   ^              "lifetime" "active",5�_�                    (       ����                                                                                                                                                                                                                                                                                                                                                             ]��    �               ^   import logging    from django.contrib import admin   from django import forms   %from django.db.models import Prefetch   3from simple_history.admin import SimpleHistoryAdmin        from .models import SupportMiner   )from coinmine.wallet.models import Wallet           $logger = logging.getLogger(__name__)           +class FilteredWalletsForm(forms.ModelForm):   (    def __init__(self, *args, **kwargs):   B        super(FilteredWalletsForm, self).__init__(*args, **kwargs)           try:   C            self.fields["wallet"].queryset = Wallet.objects.filter(   )                owner=self.instance.owner   $            ).select_related("coin")   L            self.fields["wallet"].label_from_instance = lambda obj: obj.coin           except Exception as e:   =            # when creating new config, doesn't crash the app   E            logger.error("uh oh something went wrong e={}".format(e))           class Meta:   #        labels = {"wallet": "Coin"}           @admin.register(SupportMiner)   ,class SupportMinerAdmin(SimpleHistoryAdmin):       list_display = (           "short_uuid",           "nickname",           "owner",           "coin",           "amount_mined",           "amount_mined_in_usd",           "case_version",           "lifetime", "active",           "created",       )           list_per_page = 50       =    list_select_related = ("wallet", "wallet__coin", "owner")       3    search_fields = ("nickname", "owner__username")       #    history_list_display = ["coin"]           raw_id_fields = ("owner",)       $    def get_queryset(self, request):   R        return super().get_queryset(request).prefetch_related(Prefetch("credits"))           def coin(self, obj):           try:   "            return obj.wallet.coin           except Exception:               return None            def amount_mined(self, obj):           try:   >            return obj.credits.get(coin__name=obj.coin).amount           except Exception:               return 0       '    def amount_mined_in_usd(self, obj):           try:   T            return "${:,.2f}".format(obj.credits.get(coin__name=obj.coin).usd_value)           except Exception:   *            return "${:,.2f}".format(0.00)       5    def save_model(self, request, obj, form, change):           if not change:   2            owner = form.cleaned_data.get("owner")   %            # set default to ethereum   P            obj.wallet = Wallet.objects.get(owner=owner, coin__short_name="eth")   M        super(SupportMinerAdmin, self).save_model(request, obj, form, change)       (    def add_view(self, *args, **kwargs):   7        self.exclude = ("wallet", "uuid", "short_uuid")   0        return super().add_view(*args, **kwargs)       +    def change_view(self, *args, **kwargs):   '        self.form = FilteredWalletsForm   >        self.readonly_fields = ("owner", "uuid", "short_uuid")   3        return super().change_view(*args, **kwargs)           def active(self, obj):           return obj.active           active.boolean = True5�_�                    (       ����                                                                                                                                                                                                                                                                                                                                                             ]�7    �   '   )   _              "lifetime",5�_�                    /       ����                                                                                                                                                                                                                                                                                                                                                             ]꯯     �   /   2   `          �   /   1   _    5�_�                    1       ����                                                                                                                                                                                                                                                                                                                                                             ]꯶     �   0   2   a          list_filter = ("active")5�_�                    1       ����                                                                                                                                                                                                                                                                                                                                                             ]꯷   	 �               a   import logging    from django.contrib import admin   from django import forms   %from django.db.models import Prefetch   3from simple_history.admin import SimpleHistoryAdmin        from .models import SupportMiner   )from coinmine.wallet.models import Wallet           $logger = logging.getLogger(__name__)           +class FilteredWalletsForm(forms.ModelForm):   (    def __init__(self, *args, **kwargs):   B        super(FilteredWalletsForm, self).__init__(*args, **kwargs)           try:   C            self.fields["wallet"].queryset = Wallet.objects.filter(   )                owner=self.instance.owner   $            ).select_related("coin")   L            self.fields["wallet"].label_from_instance = lambda obj: obj.coin           except Exception as e:   =            # when creating new config, doesn't crash the app   E            logger.error("uh oh something went wrong e={}".format(e))           class Meta:   #        labels = {"wallet": "Coin"}           @admin.register(SupportMiner)   ,class SupportMinerAdmin(SimpleHistoryAdmin):       list_display = (           "short_uuid",           "nickname",           "owner",           "coin",           "amount_mined",           "amount_mined_in_usd",           "case_version",           "date_of_expiration",           "active",           "created",       )           list_per_page = 50       =    list_select_related = ("wallet", "wallet__coin", "owner")           list_filter = ("active", )       3    search_fields = ("nickname", "owner__username")       #    history_list_display = ["coin"]           raw_id_fields = ("owner",)       $    def get_queryset(self, request):   R        return super().get_queryset(request).prefetch_related(Prefetch("credits"))           def coin(self, obj):           try:   "            return obj.wallet.coin           except Exception:               return None            def amount_mined(self, obj):           try:   >            return obj.credits.get(coin__name=obj.coin).amount           except Exception:               return 0       '    def amount_mined_in_usd(self, obj):           try:   T            return "${:,.2f}".format(obj.credits.get(coin__name=obj.coin).usd_value)           except Exception:   *            return "${:,.2f}".format(0.00)       5    def save_model(self, request, obj, form, change):           if not change:   2            owner = form.cleaned_data.get("owner")   %            # set default to ethereum   P            obj.wallet = Wallet.objects.get(owner=owner, coin__short_name="eth")   M        super(SupportMinerAdmin, self).save_model(request, obj, form, change)       (    def add_view(self, *args, **kwargs):   7        self.exclude = ("wallet", "uuid", "short_uuid")   0        return super().add_view(*args, **kwargs)       +    def change_view(self, *args, **kwargs):   '        self.form = FilteredWalletsForm   >        self.readonly_fields = ("owner", "uuid", "short_uuid")   3        return super().change_view(*args, **kwargs)           def active(self, obj):           return obj.active           active.boolean = True5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             ]�     �         a    5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             ]가     �      -   b       �         b    5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             ]가     �         r    5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             ]갂     �         s      5class IsVeryBenevolentFilter(admin.SimpleListFilter):5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             ]갃     �         s      !class Is(admin.SimpleListFilter):5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             ]갉     �         s           title = 'is_very_benevolent'5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             ]갉     �         s          title = 'is_'5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             ]갋     �         s          title = 'is_actibe'5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             ]갏     �         s          title = 'is_actve'5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             ]값     �         s      -class IsActiveFilter(admin.SimpleListFilter):5�_�      !                      ����                                                                                                                                                                                                                                                                                                                                                             ]강     �          s      )    parameter_name = 'is_very_benevolent'5�_�       "           !          ����                                                                                                                                                                                                                                                                                                                                                             ]강     �          s          parameter_name = ''5�_�   !   #           "   *       ����                                                                                                                                                                                                                                                                                                                                                             ]갤     �   )   +   s      =            return queryset.filter(benevolence_factor__gt=75)5�_�   "   $           #   *       ����                                                                                                                                                                                                                                                                                                                                                             ]갦     �   )   +   s                  return queryset.5�_�   #   %           $   *   #    ����                                                                                                                                                                                                                                                                                                                                                             ]��     �   )   +   s      #            return queryset.active_5�_�   $   &           %   *       ����                                                                                                                                                                                                                                                                                                                                                             ]�     �   )   +   s      ,            return queryset.active_objects()5�_�   %   '           &   *       ����                                                                                                                                                                                                                                                                                                                                                             ]�     �   )   +   s                  return 5�_�   &   (           '   ,       ����                                                                                                                                                                                                                                                                                                                                                             ]�     �   +   -   s      >            return queryset.exclude(benevolence_factor__gt=75)5�_�   '   )           (   ,       ����                                                                                                                                                                                                                                                                                                                                                             ]�     �   +   -   s                  return 5�_�   (   *           )   -       ����                                                                                                                                                                                                                                                                                                                                                             ]�   
 �               s   import logging    from django.contrib import admin   from django import forms   %from django.db.models import Prefetch   3from simple_history.admin import SimpleHistoryAdmin        from .models import SupportMiner   )from coinmine.wallet.models import Wallet           $logger = logging.getLogger(__name__)           +class FilteredWalletsForm(forms.ModelForm):   (    def __init__(self, *args, **kwargs):   B        super(FilteredWalletsForm, self).__init__(*args, **kwargs)           try:   C            self.fields["wallet"].queryset = Wallet.objects.filter(   )                owner=self.instance.owner   $            ).select_related("coin")   L            self.fields["wallet"].label_from_instance = lambda obj: obj.coin           except Exception as e:   =            # when creating new config, doesn't crash the app   E            logger.error("uh oh something went wrong e={}".format(e))           class Meta:   #        labels = {"wallet": "Coin"}       +class ActiveFilter(admin.SimpleListFilter):       title = 'actve'       parameter_name = 'active'       ,    def lookups(self, request, model_admin):           return (               ('Yes', 'Yes'),               ('No', 'No'),   	        )       *    def queryset(self, request, queryset):           value = self.value()           if value == 'Yes':   4            return SupportMiner.active_objects.all()           elif value == 'No':   6            return SupportMiner.inactive_objects.all()           return queryset           @admin.register(SupportMiner)   ,class SupportMinerAdmin(SimpleHistoryAdmin):       list_display = (           "short_uuid",           "nickname",           "owner",           "coin",           "amount_mined",           "amount_mined_in_usd",           "case_version",           "date_of_expiration",           "active",           "created",       )           list_per_page = 50       =    list_select_related = ("wallet", "wallet__coin", "owner")           list_filter = ("active",)       3    search_fields = ("nickname", "owner__username")       #    history_list_display = ["coin"]           raw_id_fields = ("owner",)       $    def get_queryset(self, request):   R        return super().get_queryset(request).prefetch_related(Prefetch("credits"))           def coin(self, obj):           try:   "            return obj.wallet.coin           except Exception:               return None            def amount_mined(self, obj):           try:   >            return obj.credits.get(coin__name=obj.coin).amount           except Exception:               return 0       '    def amount_mined_in_usd(self, obj):           try:   T            return "${:,.2f}".format(obj.credits.get(coin__name=obj.coin).usd_value)           except Exception:   *            return "${:,.2f}".format(0.00)       5    def save_model(self, request, obj, form, change):           if not change:   2            owner = form.cleaned_data.get("owner")   %            # set default to ethereum   P            obj.wallet = Wallet.objects.get(owner=owner, coin__short_name="eth")   M        super(SupportMinerAdmin, self).save_model(request, obj, form, change)       (    def add_view(self, *args, **kwargs):   7        self.exclude = ("wallet", "uuid", "short_uuid")   0        return super().add_view(*args, **kwargs)       +    def change_view(self, *args, **kwargs):   '        self.form = FilteredWalletsForm   >        self.readonly_fields = ("owner", "uuid", "short_uuid")   3        return super().change_view(*args, **kwargs)           def active(self, obj):           return obj.active           active.boolean = True5�_�   )   +           *   A       ����                                                                                                                                                                                                                                                                                                                                                             ]�@     �   @   B   q          list_filter = ("active",)5�_�   *   ,           +   A       ����                                                                                                                                                                                                                                                                                                                                                             ]�E     �   @   B   q          list_filter = ("",)5�_�   +   -           ,   A   !    ����                                                                                                                                                                                                                                                                                                                                                             ]�I     �   @   B   q      #    list_filter = ("ActiveFilter",)5�_�   ,               -   A       ����                                                                                                                                                                                                                                                                                                                                                             ]�J    �   @   B   q      "    list_filter = ("ActiveFilter,)5��