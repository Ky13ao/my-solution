def xhRequest(url_string, method='get', body_string='', headers={}, user_name="jabil\\svchcm_zebra", pwd="97v6CGFcYM"):
    headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36 Edg/99.0.1150.46'
    from win32com.client import Dispatch as CreateObject
    __xhr = CreateObject("msxml2.xmlhttp.6.0")
    __result = {}
    help(__xhr)

    def __xhStateChangeHandler():
        if __xhr and __xhr.readyState and __xhr.readyState == 4:
            __result = __xhr
    __xhr.open(method.upper(), url_string, False, user_name, pwd)
    for __header in headers:
        __xhr.setRequestHeader(__header, headers[__header])
    # __xhr.onReadyStateChange = __xhStateChangeHandler
    __xhr.send(body_string)
    __result = __xhr
    return __result


print(xhRequest("https://hcmlocal1.corp.jabil.org/eDashboardPlus/_webforms/rep_serialnumbers_bystep.aspx").responseText)
