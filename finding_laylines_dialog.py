# -*- coding: utf-8 -*-
"""
/***************************************************************************
 finding_laylinesDialog
                                 A QGIS plugin
 This Plugin finds the surface water flow path on a field.
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2021-03-19
        git sha              : $Format:%H$
        copyright            : (C) 2021 by FALASY Anamelechi
        email                : fvw.services@gmail.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

import os

from qgis.PyQt import uic
from qgis.PyQt import QtWidgets
from qgis.PyQt import QtCore
from qgis.core import *

# This loads your .ui file so that PyQt can populate your plugin with the elements from Qt Designer
FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'finding_laylines_dialog_base.ui'))


class finding_laylinesDialog(QtWidgets.QDialog, FORM_CLASS):
    def __init__(self, parent=None):
        """Constructor."""
        super(finding_laylinesDialog, self).__init__(parent)
        # Set up the user interface from Designer through FORM_CLASS.
        # After self.setupUi() you can access any designer object by doing
        # self.<objectname>, and you can use autoconnect slots - see
        # http://qt-project.org/doc/qt-4.8/designer-using-a-ui-file.html
        # #widgets-and-dialogs-with-auto-connect
        self.setupUi(self)
