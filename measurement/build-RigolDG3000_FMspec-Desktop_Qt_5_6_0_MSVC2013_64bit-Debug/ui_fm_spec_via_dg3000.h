/********************************************************************************
** Form generated from reading UI file 'fm_spec_via_dg3000.ui'
**
** Created by: Qt User Interface Compiler version 5.6.0
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_FM_SPEC_VIA_DG3000_H
#define UI_FM_SPEC_VIA_DG3000_H

#include <QtCore/QVariant>
#include <QtWidgets/QAction>
#include <QtWidgets/QApplication>
#include <QtWidgets/QButtonGroup>
#include <QtWidgets/QCheckBox>
#include <QtWidgets/QComboBox>
#include <QtWidgets/QDial>
#include <QtWidgets/QHeaderView>
#include <QtWidgets/QLabel>
#include <QtWidgets/QLineEdit>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QScrollBar>
#include <QtWidgets/QStatusBar>
#include <QtWidgets/QToolBar>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_FM_SPEC_via_DG3000
{
public:
    QWidget *centralWidget;
    QLabel *channel1;
    QLabel *channel2;
    QCheckBox *checkBox_ch1_active;
    QLabel *waveform;
    QComboBox *box_ch1_wform;
    QComboBox *box_ch2_wform;
    QLabel *amplitude;
    QLabel *frequency;
    QLabel *offset;
    QLabel *phase;
    QScrollBar *hscrollbar_ch1_freq;
    QDial *dial_ch1_phase;
    QLineEdit *textbox_ch1_freq;
    QLineEdit *textbox_ch1_phase;
    QPushButton *button_quit;
    QLineEdit *textbox_ch1_ampl;
    QLineEdit *textbox_ch1_off;
    QLabel *active;
    QCheckBox *checkBox_ch2_active;
    QPushButton *button_get;
    QScrollBar *hscrollbar_ch1_ampl;
    QScrollBar *hscrollbar_ch1_off;
    QScrollBar *hscrollbar_ch2_ampl;
    QScrollBar *hscrollbar_ch2_off;
    QLineEdit *textbox_ch2_off;
    QLineEdit *textbox_ch2_freq;
    QScrollBar *hscrollbar_ch2_freq;
    QLineEdit *textbox_ch2_ampl;
    QDial *dial_ch2_phase;
    QLineEdit *textbox_ch2_phase;
    QLabel *label;
    QLabel *label_2;
    QLabel *label_3;
    QLabel *label_4;
    QToolBar *mainToolBar;
    QStatusBar *statusBar;

    void setupUi(QMainWindow *FM_SPEC_via_DG3000)
    {
        if (FM_SPEC_via_DG3000->objectName().isEmpty())
            FM_SPEC_via_DG3000->setObjectName(QStringLiteral("FM_SPEC_via_DG3000"));
        FM_SPEC_via_DG3000->resize(499, 581);
        centralWidget = new QWidget(FM_SPEC_via_DG3000);
        centralWidget->setObjectName(QStringLiteral("centralWidget"));
        channel1 = new QLabel(centralWidget);
        channel1->setObjectName(QStringLiteral("channel1"));
        channel1->setGeometry(QRect(32, 20, 66, 16));
        QFont font;
        font.setFamily(QStringLiteral("Arial"));
        font.setPointSize(10);
        font.setBold(true);
        font.setWeight(75);
        channel1->setFont(font);
        channel2 = new QLabel(centralWidget);
        channel2->setObjectName(QStringLiteral("channel2"));
        channel2->setGeometry(QRect(290, 20, 66, 16));
        channel2->setFont(font);
        checkBox_ch1_active = new QCheckBox(centralWidget);
        checkBox_ch1_active->setObjectName(QStringLiteral("checkBox_ch1_active"));
        checkBox_ch1_active->setGeometry(QRect(104, 70, 16, 16));
        QFont font1;
        font1.setBold(true);
        font1.setWeight(75);
        checkBox_ch1_active->setFont(font1);
        waveform = new QLabel(centralWidget);
        waveform->setObjectName(QStringLiteral("waveform"));
        waveform->setGeometry(QRect(32, 110, 57, 16));
        waveform->setFont(font1);
        box_ch1_wform = new QComboBox(centralWidget);
        box_ch1_wform->setObjectName(QStringLiteral("box_ch1_wform"));
        box_ch1_wform->setGeometry(QRect(104, 110, 54, 20));
        box_ch2_wform = new QComboBox(centralWidget);
        box_ch2_wform->setObjectName(QStringLiteral("box_ch2_wform"));
        box_ch2_wform->setGeometry(QRect(288, 110, 54, 20));
        amplitude = new QLabel(centralWidget);
        amplitude->setObjectName(QStringLiteral("amplitude"));
        amplitude->setGeometry(QRect(32, 220, 57, 16));
        amplitude->setFont(font1);
        frequency = new QLabel(centralWidget);
        frequency->setObjectName(QStringLiteral("frequency"));
        frequency->setGeometry(QRect(32, 150, 57, 16));
        frequency->setFont(font1);
        offset = new QLabel(centralWidget);
        offset->setObjectName(QStringLiteral("offset"));
        offset->setGeometry(QRect(32, 290, 33, 16));
        offset->setFont(font1);
        phase = new QLabel(centralWidget);
        phase->setObjectName(QStringLiteral("phase"));
        phase->setGeometry(QRect(32, 360, 34, 16));
        phase->setFont(font1);
        hscrollbar_ch1_freq = new QScrollBar(centralWidget);
        hscrollbar_ch1_freq->setObjectName(QStringLiteral("hscrollbar_ch1_freq"));
        hscrollbar_ch1_freq->setGeometry(QRect(105, 176, 131, 17));
        hscrollbar_ch1_freq->setMinimum(0);
        hscrollbar_ch1_freq->setMaximum(2000000000);
        hscrollbar_ch1_freq->setPageStep(20);
        hscrollbar_ch1_freq->setOrientation(Qt::Horizontal);
        dial_ch1_phase = new QDial(centralWidget);
        dial_ch1_phase->setObjectName(QStringLiteral("dial_ch1_phase"));
        dial_ch1_phase->setGeometry(QRect(120, 390, 100, 100));
        dial_ch1_phase->setMinimum(-180);
        dial_ch1_phase->setMaximum(180);
        dial_ch1_phase->setTracking(true);
        dial_ch1_phase->setWrapping(true);
        dial_ch1_phase->setNotchesVisible(false);
        textbox_ch1_freq = new QLineEdit(centralWidget);
        textbox_ch1_freq->setObjectName(QStringLiteral("textbox_ch1_freq"));
        textbox_ch1_freq->setGeometry(QRect(104, 150, 133, 20));
        textbox_ch1_freq->setStyleSheet(QStringLiteral(""));
        textbox_ch1_phase = new QLineEdit(centralWidget);
        textbox_ch1_phase->setObjectName(QStringLiteral("textbox_ch1_phase"));
        textbox_ch1_phase->setGeometry(QRect(104, 360, 133, 20));
        button_quit = new QPushButton(centralWidget);
        button_quit->setObjectName(QStringLiteral("button_quit"));
        button_quit->setGeometry(QRect(420, 500, 51, 23));
        button_quit->setMinimumSize(QSize(51, 23));
        button_quit->setMaximumSize(QSize(51, 23));
        textbox_ch1_ampl = new QLineEdit(centralWidget);
        textbox_ch1_ampl->setObjectName(QStringLiteral("textbox_ch1_ampl"));
        textbox_ch1_ampl->setGeometry(QRect(104, 220, 133, 20));
        textbox_ch1_off = new QLineEdit(centralWidget);
        textbox_ch1_off->setObjectName(QStringLiteral("textbox_ch1_off"));
        textbox_ch1_off->setGeometry(QRect(104, 290, 133, 20));
        active = new QLabel(centralWidget);
        active->setObjectName(QStringLiteral("active"));
        active->setGeometry(QRect(32, 70, 35, 16));
        active->setFont(font1);
        checkBox_ch2_active = new QCheckBox(centralWidget);
        checkBox_ch2_active->setObjectName(QStringLiteral("checkBox_ch2_active"));
        checkBox_ch2_active->setGeometry(QRect(288, 70, 16, 16));
        checkBox_ch2_active->setFont(font1);
        button_get = new QPushButton(centralWidget);
        button_get->setObjectName(QStringLiteral("button_get"));
        button_get->setGeometry(QRect(30, 500, 75, 23));
        button_get->setFont(font1);
        hscrollbar_ch1_ampl = new QScrollBar(centralWidget);
        hscrollbar_ch1_ampl->setObjectName(QStringLiteral("hscrollbar_ch1_ampl"));
        hscrollbar_ch1_ampl->setGeometry(QRect(105, 246, 131, 17));
        hscrollbar_ch1_ampl->setMaximum(60);
        hscrollbar_ch1_ampl->setPageStep(2);
        hscrollbar_ch1_ampl->setOrientation(Qt::Horizontal);
        hscrollbar_ch1_off = new QScrollBar(centralWidget);
        hscrollbar_ch1_off->setObjectName(QStringLiteral("hscrollbar_ch1_off"));
        hscrollbar_ch1_off->setGeometry(QRect(105, 316, 131, 17));
        hscrollbar_ch1_off->setMaximum(60);
        hscrollbar_ch1_off->setSingleStep(1);
        hscrollbar_ch1_off->setPageStep(2);
        hscrollbar_ch1_off->setTracking(true);
        hscrollbar_ch1_off->setOrientation(Qt::Horizontal);
        hscrollbar_ch2_ampl = new QScrollBar(centralWidget);
        hscrollbar_ch2_ampl->setObjectName(QStringLiteral("hscrollbar_ch2_ampl"));
        hscrollbar_ch2_ampl->setGeometry(QRect(290, 246, 131, 17));
        hscrollbar_ch2_ampl->setMaximum(60);
        hscrollbar_ch2_ampl->setPageStep(2);
        hscrollbar_ch2_ampl->setOrientation(Qt::Horizontal);
        hscrollbar_ch2_off = new QScrollBar(centralWidget);
        hscrollbar_ch2_off->setObjectName(QStringLiteral("hscrollbar_ch2_off"));
        hscrollbar_ch2_off->setGeometry(QRect(290, 316, 131, 17));
        hscrollbar_ch2_off->setMaximum(60);
        hscrollbar_ch2_off->setPageStep(2);
        hscrollbar_ch2_off->setOrientation(Qt::Horizontal);
        textbox_ch2_off = new QLineEdit(centralWidget);
        textbox_ch2_off->setObjectName(QStringLiteral("textbox_ch2_off"));
        textbox_ch2_off->setGeometry(QRect(289, 290, 133, 20));
        textbox_ch2_freq = new QLineEdit(centralWidget);
        textbox_ch2_freq->setObjectName(QStringLiteral("textbox_ch2_freq"));
        textbox_ch2_freq->setGeometry(QRect(289, 150, 133, 20));
        hscrollbar_ch2_freq = new QScrollBar(centralWidget);
        hscrollbar_ch2_freq->setObjectName(QStringLiteral("hscrollbar_ch2_freq"));
        hscrollbar_ch2_freq->setGeometry(QRect(290, 176, 131, 17));
        hscrollbar_ch2_freq->setMaximum(2000000000);
        hscrollbar_ch2_freq->setPageStep(20);
        hscrollbar_ch2_freq->setOrientation(Qt::Horizontal);
        textbox_ch2_ampl = new QLineEdit(centralWidget);
        textbox_ch2_ampl->setObjectName(QStringLiteral("textbox_ch2_ampl"));
        textbox_ch2_ampl->setGeometry(QRect(289, 220, 133, 20));
        dial_ch2_phase = new QDial(centralWidget);
        dial_ch2_phase->setObjectName(QStringLiteral("dial_ch2_phase"));
        dial_ch2_phase->setGeometry(QRect(306, 390, 100, 100));
        dial_ch2_phase->setMinimum(-180);
        dial_ch2_phase->setMaximum(180);
        dial_ch2_phase->setNotchesVisible(false);
        textbox_ch2_phase = new QLineEdit(centralWidget);
        textbox_ch2_phase->setObjectName(QStringLiteral("textbox_ch2_phase"));
        textbox_ch2_phase->setGeometry(QRect(290, 360, 133, 20));
        label = new QLabel(centralWidget);
        label->setObjectName(QStringLiteral("label"));
        label->setGeometry(QRect(430, 150, 31, 16));
        QFont font2;
        font2.setBold(true);
        font2.setWeight(75);
        font2.setKerning(true);
        label->setFont(font2);
        label_2 = new QLabel(centralWidget);
        label_2->setObjectName(QStringLiteral("label_2"));
        label_2->setGeometry(QRect(430, 220, 41, 16));
        label_2->setFont(font2);
        label_3 = new QLabel(centralWidget);
        label_3->setObjectName(QStringLiteral("label_3"));
        label_3->setGeometry(QRect(430, 290, 41, 16));
        label_3->setFont(font2);
        label_4 = new QLabel(centralWidget);
        label_4->setObjectName(QStringLiteral("label_4"));
        label_4->setGeometry(QRect(430, 360, 41, 16));
        label_4->setFont(font2);
        FM_SPEC_via_DG3000->setCentralWidget(centralWidget);
        mainToolBar = new QToolBar(FM_SPEC_via_DG3000);
        mainToolBar->setObjectName(QStringLiteral("mainToolBar"));
        FM_SPEC_via_DG3000->addToolBar(Qt::TopToolBarArea, mainToolBar);
        statusBar = new QStatusBar(FM_SPEC_via_DG3000);
        statusBar->setObjectName(QStringLiteral("statusBar"));
        FM_SPEC_via_DG3000->setStatusBar(statusBar);

        retranslateUi(FM_SPEC_via_DG3000);

        QMetaObject::connectSlotsByName(FM_SPEC_via_DG3000);
    } // setupUi

    void retranslateUi(QMainWindow *FM_SPEC_via_DG3000)
    {
        FM_SPEC_via_DG3000->setWindowTitle(QApplication::translate("FM_SPEC_via_DG3000", "FM_SPEC_via_DG3000", 0));
        channel1->setText(QApplication::translate("FM_SPEC_via_DG3000", "channel: 1", 0));
        channel2->setText(QApplication::translate("FM_SPEC_via_DG3000", "channel: 2", 0));
        checkBox_ch1_active->setText(QString());
        waveform->setText(QApplication::translate("FM_SPEC_via_DG3000", "waveform", 0));
        box_ch1_wform->clear();
        box_ch1_wform->insertItems(0, QStringList()
         << QApplication::translate("FM_SPEC_via_DG3000", "SIN", 0)
         << QApplication::translate("FM_SPEC_via_DG3000", "RAMP", 0)
         << QApplication::translate("FM_SPEC_via_DG3000", "SQU", 0)
        );
        box_ch2_wform->clear();
        box_ch2_wform->insertItems(0, QStringList()
         << QApplication::translate("FM_SPEC_via_DG3000", "SIN", 0)
         << QApplication::translate("FM_SPEC_via_DG3000", "RAMP", 0)
         << QApplication::translate("FM_SPEC_via_DG3000", "SQU", 0)
        );
        amplitude->setText(QApplication::translate("FM_SPEC_via_DG3000", "amplitude", 0));
        frequency->setText(QApplication::translate("FM_SPEC_via_DG3000", "frequency", 0));
        offset->setText(QApplication::translate("FM_SPEC_via_DG3000", "offset", 0));
        phase->setText(QApplication::translate("FM_SPEC_via_DG3000", "phase", 0));
        textbox_ch1_freq->setText(QString());
        textbox_ch1_phase->setText(QString());
        button_quit->setText(QApplication::translate("FM_SPEC_via_DG3000", "quit", 0));
        textbox_ch1_ampl->setText(QString());
        textbox_ch1_off->setText(QString());
        active->setText(QApplication::translate("FM_SPEC_via_DG3000", "active", 0));
        checkBox_ch2_active->setText(QString());
        button_get->setText(QApplication::translate("FM_SPEC_via_DG3000", "get setting", 0));
        textbox_ch2_off->setText(QString());
        textbox_ch2_freq->setText(QString());
        textbox_ch2_ampl->setText(QString());
        textbox_ch2_phase->setText(QString());
        label->setText(QApplication::translate("FM_SPEC_via_DG3000", "[ Hz ]", 0));
        label_2->setText(QApplication::translate("FM_SPEC_via_DG3000", "[ Vpp ]", 0));
        label_3->setText(QApplication::translate("FM_SPEC_via_DG3000", "[ V ]", 0));
        label_4->setText(QApplication::translate("FM_SPEC_via_DG3000", "[ deg ]", 0));
    } // retranslateUi

};

namespace Ui {
    class FM_SPEC_via_DG3000: public Ui_FM_SPEC_via_DG3000 {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_FM_SPEC_VIA_DG3000_H
