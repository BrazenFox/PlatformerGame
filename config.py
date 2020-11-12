import colors


'''screen_width = 1600
screen_height = 900'''
screen_width = 1000
screen_height =600
background_image = 'data/images/background2.jpg'


frame_rate = 150


#########################################################################

platform_height = 65
platform_width = 65
platform_color = colors.BLACK

##########################################################################

player_width = 60
player_height = 120

player_color = colors.ALICEBLUE
player_speed = 6
player_boost_speed = 2.5

player_jump_power = 15
player_boost_jump_power = 5
player_gravity = 0.35 # Сила, которая будет тянуть нас вниз

################################################################################

bullet_radius = 5
speed_bullet = 15
color_bullet = colors.RED1
################################################################################

font_name = 'Arial'
font_size = 20

#################################################################################

button_text_color = colors.WHITE,
button_normal_back_color = colors.INDIANRED1
button_hover_back_color = colors.INDIANRED2
button_pressed_back_color = colors.INDIANRED3

menu_girl =  'data/images/girl.png'
menu_mario =  'data/images/mario.png'
menu_boy = 'data/images/boy.png'

menu_offset_x = 20
menu_offset_y = 300
menu_button_w = 80
menu_button_h = 50

coeff_loop = 10

button_loop_w = menu_button_w / 100 * coeff_loop
button_loop_h = menu_button_h / 100 * coeff_loop

font_size_loop = int((font_size / 100) *  (100 + coeff_loop))

center_image_x = 400
center_image_y = 300

##############################################################################################

objects = []
platforms = []
bullets = []

