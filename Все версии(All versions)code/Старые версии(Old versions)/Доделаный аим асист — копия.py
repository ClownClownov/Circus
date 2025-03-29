import requests
import pyMeow as pm
import keyboard
import pyautogui
import win32api
import win32api, win32con
import time
t = 0

class Offsets:
    m_pBoneArray = 496


class Colors:
    orange = pm.get_color("orange")
    black = pm.get_color("black")
    cyan = pm.get_color("cyan")
    white = pm.get_color("white")
    grey = pm.fade_color(pm.get_color("red"), 0.3)
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

    def run(self):
        pm.overlay_init("Counter-Strike 2", fps=200)
        kom = 'kt'
        while pm.overlay_loop():
            view_matrix = pm.r_floats(self.proc, self.mod + Offsets.dwViewMatrix, 16)
        
            pm.begin_drawing()
            pm.draw_fps(0, 0)
        
            for ent in self.it_entities():
                if ent.wts(view_matrix) and ent.health > 0 and not ent.dormant:
                    color = Colors.cyan if ent.team != 2 else Colors.orange


                    if keyboard.is_pressed('f2'):
                        kom = 't'
                    if keyboard.is_pressed('f1'):
                        kom = 'kt'


                    
                    if ent.team != 2 and kom == 'kt':
                        head = ent.pos2d["y"] - ent.head_pos2d["y"]
                        width = head / 4
                        center = width / 2

                        width2 = head / 2
                        center2 = width2 / 2

                        imia = f"{ent.name}"

                        if keyboard.is_pressed('x'):
    
                            x = ent.head_pos2d["x"] - center / 2
                            y = ent.head_pos2d["y"] - center / 2
                            x2=width - center
                            y2=head - center * 7
                            if  x + (x2 / 4) < 960 < (x + x2) - x2 / 4:
                                if y < 540 < (y + y2) - y2 / 7:                                
                                    pyautogui.click()
                                           
                                

                            if 1010 > x > 910:                 
                                if y > 540 < (y + y2) - y2 / 7 and y < 580 :
                                    win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, 0, 1, 0, 0)
                                elif y < 540 > (y + y2) - y2 / 7 and 500 < (y + y2) - y2 / 7 :
                                    win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, 0, -1, 0, 0)

                            if 580 > y > 500:                 
                                if x + (x2 / 4) > 960 < (x + x2) - x2 / 4 and x + (x2 / 4) < 1010:
                                    win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, 1, 0, 0, 0) 
                                elif x + (x2 / 4) < 960 > (x + x2) - x2 / 4 and 910 < (x + x2) - x2 / 4:
                                    win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, -1, 0, 0, 0)



                            
                        # Box Golova
                        pm.draw_rectangle(
                            ent.head_pos2d["x"] - center / 2,
                            ent.head_pos2d["y"] - center / 2,
                            width - center,
                            head - center * 7,
                            Colors.grey,
                        )
                        pm.draw_rectangle_lines(
                            ent.head_pos2d["x"] - center / 2,
                            ent.head_pos2d["y"] - center / 2,
                            width - center,
                            head - center * 7,
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
                            ent.head_pos2d["y"] - center * 3,
                            15,
                            Colors.white,
                        )
                    if ent.team == 2 and kom == 't':
                        head = ent.pos2d["y"] - ent.head_pos2d["y"]
                        width = head / 4
                        center = width / 2

                        width2 = head / 2
                        center2 = width2 / 2

                        if keyboard.is_pressed('x'):
                            x = ent.head_pos2d["x"] - center / 2
                            y = ent.head_pos2d["y"] - center / 2
                            x2=width - center
                            y2=head - center * 7
                            if  x + (x2 / 4) < 960 < (x + x2) - x2 / 4:
                                if y < 540 < (y + y2) - y2 / 7:                                
                                    pyautogui.click()

                            if 1010 > x > 910:                 
                                if y > 540 < (y + y2) - y2 / 7 and y < 580 :
                                    win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, 0, 1, 0, 0)
                                elif y < 540 > (y + y2) - y2 / 7 and 500 < (y + y2) - y2 / 7 :
                                    win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, 0, -1, 0, 0)

                            if 580 > y > 500:                 
                                if x + (x2 / 4) > 960 < (x + x2) - x2 / 4 and x + (x2 / 4) < 1010:
                                    win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, 1, 0, 0, 0) 
                                elif x + (x2 / 4) < 960 > (x + x2) - x2 / 4 and 910 < (x + x2) - x2 / 4:
                                    win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, -1, 0, 0, 0)


                                

                                        
                        # Box Golova
                        pm.draw_rectangle(
                            ent.head_pos2d["x"] - center / 2,
                            ent.head_pos2d["y"] - center / 2,
                            width - center,
                            head - center * 7,
                            Colors.grey,
                        )
                        pm.draw_rectangle_lines(
                            ent.head_pos2d["x"] - center / 2,
                            ent.head_pos2d["y"] - center / 2,
                            width - center,
                            head - center * 7,
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
                            ent.head_pos2d["y"] - center * 3,
                            15,
                            Colors.white,
                        )
                        

            pm.end_drawing()


if __name__ == "__main__":
    esp = CS2Esp()
    esp.run()
