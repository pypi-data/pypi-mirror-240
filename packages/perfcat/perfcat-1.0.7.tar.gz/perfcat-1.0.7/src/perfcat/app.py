#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   app.py
@Time    :   2022/04/28 19:17:00
@Author  :   Calros Teng 
@Version :   1.0
@Contact :   303359166@qq.com
@License :   (C)Copyright 2017-2018, Xin Yuan Studio
@Desc    :   app全局对象
"""


# here put the import lib
import logging

import pkg_resources
from PySide6.QtWidgets import QApplication

from . import __version__, __author__, __author_email__, pages
from .modules.hot_plug import HotPlugWatcher
from .ui.layout import MainWindow

log = logging.getLogger(__name__)


def about_content():

    about_txt: str = pkg_resources.resource_string(
        __package__, "assets/ABOUT.md"
    ).decode("utf-8")

    doc = about_txt.format(
        __version__=__version__,
        __author__=__author__,
        __author_email__=__author_email__,
    )
    return doc


class PerfcatApplication(QApplication):
    """
    Perfcat App本体
    负责App框架管理

    _extended_summary_

    Args:
        QApplication (_type_): _description_
    """

    def __init__(self, *args):
        super().__init__(*args)

        self.load_stylesheet()
        self.main_win = MainWindow()
        self.main_win.set_about_info(about_content())
        self.main_win.show()

        self._install_pages()

        HotPlugWatcher.install(self)

    @classmethod
    @property
    def instance(cls) -> "PerfcatApplication":
        return QApplication.instance()

    def load_stylesheet(self, path=None):
        if not path:
            stylesheet = pkg_resources.resource_string(
                __package__, "assets/css/default.css"
            ).decode("utf-8")
            log.debug("加载内置stylesheet")
        else:
            with open(path) as f:
                stylesheet = f.read()
            log.debug(f"加载stylesheet：{path}")

        self.setStyleSheet(stylesheet)
        log.debug("加载stylesheet")

    def _install_pages(self):
        w = self.main_win
        for page in pages.register:
            w.add_page(page(w))
