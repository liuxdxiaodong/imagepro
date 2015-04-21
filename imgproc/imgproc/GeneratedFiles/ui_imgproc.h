/********************************************************************************
** Form generated from reading UI file 'imgproc.ui'
**
** Created by: Qt User Interface Compiler version 4.8.6
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_IMGPROC_H
#define UI_IMGPROC_H

#include <QtCore/QVariant>
#include <QtGui/QAction>
#include <QtGui/QApplication>
#include <QtGui/QButtonGroup>
#include <QtGui/QHeaderView>
#include <QtGui/QMainWindow>
#include <QtGui/QMenuBar>
#include <QtGui/QPlainTextEdit>
#include <QtGui/QPushButton>
#include <QtGui/QStatusBar>
#include <QtGui/QToolBar>
#include <QtGui/QWidget>

QT_BEGIN_NAMESPACE

class Ui_imgprocClass
{
public:
    QWidget *centralWidget;
    QPlainTextEdit *plainTextEdit;
    QPushButton *OKButton;
    QMenuBar *menuBar;
    QToolBar *mainToolBar;
    QStatusBar *statusBar;

    void setupUi(QMainWindow *imgprocClass)
    {
        if (imgprocClass->objectName().isEmpty())
            imgprocClass->setObjectName(QString::fromUtf8("imgprocClass"));
        imgprocClass->resize(600, 400);
        centralWidget = new QWidget(imgprocClass);
        centralWidget->setObjectName(QString::fromUtf8("centralWidget"));
        plainTextEdit = new QPlainTextEdit(centralWidget);
        plainTextEdit->setObjectName(QString::fromUtf8("plainTextEdit"));
        plainTextEdit->setGeometry(QRect(23, 20, 301, 251));
        OKButton = new QPushButton(centralWidget);
        OKButton->setObjectName(QString::fromUtf8("OKButton"));
        OKButton->setGeometry(QRect(440, 150, 75, 23));
        imgprocClass->setCentralWidget(centralWidget);
        menuBar = new QMenuBar(imgprocClass);
        menuBar->setObjectName(QString::fromUtf8("menuBar"));
        menuBar->setGeometry(QRect(0, 0, 600, 23));
        imgprocClass->setMenuBar(menuBar);
        mainToolBar = new QToolBar(imgprocClass);
        mainToolBar->setObjectName(QString::fromUtf8("mainToolBar"));
        imgprocClass->addToolBar(Qt::TopToolBarArea, mainToolBar);
        statusBar = new QStatusBar(imgprocClass);
        statusBar->setObjectName(QString::fromUtf8("statusBar"));
        imgprocClass->setStatusBar(statusBar);

        retranslateUi(imgprocClass);
        QObject::connect(OKButton, SIGNAL(clicked()), imgprocClass, SLOT(showFullScreen()));

        QMetaObject::connectSlotsByName(imgprocClass);
    } // setupUi

    void retranslateUi(QMainWindow *imgprocClass)
    {
        imgprocClass->setWindowTitle(QApplication::translate("imgprocClass", "imgproc", 0, QApplication::UnicodeUTF8));
        OKButton->setText(QApplication::translate("imgprocClass", "OK", 0, QApplication::UnicodeUTF8));
    } // retranslateUi

};

namespace Ui {
    class imgprocClass: public Ui_imgprocClass {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_IMGPROC_H
