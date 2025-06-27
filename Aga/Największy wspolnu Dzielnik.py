def najw_wsp_dzieln(a,b):
    if b==0:
        return a
    else:
        return najw_wsp_dzieln(b, a%b)
print(najw_wsp_dzieln(48,18))
