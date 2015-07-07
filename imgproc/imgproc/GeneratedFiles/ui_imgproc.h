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
#include <QtGui/QHBoxLayout>
#include <QtGui/QHeaderView>
#include <QtGui/QLabel>
#include <QtGui/QListView>
#include <QtGui/QMainWindow>
#include <QtGui/QMenuBar>
#include <QtGui/QPushButton>
#include <QtGui/QSpacerItem>
#include <QtGui/QStatusBar>
#include <QtGui/QToolBar>
#include <QtGui/QWidget>

QT_BEGIN_NAMESPACE

class Ui_imgprocClass
{
public:
    QWidget *centralWidget;
    QLabel *imageLabel;
    QWidget *layoutWidget;
    QHBoxLayout *horizontalLayout;
    QSpacerItem *horizontalSpacer;
    QPushButton *okButton;
    QPushButton *cancelButton;
    QListView *dstImageView;
    QMenuBar *menuBar;
    QToolBar *mainToolBar;
    QStatusBar *statusBar;

    void setupUi(QMainWindow *imgprocClass)
    {
        if (imgprocClass->objectName().isEmpty())
            imgprocClass->setObjectName(QString::fromUtf8("imgprocClass"));
        imgprocClass->resize(530, 298);
        centralWidget = new QWidget(imgprocClass);
        centralWidget->setObjectName(QString::fromUtf8("centralWidget"));
        imageLabel = new QLabel(centralWidget);
        imageLabel->setObjectName(QString::fromUtf8("imageLabel"));
        imageLabel->setGeometry(QRect(9, 9, 241, 181));
        layoutWidget = new QWidget(centralWidget);
        layoutWidget->setObjectName(QString::fromUtf8("layoutWidget"));
        layoutWidget->setGeometry(QRect(9, 207, 512, 25));
        horizontalLayout = new QHBoxLayout(layoutWidget);
        horizontalLayout->setSpacing(6);
        horizontalLayout->setContentsMargins(11, 11, 11, 11);
        horizontalLayout->setObjectName(QString::fromUtf8("horizontalLayout"));
        horizontalLayout->setContentsMargins(0, 0, 0, 0);
        horizontalSpacer = new QSpacerItem(348, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        horizontalLayout->addItem(horizontalSpacer);

        okButton = new QPushButton(layoutWidget);
        okButton->setObjectName(QString::fromUtf8("okButton"));

        horizontalLayout->addWidget(okButton);

        cancelButton = new QPushButton(layoutWidget);
        cancelButton->setObjectName(QString::fromUtf8("cancelButton"));

        horizontalLayout->addWidget(cancelButton);

        dstImageView = new QListView(centralWidget);
        dstImageView->setObjectName(QString::fromUtf8("dstImageView"));
        dstImageView->setGeometry(QRect(260, 0, 256, 192));
        imgprocClass->setCentralWidget(centralWidget);
        menuBar = new QMenuBar(imgprocClass);
        menuBar->setObjectName(QString::fromUtf8("menuBar"));
        menuBar->setGeometry(QRect(0, 0, 530, 23));
        imgprocClass->setMenuBar(menuBar);
        mainToolBar = new QToolBar(imgprocClass);
        mainToolBar->setObjectName(QString::fromUtf8("mainToolBar"));
        imgprocClass->addToolBar(Qt::TopToolBarArea, mainToolBar);
        statusBar = new QStatusBar(imgprocClass);
        statusBar->setObjectName(QString::fromUtf8("statusBar"));
        imgprocClass->setStatusBar(statusBar);

        retranslateUi(imgprocClass);

        QMetaObject::connectSlotsByName(imgprocClass);
    } // setupUi

    void retranslateUi(QMainWindow *imgprocClass)
    {
        imgprocClass->setWindowTitle(QApplication::translate("imgprocClass", "imgproc", 0, QApplication::UnicodeUTF8));
        imageLabel->setText(QString());
        okButton->setText(QApplication::translate("imgprocClass", "OK", 0, QApplication::UnicodeUTF8));
        cancelButton->setText(QApplication::translate("imgprocClass", "Cancel", 0, QApplication::UnicodeUTF8));
    } // retranslateUi

};

namespace Ui {
    class imgprocClass: public Ui_imgprocClass {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_IMGPROC_H
