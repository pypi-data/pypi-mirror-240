# Copyright (C) 2023  Loren Eteval <loren.eteval@proton.me>
#
# This file is part of Furious.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

from Furious.Gui.Action import Action, Seperator
from Furious.Widget.Widget import ListWidget, MainWindow, Menu, MessageBox
from Furious.Utility.Constants import APPLICATION_NAME, PLATFORM, GOLDEN_RATIO, ROOT_DIR
from Furious.Utility.Utility import (
    StateContext,
    SupportConnectedCallback,
    SupportThemeChangedCallback,
    bootstrapIcon,
    bootstrapIconWhite,
    enumValueWrapper,
    getUbuntuRelease,
    moveToCenter,
)
from Furious.Utility.Translator import Translatable, gettext as _

from PySide6 import QtCore
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QFileDialog, QListWidget, QListWidgetItem

import os
import shutil
import logging
import darkdetect

logger = logging.getLogger(__name__)


class QuestionDeleteBox(MessageBox):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.isMulti = False
        self.possibleRemark = ''

        self.setWindowTitle(_('Delete'))

        self.setStandardButtons(
            MessageBox.StandardButton.Yes | MessageBox.StandardButton.No
        )

    def getText(self):
        if self.isMulti:
            return _('Delete these asset files?')
        else:
            return _('Delete this asset file?') + f'\n\n{self.possibleRemark}'

    def retranslate(self):
        with StateContext(self):
            self.setWindowTitle(_(self.windowTitle()))
            self.setText(self.getText())

            # Ignore informative text, buttons

            self.moveToCenter()


class AssetExistsBox(MessageBox):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle(_('Import'))

        self.setStandardButtons(
            MessageBox.StandardButton.Yes | MessageBox.StandardButton.No
        )

    def retranslate(self):
        with StateContext(self):
            self.setWindowTitle(_(self.windowTitle()))
            self.setText(_(self.text()))

            # Ignore informative text, buttons

            self.moveToCenter()


class ImportAction(Action):
    def __init__(self, **kwargs):
        super().__init__(_('Import From File...'), **kwargs)

        self.assetExistsBox = AssetExistsBox(
            icon=MessageBox.Icon.Question, parent=self.parent()
        )
        self.importErrorBox = MessageBox(
            icon=MessageBox.Icon.Critical, parent=self.parent()
        )
        self.importSuccessBox = MessageBox(
            icon=MessageBox.Icon.Information, parent=self.parent()
        )

    def triggeredCallback(self, checked):
        filename, selectedFilter = QFileDialog.getOpenFileName(
            self.parent(), _('Import File'), filter=_('All files (*)')
        )

        if filename:
            basename = os.path.basename(filename)

            if os.path.isfile(AssetViewerWidget.AssetDir / os.path.basename(filename)):
                self.assetExistsBox.setWindowTitle(_('Import'))
                self.assetExistsBox.setText(_('Asset file already exists. Overwrite?'))
                self.assetExistsBox.setInformativeText(basename)

                if self.assetExistsBox.exec() == enumValueWrapper(
                    MessageBox.StandardButton.No
                ):
                    # Do not overwrite
                    return

            try:
                shutil.copy(filename, AssetViewerWidget.AssetDir)
            except shutil.SameFileError:
                # Same file imported. Do nothing
                pass
            except Exception as ex:
                # Any non-exit exception

                self.importErrorBox.setWindowTitle(_('Import'))
                self.importErrorBox.setText(_('Error import asset file.'))
                self.importErrorBox.setInformativeText(str(ex))

                # Show the MessageBox and wait for user to close it
                self.importErrorBox.exec()
            else:
                self.parent().flushItem()

                self.importSuccessBox.setWindowTitle(_('Import'))
                self.importSuccessBox.setText(_('Import asset file success.'))

                # Show the MessageBox and wait for user to close it
                self.importSuccessBox.exec()


class ExitAction(Action):
    def __init__(self, **kwargs):
        super().__init__(_('Exit'), **kwargs)

    def triggeredCallback(self, checked):
        self.parent().hide()


class AssetViewerWidget(SupportThemeChangedCallback, MainWindow):
    AssetDir = ROOT_DIR / APPLICATION_NAME / 'Data' / 'xray'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle(_('Asset File'))
        self.setWindowIcon(bootstrapIcon('rocket-takeoff-window.svg'))

        self.questionDeleteBox = QuestionDeleteBox(
            icon=MessageBox.Icon.Question, parent=self
        )

        self.listWidget = ListWidget(parent=self)
        self.listWidget.setSelectionBehavior(QListWidget.SelectionBehavior.SelectRows)
        self.listWidget.setSelectionMode(QListWidget.SelectionMode.ExtendedSelection)
        self.listWidget.setIconSize(QtCore.QSize(64, 64))

        if PLATFORM == 'Linux' and getUbuntuRelease() == '20.04':
            self.initialTheme = darkdetect.theme()
        else:
            self.initialTheme = None

        self.flushItem()
        self.setCentralWidget(self.listWidget)

        logger.info(f'asset dir is \'{AssetViewerWidget.AssetDir}\'')

        contextMenuActions = [
            Action(
                _('Delete'), callback=lambda: self.deleteSelectedItem(), parent=self
            ),
        ]

        self.contextMenu = Menu(*contextMenuActions)

        self.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.CustomContextMenu)
        self.customContextMenuRequested.connect(self.handleCustomContextMenuRequested)

        fileMenuActions = [
            ImportAction(parent=self),
            Seperator(),
            ExitAction(parent=self),
        ]

        for menu in (fileMenuActions,):
            for action in menu:
                if isinstance(action, Action):
                    if hasattr(self, f'{action}'):
                        logger.warning(f'{self} already has action {action}')

                    setattr(self, f'{action}', action)

        self._fileMenu = Menu(*fileMenuActions, title=_('File'), parent=self)
        self.menuBar().addMenu(self._fileMenu)

    def setWidthAndHeight(self):
        self.setGeometry(100, 100, 360, 360 * GOLDEN_RATIO)

    @QtCore.Slot(QtCore.QPoint)
    def handleCustomContextMenuRequested(self, point):
        self.contextMenu.exec(self.mapToGlobal(point))

    def deleteSelectedItem(self):
        indexes = self.listWidget.selectedIndex

        if len(indexes) == 0:
            # Nothing selected
            return

        self.questionDeleteBox.isMulti = bool(len(indexes) > 1)
        self.questionDeleteBox.possibleRemark = (
            f'{self.listWidget.item(indexes[0]).text()}'
        )
        self.questionDeleteBox.setText(self.questionDeleteBox.getText())

        if self.questionDeleteBox.exec() == enumValueWrapper(
            MessageBox.StandardButton.No
        ):
            # Do not delete
            return

        for index in indexes:
            os.remove(AssetViewerWidget.AssetDir / self.listWidget.item(index).text())

        self.flushItem()

    def flushItemByTheme(self, theme):
        self.listWidget.clear()

        for filename in os.listdir(AssetViewerWidget.AssetDir):
            if os.path.isfile(AssetViewerWidget.AssetDir / filename):
                item = QListWidgetItem(filename)

                if theme == 'Dark':
                    if PLATFORM == 'Windows':
                        # Windows. Always use black icon
                        item.setIcon(bootstrapIcon('file-earmark.svg'))
                    else:
                        item.setIcon(bootstrapIconWhite('file-earmark.svg'))
                else:
                    item.setIcon(bootstrapIcon('file-earmark.svg'))

                self.listWidget.addItem(item)

    def flushItem(self):
        if PLATFORM == 'Linux' and getUbuntuRelease() == '20.04':
            assert self.initialTheme is not None

            # Ubuntu 20.04. Flush by initial theme
            self.flushItemByTheme(self.initialTheme)
        else:
            self.flushItemByTheme(darkdetect.theme())

    def themeChangedCallback(self, theme):
        if PLATFORM == 'Linux' and getUbuntuRelease() == '20.04':
            # Ubuntu 20.04 system dark theme does not
            # change menu color. Do nothing
            pass
        else:
            self.flushItemByTheme(theme)
