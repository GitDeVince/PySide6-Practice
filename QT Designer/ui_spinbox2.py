# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'spinbox.ui'
##
## Created by: Qt User Interface Compiler version 6.6.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QPushButton, QSizePolicy,
    QSpinBox, QWidget)
import resource_rc

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(400, 42)
        self.horizontalLayout = QHBoxLayout(Widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.minusbutton = QPushButton(Widget)
        self.minusbutton.setObjectName(u"minusbutton")
        icon = QIcon()
        icon.addFile(u":/newPrefix/minus.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minusbutton.setIcon(icon)

        self.horizontalLayout.addWidget(self.minusbutton)

        self.spinbox = QSpinBox(Widget)
        self.spinbox.setObjectName(u"spinbox")

        self.horizontalLayout.addWidget(self.spinbox)

        self.plusbutton = QPushButton(Widget)
        self.plusbutton.setObjectName(u"plusbutton")
        icon1 = QIcon()
        icon1.addFile(u":/newPrefix/plus.png", QSize(), QIcon.Normal, QIcon.Off)
        self.plusbutton.setIcon(icon1)

        self.horizontalLayout.addWidget(self.plusbutton)


        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Form", None))
        self.minusbutton.setText(QCoreApplication.translate("Widget", u"Minus", None))
        self.plusbutton.setText(QCoreApplication.translate("Widget", u"Plus", None))
    # retranslateUi

