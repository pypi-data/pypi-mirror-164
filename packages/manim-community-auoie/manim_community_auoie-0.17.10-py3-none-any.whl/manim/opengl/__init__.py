from __future__ import annotations

try:
    from dearpygui import dearpygui as dpg
except ImportError:
    pass


from ..renderer.shader import *
from ..utils.opengl import *
