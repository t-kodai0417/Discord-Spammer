from base import send_message,joiner
import random,string,ctypes,os
import tkinter, tkinter.filedialog, tkinter.messagebox
token=[]

def create_string(l):
    return(''.join(random.choice(string.ascii_letters + string.digits) for _ in range(l)))

def string_control(message:str,options={"options":False}):
    if options["options"]!=False:
        try:
            get_custom=options["custom_string"]
            message=message+"| "+get_custom+" |"+create_string(9)
        except:
            message=message+"| "+create_string(9)
    else:
        message=message+"| "+create_string(9)
    return message

def message_box(title,content):
    user32 = ctypes.WinDLL("user32")
    user32.MessageBoxW.restype = ctypes.c_int32
    user32.MessageBoxW.argtypes = (
        ctypes.c_void_p, ctypes.c_wchar_p, ctypes.c_wchar_p, ctypes.c_uint32
    )
    user32.MessageBoxW(None, content, title, 0)


def choose_file():
    root = tkinter.Tk()
    root.withdraw()
    fTyp = [("","*.txt")]
    iDir = os.path.abspath(os.path.dirname(__file__))
    file = tkinter.filedialog.askopenfilename(filetypes = fTyp,initialdir = iDir)
    return file

def ch_spam():
    message_to=input("送信するメッセージを入力してください\n>>")
    to_channel=input("送信先のテキストチャンネルを指定してください。\n>>")
    nankai=int(input("何回実行するの？\n>>"))
    for i in range(nankai):
        print(f'\r{i+1}/{nankai}', end='')
        message_toa=string_control(message_to)
        data_send=send_message(random.choice(token))
        data_send.send(message_toa,int(to_channel))
    start()

def dm_spam():
    message_to=input("送信するメッセージを入力してください\n>>")
    to_channel=input("送信先のUserIDを指定してください。\n>>")
    nankai=int(input("何回実行するの？\n>>"))
    for i in range(nankai):
        print(f'\r{i+1}/{nankai}', end='')
        message_toa=string_control(message_to)
        data_send=send_message(random.choice(token))
        data_send.send(message_toa,int(to_channel),dm=True)
    start()

def ch_typing():
    print("これはテキストチャンネルにしか使えません。")
    to_channel=input("送信先のテキストチャンネルを指定してください。\n>>")
    data_send=send_message(random.choice(token))
    data_send.typing(int(to_channel))
    start()

def srv_joiner():
    server_invite=input("招待リンクを入力してください\n>>")
    data_join=joiner(random.choice(token))
    data_join.join(server_invite)
    start()



print("Bom Spammer\nDeveloped by Kodai.")
message_box("Tokenを入れる","Tokenが改行で区切られて入ってるtxtを指定してください。")
get_file=choose_file()
with open(get_file,"r") as f:
    token=f.read().split('\n')
print(f"{len(token)}個のTokenを取得。")
def start():
    print("何をしますか？")
    one_select=input(
        "<1> Channel Spam"+'\n'+
        "<2> DM Spam"+'\n'+
        "<3> Typing"+'\n'+
        "<4> Joiner"+'\n'+
        "<5> Exit"+'\n'+">>"
    )
    try:
        one_select=int(one_select)
    except:
        start()
    if 1<=one_select and 5>=one_select:
        if one_select==1:
            ch_spam()
        elif one_select==2:
            dm_spam()
        elif one_select==3:
            ch_typing()
        elif one_select==4:
            srv_joiner()
        else:
            exit()
    else:
        start()

start()
  
