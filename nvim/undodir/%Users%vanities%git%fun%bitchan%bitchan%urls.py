Vim�UnDo� i��8���du3E�_lF��p�G��/G�   %                                   ^��    _�                            ����                                                                                                                                                                                                                                                                                                                                                             ^���     �             5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             ^���     �                �             5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             ^���     �                �             5�_�                       #    ����                                                                                                                                                                                                                                                                                                                                                             ^���     �             5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             ^���    �                  )from django.conf.urls import include, url    from django.contrib import admin   $from django.http import HttpResponse       *from web3auth import urls as web3auth_urls       urlpatterns = [   3    url(r"^admin/", admin.site.urls, name="admin"),   &    url(r'^', include(web3auth_urls)),       url(           r"^robots.txt",           lambda x: HttpResponse(   F            "User-Agent: *\n" "Disallow: /", content_type="text/plain"   
        ),           name="robots_file",       ),   ]5�_�                   	        ����                                                                                                                                                                                                                                                                                                                                                             ^��F     �   	          5�_�      
                     ����                                                                                                                                                                                                                                                                                                                                                             ^��H     �      
       5�_�         	       
          ����                                                                                                                                                                                                                                                                                                                                                             ^��R     �      
       5�_�   
                 	        ����                                                                                                                                                                                                                                                                                                                                                             ^��R     �                �   	   
       5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             ^��S     �      
       5�_�                    
       ����                                                                                                                                                                                                                                                                                                                                                             ^��V     �   	   
          3    url(r'^$', RedirectView.as_view(url='/login')),5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             ^��W     �      	       �             5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             ^��[    �                  )from django.conf.urls import include, url    from django.contrib import admin   $from django.http import HttpResponse       *from web3auth import urls as web3auth_urls       urlpatterns = [   3    url(r'^$', RedirectView.as_view(url='/login')),   3    url(r"^admin/", admin.site.urls, name="admin"),       )    url(r'^login/', login, name='login'),   7    url(r'^auto_login/', auto_login, name='autologin'),       &    url(r"^", include(web3auth_urls)),           url(           r"^robots.txt",           lambda x: HttpResponse(   F            "User-Agent: *\n" "Disallow: /", content_type="text/plain"   
        ),           name="robots_file",       ),   ]5�_�                          ����                                                                                                                                                                                                                                                                                                                                                             ^��     �                �             5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             ^��    �               #   )from django.conf.urls import include, url    from django.contrib import admin   $from django.http import HttpResponse       *from web3auth import urls as web3auth_urls           def login(request):   )    if not request.user.is_authenticated:   5        return render(request, 'web3auth/login.html')   	    else:   '        return redirect('/admin/login')           def auto_login(request):   )    if not request.user.is_authenticated:   9        return render(request, 'web3auth/autologin.html')   	    else:   '        return redirect('/admin/login')           urlpatterns = [   3    url(r"^$", RedirectView.as_view(url="/login")),   3    url(r"^admin/", admin.site.urls, name="admin"),   )    url(r"^login/", login, name="login"),   7    url(r"^auto_login/", auto_login, name="autologin"),   &    url(r"^", include(web3auth_urls)),       url(           r"^robots.txt",           lambda x: HttpResponse(   F            "User-Agent: *\n" "Disallow: /", content_type="text/plain"   
        ),           name="robots_file",       ),   ]5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             ^��     �         #    5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             ^��     �         $       �         $    5�_�                             ����                                                                                                                                                                                                                                                                                                                                                             ^��    �                 from django.contrib import admin5�_�                          ����                                                                                                                                                                                                                                                                                                                                                             ^��     �                �                   def login(request):5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             ^��c    �               )from django.contrib import admin, include5�_�              
   	          ����                                                                                                                                                                                                                                                                                                                                                             ^��N     �      	       �      	         8    u    url(r'^$', RedirectView.as_view(url='/login')),   )    url(r'^login/', login, name='login'),   e    url(r'^auto_login/', auto_login, name='autologin'),rl(r"^admin/", admin.site.urls, name="admin"),5�_�                    	        ����                                                                                                                                                                                                                                                                                                                                                             ^��D     �   	   
       �      
         4     url(r'^$', RedirectView.as_view(url='/login')),   )    url(r'^login/', login, name='login'),   \    url(r'^auto_login/', auto_login, name='autologin'),   url(r"^", include(web3auth_urls)),5��