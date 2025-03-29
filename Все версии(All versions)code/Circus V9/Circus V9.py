import requests
import pyMeow as pm
import keyboard
import pyautogui
import win32api
import win32api, win32con
import time
import win32gui, win32console
from tkinter import *
from tkinter import ttk
import tkinter as tk
from win32api import GetSystemMetrics
import threading
from queue import Queue
import pygetwindow

thenter_x = GetSystemMetrics(0)/2
thenter_y = GetSystemMetrics(1)/2

win123 = win32console.GetConsoleWindow()
win32gui.ShowWindow(win123, 0)


class Offsets:
    m_pBoneArray = 496


class Colors:
    orange = pm.get_color("orange")
    black = pm.get_color("black")
    cyan = pm.get_color("cyan")
    white = pm.get_color("white")
    red = pm.get_color("red")
    grey = pm.fade_color(pm.get_color("red"), 0.3)
    grey1 = pm.fade_color(pm.get_color("blue"), 0.3)
    grey2 = pm.fade_color(pm.get_color("#242625"), 0)


class Entity:
    def __init__(self, ptr, pawn_ptr, proc):
        self.ptr = ptr
        self.pawn_ptr = pawn_ptr
        self.proc = proc
        self.pos2d = None
        self.head_pos2d = None

    @property
    def name(self):
        return pm.r_string(self.proc, self.ptr + Offsets.m_iszPlayerName)

    @property
    def health(self):
        return pm.r_int(self.proc, self.pawn_ptr + Offsets.m_iHealth)

    @property
    def team(self):
        return pm.r_int(self.proc, self.pawn_ptr + Offsets.m_iTeamNum)

    @property
    def pos(self):
        return pm.r_vec3(self.proc, self.pawn_ptr + Offsets.m_vOldOrigin)
    
    @property
    def dormant(self):
        return pm.r_bool(self.proc, self.pawn_ptr + Offsets.m_bDormant)

    def bone_pos(self, bone):
        game_scene = pm.r_int64(self.proc, self.pawn_ptr + Offsets.m_pGameSceneNode)
        bone_array_ptr = pm.r_int64(self.proc, game_scene + Offsets.m_pBoneArray)
        return pm.r_vec3(self.proc, bone_array_ptr + bone * 32)
    
    def wts(self, view_matrix):
        try:
            self.pos2d = pm.world_to_screen(view_matrix, self.pos, 1)
            self.head_pos2d = pm.world_to_screen(view_matrix, self.bone_pos(6), 1)
        except:
            return False
        return True
    

class CS2Esp:
    def __init__(self):
        self.proc = pm.open_process("cs2.exe")
        self.mod = pm.get_module(self.proc, "client.dll")["base"]

        offsets_name = ["dwViewMatrix", "dwEntityList", "dwLocalPlayerController", "dwLocalPlayerPawn"]
        offsets = requests.get("https://raw.githubusercontent.com/a2x/cs2-dumper/main/output/offsets.json").json()
        [setattr(Offsets, k, offsets["client.dll"][k]) for k in offsets_name]

        client_dll_name = {
            "m_iIDEntIndex": "C_CSPlayerPawnBase",
            "m_hPlayerPawn": "CCSPlayerController",
            "m_fFlags": "C_BaseEntity",
            "m_iszPlayerName": "CBasePlayerController",
            "m_iHealth": "C_BaseEntity",
            "m_iTeamNum": "C_BaseEntity",
            "m_vOldOrigin": "C_BasePlayerPawn",
            "m_pGameSceneNode": "C_BaseEntity",
            "m_bDormant": "CGameSceneNode",
        }
        clientDll = requests.get("https://raw.githubusercontent.com/a2x/cs2-dumper/main/output/client_dll.json").json()
        [setattr(Offsets, k, clientDll["client.dll"]["classes"][client_dll_name[k]]["fields"][k]) for k in client_dll_name]

    def it_entities(self):
        ent_list = pm.r_int64(self.proc, self.mod + Offsets.dwEntityList)
        local = pm.r_int64(self.proc, self.mod + Offsets.dwLocalPlayerController)

        for i in range(1, 65):
            try:
                entry_ptr = pm.r_int64(self.proc, ent_list + (8 * (i & 0x7FFF) >> 9) + 16)
                controller_ptr = pm.r_int64(self.proc, entry_ptr + 120 * (i & 0x1FF))

                if controller_ptr == local:
                    continue
                
                controller_pawn_ptr = pm.r_int64(self.proc, controller_ptr + Offsets.m_hPlayerPawn)
                list_entry_ptr = pm.r_int64(self.proc, ent_list + 0x8 * ((controller_pawn_ptr & 0x7FFF) >> 9) + 16)
                pawn_ptr = pm.r_int64(self.proc, list_entry_ptr + 120 * (controller_pawn_ptr & 0x1FF))
            except:
                continue

            yield Entity(controller_ptr, pawn_ptr, self.proc)

    def ogon(self):
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, True , True , 0, 0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, True , True , 0, 0)

    def run(self):
        pm.overlay_init("Counter-Strike 2", fps= int(fps_th) )
        kom = 'kt'
        s_zap = 6
        s = 0
        thel = 1
        thel2 = 0
        im_thel = "q"
        while pm.overlay_loop() and stop == True:
            view_matrix = pm.r_floats(self.proc, self.mod + Offsets.dwViewMatrix, 16)
        
            pm.begin_drawing()
            pm.draw_fps(0, 0)


        
            for ent in self.it_entities():
                if ent.wts(view_matrix) and ent.health > 0 and not ent.dormant:
                    color = Colors.cyan if ent.team != 2 else Colors.orange

                    

                    if keyboard.is_pressed('f7'):
                        kom = 't_kt'
                        s_zap = 12
                    if keyboard.is_pressed('f6'):
                        kom = 't'
                        s_zap = 6
                    if keyboard.is_pressed('f5'):
                        kom = 'kt'
                        s_zap = 6

                    if kvadrat_poiska == 1:    
                    # Box radius_poika aim
                        pm.draw_rectangle_lines(
                        thenter_x - radius_poika,
                        thenter_y - radius_poika,
                        radius_poika*2,
                        radius_poika*2,
                        Colors.white,
                        1,
                        )
                    
                    
                    if (ent.team != 2 and kom == 'kt' or ent.team == 2 and kom == 't') or kom == 't_kt':
                        head = ent.pos2d["y"] - ent.head_pos2d["y"]
                        width = head / 4
                        center = width / 2

                        width2 = head / 2
                        center2 = width2 / 2

                        imia = f"{ent.name}"

                        
                        if telo == 0:
                            p_telo = 7
                        else:
                            p_telo = 3
                        
                        x = ent.head_pos2d["x"] - center / 2
                        y = ent.head_pos2d["y"] - center / 2
                        x2=width - center
                        y2=head - center * p_telo
                        y_aim = head - center * 7

                        #старый тригер

                        if keyboard.is_pressed(trig):
                            if telo == 0 :
                                if  x + (x2 / 3) < thenter_x < (x + x2) - x2 / 3: # x + (x2 / 4) < thenter_x < (x + x2) - x2 / 4
                                    if y < thenter_y < (y + y2) - y2 / 3:          
                                        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, True , True , 0, 0)
                                        time.sleep(0.05)
                                        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, True , True , 0, 0)
                            else:
                                if  x + (x2 / 4) < thenter_x < (x + x2) - x2 / 4:
                                    if y < thenter_y < (y + y2) - y2 / 7:          
                                        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, True , True , 0, 0)
                                        time.sleep(0.05)
                                        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, True , True , 0, 0)


                        #Выделение чела другим цветом

                        
                        #Голова или тело аим
                        if aim_telo == True or (aim_telo_50 == True and int(f"{ent.health}") < 50):
                            thenter_y2 = thenter_y - (head - center * 6)
                        else:
                            thenter_y2 = thenter_y

                        
                        #Фильтрация челов
                        if ((thenter_x + radius_poika > x > thenter_x - radius_poika) and (thenter_y2 + radius_poika > y > thenter_y2 - radius_poika)) and im_thel == "q":
                            im_thel = f"{ent.name}"

                        if (thenter_x + radius_poika > x > thenter_x - radius_poika) and (thenter_y2 + radius_poika > y > thenter_y2 - radius_poika):
                            if f"{ent.name}" == im_thel:
                                s = 0
                                thel2 = 1
                            else:
                                s = s + 1
                                thel2 = 0

                            if s >= s_zap:
                                im_thel = "q"


    
                                        
                        if (keyboard.is_pressed(aim)) and im_thel == f"{ent.name}":

                            #ускорение доводки
                            if not( y - zona_zamed_navodki > thenter_y < ((y + y_aim) - y_aim / 3) + zona_zamed_navodki or y - zona_zamed_navodki < thenter_y > ((y + y_aim) - y_aim / 3)+zona_zamed_navodki):
                                if not((x + (x2 / 3)) - zona_zamed_navodki > thenter_x < ((x + x2) - x2 / 3) + zona_zamed_navodki or (x + (x2 / 3)) - zona_zamed_navodki < thenter_x > ((x + x2) - x2 / 3) + zona_zamed_navodki):
                                    skorost_aim2 = skorost_aim
                                else:
                                    skorost_aim2 = skorost_aim * mnosz_usk_navodki
                            else:
                                skorost_aim2 = skorost_aim * mnosz_usk_navodki
                                
                            #аим доводка 
                                        
                            if thenter_x + radius_poika/1.3 > x > thenter_x - radius_poika:

                                if not( y - zona_zamed_navodki > thenter_y2 < ((y + y_aim) - y_aim / 3) + zona_zamed_navodki or y - zona_zamed_navodki < thenter_y2 > ((y + y_aim) - y_aim / 3)+zona_zamed_navodki):
                                    skorost_aim_y = skorost_aim 
                                else:
                                    skorost_aim_y = skorost_aim2
                                
                                if y > thenter_y2 < (y + y_aim) - y_aim / 3 and y < thenter_y2 + radius_poika :
                                     win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, 0, skorost_aim_y, 0, 0)
                                elif y < thenter_y2 > (y + y_aim) - y_aim / 3 and thenter_y2 - radius_poika < (y + y_aim) - y_aim / 3 :
                                     win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, 0, -(skorost_aim_y), 0, 0)
                                     

                            if thenter_y2 + radius_poika > y > thenter_y2 - radius_poika:

                                if not((x + (x2 / 3)) - zona_zamed_navodki > thenter_x < ((x + x2) - x2 / 3) + zona_zamed_navodki or (x + (x2 / 3)) - zona_zamed_navodki < thenter_x > ((x + x2) - x2 / 3) + zona_zamed_navodki):
                                    skorost_aim_x = skorost_aim
                                else:
                                    skorost_aim_x = skorost_aim2
                                
                                if x + (x2 / 3) > thenter_x < (x + x2) - x2 / 3 and x + (x2 / 3) < thenter_x + radius_poika:
                                     win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, skorost_aim_x, 0, 0, 0) 
                                elif x + (x2 / 3) < thenter_x > (x + x2) - x2 / 3 and thenter_x - radius_poika < (x + x2) - x2 / 3:
                                     win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, -(skorost_aim_x), 0, 0, 0)
                            #тригерр       
                            if aim_ogon == 1:
                                if not( y > thenter_y2 < (y + y_aim) - y_aim / 3 or y < thenter_y2 > (y + y_aim) - y_aim / 3) :
                                    if not(x + (x2 / 3) > thenter_x < (x + x2) - x2 / 3 or x + (x2 / 3) < thenter_x > (x + x2) - x2 / 3) :
                                        thread1 = threading.Thread(target=self.ogon)
                                        thread1.start()

                                     



                        if True:    
                            # Box Golova
                            pm.draw_rectangle(
                                ent.head_pos2d["x"] - center / 2,
                                ent.head_pos2d["y"] - center / 2,
                                width - center,
                                head - center * 7,
                                Colors.grey,
                                )

                        if box_telo == 1:
                                # Box Telo
                                pm.draw_rectangle(
                                    ent.head_pos2d["x"] - center / 2,
                                    ent.head_pos2d["y"] - center / 2,
                                    width - center,
                                    head - center * 3,
                                    Colors.grey1,
                                )
                                pm.draw_rectangle_lines(
                                    ent.head_pos2d["x"] - center / 2,
                                    ent.head_pos2d["y"] - center / 2,
                                    width - center,
                                    head - center * 3,
                                    color,
                                    0,
                                )

                        # Box
                        pm.draw_rectangle(
                            ent.head_pos2d["x"] - center2,
                            ent.head_pos2d["y"] - center2 / 2,
                            width2,
                            head + center2 / 2,
                            Colors.grey2,
                        )
                        pm.draw_rectangle_lines(
                            ent.head_pos2d["x"] - center2,
                            ent.head_pos2d["y"] - center2 / 2,
                            width2,
                            head + center2 / 2,
                            color,
                           1.2,
                        )

                        # Info
                        txt = f"{ent.name} {ent.health}"
                        pm.draw_text(
                            txt,
                            ent.head_pos2d["x"] - pm.measure_text(txt, 15) // 2,
                            ent.head_pos2d["y"] - ((thenter_x*2)/70),
                            15,
                            Colors.white if int(f"{ent.health}") > 50 else Colors.red, 
                        )

            pm.end_drawing()

global stop
stop = False

lock = threading.Lock()

def Zapysk2() :

    with lock:
        global trig
        trig = entry.get()
        global aim 
        aim = entry1.get()
        global fps_th 
        fps_th = entry2.get()
        global pop_trig 
        pop_trig = entry2.get()
        global telo 
        telo = i.get()
        global box_telo 
        box_telo = i2.get()
        global mnosz_usk_navodki
        mnosz_usk_navodki = int(entry3.get())
        global zona_zamed_navodki
        zona_zamed_navodki = int(entry4.get())
        global radius_poika
        radius_poika = int(entry5.get()) / 2
        global skorost_aim
        skorost_aim = int(entry6.get())
        global aim_ogon
        aim_ogon = int(i3.get())
        global kvadrat_poiska
        kvadrat_poiska = int(i4.get())
        global aim_telo
        aim_telo = int(i5.get())
        global aim_telo_50
        aim_telo_50 = int(i6.get())

        if not('PyMeow' in pygetwindow.getAllTitles()):
            global stop
            stop = False
            Zapysk()


        with open('nastroiki.txt', 'r+') as file:
            file.truncate(0)
            file.write(str(trig)+"\n"+str(aim)+"\n"+str(fps_th)+"\n"+str(int(mnosz_usk_navodki))
                       +"\n"+str(int(zona_zamed_navodki))+"\n"+str(int(radius_poika)*2)+"\n"+str(telo)
                       +"\n"+str(box_telo)+"\n"+str(skorost_aim)+"\n"+str(aim_ogon)+"\n"+str(kvadrat_poiska)+"\n"+str(aim_telo)+"\n"+str(aim_telo_50))


def Zapysk() :
    global stop


    if stop == True:
        Zapysk2()
        
    elif stop == False:
        global trig
        trig = entry.get()
        global aim 
        aim = entry1.get()
        global fps_th 
        fps_th = entry2.get()
        global pop_trig 
        pop_trig = entry2.get()
        global telo 
        telo = i.get()
        global box_telo 
        box_telo = i2.get()
        global mnosz_usk_navodki
        mnosz_usk_navodki = int(entry3.get())
        global zona_zamed_navodki
        zona_zamed_navodki = int(entry4.get())
        global radius_poika
        radius_poika = int(entry5.get()) / 2
        global skorost_aim
        skorost_aim = int(entry6.get())
        global aim_ogon
        aim_ogon = int(i3.get())
        global kvadrat_poiska
        kvadrat_poiska = int(i4.get())
        global aim_telo
        aim_telo = int(i5.get())
        global aim_telo_50
        aim_telo_50 = int(i6.get())


        with open('nastroiki.txt', 'r+') as file:
            file.truncate(0)
            file.write(str(trig)+"\n"+str(aim)+"\n"+str(fps_th)+"\n"+str(int(mnosz_usk_navodki))
                       +"\n"+str(int(zona_zamed_navodki))+"\n"+str(int(radius_poika)*2)+"\n"+str(telo)
                       +"\n"+str(box_telo)+"\n"+str(skorost_aim)+"\n"+str(aim_ogon)+"\n"+str(kvadrat_poiska)+"\n"+str(aim_telo)+"\n"+str(aim_telo_50))
        stop = True
        try:
            thread = threading.Thread(target=Start)
            thread.start()
        except:
            stop = False
        
    
    

def Start() :
    esp = CS2Esp()
    esp.run()


#Чтение сохранённых настроек
try:
    nastroiki = open("nastroiki.txt","r")
    nastroiki.close()

except:
    nastroiki = open("nastroiki.txt","w")
    nastroiki.write("alt\nx\n250\n6\n8\n100\n0\n0\n1\n1\n1\n0\n0")

finally:
    nastroiki = open("nastroiki.txt","r")
    knopka_trigera = nastroiki.readline().strip()
    knopka_aim = nastroiki.readline().strip()
    fps_thita = nastroiki.readline().strip()
    mnosz_usk_navodki = nastroiki.readline().strip()
    zona_zamed_navodki = nastroiki.readline().strip()
    radius_poiska = nastroiki.readline().strip()
    triger_telo = nastroiki.readline().strip()
    hit_box_telo = nastroiki.readline().strip()
    skorost_aim = nastroiki.readline().strip()
    aim_ogon = nastroiki.readline().strip()
    kvadrat_poiska = nastroiki.readline().strip()
    aim_telo = nastroiki.readline().strip()
    aim_telo_50 = nastroiki.readline().strip()
    nastroiki.close()
    
if int(triger_telo) == 0:
    triger_telo1 = False
else:
    triger_telo1 = True

if int(hit_box_telo) == 0:
    hit_box_telo1 = False
else:
    hit_box_telo1 = True

if int(aim_ogon) == 0:
    aim_ogon1 = False
else:
    aim_ogon1 = True

if int(kvadrat_poiska) == 0:
    kvadrat_poiska1 = False
else:
    kvadrat_poiska1 = True

if int(aim_telo) == 0:
    aim_telo1 = False
else:
    aim_telo1 = True

if int(aim_telo_50) == 0:
    aim_telo_501 = False
else:
    aim_telo_501 = True


root = Tk()

i=IntVar(value=bool(triger_telo1))
i2=IntVar(value=bool(hit_box_telo1))
i3=IntVar(value=bool(aim_ogon1))
i4=IntVar(value=bool(kvadrat_poiska1))
i5=IntVar(value=bool(aim_telo1))
i6=IntVar(value=bool(aim_telo_501))
root.title("Circus")
root.geometry("500x370")
root.resizable(width=False, height=False) 

#Кнопка тригера
label = Label(root, text = "Кнопка тригера (учитывайте язык ввода!):" )
label.place(x=5, y=50)

entry = Entry(root, font=1)
entry.place(x=240, y=50)
entry.config (width=3)
entry.insert(0, knopka_trigera)

#Кнопка асиста
label1 = Label(root, text = "Кнопка АимАсист:" )
label1.place(x=5, y=95)
checkbox = ttk.Checkbutton(root, text='Стрелять при наведении?',variable=i3)
checkbox.place(x=130, y=95)
checkbox = ttk.Checkbutton(root, text='В тело?',variable=i5)
checkbox.place(x=290, y=95)
checkbox = ttk.Checkbutton(root, text='В тело если XP<50',variable=i6)
checkbox.place(x=350, y=95)
checkbox = ttk.Checkbutton(root, text='Квадрат поиска целей.',variable=i4)
checkbox.place(x=190, y=115)

entry1 = Entry(root, font=1)
entry1.place(x=113, y=90)
entry1.config (width=1)
entry1.insert(0, knopka_aim)
#Скорость наведения аима

label1 = Label(root, text = "Множ. наведения (Чувствительности мыши 4 ставим 1, при 2 став. 2)подбирайте:" )
label1.place(x=5, y=165)

entry6 = Entry(root, font=1)
entry6.place(x=460, y=164)
entry6.config (width=1)
entry6.insert(0, skorost_aim)

#ФПС чита
label2 = Label(root, text = "Лок FPS чита,влияет на скорость AIM в идеале сколько фпс в KS столько и в чите:" )
label2.place(x=5, y=188)
entry2 = Entry(root, font=1)
entry2.place(x=460, y=188)
entry2.config (width=3)
entry2.insert(0, fps_thita)
#Бокс тела
checkbox = ttk.Checkbutton(root, text='Учитывать тело?',variable=i)
checkbox.place(x=265, y=50)
checkbox = ttk.Checkbutton(root, text='Влючить бокс тела? (Чтоб лучше понимать куда ставить прицел для тригера на тело)',variable=i2)
checkbox.place(x=5, y=70)
#Настройка разрешения
label3 = Label(root, text = "Множ.ускорения наведения:          Зона замедления (Множ.ускорения+3 примерно):" )
label3.place(x=5, y=140)

entry3 = Entry(root, font=1)
entry3.place(x=170, y=140)
entry3.config (width=2)
entry3.insert(0, mnosz_usk_navodki)

entry4 = Entry(root, font=1)
entry4.place(x=475, y=140)
entry4.config (width=2)
entry4.insert(0, zona_zamed_navodki)
#Настройка радиуса поиска
label3 = Label(root, text = "Радиус поиска в пикселях:" )
label3.place(x=5, y=115)

entry5 = Entry(root, font=1)
entry5.place(x=155, y=115)
entry5.config (width=3)
entry5.insert(0, radius_poiska)


label3 = Label(root, text = "ВНИМАНИЕ: Если в области действия аим асиста (квадрат "+entry5.get()+"х"+entry5.get()+" пикселей) будет\n 6 и более целей, возможны ошибки наведения. " )
label3.place(x=20, y=210)

label4 = Label(root, text = "Чит не инжектится в игру и не подменяет значения, шанс детекта VAC-ом нулевой." )
label4.place(x=29, y=245)

label5 = Label(root, text = "Для корректного запуска в настройках изображения поставьте отображения в\n окне или в окне без рамки, далее в окне чита нажмите запуск с РАЗВЁРНУТОЙ игрой\nне сворачивайте игру во избежании зависаний чита." )
label5.place(x=5, y=265)

label6 = Label(root, text = "Возможны мелкие недочёты в чите по причине того что я котик у меня лапки" )
label6.place(x=30, y=335)

label7 = Label(root, text = "Переключения сторон f5   f6   f7 " )
label7.place(x=150, y=315)

button = Button(root, text = "Запуск / Изменнение настроек", font=40, command = Zapysk)
button.place(x=140, y=10)


    
root.mainloop()


with lock:
    stop = False
