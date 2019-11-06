# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

import os
import bpy
from . Operators.basic_commands import *
from . Operators.curve import *
from . Operators .helpers import *
from . Operators.path import *
from . Operators.selection import *
from . Operators.vertex_group import *
from . Operators.aliases import *

bl_info = {
    "name": "BlendedTurtle",
    "author": "Richard Rose",
    "description": "Turtle graphics in blender",
    "blender": (2, 80, 0),
    "version": (0, 0, 2),
    "location": "View3d > Add > Mesh > New Object",
    "warning": "",
    "category": "Add Mesh"
}

classes = (
    TURTLE_OT_add_turtle,
    TURTLE_OT_clear_screen,
    TURTLE_OT_clean,
    TURTLE_OT_home,
    TURTLE_OT_pen_down,
    TURTLE_OT_pen_up,
    TURTLE_OT_forward,
    TURTLE_OT_backward,
    TURTLE_OT_up,
    TURTLE_OT_down,
    TURTLE_OT_left,
    TURTLE_OT_right,
    TURTLE_OT_left_turn,
    TURTLE_OT_right_turn,
    TURTLE_OT_look_up,
    TURTLE_OT_look_down,
    TURTLE_OT_roll_left,
    TURTLE_OT_roll_right,
    TURTLE_OT_set_pos,
    TURTLE_OT_set_rotation,
    TURTLE_OT_set_heading,
    TURTLE_OT_set_pitch,
    TURTLE_OT_set_roll,
    TURTLE_OT_quadratic_curve,
    TURTLE_OT_cubic_curve,
    TURTLE_OT_begin_path,
    TURTLE_OT_stroke_path,
    TURTLE_OT_fill_path,
    TURTLE_OT_select_all,
    TURTLE_OT_deselect_all,
    TURTLE_OT_select_path,
    TURTLE_OT_new_vert_group,
    TURTLE_OT_select_vert_group,
    TURTLE_OT_deselect_vert_group,
    TURTLE_OT_add_to_vert_group,
    TURTLE_OT_remove_from_vert_group,
    TURTLE_OT_bridge,
    TURTLE_OT_merge,
    TURTLE_OT_select_by_location,
    TURTLE_OT_add_vert,
    TURTLE_OT_select_at_cursor,
    TURTLE_OT_clear_screen_alias,
    TURTLE_OT_pen_down_alias,
    TURTLE_OT_pen_up_alias,
    TURTLE_OT_forward_alias,
    TURTLE_OT_backward_alias,
    TURTLE_OT_down_alias,
    TURTLE_OT_left_alias,
    TURTLE_OT_right_alias,
    TURTLE_OT_left_turn_alias,
    TURTLE_OT_right_turn_alias,
    TURTLE_OT_look_up_alias,
    TURTLE_OT_look_down_alias,
    TURTLE_OT_roll_left_alias,
    TURTLE_OT_roll_right_alias,
    TURTLE_OT_set_pos_alias,
    TURTLE_OT_set_rotation_alias,
    TURTLE_OT_set_heading_alias,
    TURTLE_OT_set_roll_alias,
    TURTLE_OT_quadratic_curve_alias,
    TURTLE_OT_cubic_curve_alias,
    TURTLE_OT_select_all_alias,
    TURTLE_OT_deselect_all_alias,
    TURTLE_OT_select_path_alias,
    TURTLE_OT_new_vert_group_alias,
    TURTLE_OT_select_vert_group_alias,
    TURTLE_OT_deselect_vert_group_alias,
    TURTLE_OT_add_to_vert_group_alias,
    TURTLE_OT_remove_from_vert_group_alias)


def register():
    for cls in classes:
        bpy.utils.register_class(cls)
    bpy.utils.register_manual_map(TURTLE_OT_add_turtle.add_object_manual_map)
    bpy.types.VIEW3D_MT_mesh_add.append(TURTLE_OT_add_turtle.add_object_button)


def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
    bpy.types.VIEW3D_MT_mesh_add.remove(TURTLE_OT_add_turtle.add_object_button)
    bpy.utils.unregister_manual_map(TURTLE_OT_add_turtle.add_object_manual_map)
