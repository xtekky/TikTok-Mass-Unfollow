import os

try:
    import threading, json, sys, requests, wmi, psutil
    from time import sleep
    from json import JSONDecodeError
except Exception as Nigger:
    input(Nigger)
    sys.exit()

PRNT = threading.Lock()


class Cleaner:
    def __init__(self, ID, SEC, sessid):

        self.sessid       = sessid
        self.id           = ID
        self.SEC          = SEC
        self.err          = 0
        self.current_user = ""
        self.del_count = 0

        self.get_following()
        
    def unfollow(self, idss, User):

        HEAD = {
            'Host': 'api16-normal-c-alisg.tiktokv.com',
            'User-Agent': 'TikTok 20.5.0 rv:205020 (iPhone; iOS 13.5; ONLP@numbers=latn) Cronet',
            'Cookie': f'sessionid={self.sessid}',
            'X-Argus': '6GcIPqHpj254NmWUQL7H2Y32q5Q0QZLjlWwr0QTX1MpzlcXKoHOcsmP6+NLaE9b5DAW40Z4nUMke/0kjuA7g+HXRdtVWir2xSSqxQhdU3cGG9Nc70ZbMsdIZqvbJ4sYVboUdmSJiwMJjvN4SU025JXkYEOpJTpAnSr6Yk4Z96eKzfG8zUJj1rBwpVN2TM2363C2yFFqCg1L52DjKc50pzKBrq23xGVicI9U7Zy/2A1yomyGqq1z8etvIFFuxs+xWeBDdsv77mIkCXQysy4g8PpG78Z0IwNmHSg0Go4OkfEQ123MNUd+bHmAVwyrm6hgUVTmZy6BIiBNqiddYlVbEISwr',
            'X-Gorgon': '8404e0580000025b62c8b99cbe848daa3db9a1398962887e142b',
            'x-common-params-v2': 'language=ar&version_code=20.5.0&app_name=musical_ly&app_version=20.5.0&channel=App%20Store&mcc_mnc=&device_id=7023615385938740741&tz_offset=7200&account_region=&sys_region=JO&aid=1233&residence=JO&screen_width=750&uoo=0&openudid=4bf5c9491d8f851bee9cb8a73a48ce3935a30d6b&os_api=18&os_version=13.5&app_language=ar&tz_name=Asia/Amman&current_region=ONLP&device_platform=iphone&build_number=205020&device_type=iPhone8,1&iid=7027405281118750470&idfa=3D876826-942D-4BFE-A9AA-5E34E6A6E72D&locale=ar&cdid=A0DF5056-F002-4CF3-B02A-1E362753CC57&content_language='
        }

        requests.get(f'https://api16-normal-c-alisg.tiktokv.com/aweme/v1/commit/follow/user/?ac=WIFI&js_sdk_version=1.77.0.2&op_region=ONLP&tma_jssdk_version=1.77.0.2&idfv=3D876826-942D-4BFE-A9AA-5E34E6A6E72D&user_id={idss}&type=0&sec_user_id=&previous_page=following&', headers=HEAD)

        if User == self.current_user:
            return

        self.current_user = User
        self.del_count += 1

        print(f'   [ x ] Unfollowed [{self.del_count}] >> ( {User} ) ')
        os.system(f"title TikTok Wiper ^| Deleted ^> {self.del_count} ^| By Tekky#9999")
    


    def get_following(self):
        while True:
            try:

                HEAD = {
                    'Host': 'api2-16-h2.musical.ly',
                    'Connection': 'keep-alive',
                    'x-tt-store-idc': 'alisg',
                    'x-tt-store-region': 'onlp',
                    'X-SS-DP': '1233',
                    'Cookie': f'sessionid={self.sessid}',
                    'X-Khronos': '1636287035',
                    'X-Pods': '',
                    'X-Gorgon': '8300a60d2001fef8e08b3f7d1eccb4d6a997682985911a998c64',
                    'x-Tt-Token': f'01{self.sessid}0127e2928aa6c29cf7d2757d13ce88f5ec64ced2158c43e6ef61b50bff98482ea80c13528d2a7b2a60028586c336e666116a2255f4944a0502d22f8ed33da2725a37d3ec2c6532b9d3da0054924e91eef7b-1.0.1',
                    'User-Agent': 'TikTok 12.0.0 rv:120008 (iPhone; iOS 13.5; ar_JO@numbers=latn) Cronet'
                }

                info = requests.get(f'https://api2-16-h2.musical.ly/aweme/v1/user/following/list/?version_code=12.0.0&pass-region=1&pass-route=1&language=ar&app_name=musical_ly&vid=D89D043C-FEE3-4404-895E-C9536618B96F&app_version=12.0.0&residence=ONLP&is_my_cn=0&channel=App%20Store&mcc_mnc=&device_id=7023615385938740741&tz_offset=7200&account_region=&sys_region=ONLP&aid=1233&screen_width=750&uoo=0&openudid=b391b6c4a559f59af4481dcf8899e10de5f73803&os_api=18&ac=WIFI&os_version=13.5&app_language=en&tz_name=Asia/Amman&current_region=ONLP&device_platform=iphone&build_number=120008&device_type=iPhone8,1&iid=7027799084266424070&idfa=3D876826-942D-4BFE-A9AA-5E34E6A6E72D&offset=0&sec_user_id={self.SEC}&address_book_access=1&gps_access=0&source_type=2&count=200&user_id={self.id}&max_time=0', headers=HEAD)


                for negg in info.json()["followings"]:
                    idss = negg['uid']
                    User = negg['unique_id']
                    threading.Thread(target=self.unfollow, args=(idss, User,)).start()
            except:
                break


        #print(json.dumps(info.json(), indent=4))


def start(sessid):


    HEAD = {
        'Host': 'api16-normal-c-alisg.tiktokv.com', 
	    'Cookie': f'sessionid={sessid}',
        'Accept-Encoding': 'gzip, deflate',
        'User-Agent': 'com.zhiliaoapp.musically/2022107060 (Linux; U; Android 7.1.2; en_US; G011A; Build/N2G48H;tt-ok/3.10.0.2)'
    }

    GET_ID = requests.get('https://api16-normal-c-alisg.tiktokv.com/passport/account/info/v2/?scene=normal&multi_login=1&account_sdk_source=app&passport-sdk-version=19&os_api=25&device_type=A5010&ssmix=a&manifest_version_code=2018093009&dpi=191&carrier_region=JO&uoo=1&region=US&app_name=musical_ly&version_name=7.1.2&timezone_offset=28800&ts=1628767214&ab_version=7.1.2&residence=SA&cpu_support64=false&current_region=JO&ac2=wifi&ac=wifi&app_type=normal&host_abi=armeabi-v7a&channel=googleplay&update_version_code=2018093009&_rticket=1628767221573&device_platform=android&iid=7396386396296286392&build_number=7.1.2&locale=en&op_region=SA&version_code=200705&timezone_name=Asia%2FShanghai&cdid=f61ca549-c9ee-450b-90da-8854423b74e7&openudid=3e5afbd3f6dde322&sys_region=US&device_id=7296396296396396393&app_language=en&resolution=576*1024&device_brand=OnePlus&language=en&os_version=7.1.2&aid=1233&mcc_mnc=2947',headers = HEAD)

   

    ID = str(GET_ID.json()['data']['user_id'])
    SEC = GET_ID.json()['data']['sec_user_id']

    Cleaner(ID, SEC, sessid)



if __name__ == '__main__':
    os.system('cls' if os.name == 'nt' else 'clear')
    os.system(f"title TikTok Wiper ^| By Tekky#9999")


    sessid = input(r'''             
             ^
            /A\
           //I\\             TikTok Cleaner                \
          ///I\\\               By Tekky#9999               \
         ////I\\\\                 Serverv: discord.gg/onlp  \          
        /////I\\\\\                    Github: @xtekky        >
       //////I\\\\\\               Wipes user following      /
      ///////I\\\\\\\           Speed: very fast            /
     ////////I\\\\\\\\        Enjoy botting !!             /
    /////////I\\\\\\\\\
   //////////I\\\\\\\\\\
    '////////I\\\\\\\\'
      '//////I\\\\\\'        
        '////I\\\\'
          '//I\\'
            'I'    input ~ sessid       > ''')

    print('\n', "___________"*4, "\n\n")
    start(sessid)
