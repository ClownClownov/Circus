import requests
import pyMeow as pm
import keyboard
import pyautogui
import win32api
import win32api, win32con
import time
import win32gui, win32console
import customtkinter
from PIL import Image
import PIL
from win32api import GetSystemMetrics
import threading
import pygetwindow
import sys
import os
import triggerbot
import pyautogui
import math
import win32gui


flagon_aniotdathi = False

potok_ogon = threading.Event() #Хуета нажная чтоб поток вызывающий выстрел не запускался многократно
potok_ogon_trig = threading.Event()

thenter_x_otd = GetSystemMetrics(0)/2
thenter_y_otd = GetSystemMetrics(1)/2

thenter_x = GetSystemMetrics(0)/2 #Поиск центра экрана-прицела
thenter_y = GetSystemMetrics(1)/2



win123 = win32console.GetConsoleWindow()#Отключение консоли вроде :)
win32gui.ShowWindow(win123, 0)

def img_resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

class Offsets:
    m_pBoneArray = 496


class Colors:
    orange = pm.get_color("orange")
    black = pm.get_color("black")
    cyan = pm.get_color("cyan")
    white = pm.get_color("white")
    white2 = pm.get_color("white")
    red = pm.get_color("red")
    grey = pm.fade_color(pm.get_color("red"), 0.8)
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
    def vid(self):
        return pm.r_int(self.proc, self.pawn_ptr + Offsets.m_entitySpottedState + Offsets.m_bSpottedByMask)

    @property
    def otd(self): #Углы отдачи (изменяются только после выстрела)
        return pm.r_vec3(self.proc, self.pawn_ptr + Offsets.m_aimPunchAngle)

    @property
    def detect_vistrela(self):#Смотрим стеляем ли мы (для атиотдачи)
        return pm.r_int(self.proc, self.pawn_ptr + Offsets.m_iShotsFired)

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

def vistrell():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0 , 0 , 0, 0)
    time.sleep(dlit_otheredi)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0 , 0 , 0, 0)
    



def deagonal_cont_streif(klav1, klav2, kt_klav1, kt_klav2):
    keyboard.block_key(klav1)
    time.sleep(0.01)
    keyboard.block_key(klav2)
    time.sleep(0.01)
    keyboard.release(klav1)
    time.sleep(0.01)
    keyboard.release(klav2)
    time.sleep(0.02)
    keyboard.press(kt_klav1)
    time.sleep(0.01)
    keyboard.press(kt_klav2)
    time.sleep(0.08)
    keyboard.release(kt_klav1)
    time.sleep(0.01)
    keyboard.release(kt_klav2)
    time.sleep(0.01)
    vistrell()
    keyboard.unblock_key(klav1)
    time.sleep(0.01)
    keyboard.unblock_key(klav2)
    time.sleep(0.01)
    if keyboard.is_pressed(klav2) and keyboard.is_pressed(klav1):
        time.sleep(0.01)
        keyboard.press(klav1)
        time.sleep(0.01)
        keyboard.press(klav2)
    time.sleep(zad_m_vistri)

def cont_streif(klav, kt_klav):
    keyboard.block_key(klav)
    time.sleep(0.01)
    keyboard.release(klav)
    time.sleep(0.02)
    keyboard.press(kt_klav)
    time.sleep(0.08)
    keyboard.release(kt_klav)
    time.sleep(0.01)
    vistrell()
    time.sleep(0.01)
    keyboard.unblock_key(klav)
    if keyboard.is_pressed(klav):
        time.sleep(0.01)
        keyboard.press(klav)
    time.sleep(zad_m_vistri)  
    
 



 
def Ogon():
    potok_ogon.set() #предотвращение запуска если такой поток уже работает
    if kt_streif == 1 and not keyboard.is_pressed('ctrl'):
        if keyboard.is_pressed(17) and keyboard.is_pressed(30):
            deagonal_cont_streif(17,30,31,32)
        elif keyboard.is_pressed(17) and keyboard.is_pressed(32):
            deagonal_cont_streif(17,32,31,30)
        elif keyboard.is_pressed(31) and keyboard.is_pressed(30):
            deagonal_cont_streif(31,30,17,32)
        elif keyboard.is_pressed(31) and keyboard.is_pressed(32):
            deagonal_cont_streif(31,32,17,30)
        elif keyboard.is_pressed(17):
            cont_streif(17,31)
        elif keyboard.is_pressed(30):
            cont_streif(30,32)
        elif keyboard.is_pressed(31):
            cont_streif(31,17)
        elif keyboard.is_pressed(32):
            cont_streif(32,30)    
            
        else:
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0 , 0 , 0, 0)
            time.sleep(dlit_otheredi )
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0 , 0 , 0, 0)
            time.sleep(zad_m_vistri)
    else:
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0 , 0 , 0, 0)
        time.sleep(dlit_otheredi)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0 , 0 , 0, 0)
        time.sleep(zad_m_vistri)
        

    potok_ogon.clear()
    time.sleep(0.01)

def Ogon_trig():
    potok_ogon_trig.set() #предотвращение запуска если такой поток уже работает
    bot.run()  
    potok_ogon_trig.clear()
    time.sleep(0.01)


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
            "m_entitySpottedState": "C_CSPlayerPawn",
            "m_iShotsFired": "C_CSPlayerPawn", #детект выстрела
            "m_aimPunchAngle": "C_CSPlayerPawn", # углы отдачи
            "m_bSpottedByMask": "EntitySpottedState_t",
            "m_pGameSceneNode": "C_BaseEntity",
            "m_bDormant": "CGameSceneNode",
        }
        clientDll = requests.get("https://raw.githubusercontent.com/a2x/cs2-dumper/main/output/client_dll.json").json()
        [setattr(Offsets, k, clientDll["client.dll"]["classes"][client_dll_name[k]]["fields"][k]) for k in client_dll_name]

    def it_entities(self):
        ent_list = pm.r_int64(self.proc, self.mod + Offsets.dwEntityList)
        global local
        local = pm.r_int64(self.proc, self.mod + Offsets.dwLocalPlayerController)

        for i in range(1, 65):
            try:
                entry_ptr = pm.r_int64(self.proc, ent_list + (8 * (i & 0x7FFF) >> 9) + 16)
                global controller_ptr
                controller_ptr = pm.r_int64(self.proc, entry_ptr + 120 * (i & 0x1FF))

                    
                
                controller_pawn_ptr = pm.r_int64(self.proc, controller_ptr + Offsets.m_hPlayerPawn)
                list_entry_ptr = pm.r_int64(self.proc, ent_list + 0x8 * ((controller_pawn_ptr & 0x7FFF) >> 9) + 16)
                pawn_ptr = pm.r_int64(self.proc, list_entry_ptr + 120 * (controller_pawn_ptr & 0x1FF))
            except:
                continue

            yield Entity(controller_ptr, pawn_ptr, self.proc)



    def run(self):
        pm.overlay_init("Counter-Strike 2", fps= int(fps_th) )
        kom = 'kt'
        s_zap = 6
        s = 0
        thel = 1
        thel2 = 0
        im_thel = "q"
        
        old_punch_x = 0.0
        old_punch_y = 0.0

        while pm.overlay_loop() and stop == True:
            view_matrix = pm.r_floats(self.proc, self.mod + Offsets.dwViewMatrix, 16)
        
            pm.begin_drawing()
            pm.draw_fps(0, 0)




            for ent in self.it_entities():

                if controller_ptr == local:
                    if antiotd_obith == 1 and not keyboard.is_pressed(aim) and not potok_ogon.is_set() and win32api.GetAsyncKeyState(0x01) < 0: #Антиотдача на обычные выстрелы
                        if controller_ptr == local and int(ent.detect_vistrela) > 1:
                            delta_x = (ent.otd['y'] - old_punch_y) * nast_antiotd_obith
                            delta_y = (ent.otd['x'] - old_punch_x) * -nast_antiotd_obith

                            move_x = int(delta_x / 0.022)
                            move_y = int(delta_y / 0.022)

                            win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, move_x, move_y, 0, 0)

                            old_punch_x = ent.otd['x']
                            old_punch_y = ent.otd['y']
                        elif controller_ptr == local and int(ent.detect_vistrela) < 1:
                            old_punch_x = 0.0
                            old_punch_y = 0.0
                            


                    if aim_anti_otdatha_if == 1:
                        thenter_prit_otd_x = thenter_x_otd - ((ent.otd['y'] * (thenter_x_otd*2)) / 90)#тут х и у местами поменяны скорее всего в переменной онди идут в другом порядке хз
                        thenter_prit_otd_y = thenter_y_otd + ((ent.otd['x'] * (thenter_y_otd*2)) / 90)

                        if keyboard.is_pressed(aim) and int(ent.detect_vistrela) != 0:
                            flagon_aniotdathi = True

                        if not keyboard.is_pressed(aim) and not int(ent.detect_vistrela) != 0:
                            flagon_aniotdathi = False
                        
                        if flagon_aniotdathi == False:
                            thenter_x = thenter_x_otd
                            thenter_y = thenter_y_otd
                        else:
                            thenter_x = thenter_prit_otd_x
                            thenter_y = thenter_prit_otd_y
                    elif aim_anti_otdatha_if == 0:
                        thenter_x = thenter_x_otd
                        thenter_y = thenter_y_otd


                
                if ent.wts(view_matrix) and ent.health > 0 and not ent.dormant and controller_ptr != local:
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
                        pm.draw_circle_lines(
                        thenter_x ,
                        thenter_y ,
                        radius_poika,
                        Colors.white2,
                        )
                    
                    
                    if (ent.team != 2 and kom == 'kt' or ent.team == 2 and kom == 't') or kom == 't_kt':
                        head = ent.pos2d["y"] - ent.head_pos2d["y"]
                        ###
                        width = head / 4
                        center = width / 2
                                             #Насрано пиздец я уже забыл что это
                        width2 = head / 2
                        center2 = width2 / 2
                        ###
                        imia = f"{ent.name}"

                        
                        if telo == 0:
                            p_telo = 7
                        else:
                            p_telo = 3

                        thenter_y2 = thenter_y #костыль лень переделывать
                        #Голова или тело аим
                        if aim_telo == True or (aim_telo_50 == True and int(f"{ent.health}") < 50):                          
                            x_gol_rast = thenter_x - ent.head_pos2d["x"]
                            y_gol_rast = thenter_y2 - (ent.head_pos2d["y"] - int(head - center * 10))
                            x_gol = ent.head_pos2d["x"]
                            y_gol = ent.head_pos2d["y"] - int(head - center * 10)
                        else:                           
                            x_gol_rast = thenter_x - ent.head_pos2d["x"]
                            y_gol_rast = thenter_y2 - (ent.head_pos2d["y"] - int(head - center * 7.8))
                            x_gol = ent.head_pos2d["x"]
                            y_gol = ent.head_pos2d["y"] - int(head - center * 7.8)
                        
                        ###
                        x = x_gol - center / 2
                        y = y_gol - center / 2
                        x2=width - center         #Насрано пиздец я уже забыл что это
                        y2=head - center * p_telo
                        y_aim = head - center * 7
                        ###

                        if keyboard.is_pressed(trig):
                            if levii_triger == 1:
                                if not potok_ogon_trig.is_set():
                                    threading.Thread(target=Ogon_trig, daemon=True).start()
                                
                            else:                                
                                if telo == 0 :
                                    if  (ent.head_pos2d["x"] - center / 2) + (x2 / 3) < thenter_x < ((ent.head_pos2d["x"] - center / 2) + x2) - x2 / 3: # x + (x2 / 4) < thenter_x < (x + x2) - x2 / 4
                                        if (ent.head_pos2d["y"] - center / 2) < thenter_y < ((ent.head_pos2d["y"] - center / 2) + y2) - y2 / 3:          
                                            if not potok_ogon.is_set():
                                                threading.Thread(target=Ogon, daemon=True).start()
                                else:
                                    if  (ent.head_pos2d["x"] - center / 2) + (x2 / 4) < thenter_x < ((ent.head_pos2d["x"] - center / 2) + x2) - x2 / 4:
                                        if (ent.head_pos2d["y"] - center / 2) < thenter_y < ((ent.head_pos2d["y"] - center / 2) + y2) - y2 / 7:          
                                            if not potok_ogon.is_set():
                                                threading.Thread(target=Ogon, daemon=True).start()
                                            


                            
                        #Видит ли чит чела
                        if int(aim_steni_if) == 1:
                            vigu = ent.vid
                        else:
                            vigu = 1
                            
                        #Фильтрация челов
                        if (((thenter_x + radius_poika > x > thenter_x - radius_poika) and (thenter_y2 + radius_poika > y > thenter_y2 - radius_poika))
                            and im_thel == "q") and vigu > 0:
                            im_thel = f"{ent.name}"

                        if (thenter_x + radius_poika > x > thenter_x - radius_poika) and (thenter_y2 + radius_poika > y > thenter_y2 - radius_poika):
                            if f"{ent.name}" == im_thel:
                                s = 0
                                thel2 = 1
                            else:
                                s = s + 1
                                thel2 = 0

                            if s >= s_zap or vigu == 0:
                                im_thel = "q"


                        
                        #Аим                
                        if (keyboard.is_pressed(aim)) and im_thel == f"{ent.name}" and math.sqrt((thenter_x - x_gol) ** 2 + (thenter_y - y_gol) ** 2) < radius_poika:
                            rast_do_gol = math.sqrt((x_gol_rast) ** 2 + (y_gol_rast) ** 2)
                            skorost_x = rast_do_gol
                            skorost_y = rast_do_gol
                            if abs(x_gol_rast) < skorost_aim:
                                skorost_x = int(abs(x_gol_rast))
                            else:
                                skorost_x = skorost_aim

                            skorost_x = int(skorost_x * mnosz_usk_navodki)

                            if thenter_x > x_gol:
                                win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, -skorost_x, 0, 0, 0)
                            else:
                                win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, skorost_x, 0, 0, 0)

                            if abs(y_gol_rast) < skorost_aim:
                                skorost_y = int(abs(y_gol_rast))
                            else:
                                skorost_y = skorost_aim

                            skorost_y = int(skorost_y * mnosz_usk_navodki)

                            if thenter_y > y_gol:
                                win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, 0, -skorost_y, 0, 0)
                            else:
                                win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, 0, skorost_y, 0, 0)

                            if aim_ogon == 1 and rast_do_gol < 2 and not potok_ogon.is_set():
                                threading.Thread(target=Ogon, daemon=True).start()
                                

                                

   
                        # Box Golova
                        pm.draw_circle(
                            ent.head_pos2d["x"],
                            ent.head_pos2d["y"] - center / 4,
                            head - center * 7.5,
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
                           1.5,
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
            time.sleep(0.0001)

global stop
stop = False

lock = threading.Lock()

def Zapysk2() :
    with lock:
        global trig
        trig = knop_trig.get()
        global aim 
        aim = knop_aim.get()
        global fps_th 
        fps_th = FPS_t.get()
        global telo 
        telo = trig_na_telo.get()
        global box_telo 
        box_telo = hitt_box_telo.get()
        global mnosz_usk_navodki
        mnosz_usk_navodki = float(mnojit_usk.get())
        global zona_zamed_navodki
        zona_zamed_navodki = float(mnojit_usk.get()) + 3
        global radius_poika
        radius_poika = int(kvadrat_the.get()) / 2
        global skorost_aim
        skorost_aim = int(skor_aim.get())
        global aim_ogon
        aim_ogon = int(aim_og.get())
        global kvadrat_poiska
        kvadrat_poiska = int(ot_kvadrat.get())
        global aim_telo
        aim_telo = int(aim_v_telo.get())
        global aim_telo_50
        aim_telo_50 = int(aim_v_telo_50.get())
        global dlit_otheredi
        dlit_otheredi = float(dlit_othered.get())
        global aim_steni_if
        aim_steni_if = int(aim_steni.get())
        global zad_m_vistri
        zad_m_vistri = float(zad_m_vistr.get())
        global kt_streif 
        kt_streif = Kontr_stre.get()
        global levii_triger 
        levii_triger = lev_trig.get()
        global aim_anti_otdatha_if
        aim_anti_otdatha_if = int(aim_anti_otdatha.get())
        global antiotd_obith
        antiotd_obith = int(antiotd_ob.get())
        global nast_antiotd_obith
        nast_antiotd_obith = float(nast_antiotd_ob.get())


        if not('PyMeow' in pygetwindow.getAllTitles()):
            global stop
            stop = False
            Zapysk()


        with open('nastroiki.txt', 'r+') as file:
            file.truncate(0)
            file.write(str(trig)+"\n"+str(aim)+"\n"+str(fps_th)+"\n"+str(int(mnosz_usk_navodki))
                       +"\n"+str(int(zona_zamed_navodki))+"\n"+str(int(radius_poika)*2)+"\n"+str(telo)
                       +"\n"+str(box_telo)+"\n"+str(skorost_aim)+"\n"+str(aim_ogon)+"\n"+str(kvadrat_poiska)
                       +"\n"+str(aim_telo)+"\n"+str(aim_telo_50)+"\n"+str(dlit_otheredi)+"\n"+str(aim_steni_if)
                       +"\n"+str(zad_m_vistri)+"\n"+str(kt_streif)+"\n"+str(levii_triger)+"\n"+str(aim_anti_otdatha_if)
                       +"\n"+str(antiotd_obith)+"\n"+str(nast_antiotd_obith))


def Zapysk() :
    
    global stop


    if stop == True:
        Zapysk2()
        
    elif stop == False:
        global trig
        trig = knop_trig.get()
        global aim 
        aim = knop_aim.get()
        global fps_th 
        fps_th = FPS_t.get()
        global telo 
        telo = trig_na_telo.get()
        global box_telo 
        box_telo = hitt_box_telo.get()
        global mnosz_usk_navodki
        mnosz_usk_navodki = float(mnojit_usk.get())
        global zona_zamed_navodki
        zona_zamed_navodki = float(mnojit_usk.get()) + 3
        global radius_poika
        radius_poika = int(kvadrat_the.get()) / 2
        global skorost_aim
        skorost_aim = int(skor_aim.get())
        global aim_ogon
        aim_ogon = int(aim_og.get())
        global kvadrat_poiska
        kvadrat_poiska = int(ot_kvadrat.get())
        global aim_telo
        aim_telo = int(aim_v_telo.get())
        global aim_telo_50
        aim_telo_50 = int(aim_v_telo_50.get())
        global dlit_otheredi
        dlit_otheredi = float(dlit_othered.get())
        global aim_steni_if
        aim_steni_if = int(aim_steni.get())
        global zad_m_vistri
        zad_m_vistri = float(zad_m_vistr.get())
        global kt_streif 
        kt_streif = Kontr_stre.get()
        global levii_triger 
        levii_triger = lev_trig.get()
        global aim_anti_otdatha_if
        aim_anti_otdatha_if = int(aim_anti_otdatha.get())
        global antiotd_obith
        antiotd_obith = int(antiotd_ob.get())
        global nast_antiotd_obith
        nast_antiotd_obith = float(nast_antiotd_ob.get())



        with open('nastroiki.txt', 'r+') as file:
            file.truncate(0)
            file.write(str(trig)+"\n"+str(aim)+"\n"+str(fps_th)+"\n"+str(int(mnosz_usk_navodki))
                       +"\n"+str(int(zona_zamed_navodki))+"\n"+str(int(radius_poika)*2)+"\n"+str(telo)
                       +"\n"+str(box_telo)+"\n"+str(skorost_aim)+"\n"+str(aim_ogon)+"\n"+str(kvadrat_poiska)
                       +"\n"+str(aim_telo)+"\n"+str(aim_telo_50)+"\n"+str(dlit_otheredi)+"\n"+str(aim_steni_if)
                       +"\n"+str(zad_m_vistri)+"\n"+str(kt_streif)+"\n"+str(levii_triger)+"\n"+str(aim_anti_otdatha_if)
                       +"\n"+str(antiotd_obith)+"\n"+str(nast_antiotd_obith))
        stop = True
        try:
            global bot
            bot = triggerbot.TriggerBot()  # Левый тригер лучше моего
            threading.Thread(target=Start, daemon=True).start()
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
    nastroiki.write("alt\nx\n100\n1.0\n8\n300\n0\n0\n15\n1\n1\n0\n0\n0.1\n0\n0.6\n0\n0\n0\n0\n0.55")

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
    dlit_otheredi = nastroiki.readline().strip()
    aim_steni_if = nastroiki.readline().strip()
    zad_m_vistri = nastroiki.readline().strip()
    Kontr_streif = nastroiki.readline().strip()
    lev_triger = nastroiki.readline().strip()
    aim_anti_otdatha_if = nastroiki.readline().strip()
    antiotd_obith = nastroiki.readline().strip()
    nast_antiotd_obith = nastroiki.readline().strip()
    nastroiki.close()
    

def flagok():
    aim_v_telo_50.deselect()

def flagok50():
    aim_v_telo.deselect()
        
def update_interface():
    app.after(100000, update_interface)

    
app = customtkinter.CTk()
customtkinter.deactivate_automatic_dpi_awareness()
app.title("Circus: Точно без багов...")
app.geometry("700x650")
icon_path = img_resource_path('123.ico')
app.iconbitmap(icon_path)

app.grid_columnconfigure(0, weight=1)
app.resizable(width=False, height=False) 


#Кнопка старта
button = customtkinter.CTkButton(app, text="Запуск (или) Применить настройки", command=Zapysk)
button.grid(row=0, column=0, padx=20, pady=20, sticky="ew",columnspan=2)


#Кнопка тригера
label = customtkinter.CTkLabel( app, text = "Кнопка тригера (учитывайте язык ввода!) можно писать alt и т.п.:" )
label.place(x=20,y=60)

knop_trig = customtkinter.CTkEntry( app)
knop_trig.place(x=425,y=60)
knop_trig.configure (width=31)
knop_trig.insert(0, knopka_trigera)
    #Тригер на тело галочка
trig_na_telo = customtkinter.CTkCheckBox( app, text="Реагаровать на тело?")
trig_na_telo.place(x=460,y=60)
if triger_telo == "1":
    trig_na_telo.select()
else:
    trig_na_telo.deselect()
    #Хитбокс тела галочка
hitt_box_telo = customtkinter.CTkCheckBox( app, text="Включить бокс тела?")
hitt_box_telo.place(x=460,y=90)
if hit_box_telo == "1":
    hitt_box_telo.select()
else:
    hitt_box_telo.deselect()
    #Использовать левый тригер
lev_trig = customtkinter.CTkCheckBox( app, text="Альтернативный триггер, только на врагов и в прямой видимости")
lev_trig.place(x=20,y=90)
if lev_triger == "1":
    lev_trig.select()
else:
    lev_trig.deselect()

#Кнопка аим
label = customtkinter.CTkLabel(app, text = "Кнопка тригера АИМ-Асист:" )
label.place(x=20,y=140)

knop_aim = customtkinter.CTkEntry(app)
knop_aim.place(x=194,y=140)
knop_aim.configure (width=31)
knop_aim.insert(0, knopka_aim)
    #Стрельба аим галочка
aim_og = customtkinter.CTkCheckBox(app, text="Стрелять при наведении?")
aim_og.place(x=230,y=140)
if aim_ogon == "1":
    aim_og.select()
else:
    aim_og.deselect()
    #Очередь аима
label = customtkinter.CTkLabel(app, text = "Длительность очереди AIM в секундах (можно дробные):" )
label.place(x=20,y=170)

dlit_othered = customtkinter.CTkEntry(app)
dlit_othered.place(x=376,y=170)
dlit_othered.configure (width=35)
dlit_othered.insert(0, dlit_otheredi)
    #Задержка между выстрелами(очередями)
label = customtkinter.CTkLabel(app, text = "Задержка между выстрелами или очередями:" )
label.place(x=20,y=200)

zad_m_vistr = customtkinter.CTkEntry(app)
zad_m_vistr.place(x=310,y=200)
zad_m_vistr.configure (width=35)
zad_m_vistr.insert(0, zad_m_vistri)
    #Аим в тело ?Аим в тело если >50 ?
aim_v_telo = customtkinter.CTkCheckBox(app, command = flagok, text="Стелять в тело?")
aim_v_telo.place(x=425,y=140)
aim_v_telo_50 = customtkinter.CTkCheckBox(app, command = flagok50, text="Стелять в тело если меньше 50хр?")
aim_v_telo_50.place(x=425,y=170)
if aim_telo == "1":
    aim_v_telo.select()
else:
    aim_v_telo.deselect()
if aim_telo_50 == "1":
    aim_v_telo_50.select()
else:
    aim_v_telo_50.deselect()
    #Котрстрейф
Kontr_stre = customtkinter.CTkCheckBox(app, text="Делать кон-стрейф перед выстрелом?")
Kontr_stre.place(x=425,y=200)
if Kontr_streif == "1":
    Kontr_stre.select()
else:
    Kontr_stre.deselect()
    #Учитывать препятствия?
aim_steni = customtkinter.CTkCheckBox(app, text="AIM будет стрелять только в видимых противников (Работает с задержкой и только вблизи прицела)")
aim_steni.place(x=20,y=230)
if aim_steni_if == "1":
    aim_steni.select()
else:
    aim_steni.deselect()
    #Антиотдача в аим
aim_anti_otdatha = customtkinter.CTkCheckBox(app, text="Использовать антиотдачу в AIM ")
aim_anti_otdatha.place(x=20,y=260)
if aim_anti_otdatha_if == "1":
    aim_anti_otdatha.select()
else:
    aim_anti_otdatha.deselect()
    #Радиус поиска аим
label = customtkinter.CTkLabel(app, text = "Радиус поиска целей АИМ в пикселях:" )
label.place(x=20,y=290)

kvadrat_the = customtkinter.CTkEntry(app)
kvadrat_the.place(x=260,y=290)
kvadrat_the.configure (width=45)
kvadrat_the.insert(0, radius_poiska)
    #Показывать ли квадрат поиска галочка
ot_kvadrat = customtkinter.CTkCheckBox(app, text="Отоброжать радиус поиска целей?")
ot_kvadrat.place(x=310,y=290)
if kvadrat_poiska == "1":
    ot_kvadrat.select()
else:
    ot_kvadrat.deselect()


    #Настройка компенсации отдачи

label = customtkinter.CTkLabel(app, text = "Настройка компенсации отдачи, подбирать эксперементально:" )
label.place(x=20,y=355)

nast_antiotd_ob = customtkinter.CTkEntry(app)
nast_antiotd_ob.place(x=418,y=355)
nast_antiotd_ob.configure (width=65)
nast_antiotd_ob.insert(0, nast_antiotd_obith)

    #Показывать ли квадрат поиска галочка
antiotd_ob = customtkinter.CTkCheckBox(app, text="Компенсация отдачи для обычных выстрелов (требует тонкой индивидуальной настройки)")
antiotd_ob.place(x=20,y=325)
if antiotd_obith == "1":
    antiotd_ob.select()
else:
    antiotd_ob.deselect()

    
    #Множ ускорения наводки
label = customtkinter.CTkLabel(app, text = "Множитель скорости AIM (НЕ ТРОГАТЬ ПРОСТО ТАК!) можно и нужно дробные \"пример 0.8 или 1.2\":" )
label.place(x=20,y=420)

mnojit_usk = customtkinter.CTkEntry(app)
mnojit_usk.place(x=635,y=420)
mnojit_usk.configure (width=35)
mnojit_usk.insert(0, mnosz_usk_navodki)
    #Скорость аим
label = customtkinter.CTkLabel(app, text = "Максимальная скорость наведения AIM (На скорость так-же влияет фпс чита) :" )
label.place(x=20,y=390)

skor_aim = customtkinter.CTkEntry(app)
skor_aim.place(x=512,y=390)
skor_aim.configure (width=45)
skor_aim.insert(0, skorost_aim)

#Ограничение фпс чита
label = customtkinter.CTkLabel(app, text = "FPS Лок!--> (ФПС чита НЕ ДОЛЖЕН БЫТЬ ВЫШЕ ЧЕМ В CS!)(от ФПС зависить скорость наведения):" )
label.place(x=20,y=450)

FPS_t = customtkinter.CTkEntry(app)
FPS_t.place(x=622,y=450)
FPS_t.configure (width=44)
FPS_t.insert(0, fps_thita)

#Инфа
label = customtkinter.CTkLabel(app, text = "Переключения команд f5   f6   f7 " )
label.place(x=250,y=475)

label = customtkinter.CTkLabel(app, text = "Чит не инжектица в игру и не подменяет значения шанс детекта VAC-ом нулевой" )
label.place(x=80,y=580)

label = customtkinter.CTkLabel(app, text = "Вы можете менять все настройки прямо во время игры нажав на кнопку не перезапуская чит, кроме FPS " )
label.place(x=20,y=500)

label = customtkinter.CTkLabel(app, text = "Для корректного запуска в настройках изображения поставьте отображения в\n окне или в окне без рамки, далее в окне чита нажмите запуск с РАЗВЁРНУТОЙ игрой\nне сворачивайте игру во избежании зависаний чита." )
label.place(x=80,y=530)

label = customtkinter.CTkLabel(app, text = "Возможны мелкие недочёты в чите по причине того что я котик у меня лапки" )
label.place(x=100,y=600)


app.mainloop()
  
#Остановка процесса чита
with lock:
    stop = False
