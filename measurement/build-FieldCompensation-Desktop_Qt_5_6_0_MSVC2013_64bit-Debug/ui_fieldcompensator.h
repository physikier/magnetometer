/********************************************************************************
** Form generated from reading UI file 'fieldcompensator.ui'
**
** Created by: Qt User Interface Compiler version 5.6.0
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_FIELDCOMPENSATOR_H
#define UI_FIELDCOMPENSATOR_H

#include <QtCore/QVariant>
#include <QtWidgets/QAction>
#include <QtWidgets/QApplication>
#include <QtWidgets/QButtonGroup>
#include <QtWidgets/QHeaderView>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QMenuBar>
#include <QtWidgets/QStatusBar>
#include <QtWidgets/QToolBar>
#include <QtWidgets/QWidget>
#include "pyqtgraph"

QT_BEGIN_NAMESPACE

class Ui_fieldCompensator
{
public:
    QWidget *centralWidget;
    PlotWidget *plot;
    QMenuBar *menuBar;
    QToolBar *mainToolBar;
    QStatusBar *statusBar;

    void setupUi(QMainWindow *fieldCompensator)
    {
        if (fieldCompensator->objectName().isEmpty())
            fieldCompensator->setObjectName(QStringLiteral("fieldCompensator"));
        fieldCompensator->resize(641, 498);
        centralWidget = new QWidget(fieldCompensator);
        centralWidget->setObjectName(QStringLiteral("centralWidget"));
        plot = new PlotWidget(centralWidget);
        plot->setObjectName(QStringLiteral("plot"));
        plot->setGeometry(QRect(30, 10, 581, 421));
        plot->setLayoutDirection(Qt::LeftToRight);
        plot->setResizeAnchor(QGraphicsView::NoAnchor);
        fieldCompensator->setCentralWidget(centralWidget);
        menuBar = new QMenuBar(fieldCompensator);
        menuBar->setObjectName(QStringLiteral("menuBar"));
        menuBar->setGeometry(QRect(0, 0, 641, 21));
        fieldCompensator->setMenuBar(menuBar);
        mainToolBar = new QToolBar(fieldCompensator);
        mainToolBar->setObjectName(QStringLiteral("mainToolBar"));
        fieldCompensator->addToolBar(Qt::TopToolBarArea, mainToolBar);
        statusBar = new QStatusBar(fieldCompensator);
        statusBar->setObjectName(QStringLiteral("statusBar"));
        fieldCompensator->setStatusBar(statusBar);

        retranslateUi(fieldCompensator);

        QMetaObject::connectSlotsByName(fieldCompensator);
    } // setupUi

    void retranslateUi(QMainWindow *fieldCompensator)
    {
        fieldCompensator->setWindowTitle(QApplication::translate("fieldCompensator", "fieldCompensator", 0));
    } // retranslateUi

};

namespace Ui {
    class fieldCompensator: public Ui_fieldCompensator {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_FIELDCOMPENSATOR_H
