import sython
import pygame
from pygame.locals import *

class BaseEvents(object):
    def __init__(self) -> None:
        """Base class for all events

        This class handles all possible events in Sython. For example:

            >>> win = Window()
            >>> sprite = win.new_sprite("Sprite", "/path/to/img")
            >>> # When the user clicks the `sprite`, the `foo` function will be called.
            >>> sprite.on_sprite_clicked = foo()
        
        This class can not be used alone. Its child class must be `sython.Sprite`.
        """
        super().__init__()
        # Event handlers
        self.on_space_pressed = None
        self.on_up_arr_pressed = None
        self.on_down_arr_pressed = None
        self.on_right_arr_pressed = None
        self.on_left_arr_pressed = None
        self.on_a_pressed = None
        self.on_b_pressed = None
        self.on_c_pressed = None
        self.on_d_pressed = None
        self.on_e_pressed = None
        self.on_f_pressed = None
        self.on_g_pressed = None
        self.on_h_pressed = None
        self.on_i_pressed = None
        self.on_j_pressed = None
        self.on_k_pressed = None
        self.on_l_pressed = None
        self.on_m_pressed = None
        self.on_n_pressed = None
        self.on_o_pressed = None
        self.on_p_pressed = None
        self.on_q_pressed = None
        self.on_r_pressed = None
        self.on_s_pressed = None
        self.on_t_pressed = None
        self.on_u_pressed = None
        self.on_v_pressed = None
        self.on_w_pressed = None
        self.on_x_pressed = None
        self.on_y_pressed = None
        self.on_z_pressed = None
        self.on_0_pressed = None
        self.on_1_pressed = None
        self.on_2_pressed = None
        self.on_3_pressed = None
        self.on_4_pressed = None
        self.on_5_pressed = None
        self.on_6_pressed = None
        self.on_7_pressed = None
        self.on_8_pressed = None
        self.on_9_pressed = None
        self.on_sprite_clicked = None
    
    def handle_events(self):
        """Handles Sython events.

        This method handles pre-defined events inside Sython. E.g.: `on_space_pressed`
        and `on_sprite_clicked`.

        Note that this is function can only be used properly with native Sython.
        """
        for event in sython.events:
            if event.type == KEYDOWN and event.key == K_a:
                func = self.on_a_pressed
                func() if func is not None else None
            elif event.type == KEYDOWN and event.key == K_b:
                func = self.on_b_pressed
                func() if func is not None else None     
            elif event.type == KEYDOWN and event.key == K_c:
                func = self.on_c_pressed
                func() if func is not None else None        
            elif event.type == KEYDOWN and event.key == K_d:
                func = self.on_d_pressed
                func() if func is not None else None
            elif event.type == KEYDOWN and event.key == K_e:
                func = self.on_e_pressed
                func() if func is not None else None
            elif event.type == KEYDOWN and event.key == K_f:
                func = self.on_f_pressed
                func() if func is not None else None
            elif event.type == KEYDOWN and event.key == K_g:
                func = self.on_g_pressed
                func() if func is not None else None
            elif event.type == KEYDOWN and event.key == K_h:
                func = self.on_h_pressed
                func() if func is not None else None
            elif event.type == KEYDOWN and event.key == K_i:
                func = self.on_i_pressed
                func() if func is not None else None
            elif event.type == KEYDOWN and event.key == K_j:
                func = self.on_j_pressed
                func() if func is not None else None
            elif event.type == KEYDOWN and event.key == K_k:
                func = self.on_k_pressed
                func() if func is not None else None
            elif event.type == KEYDOWN and event.key == K_l:
                func = self.on_l_pressed
                func() if func is not None else None
            elif event.type == KEYDOWN and event.key == K_m:
                func = self.on_m_pressed
                func() if func is not None else None
            elif event.type == KEYDOWN and event.key == K_n:
                func = self.on_n_pressed
                func() if func is not None else None
            elif event.type == KEYDOWN and event.key == K_o:
                func = self.on_o_pressed
                func() if func is not None else None
            elif event.type == KEYDOWN and event.key == K_p:
                func = self.on_p_pressed
                func() if func is not None else None
            elif event.type == KEYDOWN and event.key == K_q:
                func = self.on_q_pressed
                func() if func is not None else None
            elif event.type == KEYDOWN and event.key == K_r:
                func = self.on_r_pressed
                func() if func is not None else None
            elif event.type == KEYDOWN and event.key == K_s:
                func = self.on_s_pressed
                func() if func is not None else None
            elif event.type == KEYDOWN and event.key == K_t:
                func = self.on_t_pressed
                func() if func is not None else None
            elif event.type == KEYDOWN and event.key == K_u:
                func = self.on_u_pressed
                func() if func is not None else None
            elif event.type == KEYDOWN and event.key == K_v:
                func = self.on_v_pressed
                func() if func is not None else None
            elif event.type == KEYDOWN and event.key == K_w:
                func = self.on_w_pressed
                func() if func is not None else None
            elif event.type == KEYDOWN and event.key == K_x:
                func = self.on_x_pressed
                func() if func is not None else None
            elif event.type == KEYDOWN and event.key == K_y:
                func = self.on_y_pressed
                func() if func is not None else None
            elif event.type == KEYDOWN and event.key == K_z:
                func = self.on_z_pressed
                func() if func is not None else None
            elif event.type == KEYDOWN and event.key == K_0:
                func = self.on_0_pressed
                func() if func is not None else None
            elif event.type == KEYDOWN and event.key == K_1:
                func = self.on_1_pressed
                func() if func is not None else None
            elif event.type == KEYDOWN and event.key == K_2:
                func = self.on_2_pressed
                func() if func is not None else None
            elif event.type == KEYDOWN and event.key == K_3:
                func = self.on_3_pressed
                func() if func is not None else None
            elif event.type == KEYDOWN and event.key == K_4:
                func = self.on_4_pressed
                func() if func is not None else None
            elif event.type == KEYDOWN and event.key == K_5:
                func = self.on_5_pressed
                func() if func is not None else None
            elif event.type == KEYDOWN and event.key == K_6:
                func = self.on_6_pressed
                func() if func is not None else None
            elif event.type == KEYDOWN and event.key == K_7:
                func = self.on_7_pressed
                func() if func is not None else None
            elif event.type == KEYDOWN and event.key == K_8:
                func = self.on_8_pressed
                func() if func is not None else None
            elif event.type == KEYDOWN and event.key == K_9:
                func = self.on_9_pressed
                func() if func is not None else None
            elif event.type == KEYDOWN and event.key == K_LEFT:
                func = self.on_left_arr_pressed
                func() if func is not None else None
            elif event.type == KEYDOWN and event.key == K_RIGHT:
                func = self.on_right_arr_pressed
                func() if func is not None else None
            elif event.type == KEYDOWN and event.key == K_UP:
                func = self.on_up_arr_pressed
                func() if func is not None else None
            elif event.type == KEYDOWN and event.key == K_DOWN:
                func = self.on_down_arr_pressed
                func() if func is not None else None
            elif event.type == KEYDOWN and event.key == K_SPACE:
                func = self.on_space_pressed
                func() if func is not None else None
            try:
                if event.type == MOUSEBUTTONDOWN and self.img.get_rect().collidepoint(pygame.mouse.get_pos()):
                    func = self.on_sprite_clicked
                    func() if func is not None else None
            except:
                pass
