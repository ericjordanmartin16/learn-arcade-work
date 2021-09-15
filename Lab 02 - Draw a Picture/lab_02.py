"""
Eric Martin, Intro to Computer Science, Instructor Paul Craven. Lab #2: Draw a Picture.
"""
import arcade

# Open a window
arcade.open_window(600, 600, "Drawing Example")

# Set the background color
# arcade.set_background_color((158,93,153)) # two parenthesis for RGB color.
arcade.set_background_color((52, 168, 50))

# Get ready to draw
arcade.start_render()

# Draw east-west streets.
arcade.draw_lrtb_rectangle_filled(0, 250, 550, 530, (168, 111, 50)) # upper
arcade.draw_lrtb_rectangle_filled(0, 600, 350, 330, (168, 111, 50)) # middle
arcade.draw_lrtb_rectangle_filled(0, 525, 150, 130, (168, 111, 50)) # lower

# Draw north-south streets.
arcade.draw_lrtb_rectangle_filled(250, 270, 600, 0, (168, 111, 50)) # left
arcade.draw_lrtb_rectangle_filled(525, 545, 330, 0, (168, 111, 50)) # right


def get_right_house_coordinate(left_house_coordinate):
    right_house_coordinate = left_house_coordinate + 40
    return right_house_coordinate


def get_bottom_house_coordinate(top_house_coordinate):
    bottom_house_coordinate = top_house_coordinate - 40
    return bottom_house_coordinate


# Draw squares for the houses.
house_2nd_street_top = 400
house_2nd_street_bottom = get_bottom_house_coordinate(house_2nd_street_top)

house_3rd_street_top = 200
house_3rd_street_bottom = get_bottom_house_coordinate(house_3rd_street_top)

house1_left = 290
house1_right = get_right_house_coordinate(house1_left)
house2_left = 350
house2_right = get_right_house_coordinate(house2_left)
house3_left = 410
house3_right = get_right_house_coordinate(house3_left)
house4_left = 470
house4_right = get_right_house_coordinate(house4_left)

arcade.draw_lrtb_rectangle_filled(house1_left, house1_right, house_2nd_street_top, house_2nd_street_bottom, (70, 50, 168)) # purple
arcade.draw_lrtb_rectangle_filled(house2_left, house2_right, house_2nd_street_top, house_2nd_street_bottom, (50, 173, 149)) # turquoise
arcade.draw_lrtb_rectangle_filled(house3_left, house3_right, house_2nd_street_top, house_2nd_street_bottom, (207, 10, 17)) # red
arcade.draw_lrtb_rectangle_filled(house4_left, house4_right, house_2nd_street_top, house_2nd_street_bottom, (201, 201, 157)) # off-white


arcade.draw_lrtb_rectangle_filled(house1_left, house1_right, house_3rd_street_top, house_3rd_street_bottom, (70, 50, 168)) # purple
arcade.draw_lrtb_rectangle_filled(house2_left, house2_right, house_3rd_street_top, house_3rd_street_bottom, (50, 173, 149)) # turquoise
arcade.draw_lrtb_rectangle_filled(house3_left, house3_right, house_3rd_street_top, house_3rd_street_bottom, (207, 10, 17)) # red
arcade.draw_lrtb_rectangle_filled(house4_left, house4_right, house_3rd_street_top, house_3rd_street_bottom, (201, 201, 157)) # off-white


def draw_roof(house_left, house_right, house_top):
    """Draw roofs for the houses"""
    house_center = (house_right + house_left) / 2
    roof_top = house_top + 30
    roof = arcade.draw_triangle_filled(house_left, house_top, house_right, house_top, house_center, roof_top, (59, 52, 26))
    return roof


draw_roof(house1_left, house1_right, house_2nd_street_top)
draw_roof(house2_left, house2_right, house_2nd_street_top)
draw_roof(house3_left, house3_right, house_2nd_street_top)
draw_roof(house4_left, house4_right, house_2nd_street_top)

draw_roof(house1_left, house1_right, house_3rd_street_top)
draw_roof(house2_left, house2_right, house_3rd_street_top)
draw_roof(house3_left, house3_right, house_3rd_street_top)
draw_roof(house4_left, house4_right, house_3rd_street_top)

# Draw a tree using a polygon with a list of points
arcade.draw_rectangle_filled(150, 390, 20, 60, arcade.csscolor.SIENNA)
arcade.draw_polygon_filled(((150, 470),
                            (130, 430),
                            (120, 390),
                            (180, 390),
                            (170, 430)
                            ),
                           arcade.csscolor.DARK_GREEN)

arcade.draw_rectangle_filled(120, 190, 20, 60, arcade.csscolor.SIENNA)
arcade.draw_polygon_filled(((120, 270),
                            (100, 230),
                            (90, 190),
                            (150, 190),
                            (140, 230)
                            ),
                           arcade.csscolor.DARK_GREEN)

# Draw a pond
arcade.draw_ellipse_filled(450, 550, 100, 60, arcade.csscolor.BLUE, 0, -1)

# Finish drawing
arcade.finish_render()

# Keep the window up until someone closes it.
arcade.run()