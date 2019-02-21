# coding:utf-8
# --author-- lanhua.zhou
from __future__ import print_function

import sys
import logging

from qtpy import QtGui, QtCore

__all__ = ["MenuListModel"]

_logger = logging.getLogger(__name__)


class MenuListModel(QtCore.QAbstractListModel):
    """
    asset model

    """

    def __init__(self, data=[], parent=None):
        super(MenuListModel, self).__init__(parent)
        self._items = data

    def rowCount(self, parent=QtCore.QModelIndex()):
        """
        return len asset
        """
        return len(self._items)

    def data(self, index, role=0):
        if not index.isValid() or not 0 <= index.row() < len(self._items):
            return None

        if role == 0:
            return self._items[index.row()]