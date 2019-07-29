#    Copyright (c) 2019 Melvyn Depeyrot
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.

from PyQt5 import QtWidgets

import PyUIs


def error_popup(message, header=None):
    error_dialog = QtWidgets.QDialog()
    error_ui = PyUIs.ErrorDialog.Ui_Dialog()
    error_ui.setupUi(error_dialog)
    if header:
        error_ui.header.setText(str(header))
        error_dialog.setWindowTitle(str(header))
    error_ui.errorBox.setText(str(message))
    error_dialog.exec_()
    error_dialog.close()
    error_dialog.deleteLater()
