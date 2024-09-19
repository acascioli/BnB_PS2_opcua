# IMPORT PACKAGES AND MODULES
# ///////////////////////////////////////////////////////////////
import os
import sys
import subprocess


class Functions:
    # SET SVG ICON
    # ///////////////////////////////////////////////////////////////
    def set_svg_icon(icon_name):
        app_path = os.path.abspath(os.getcwd())
        folder = "gui/images/svg_icons/"
        path = os.path.join(app_path, folder)
        icon = os.path.normpath(os.path.join(path, icon_name))
        return icon

    # SET SVG IMAGE
    # ///////////////////////////////////////////////////////////////
    def set_svg_image(icon_name):
        app_path = os.path.abspath(os.getcwd())
        folder = "gui/images/svg_images/"
        path = os.path.join(app_path, folder)
        icon = os.path.normpath(os.path.join(path, icon_name))
        return icon

    # SET IMAGE
    # ///////////////////////////////////////////////////////////////
    def set_image(image_name):
        app_path = os.path.abspath(os.getcwd())
        folder = "gui/images/images/"
        path = os.path.join(app_path, folder)
        image = os.path.normpath(os.path.join(path, image_name))
        return image

    # KEYLOGGER
    # ///////////////////////////////////////////////////////////////

    def keylogging(self):
        app_path = os.path.abspath(os.getcwd())
        self.proc = subprocess.Popen(
            [sys.executable, os.path.join(app_path, "keylogger.py")])
    
    def killkeylogging(self):
        self.proc.terminate()

    # TESTS
    # ///////////////////////////////////////////////////////////////

    def test(chart):
        print('Hols')
        return not True

    def checkbox_toggled(self, state):
        # self.chart.setVisible(state)
        # self.toolbar.setVisible(state)
        print(state)
        self.chart1.setVisible(not state)
        self.toolbar1.setVisible(not state)
