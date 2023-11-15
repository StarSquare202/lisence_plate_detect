# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'loadingWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
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
from PySide6.QtWidgets import (QApplication, QDialog, QGridLayout, QLabel,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_Loading(object):
    def setupUi(self, Loading):
        if not Loading.objectName():
            Loading.setObjectName(u"Loading")
        Loading.resize(522, 472)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Loading.sizePolicy().hasHeightForWidth())
        Loading.setSizePolicy(sizePolicy)
        Loading.setMinimumSize(QSize(522, 472))
        Loading.setWindowOpacity(0.8)
        Loading.setStyleSheet(u"background-color: rgba(74, 74, 74, 70);")
        Loading.setWindowFlags(Qt.FramelessWindowHint)
        self.gridLayout = QGridLayout(Loading)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(5, -1, 5, -1)
        self.loading_label_2 = QLabel(Loading)
        self.loading_label_2.setObjectName(u"loading_label_2")
        self.loading_label_2.setStyleSheet(u"background-color:rgba(0,0,0,0);")
        self.loading_label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.loading_label_2)

        self.label_4 = QLabel(Loading)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"background-color:rgba(0,0,0,0);")

        self.verticalLayout_3.addWidget(self.label_4)

        self.label_5 = QLabel(Loading)
        self.label_5.setObjectName(u"label_5")
        font = QFont()
        font.setFamilies([u"\ub098\ub214\uc2a4\ud018\uc5b4 Bold"])
        font.setPointSize(12)
        font.setBold(False)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet(u"background-color:rgba(0,0,0,0);\n"
"color: rgb(255, 255, 255);")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_5)

        self.label_6 = QLabel(Loading)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setStyleSheet(u"background-color:rgba(0,0,0,0);")

        self.verticalLayout_3.addWidget(self.label_6)

        self.verticalLayout_3.setStretch(0, 2)
        self.verticalLayout_3.setStretch(2, 2)
        self.verticalLayout_3.setStretch(3, 3)

        self.gridLayout.addLayout(self.verticalLayout_3, 0, 0, 1, 1)


        self.retranslateUi(Loading)

        QMetaObject.connectSlotsByName(Loading)
    # setupUi

    def retranslateUi(self, Loading):
        Loading.setWindowTitle(QCoreApplication.translate("Loading", u"Dialog", None))
        self.loading_label_2.setText("")
        self.label_4.setText("")
        self.label_5.setText(QCoreApplication.translate("Loading", u"\ucd94\ucd9c \uacb0\uacfc \uc0dd\uc131 \uc911...", None))
        self.label_6.setText("")
    # retranslateUi

