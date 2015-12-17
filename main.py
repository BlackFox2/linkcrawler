#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
blablabla
"""
from PyQt5.QtGui import QIcon, QFont, QPainter, QColor
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
import random

from link_crawler import LinkCrawler


class Form(QWidget):
    def __init__(self, parent=None):
        super().__init__()
        self.initUI()

    def initUI(self):

        self.text = u'\u041b\u0435\u0432 \u041d\u0438\u043a\u043e\u043b\u0430\
\u0435\u0432\u0438\u0447 \u0422\u043e\u043b\u0441\u0442\u043e\u0439: \n\
\u0410\u043d\u043d\u0430 \u041a\u0430\u0440\u0435\u043d\u0438\u043d\u0430'

        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('Draw text')
        self.show()


    def paintEvent(self, event):

        qp = QPainter()
        qp.begin(self)
        self.drawPoints(qp)
        qp.end()


    def drawText(self, event, qp):

        qp.setPen(QColor(168, 34, 3))
        qp.setFont(QFont('Decorative', 10))
        qp.drawText(event.rect(), Qt.AlignCenter, self.text)

    def drawPoints(self, qp):

        qp.setPen(Qt.red)
        size = self.size()

        for i in range(1000):
            x = random.randint(1, size.width()-1)
            y = random.randint(1, size.height()-1)
            qp.drawPoint(x, y)

if __name__ == "__main__":
    import sys
    # app = QApplication(sys.argv)
    # ex = Form()
    # sys.exit(app.exec_())
    crawler = LinkCrawler('http://www.computerbase.de')
    links = crawler.get_links()
    print("asdf")

