import requests
import pyMeow as pm
import keyboard
import pyautogui
import win32api
import win32api, win32con
import time
import win32gui, win32console
import customtkinter as ctk
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
import webbrowser  # Для открытия веб-страниц

flagon_aniotdathi = False

potok_ogon = threading.Event() #Хуета нажная чтоб поток вызывающий выстрел не запускался многократно
potok_ogon_trig = threading.Event()
potok_anti_otdathi = threading.Event()

thenter_x = GetSystemMetrics(0)/2 #Поиск центра экрана-прицела
thenter_y = GetSystemMetrics(1)/2

thenter_x_otd = thenter_x
thenter_y_otd = thenter_y

#win123 = win32console.GetConsoleWindow()#Отключение консоли вроде :)
#win32gui.ShowWindow(win123, 0)

def img_resource_path(relative_path):
    """ Это для правильной работы картинок auto-py-to-exe """
    try:
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
    white2 = pm.fade_color(pm.get_color("white"), 0.3)
    red = pm.get_color("red")
    grey = pm.fade_color(pm.get_color("red"), 0.8)
    grey1 = pm.fade_color(pm.get_color("blue"), 0.3)
    prozrath = pm.fade_color(pm.get_color("#242625"), 0)
    xp_box = pm.fade_color(pm.get_color("red"), 0.3)

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
    if soroni2 == 0: #Будет ли не мой тригер работать по всем
        bot.attack_all = False
    else:
        bot.attack_all = True
    bot.run()  
    potok_ogon_trig.clear()
    time.sleep(0.01)

def Anti_otdatha_vedenie(move_x, move_y):#Плавная компенсация отдачи (из-за кривости чуть падает точность но не критично)
    potok_anti_otdathi.set()
    for _ in range(5):
        win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, round(move_x/5), round(move_y/5), 0, 0)
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
        global flagon_aniotdathi
        old_vistrel = 0
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
            not_povtor = True #Флажёк чтоб не отрисовывал радиус поиска несколько раз за такт (p.s. уже через время я понял какая это хуета, ну ладно)




            for ent in self.it_entities(): # Типо такт отрисовки

                if controller_ptr == local: #Проверка на пидора(себя)
                    #Антиотдача для обычной стрельбы
                    if antiotd_obith == 1 and not keyboard.is_pressed(aim) and not potok_ogon.is_set() and win32api.GetAsyncKeyState(0x01) < 0:
                        if int(ent.detect_vistrela) > 1:
                            delta_x = (ent.otd['y'] - old_punch_x) * nast_antiotd_obith_x  #тут х и у местами поменяны скорее всего в переменной онди идут в другом порядке хз
                            delta_y = (ent.otd['x'] - old_punch_y) * -nast_antiotd_obith_x

                            move_x = int(delta_x / 0.022)
                            move_y = int(delta_y / 0.022)

                            if antiotd_obith_plav == 1:
                                threading.Thread(target=Anti_otdatha_vedenie, args=(move_x, move_y), daemon=True).start()
                            else:
                                win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, move_x, move_y, 0, 0)

                            old_punch_x = ent.otd['y']
                            old_punch_y = ent.otd['x']
                        else:
                            old_punch_x = 0.0
                            old_punch_y = 0.0

                            


                    if aim_anti_otdatha_if == 1:
                        thenter_prit_otd_x = thenter_x_otd - ((ent.otd['y'] * (thenter_x_otd*2)) / 135)#тут х и у местами поменяны скорее всего в переменной онди идут в другом порядке хз
                        thenter_prit_otd_y = thenter_y_otd + ((ent.otd['x'] * (thenter_y_otd*2)) / 80)

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


                    if soroni2 == 0: #Переключение сторон
                        if ent.team != 2:
                            kom = 't'
                        elif ent.team == 2:
                            kom = 'kt'
                    else:
                        kom = 't_kt'

    
                        
                
                if ent.wts(view_matrix) and ent.health > 0 and not ent.dormant and controller_ptr != local:
                    color = Colors.cyan if ent.team != 2 else Colors.orange
                                                         
                    if kvadrat_poiska == 1 and not_povtor == True:   #Отрисовка радиуса поиска целей аим 
                        pm.draw_circle_lines(
                        thenter_x ,
                        thenter_y ,
                        radius_poika,
                        Colors.white2,
                        )
                        not_povtor = False
                    
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

                            if s >= 6 or vigu == 0:
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

                            if aim_ogon == 1 and rast_do_gol < (head - center * 7.7 if head - center * 7.7 > 2 else 2) and not potok_ogon.is_set():                                
                                threading.Thread(target=Ogon, daemon=True).start()
                                

                                

                        if WH_on_off2 == 1:
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
                            pm.draw_rectangle_lines(
                                ent.head_pos2d["x"] - center2,
                                ent.head_pos2d["y"] - center2 / 2,
                                width2,
                                head + center2 / 2,
                                color,
                                1.5,
                            )

                            
                            # ХП бар
                            if wh_xp_bar2 == 1:
                                pm.draw_rectangle(
                                    ent.head_pos2d["x"] - center2 - width2/30, #Насрано
                                    (ent.head_pos2d["y"] - center2 / 2) + head + center2 / 2,
                                    -width2/6,
                                    (-head - center2 / 2) * (ent.health/100),
                                    Colors.grey,
                                )

                                pm.draw_rectangle_lines(
                                    ent.head_pos2d["x"] - center2 - width2/5 ,
                                    ent.head_pos2d["y"] - center2 / 2,
                                    width2/6,
                                    head + center2 / 2,
                                    Colors.grey,
                                    0.8,
                                )                          

                            # Info
                            txt = str(ent.name if imia_wh2 == 1 else "") + " " + str(ent.health if imia_xp2 == 1 else "")
                            pm.draw_text(
                                txt,
                                ent.head_pos2d["x"] - pm.measure_text(txt, 15) // 2,
                                ent.head_pos2d["y"] - ((thenter_x*2)/70),
                                15,
                                Colors.white if int(f"{ent.health}") > 50 else Colors.red, 
                            )
            
            pm.end_drawing()
            time.sleep(0.0003)#задержка для нормальной работы интерфейса (нехоршо но пока похуй)

global stop
stop = False

lock = threading.Lock()

def Zapysk2() :#Ебать я насрал, каюсь. Это зашло слишком далеко, я заебусь переделывать нормально.(в целом как и весь код) =(
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
        global nast_antiotd_obith_x
        nast_antiotd_obith_x = float(nast_antiotd_ob_x.get())
        global WH_on_off2
        WH_on_off2 = WH_on_off1.get()
        global soroni2
        soroni2 = soroni1.get()
        global imia_wh2
        imia_wh2 = imia_wh1.get()
        global imia_xp2
        imia_xp2 = imia_xp1.get()
        global wh_xp_bar2
        wh_xp_bar2 = wh_xp_bar1.get()
        global antiotd_obith_plav
        antiotd_obith_plav = int(antiotd_ob_plav.get())        
        
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
                       +"\n"+str(antiotd_obith)+"\n"+str(nast_antiotd_obith_x)+"\n"+str(WH_on_off2)+"\n"+str(soroni2)
                       +"\n"+str(imia_wh2)+"\n"+str(imia_xp2)+"\n"+str(wh_xp_bar2)+"\n"+str(antiotd_obith_plav))


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
        global nast_antiotd_obith_x
        nast_antiotd_obith_x = float(nast_antiotd_ob_x.get())
        global WH_on_off2
        WH_on_off2 = WH_on_off1.get()
        global soroni2
        soroni2 = soroni1.get()
        global imia_wh2
        imia_wh2 = imia_wh1.get()
        global imia_xp2
        imia_xp2 = imia_xp1.get()
        global wh_xp_bar2
        wh_xp_bar2 = wh_xp_bar1.get()
        global antiotd_obith_plav
        antiotd_obith_plav = int(antiotd_ob_plav.get())


        with open('nastroiki.txt', 'r+') as file:
            file.truncate(0)
            file.write(str(trig)+"\n"+str(aim)+"\n"+str(fps_th)+"\n"+str(int(mnosz_usk_navodki))
                       +"\n"+str(int(zona_zamed_navodki))+"\n"+str(int(radius_poika)*2)+"\n"+str(telo)
                       +"\n"+str(box_telo)+"\n"+str(skorost_aim)+"\n"+str(aim_ogon)+"\n"+str(kvadrat_poiska)
                       +"\n"+str(aim_telo)+"\n"+str(aim_telo_50)+"\n"+str(dlit_otheredi)+"\n"+str(aim_steni_if)
                       +"\n"+str(zad_m_vistri)+"\n"+str(kt_streif)+"\n"+str(levii_triger)+"\n"+str(aim_anti_otdatha_if)
                       +"\n"+str(antiotd_obith)+"\n"+str(nast_antiotd_obith_x)+"\n"+str(WH_on_off2)+"\n"+str(soroni2)
                       +"\n"+str(imia_wh2)+"\n"+str(imia_xp2)+"\n"+str(wh_xp_bar2)+"\n"+str(antiotd_obith_plav))
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
    nastroiki.write("alt\nx\n100\n1.0\n8\n300\n0\n0\n15\n1\n1\n0\n0\n0.1\n0\n0.6\n0\n0\n0\n0\n0.5555\n1\n0\n1\n0\n1\n0")

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
    nast_antiotd_obith_x = nastroiki.readline().strip()
    WH_on_off = nastroiki.readline().strip()
    soroni = nastroiki.readline().strip()
    imia_wh = nastroiki.readline().strip()
    imia_xp = nastroiki.readline().strip()
    wh_xp_bar = nastroiki.readline().strip()
    antiotd_obith_plav = nastroiki.readline().strip()
    
    nastroiki.close()
    

def flagok():
    aim_v_telo_50.deselect()

def flagok50():
    aim_v_telo.deselect()
        
def update_interface(): #Бля я забыл зачем это, на всякий случай трогать не буду :)
    app.after(100000, update_interface)

    
app = ctk.CTk()
ctk.deactivate_automatic_dpi_awareness()
app.title("Circus: Точно без багов...")
app.geometry("600x450")
app.configure(fg_color="black")  # Фон окна
icon_path = img_resource_path('123.ico')
app.iconbitmap(icon_path)

app.grid_columnconfigure(0, weight=1)
app.resizable(width=False, height=False) 


#Кнопка старта
button = ctk.CTkButton(app, text="Запуск (или) Применить настройки", command=Zapysk)
button.grid(row=0, column=0, padx=5, pady=5, sticky="ew",columnspan=2)


#фрейм с группой кнопок вкладок

frame = ctk.CTkFrame(master=app, width=90, height=405, corner_radius=10)
frame.place(x=5, y=40)

info_image_on = ctk.CTkImage(light_image=Image.open(img_resource_path("Info2.png")), size=(65, 65))
info_image_off = ctk.CTkImage(light_image=Image.open(img_resource_path("Info.png")), size=(65, 65))
button_INFO = ctk.CTkButton(frame, image=info_image_off, text="", width=20, height=20, fg_color="transparent", command=lambda: nashatie_knopok_fkladok("info"))
button_INFO.place(x=5, y=5)

WH_image_off = ctk.CTkImage(light_image=Image.open(img_resource_path("WH1.png")), size=(65, 65))
WH_image_on = ctk.CTkImage(light_image=Image.open(img_resource_path("WH2.png")), size=(65, 65))
button_WH = ctk.CTkButton(frame, image=WH_image_off, text="", width=20, height=20, fg_color="transparent", command=lambda: nashatie_knopok_fkladok("WH"))
button_WH.place(x=5, y=80)

AIM_image_off = ctk.CTkImage(light_image=Image.open(img_resource_path("AIM1.png")), size=(65, 65))
AIM_image_on = ctk.CTkImage(light_image=Image.open(img_resource_path("AIM2.png")), size=(65, 65))
button_AIM = ctk.CTkButton(frame, image=AIM_image_off, text="", width=20, height=20, fg_color="transparent", command=lambda: nashatie_knopok_fkladok("aim"))
button_AIM.place(x=5, y=155)

seting_image_off = ctk.CTkImage(light_image=Image.open(img_resource_path("Obshee1.png")), size=(65, 65))
seting_image_on = ctk.CTkImage(light_image=Image.open(img_resource_path("Obshee2.png")), size=(65, 65))
button_seting = ctk.CTkButton(frame, image=seting_image_off, text="", width=20, height=20, fg_color="transparent", command=lambda: nashatie_knopok_fkladok("seting"))
button_seting.place(x=5, y=230)



language_flag = True #Флажёк для переключения языка

language_image_ru = ctk.CTkImage(light_image=Image.open(img_resource_path("Ru.png")), size=(65, 65))
language_image_usa = ctk.CTkImage(light_image=Image.open(img_resource_path("USA.png")), size=(65, 65))
button_language = ctk.CTkButton(frame, image=language_image_ru, text="", width=20, height=20, fg_color="transparent", command=lambda: language())
button_language.place(x=5, y=305)

def nashatie_knopok_fkladok(knopka): 
    button_INFO.configure(image=info_image_off)
    frame_info.place(x=100, y=600)  # Перемещяем фрейм за границу окна
    
    button_AIM.configure(image=AIM_image_off)
    frame_aim.place(x=100, y=600)
    
    button_seting.configure(image=seting_image_off)
    frame_seting.place(x=100, y=600)

    button_WH.configure(image=WH_image_off)
    frame_WH.place(x=100, y=600)
    
    if knopka == "info":
        button_INFO.configure(image=info_image_on)
        frame_info.place(x=100, y=40)  # Возвращяем нужный фрейм на место
    elif knopka == "aim":
        button_AIM.configure(image=AIM_image_on)
        frame_aim.place(x=100, y=40)
    elif knopka == "seting":
        button_seting.configure(image=seting_image_on)
        frame_seting.place(x=100, y=40)
    elif knopka == "WH":
        button_WH.configure(image=WH_image_on)
        frame_WH.place(x=100, y=40)

def language():
    global language_flag
    
    if language_flag == True:
        button_language.configure(image=language_image_usa)
        perevod_na_usa()#Функция перевода на англ
        language_flag = False
    else:
        button_language.configure(image=language_image_ru)
        perevod_na_ru()#Функция перевода на ру
        language_flag = True



def perevod_na_ru():
    #info
    button.configure(text="Запуск (или) Применить настройки")
    label1.configure(text="Проект создан при поддержке разрабов CS2\n если-бы не их похуизм с читерами, проекта бы не существовало.")
    label2.configure(text="Чит не инжектица в игру и не подменяет значения\n шанс детекта VAC-ом нулевой, если не использовать огромную\n скорость наведения AIM")
    label3.configure(text="Для корректного запуска, в настройках изображения\n поставьте отображения в окне или в окне без рамки\n далее в окне чита нажмите запуск с РАЗВЁРНУТОЙ игрой\nне сворачивайте игру во избежании зависаний чита.")
    label4.configure(text="По всем вопросам, проблемам и пожланиям писать сюда")
    link_button_dis.configure(text="Ссылка на дискорд канал")
    label5.configure(text="Вы можете менять настройки во время игры нажав на кнопку, кроме FPS")
    label6.configure(text="Возможны мелкие недочёты в чите по причине того что я котик у меня лапки")
    link_button.configure(text="Сайт проекта на GitHub")

    #wh
    label_WH1.configure(text="Настроки WH")
    WH_on_off1.configure(text="Влючить WH (Не влияет на AIM и триггер)")
    hitt_box_telo.configure(text="Включить бокс тела. (Просто включает прямоугольник тела)")
    imia_wh1.configure(text="Отображать имена (Плохо работает с русскими символами)")
    imia_xp1.configure(text="Отображать кол-во хп в цифрах")
    wh_xp_bar1.configure(text="Отображать хп бар")

    #aim
    label_aim1.configure(text = "Настроки AIM-асиста" )
    label_aim2.configure(text = "Кнопка AIM-асиста (учитывайте язык ввода!) можно писать alt и т.п.:" )
    aim_og.configure(text = "Стрелять при наведении.(AIM будет стрелять автоматически)")
    label_aim3.configure(text = "Длительность очереди AIM (AIM будет стрелять заданное время):              сек." )
    label_aim4.configure(text = "Задержка между выстрелами (таймаут на выстрел AIMа):" )
    aim_v_telo.configure(text = "AIM наводится всегда в тело, или")
    aim_v_telo_50.configure(text = "если меньше 50хр")
    Kontr_stre.configure(text = "Делать кон-стрейф перед выстрелом. (делает контр-стрейф в AIMе)")
    aim_steni.configure(text = "AIM будет аводится только в видимых противников (есть задержка)")
    aim_anti_otdatha.configure(text = "Использовать антиотдачу в AIM (зависит от скорости наведения) ")
    label_aim5.configure(text = "Радиус поиска целей АИМ в пикселях (расстояние от прицела):" )
    ot_kvadrat.configure(text = "Отоброжать радиус поиска целей AIM (рисует кружок радиуса)")
    label_aim6.configure(text = "Множитель скорости AIM (изменяет общую скорость) нужно дробные:" )
    label_aim7.configure(text = "Макс. скорость наведения AIM (На скорость влияет фпс чита):" )

    #setings
    label_seting1.configure(text = "Настройки триггер-бота" )
    label_seting2.configure(text = "Кнопка тригера (учитывайте язык ввода!) можно писать alt и т.п.:" )
    trig_na_telo.configure(text = "Реагаровать на тело. (Тригер будет реагировать на тело и голову)")
    lev_trig.configure(text = "Альтернативный триггер (В прямой видимости и на все части тела)")
    label_seting3.configure(text = "Настройки антиотдачи" )
    antiotd_ob.configure(text = "Анти-отдача для обычных выстрелов. (Требует тонкой настройки)")
    label_seting4.configure(text = "Настройка компенсации отдачи, подбирать эксперементально:" )
    antiotd_ob_plav.configure(text = "Плавная компенсация(Без дерганий, но чуть хуже работает)")
    label_seting5.configure(text = "Прочие настройки" )
    label_seting6.configure(text = "FPS лок чита(НЕ ДОЛЖЕН БЫТЬ ВЫШЕ ЧЕМ В ИГРЕ! ВАЖНО ДЛЯ AIM):" )
    soroni1.configure(text = "Против всех (WH, AIM и триггер на всех) для гонки вооружений")
    
    

def perevod_na_usa():
    #info
    button.configure(text="Run (or) Apply settings")
    label1.configure(text="The project was created with the support of CS2 developers\n If it weren't for their indifference to cheaters, the project wouldn't exist.")
    label2.configure(text="The cheat is not an injection into the game and does not replace the values\n the chance of detection by VAC is zero, unless you use the huge\n AIM aiming speed")
    label3.configure(text="For correct launch, in the image settings\n set the display to windowed or frameless\n then in the cheat window press launch with the EXPANDED game\ndo not minimize the game to avoid the cheat freezing.")
    label4.configure(text="For all questions, problems and requests write here")
    link_button_dis.configure(text="Link to discord channel")
    label5.configure(text="You can change the settings during the game by pressing the button, except for FPS")
    label6.configure(text="There may be minor flaws in the cheat due to the fact that I am a cat and I have paws")
    link_button.configure(text="Project website on GitHub")

    #wh
    label_WH1.configure(text="WH Settings")
    WH_on_off1.configure(text="Enable WH (Does not affect AIM and trigger)")
    hitt_box_telo.configure(text="Toggle body box. (Just toggles body rectangle)")
    imia_wh1.configure(text="Display names (Works poorly with Russian characters)")
    imia_xp1.configure(text="Display HP in numbers")
    wh_xp_bar1.configure(text="Show HP bar")

    #aim
    label_aim1.configure(text = "AIM assistant settings" )
    label_aim2.configure(text = "AIM-assist button (take into account the input language!) you can write alt :" )
    aim_og.configure(text = "Shoot on aim.(AIM will fire automatically)")
    label_aim3.configure(text = "AIM Burst Duration (AIM will fire for a set amount of time):------------------>             sec." )
    label_aim4.configure(text = "Delay between shots (AIM shot timeout):------------------------------>" )
    aim_v_telo.configure(text="AIM is always aimed at the body, or")
    aim_v_telo_50.configure(text = "if less than 50xp")
    Kontr_stre.configure(text = "Do counter-strafe before shooting. (does counter-strafe in AIM)")
    aim_steni.configure(text = "AIM will be aimed only at visible enemies (there is a delay)")
    aim_anti_otdatha.configure(text = "Use anti-recoil in AIM (depends on aiming speed)")
    label_aim5.configure(text = "AIM target search radius in pixels (distance from crosshair):------------>" )
    ot_kvadrat.configure(text = "Display AIM target search radius (draws radius circle)")
    label_aim6.configure(text = "AIM speed multiplier (changes overall speed) needs to be fractional:----------->" )
    label_aim7.configure(text = "Max. AIM aiming speed (speed is affected by cheat fps):-------------->" )

    #setings
    label_seting1.configure(text = "Trigger Bot Settings" )
    label_seting2.configure(text = "Trigger button (take into account the input language!) you can write alt:" )
    trig_na_telo.configure(text = "Regard on body. (Trigger will react to body and head)")
    lev_trig.configure(text = "Alternative trigger (In line of sight and on all body parts)")
    label_seting3.configure(text = "Anti-recoil settings" )
    antiotd_ob.configure(text = "Anti-recoil for normal shots. (Requires fine tuning)")
    label_seting4.configure(text = "Recoil compensation settings, select experimentally:----------------------->" )
    antiotd_ob_plav.configure(text = "Smooth compensation (without jerking, but works a little worse)")
    label_seting5.configure(text = "Other settings" )
    label_seting6.configure(text = "Cheat for blocking FPS (MUST NOT BE HIGHER THAN IN THE GAME!):------>" )
    soroni1.configure(text = "Against all (WH, AIM and trigger on all) for arms race")

    
app.after(100, button_INFO.invoke) #Эмуляция нажатия кнопки чтоб при запуске была активна инфо


###фрейм с группой кнопок вкладок


#Фрейм фкладки инфо

frame_info = ctk.CTkFrame(master=app, width=495, height=405, corner_radius=10)
frame_info.place(x=100, y=40)

label1 = ctk.CTkLabel(frame_info,
                     text = "Проект создан при поддержке разрабов CS2\n если-бы не их похуизм с читерами, проекта бы не существовало." )
label1.place(x=45,y=10)

label2 = ctk.CTkLabel(frame_info,
                     text = "Чит не инжектица в игру и не подменяет значения\n шанс детекта VAC-ом нулевой, если не использовать огромную\n скорость наведения AIM" )
label2.place(x=50,y=50)

label3 = ctk.CTkLabel(frame_info,
                     text = "Для корректного запуска, в настройках изображения\n поставьте отображения в окне или в окне без рамки\n далее в окне чита нажмите запуск с РАЗВЁРНУТОЙ игрой\nне сворачивайте игру во избежании зависаний чита." )
label3.place(x=70,y=100)

label4 = ctk.CTkLabel(frame_info,
                     text = "По всем вопросам, проблемам и пожланиям писать сюда" )
label4.place(x=70,y=175)

def open_link_discord():
    webbrowser.open("https://discord.gg/hseN2eW6gw")  # Открывает ссылку в браузере

link_button_dis = ctk.CTkButton(frame_info,
                            text="Ссылка на дискорд канал",
                            command=open_link_discord,fg_color="transparent",
                            text_color="#1E90FF",
                            border_width=0,
                            font=("Arial", 12))
link_button_dis.place(x=160,y=200)

label5 = ctk.CTkLabel(frame_info,
                     text = "Вы можете менять настройки во время игры нажав на кнопку, кроме FPS" )
label5.place(x=20,y=230)

label6 = ctk.CTkLabel(frame_info,
                     text = "Возможны мелкие недочёты в чите по причине того что я котик у меня лапки" )
label6.place(x=8,y=260)

def open_link_githab():
    webbrowser.open("https://www.google.com")  # Открывает ссылку в браузере

link_button = ctk.CTkButton(frame_info,
                            text="Сайт проекта на GitHub",
                            command=open_link_githab,fg_color="transparent",
                            text_color="#1E90FF",
                            border_width=0,
                            font=("Arial", 16))
link_button.place(x=150,y=290)

###Фрейм фкладки инфо


#Фрейи настройки WH
frame_WH = ctk.CTkFrame(master=app, width=495, height=405, corner_radius=10)
frame_WH.place(x=100, y=40)

label_WH1 = ctk.CTkLabel(frame_WH, text = "Настроки WH" )
label_WH1.place(x=180,y=0)


WH_on_off1 = ctk.CTkCheckBox(frame_WH, text="Влючить WH (Не влияет на AIM и триггер)")
WH_on_off1.place(x=20,y=20)
if WH_on_off == "1":
    WH_on_off1.select()
else:
    WH_on_off1.deselect()

#Хитбокс тела галочка
hitt_box_telo = ctk.CTkCheckBox( frame_WH, text="Включить бокс тела. (Просто включает прямоугольник тела)")
hitt_box_telo.place(x=20,y=50)
if hit_box_telo == "1":
    hitt_box_telo.select()
else:
    hitt_box_telo.deselect()

#Отображать ли имя
imia_wh1 = ctk.CTkCheckBox(frame_WH, text="Отображать имена (Плохо работает с русскими символами)")
imia_wh1.place(x=20,y=80)
if imia_wh == "1":
    imia_wh1.select()
else:
    imia_wh1.deselect()

#Отображать ли хп
imia_xp1 = ctk.CTkCheckBox(frame_WH, text="Отображать кол-во хп в цифрах")
imia_xp1.place(x=20,y=110)
if imia_xp == "1":
    imia_xp1.select()
else:
    imia_xp1.deselect()

#Отображать ли хп_бар
wh_xp_bar1 = ctk.CTkCheckBox(frame_WH, text="Отображать хп бар")
wh_xp_bar1.place(x=20,y=140)
if wh_xp_bar == "1":
    wh_xp_bar1.select()
else:
    wh_xp_bar1.deselect()

###Фрейи настройки WH


#Фрейм фкладки аим
frame_aim = ctk.CTkFrame(master=app, width=495, height=405, corner_radius=10)
frame_aim.place(x=100, y=40)

label_aim1 = ctk.CTkLabel(frame_aim, text = "Настроки AIM-асиста" )
label_aim1.place(x=170,y=0)


#Кнопка аим
label_aim2 = ctk.CTkLabel(frame_aim, text = "Кнопка AIM-асиста (учитывайте язык ввода!) можно писать alt и т.п.:" )
label_aim2.place(x=20,y=20)

knop_aim = ctk.CTkEntry(frame_aim)
knop_aim.place(x=448,y=20)
knop_aim.configure (width=31)
knop_aim.insert(0, knopka_aim)

#Стрельба аим галочка
aim_og = ctk.CTkCheckBox(frame_aim, text="Стрелять при наведении.(AIM будет стрелять автоматически)")
aim_og.place(x=20,y=50)
if aim_ogon == "1":
    aim_og.select()
else:
    aim_og.deselect()


#Очередь аима
label_aim3 = ctk.CTkLabel(frame_aim,
                          text = "Длительность очереди AIM (AIM будет стрелять заданное время):              сек." )
label_aim3.place(x=20,y=80)

dlit_othered = ctk.CTkEntry(frame_aim)
dlit_othered.place(x=430,y=80)
dlit_othered.configure (width=35)
dlit_othered.insert(0, dlit_otheredi)

#Задержка между выстрелами(очередями)
label_aim4 = ctk.CTkLabel(frame_aim, text = "Задержка между выстрелами (таймаут на выстрел AIMа):" )
label_aim4.place(x=20,y=110)

zad_m_vistr = ctk.CTkEntry(frame_aim)
zad_m_vistr.place(x=380,y=110)
zad_m_vistr.configure (width=35)
zad_m_vistr.insert(0, zad_m_vistri)


#Аим в тело ?Аим в тело если >50 ?
aim_v_telo = ctk.CTkCheckBox(frame_aim, command = flagok, text="AIM наводится всегда в тело, или")
aim_v_telo.place(x=20,y=140)
aim_v_telo_50 = ctk.CTkCheckBox(frame_aim, command = flagok50, text="если меньше 50хр")
aim_v_telo_50.place(x=260,y=140)
if aim_telo == "1":
    aim_v_telo.select()
else:
    aim_v_telo.deselect()
if aim_telo_50 == "1":
    aim_v_telo_50.select()
else:
    aim_v_telo_50.deselect()

#Котрстрейф
Kontr_stre = ctk.CTkCheckBox(frame_aim, text="Делать кон-стрейф перед выстрелом. (делает контр-стрейф в AIMе)")
Kontr_stre.place(x=20,y=170)
if Kontr_streif == "1":
    Kontr_stre.select()
else:
    Kontr_stre.deselect()

#Учитывать препятствия?
aim_steni = ctk.CTkCheckBox(frame_aim, text="AIM будет аводится только в видимых противников (есть задержка)")
aim_steni.place(x=20,y=200)
if aim_steni_if == "1":
    aim_steni.select()
else:
    aim_steni.deselect()

#Антиотдача в аим
aim_anti_otdatha = ctk.CTkCheckBox(frame_aim, text="Использовать антиотдачу в AIM (зависит от скорости наведения) ")
aim_anti_otdatha.place(x=20,y=230)
if aim_anti_otdatha_if == "1":
    aim_anti_otdatha.select()
else:
    aim_anti_otdatha.deselect()

#Радиус поиска аим
label_aim5 = ctk.CTkLabel(frame_aim, text = "Радиус поиска целей АИМ в пикселях (расстояние от прицела):" )
label_aim5.place(x=20,y=260)

kvadrat_the = ctk.CTkEntry(frame_aim)
kvadrat_the.place(x=415,y=260)
kvadrat_the.configure (width=45)
kvadrat_the.insert(0, radius_poiska)

#Показывать ли адиус поиска галочка
ot_kvadrat = ctk.CTkCheckBox(frame_aim, text="Отоброжать радиус поиска целей AIM (рисует кружок радиуса)")
ot_kvadrat.place(x=20,y=290)
if kvadrat_poiska == "1":
    ot_kvadrat.select()
else:
    ot_kvadrat.deselect()

#Множ ускорения наводки
label_aim6 = ctk.CTkLabel(frame_aim, text = "Множитель скорости AIM (изменяет общую скорость) нужно дробные:" )
label_aim6.place(x=20,y=350)

mnojit_usk = ctk.CTkEntry(frame_aim)
mnojit_usk.place(x=457,y=350)
mnojit_usk.configure (width=35)
mnojit_usk.insert(0, mnosz_usk_navodki)


#Скорость аим
label_aim7 = ctk.CTkLabel(frame_aim, text = "Макс. скорость наведения AIM (На скорость влияет фпс чита):" )
label_aim7.place(x=20,y=320)

skor_aim = ctk.CTkEntry(frame_aim)
skor_aim.place(x=405,y=320)
skor_aim.configure (width=45)
skor_aim.insert(0, skorost_aim)    
###Фрейм фкладки аим



#Фрейм фкладки настройки
frame_seting = ctk.CTkFrame(master=app, width=495, height=405, corner_radius=10)
frame_seting.place(x=100, y=40)

#Имя группы настроек триггер
label_seting1 = ctk.CTkLabel(frame_seting, text = "Настройки триггер-бота" )
label_seting1.place(x=160,y=0)

#Кнопка тригера
label_seting2 = ctk.CTkLabel( frame_seting, text = "Кнопка тригера (учитывайте язык ввода!) можно писать alt и т.п.:" )
label_seting2.place(x=20,y=20)

knop_trig = ctk.CTkEntry( frame_seting)
knop_trig.place(x=425,y=20)
knop_trig.configure (width=31)
knop_trig.insert(0, knopka_trigera)


#Тригер на тело галочка
trig_na_telo = ctk.CTkCheckBox( frame_seting,
                                text="Реагаровать на тело. (Тригер будет реагировать на тело и голову)")
trig_na_telo.place(x=20,y=50)
if triger_telo == "1":
    trig_na_telo.select()
else:
    trig_na_telo.deselect()

#Использовать левый тригер
lev_trig = ctk.CTkCheckBox( frame_seting,
                            text="Альтернативный триггер (В прямой видимости и на все части тела)")
lev_trig.place(x=20,y=80)
if lev_triger == "1":
    lev_trig.select()
else:
    lev_trig.deselect()

#Отделяющая полоска
label_seting0 = ctk.CTkLabel( frame_seting, text = "-"*114 )
label_seting0.place(x=20,y=105)

#Имя группы настроек антиотдача
label_seting3 = ctk.CTkLabel( frame_seting, text = "Настройки антиотдачи" )
label_seting3.place(x=160,y=120)

#Антиотдача для обычных выстрелов галочка
antiotd_ob = ctk.CTkCheckBox(frame_seting,
                                       text="Анти-отдача для обычных выстрелов. (Требует тонкой настройки)")
antiotd_ob.place(x=20,y=140)
if antiotd_obith == "1":
    antiotd_ob.select()
else:
    antiotd_ob.deselect()

#Настройка компенсации отдачи x 
label_seting4 = ctk.CTkLabel(frame_seting, text = "Настройка компенсации отдачи, подбирать эксперементально:" )
label_seting4.place(x=20,y=170)

nast_antiotd_ob_x = ctk.CTkEntry(frame_seting)
nast_antiotd_ob_x.place(x=418,y=170)
nast_antiotd_ob_x.configure (width=65)
nast_antiotd_ob_x.insert(0, nast_antiotd_obith_x)

#Плавная антиотдача
antiotd_ob_plav = ctk.CTkCheckBox(frame_seting,
                                       text="Плавная компенсация(Без дерганий, но чуть хуже работает)")
antiotd_ob_plav.place(x=20,y=200)
if antiotd_obith_plav == "1":
    antiotd_ob_plav.select()
else:
    antiotd_ob_plav.deselect()

#Отделяющая полоска
label_seting0 = ctk.CTkLabel( frame_seting, text = "-"*114 )
label_seting0.place(x=20,y=225)

#Имя группы настроек другое
label_seting5 = ctk.CTkLabel(frame_seting, text = "Прочие настройки" )
label_seting5.place(x=175,y=240)

#Ограничение фпс чита
label_seting6 = ctk.CTkLabel(frame_seting, text = "FPS лок чита(НЕ ДОЛЖЕН БЫТЬ ВЫШЕ ЧЕМ В ИГРЕ! ВАЖНО ДЛЯ AIM):" )
label_seting6.place(x=20,y=260)

FPS_t = ctk.CTkEntry(frame_seting)
FPS_t.place(x=452,y=260)
FPS_t.configure (width=36)
FPS_t.insert(0, fps_thita)

soroni1 = ctk.CTkCheckBox(frame_seting, text="Против всех (WH, AIM и триггер на всех) для гонки вооружений")
soroni1.place(x=20,y=290)
if soroni == "1":
    soroni1.select()
else:
    soroni1.deselect()

###Фрейм фкладки настройки

app.mainloop()
  
#Остановка процесса чита
with lock:
    stop = False
