/********************************************************************************
** Form generated from reading UI file 'hanle_measurement_worker.ui'
**
** Created by: Qt User Interface Compiler version 5.6.0
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_HANLE_MEASUREMENT_WORKER_H
#define UI_HANLE_MEASUREMENT_WORKER_H

#include <QtCore/QVariant>
#include <QtWidgets/QAction>
#include <QtWidgets/QApplication>
#include <QtWidgets/QButtonGroup>
#include <QtWidgets/QCheckBox>
#include <QtWidgets/QComboBox>
#include <QtWidgets/QDoubleSpinBox>
#include <QtWidgets/QFrame>
#include <QtWidgets/QHeaderView>
#include <QtWidgets/QLabel>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QMenuBar>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QSpinBox>
#include <QtWidgets/QStatusBar>
#include <QtWidgets/QToolBar>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_hanle_measurement_worker
{
public:
    QWidget *centralWidget;
    QDoubleSpinBox *spinBox_freq_stop_B0;
    QLabel *label_4;
    QDoubleSpinBox *spinBox_freq_step_B0;
    QDoubleSpinBox *spinBox_freq_start_B0;
    QLabel *label_5;
    QDoubleSpinBox *spinBox_off_start_B0;
    QDoubleSpinBox *spinBox_ampl_start_B0;
    QDoubleSpinBox *spinBox_ampl_stop_B0;
    QDoubleSpinBox *spinBox_ampl_step_B0;
    QLabel *label_6;
    QDoubleSpinBox *spinBox_off_stop_B0;
    QDoubleSpinBox *spinBox_off_step_B0;
    QDoubleSpinBox *spinBox_freq_step_B1;
    QDoubleSpinBox *spinBox_off_step_B1;
    QDoubleSpinBox *spinBox_off_start_B1;
    QDoubleSpinBox *spinBox_ampl_stop_B1;
    QDoubleSpinBox *spinBox_ampl_step_B1;
    QLabel *label_7;
    QDoubleSpinBox *spinBox_ampl_start_B1;
    QLabel *label_8;
    QDoubleSpinBox *spinBox_freq_stop_B1;
    QDoubleSpinBox *spinBox_off_stop_B1;
    QLabel *label_9;
    QDoubleSpinBox *spinBox_freq_start_B1;
    QLabel *label_10;
    QLabel *label_11;
    QLabel *label_12;
    QLabel *label_13;
    QLabel *label_14;
    QLabel *label_15;
    QLabel *label_16;
    QLabel *label_17;
    QCheckBox *checkBox_B0;
    QCheckBox *checkBox_B1;
    QSpinBox *spinBox_measure_no;
    QSpinBox *spinBox_cell_id;
    QDoubleSpinBox *spinBox_temp;
    QDoubleSpinBox *spinBox_lpower;
    QSpinBox *spinBox_diode_gain;
    QLabel *label_18;
    QLabel *label_19;
    QLabel *label_20;
    QLabel *label_21;
    QLabel *label_22;
    QSpinBox *spinBox_samples;
    QSpinBox *spinBox_downsampling;
    QDoubleSpinBox *spinBox_mtime;
    QLabel *label_23;
    QLabel *label_24;
    QLabel *label_25;
    QLabel *label_26;
    QLabel *label_27;
    QFrame *line;
    QFrame *line_2;
    QComboBox *comboBox_method_B0;
    QLabel *label_28;
    QComboBox *comboBox_method_B1;
    QLabel *label_29;
    QPushButton *pushButton;
    QMenuBar *menuBar;
    QToolBar *mainToolBar;
    QStatusBar *statusBar;

    void setupUi(QMainWindow *hanle_measurement_worker)
    {
        if (hanle_measurement_worker->objectName().isEmpty())
            hanle_measurement_worker->setObjectName(QStringLiteral("hanle_measurement_worker"));
        hanle_measurement_worker->resize(724, 527);
        centralWidget = new QWidget(hanle_measurement_worker);
        centralWidget->setObjectName(QStringLiteral("centralWidget"));
        centralWidget->setEnabled(true);
        spinBox_freq_stop_B0 = new QDoubleSpinBox(centralWidget);
        spinBox_freq_stop_B0->setObjectName(QStringLiteral("spinBox_freq_stop_B0"));
        spinBox_freq_stop_B0->setGeometry(QRect(120, 130, 62, 22));
        spinBox_freq_stop_B0->setDecimals(4);
        label_4 = new QLabel(centralWidget);
        label_4->setObjectName(QStringLiteral("label_4"));
        label_4->setGeometry(QRect(30, 100, 71, 16));
        QFont font;
        font.setPointSize(8);
        font.setBold(true);
        font.setWeight(75);
        label_4->setFont(font);
        label_4->setAlignment(Qt::AlignRight|Qt::AlignTrailing|Qt::AlignVCenter);
        spinBox_freq_step_B0 = new QDoubleSpinBox(centralWidget);
        spinBox_freq_step_B0->setObjectName(QStringLiteral("spinBox_freq_step_B0"));
        spinBox_freq_step_B0->setGeometry(QRect(120, 160, 62, 22));
        spinBox_freq_step_B0->setDecimals(4);
        spinBox_freq_start_B0 = new QDoubleSpinBox(centralWidget);
        spinBox_freq_start_B0->setObjectName(QStringLiteral("spinBox_freq_start_B0"));
        spinBox_freq_start_B0->setGeometry(QRect(120, 100, 62, 22));
        spinBox_freq_start_B0->setDecimals(4);
        label_5 = new QLabel(centralWidget);
        label_5->setObjectName(QStringLiteral("label_5"));
        label_5->setGeometry(QRect(30, 130, 71, 16));
        label_5->setFont(font);
        label_5->setAlignment(Qt::AlignRight|Qt::AlignTrailing|Qt::AlignVCenter);
        spinBox_off_start_B0 = new QDoubleSpinBox(centralWidget);
        spinBox_off_start_B0->setObjectName(QStringLiteral("spinBox_off_start_B0"));
        spinBox_off_start_B0->setGeometry(QRect(320, 100, 62, 22));
        spinBox_off_start_B0->setDecimals(4);
        spinBox_ampl_start_B0 = new QDoubleSpinBox(centralWidget);
        spinBox_ampl_start_B0->setObjectName(QStringLiteral("spinBox_ampl_start_B0"));
        spinBox_ampl_start_B0->setGeometry(QRect(220, 100, 62, 22));
        spinBox_ampl_start_B0->setDecimals(4);
        spinBox_ampl_stop_B0 = new QDoubleSpinBox(centralWidget);
        spinBox_ampl_stop_B0->setObjectName(QStringLiteral("spinBox_ampl_stop_B0"));
        spinBox_ampl_stop_B0->setGeometry(QRect(220, 130, 62, 22));
        spinBox_ampl_stop_B0->setDecimals(4);
        spinBox_ampl_step_B0 = new QDoubleSpinBox(centralWidget);
        spinBox_ampl_step_B0->setObjectName(QStringLiteral("spinBox_ampl_step_B0"));
        spinBox_ampl_step_B0->setGeometry(QRect(220, 160, 62, 22));
        spinBox_ampl_step_B0->setDecimals(4);
        label_6 = new QLabel(centralWidget);
        label_6->setObjectName(QStringLiteral("label_6"));
        label_6->setGeometry(QRect(40, 160, 61, 16));
        label_6->setFont(font);
        label_6->setAlignment(Qt::AlignRight|Qt::AlignTrailing|Qt::AlignVCenter);
        spinBox_off_stop_B0 = new QDoubleSpinBox(centralWidget);
        spinBox_off_stop_B0->setObjectName(QStringLiteral("spinBox_off_stop_B0"));
        spinBox_off_stop_B0->setGeometry(QRect(320, 130, 62, 22));
        spinBox_off_stop_B0->setDecimals(4);
        spinBox_off_step_B0 = new QDoubleSpinBox(centralWidget);
        spinBox_off_step_B0->setObjectName(QStringLiteral("spinBox_off_step_B0"));
        spinBox_off_step_B0->setGeometry(QRect(320, 160, 62, 22));
        spinBox_off_step_B0->setDecimals(4);
        spinBox_freq_step_B1 = new QDoubleSpinBox(centralWidget);
        spinBox_freq_step_B1->setObjectName(QStringLiteral("spinBox_freq_step_B1"));
        spinBox_freq_step_B1->setGeometry(QRect(120, 390, 62, 22));
        spinBox_freq_step_B1->setDecimals(4);
        spinBox_off_step_B1 = new QDoubleSpinBox(centralWidget);
        spinBox_off_step_B1->setObjectName(QStringLiteral("spinBox_off_step_B1"));
        spinBox_off_step_B1->setGeometry(QRect(320, 390, 62, 22));
        spinBox_off_step_B1->setDecimals(4);
        spinBox_off_start_B1 = new QDoubleSpinBox(centralWidget);
        spinBox_off_start_B1->setObjectName(QStringLiteral("spinBox_off_start_B1"));
        spinBox_off_start_B1->setGeometry(QRect(320, 330, 62, 22));
        spinBox_off_start_B1->setDecimals(4);
        spinBox_ampl_stop_B1 = new QDoubleSpinBox(centralWidget);
        spinBox_ampl_stop_B1->setObjectName(QStringLiteral("spinBox_ampl_stop_B1"));
        spinBox_ampl_stop_B1->setGeometry(QRect(220, 360, 62, 22));
        spinBox_ampl_stop_B1->setDecimals(4);
        spinBox_ampl_step_B1 = new QDoubleSpinBox(centralWidget);
        spinBox_ampl_step_B1->setObjectName(QStringLiteral("spinBox_ampl_step_B1"));
        spinBox_ampl_step_B1->setGeometry(QRect(220, 390, 62, 22));
        spinBox_ampl_step_B1->setDecimals(4);
        label_7 = new QLabel(centralWidget);
        label_7->setObjectName(QStringLiteral("label_7"));
        label_7->setGeometry(QRect(40, 360, 61, 20));
        label_7->setFont(font);
        label_7->setAlignment(Qt::AlignRight|Qt::AlignTrailing|Qt::AlignVCenter);
        spinBox_ampl_start_B1 = new QDoubleSpinBox(centralWidget);
        spinBox_ampl_start_B1->setObjectName(QStringLiteral("spinBox_ampl_start_B1"));
        spinBox_ampl_start_B1->setGeometry(QRect(220, 330, 62, 22));
        spinBox_ampl_start_B1->setDecimals(4);
        label_8 = new QLabel(centralWidget);
        label_8->setObjectName(QStringLiteral("label_8"));
        label_8->setGeometry(QRect(40, 390, 61, 20));
        label_8->setFont(font);
        label_8->setAlignment(Qt::AlignRight|Qt::AlignTrailing|Qt::AlignVCenter);
        spinBox_freq_stop_B1 = new QDoubleSpinBox(centralWidget);
        spinBox_freq_stop_B1->setObjectName(QStringLiteral("spinBox_freq_stop_B1"));
        spinBox_freq_stop_B1->setGeometry(QRect(120, 360, 62, 22));
        spinBox_freq_stop_B1->setDecimals(4);
        spinBox_off_stop_B1 = new QDoubleSpinBox(centralWidget);
        spinBox_off_stop_B1->setObjectName(QStringLiteral("spinBox_off_stop_B1"));
        spinBox_off_stop_B1->setGeometry(QRect(320, 360, 62, 22));
        spinBox_off_stop_B1->setDecimals(4);
        label_9 = new QLabel(centralWidget);
        label_9->setObjectName(QStringLiteral("label_9"));
        label_9->setGeometry(QRect(40, 330, 71, 20));
        label_9->setFont(font);
        spinBox_freq_start_B1 = new QDoubleSpinBox(centralWidget);
        spinBox_freq_start_B1->setObjectName(QStringLiteral("spinBox_freq_start_B1"));
        spinBox_freq_start_B1->setGeometry(QRect(120, 330, 62, 22));
        spinBox_freq_start_B1->setDecimals(4);
        label_10 = new QLabel(centralWidget);
        label_10->setObjectName(QStringLiteral("label_10"));
        label_10->setGeometry(QRect(120, 70, 101, 16));
        label_10->setFont(font);
        label_11 = new QLabel(centralWidget);
        label_11->setObjectName(QStringLiteral("label_11"));
        label_11->setGeometry(QRect(220, 70, 91, 16));
        label_11->setFont(font);
        label_12 = new QLabel(centralWidget);
        label_12->setObjectName(QStringLiteral("label_12"));
        label_12->setGeometry(QRect(320, 70, 61, 16));
        label_12->setFont(font);
        label_13 = new QLabel(centralWidget);
        label_13->setObjectName(QStringLiteral("label_13"));
        label_13->setGeometry(QRect(220, 300, 101, 16));
        label_13->setFont(font);
        label_14 = new QLabel(centralWidget);
        label_14->setObjectName(QStringLiteral("label_14"));
        label_14->setGeometry(QRect(120, 300, 91, 16));
        label_14->setFont(font);
        label_15 = new QLabel(centralWidget);
        label_15->setObjectName(QStringLiteral("label_15"));
        label_15->setGeometry(QRect(320, 300, 61, 16));
        label_15->setFont(font);
        label_16 = new QLabel(centralWidget);
        label_16->setObjectName(QStringLiteral("label_16"));
        label_16->setGeometry(QRect(40, 20, 61, 16));
        QFont font1;
        font1.setPointSize(10);
        font1.setBold(true);
        font1.setWeight(75);
        label_16->setFont(font1);
        label_16->setStyleSheet(QStringLiteral("background-color: rgb(0, 255, 127);"));
        label_17 = new QLabel(centralWidget);
        label_17->setObjectName(QStringLiteral("label_17"));
        label_17->setGeometry(QRect(40, 251, 61, 16));
        label_17->setFont(font1);
        label_17->setAutoFillBackground(false);
        label_17->setStyleSheet(QStringLiteral("background-color: rgb(85, 255, 127);"));
        label_17->setFrameShape(QFrame::NoFrame);
        label_17->setFrameShadow(QFrame::Plain);
        label_17->setMidLineWidth(0);
        checkBox_B0 = new QCheckBox(centralWidget);
        checkBox_B0->setObjectName(QStringLiteral("checkBox_B0"));
        checkBox_B0->setGeometry(QRect(120, 20, 70, 17));
        QFont font2;
        font2.setBold(true);
        font2.setWeight(75);
        checkBox_B0->setFont(font2);
        checkBox_B1 = new QCheckBox(centralWidget);
        checkBox_B1->setObjectName(QStringLiteral("checkBox_B1"));
        checkBox_B1->setGeometry(QRect(120, 250, 70, 17));
        checkBox_B1->setFont(font2);
        spinBox_measure_no = new QSpinBox(centralWidget);
        spinBox_measure_no->setObjectName(QStringLiteral("spinBox_measure_no"));
        spinBox_measure_no->setGeometry(QRect(581, 60, 61, 22));
        spinBox_cell_id = new QSpinBox(centralWidget);
        spinBox_cell_id->setObjectName(QStringLiteral("spinBox_cell_id"));
        spinBox_cell_id->setGeometry(QRect(580, 90, 61, 22));
        spinBox_temp = new QDoubleSpinBox(centralWidget);
        spinBox_temp->setObjectName(QStringLiteral("spinBox_temp"));
        spinBox_temp->setGeometry(QRect(580, 150, 62, 22));
        spinBox_temp->setDecimals(4);
        spinBox_lpower = new QDoubleSpinBox(centralWidget);
        spinBox_lpower->setObjectName(QStringLiteral("spinBox_lpower"));
        spinBox_lpower->setGeometry(QRect(580, 180, 62, 22));
        spinBox_lpower->setDecimals(4);
        spinBox_diode_gain = new QSpinBox(centralWidget);
        spinBox_diode_gain->setObjectName(QStringLiteral("spinBox_diode_gain"));
        spinBox_diode_gain->setGeometry(QRect(580, 210, 61, 22));
        label_18 = new QLabel(centralWidget);
        label_18->setObjectName(QStringLiteral("label_18"));
        label_18->setGeometry(QRect(460, 60, 101, 20));
        label_18->setFont(font);
        label_18->setAlignment(Qt::AlignRight|Qt::AlignTrailing|Qt::AlignVCenter);
        label_19 = new QLabel(centralWidget);
        label_19->setObjectName(QStringLiteral("label_19"));
        label_19->setGeometry(QRect(460, 90, 101, 20));
        label_19->setFont(font);
        label_19->setAlignment(Qt::AlignRight|Qt::AlignTrailing|Qt::AlignVCenter);
        label_20 = new QLabel(centralWidget);
        label_20->setObjectName(QStringLiteral("label_20"));
        label_20->setGeometry(QRect(460, 150, 101, 20));
        label_20->setFont(font);
        label_20->setAlignment(Qt::AlignRight|Qt::AlignTrailing|Qt::AlignVCenter);
        label_21 = new QLabel(centralWidget);
        label_21->setObjectName(QStringLiteral("label_21"));
        label_21->setGeometry(QRect(460, 180, 101, 20));
        label_21->setFont(font);
        label_21->setAlignment(Qt::AlignRight|Qt::AlignTrailing|Qt::AlignVCenter);
        label_22 = new QLabel(centralWidget);
        label_22->setObjectName(QStringLiteral("label_22"));
        label_22->setGeometry(QRect(460, 210, 101, 20));
        label_22->setFont(font);
        label_22->setAlignment(Qt::AlignRight|Qt::AlignTrailing|Qt::AlignVCenter);
        spinBox_samples = new QSpinBox(centralWidget);
        spinBox_samples->setObjectName(QStringLiteral("spinBox_samples"));
        spinBox_samples->setGeometry(QRect(580, 320, 61, 22));
        spinBox_samples->setMaximum(200000);
        spinBox_samples->setValue(200000);
        spinBox_downsampling = new QSpinBox(centralWidget);
        spinBox_downsampling->setObjectName(QStringLiteral("spinBox_downsampling"));
        spinBox_downsampling->setGeometry(QRect(580, 350, 61, 22));
        spinBox_mtime = new QDoubleSpinBox(centralWidget);
        spinBox_mtime->setObjectName(QStringLiteral("spinBox_mtime"));
        spinBox_mtime->setGeometry(QRect(580, 380, 62, 22));
        spinBox_mtime->setDecimals(4);
        label_23 = new QLabel(centralWidget);
        label_23->setObjectName(QStringLiteral("label_23"));
        label_23->setGeometry(QRect(460, 320, 101, 20));
        label_23->setFont(font);
        label_23->setAlignment(Qt::AlignRight|Qt::AlignTrailing|Qt::AlignVCenter);
        label_24 = new QLabel(centralWidget);
        label_24->setObjectName(QStringLiteral("label_24"));
        label_24->setGeometry(QRect(440, 350, 121, 20));
        label_24->setFont(font);
        label_24->setAlignment(Qt::AlignRight|Qt::AlignTrailing|Qt::AlignVCenter);
        label_25 = new QLabel(centralWidget);
        label_25->setObjectName(QStringLiteral("label_25"));
        label_25->setGeometry(QRect(440, 380, 121, 20));
        label_25->setFont(font);
        label_25->setAlignment(Qt::AlignRight|Qt::AlignTrailing|Qt::AlignVCenter);
        label_26 = new QLabel(centralWidget);
        label_26->setObjectName(QStringLiteral("label_26"));
        label_26->setGeometry(QRect(460, 290, 31, 16));
        label_26->setFont(font1);
        label_26->setStyleSheet(QStringLiteral("background-color: rgb(255, 143, 145);"));
        label_27 = new QLabel(centralWidget);
        label_27->setObjectName(QStringLiteral("label_27"));
        label_27->setGeometry(QRect(460, 20, 121, 16));
        label_27->setFont(font1);
        label_27->setStyleSheet(QStringLiteral("background-color: rgb(112, 193, 255);"));
        line = new QFrame(centralWidget);
        line->setObjectName(QStringLiteral("line"));
        line->setGeometry(QRect(420, 60, 21, 351));
        line->setFrameShape(QFrame::VLine);
        line->setFrameShadow(QFrame::Sunken);
        line_2 = new QFrame(centralWidget);
        line_2->setObjectName(QStringLiteral("line_2"));
        line_2->setGeometry(QRect(40, 200, 341, 21));
        line_2->setFrameShape(QFrame::HLine);
        line_2->setFrameShadow(QFrame::Sunken);
        comboBox_method_B0 = new QComboBox(centralWidget);
        comboBox_method_B0->setObjectName(QStringLiteral("comboBox_method_B0"));
        comboBox_method_B0->setGeometry(QRect(330, 19, 51, 20));
        label_28 = new QLabel(centralWidget);
        label_28->setObjectName(QStringLiteral("label_28"));
        label_28->setGeometry(QRect(250, 20, 61, 16));
        label_28->setFont(font);
        label_28->setAlignment(Qt::AlignRight|Qt::AlignTrailing|Qt::AlignVCenter);
        comboBox_method_B1 = new QComboBox(centralWidget);
        comboBox_method_B1->setObjectName(QStringLiteral("comboBox_method_B1"));
        comboBox_method_B1->setGeometry(QRect(330, 250, 51, 20));
        label_29 = new QLabel(centralWidget);
        label_29->setObjectName(QStringLiteral("label_29"));
        label_29->setGeometry(QRect(250, 250, 61, 16));
        label_29->setFont(font);
        label_29->setAlignment(Qt::AlignRight|Qt::AlignTrailing|Qt::AlignVCenter);
        pushButton = new QPushButton(centralWidget);
        pushButton->setObjectName(QStringLiteral("pushButton"));
        pushButton->setGeometry(QRect(520, 440, 121, 23));
        pushButton->setFont(font2);
        pushButton->setStyleSheet(QLatin1String("color: rgb(255, 0, 127);\n"
"background-color: rgb(255, 87, 90);"));
        hanle_measurement_worker->setCentralWidget(centralWidget);
        menuBar = new QMenuBar(hanle_measurement_worker);
        menuBar->setObjectName(QStringLiteral("menuBar"));
        menuBar->setGeometry(QRect(0, 0, 724, 21));
        hanle_measurement_worker->setMenuBar(menuBar);
        mainToolBar = new QToolBar(hanle_measurement_worker);
        mainToolBar->setObjectName(QStringLiteral("mainToolBar"));
        hanle_measurement_worker->addToolBar(Qt::TopToolBarArea, mainToolBar);
        statusBar = new QStatusBar(hanle_measurement_worker);
        statusBar->setObjectName(QStringLiteral("statusBar"));
        hanle_measurement_worker->setStatusBar(statusBar);

        retranslateUi(hanle_measurement_worker);

        QMetaObject::connectSlotsByName(hanle_measurement_worker);
    } // setupUi

    void retranslateUi(QMainWindow *hanle_measurement_worker)
    {
        hanle_measurement_worker->setWindowTitle(QApplication::translate("hanle_measurement_worker", "hanle_measurement_worker", 0));
        label_4->setText(QApplication::translate("hanle_measurement_worker", "start value", 0));
        label_5->setText(QApplication::translate("hanle_measurement_worker", "stop value", 0));
        label_6->setText(QApplication::translate("hanle_measurement_worker", "step size", 0));
        label_7->setText(QApplication::translate("hanle_measurement_worker", "stop value", 0));
        label_8->setText(QApplication::translate("hanle_measurement_worker", "step size", 0));
        label_9->setText(QApplication::translate("hanle_measurement_worker", "start value", 0));
        label_10->setText(QApplication::translate("hanle_measurement_worker", "frequency [Hz]", 0));
        label_11->setText(QApplication::translate("hanle_measurement_worker", "amplitude [Vpp]", 0));
        label_12->setText(QApplication::translate("hanle_measurement_worker", "offset [V]", 0));
        label_13->setText(QApplication::translate("hanle_measurement_worker", "amplitude [Vpp]", 0));
        label_14->setText(QApplication::translate("hanle_measurement_worker", "frequency [Hz]", 0));
        label_15->setText(QApplication::translate("hanle_measurement_worker", "offset [V]", 0));
        label_16->setText(QApplication::translate("hanle_measurement_worker", "B0", 0));
        label_17->setText(QApplication::translate("hanle_measurement_worker", "B1", 0));
        checkBox_B0->setText(QApplication::translate("hanle_measurement_worker", "active", 0));
        checkBox_B1->setText(QApplication::translate("hanle_measurement_worker", "active", 0));
        label_18->setText(QApplication::translate("hanle_measurement_worker", "measurement no.", 0));
        label_19->setText(QApplication::translate("hanle_measurement_worker", "cell id", 0));
        label_20->setText(QApplication::translate("hanle_measurement_worker", "temperature [C]", 0));
        label_21->setText(QApplication::translate("hanle_measurement_worker", "laser power [\302\265W]", 0));
        label_22->setText(QApplication::translate("hanle_measurement_worker", "photo diode gain [dB]", 0));
        label_23->setText(QApplication::translate("hanle_measurement_worker", "samples", 0));
        label_24->setText(QApplication::translate("hanle_measurement_worker", "downsampling factor", 0));
        label_25->setText(QApplication::translate("hanle_measurement_worker", "measurment time [s]", 0));
        label_26->setText(QApplication::translate("hanle_measurement_worker", "DAQ", 0));
        label_27->setText(QApplication::translate("hanle_measurement_worker", "Global parameters", 0));
        comboBox_method_B0->clear();
        comboBox_method_B0->insertItems(0, QStringList()
         << QApplication::translate("hanle_measurement_worker", "freq", 0)
         << QApplication::translate("hanle_measurement_worker", "ampl", 0)
         << QApplication::translate("hanle_measurement_worker", "off", 0)
         << QApplication::translate("hanle_measurement_worker", "const", 0)
        );
        label_28->setText(QApplication::translate("hanle_measurement_worker", "method", 0));
        comboBox_method_B1->clear();
        comboBox_method_B1->insertItems(0, QStringList()
         << QApplication::translate("hanle_measurement_worker", "const", 0)
         << QApplication::translate("hanle_measurement_worker", "freq", 0)
         << QApplication::translate("hanle_measurement_worker", "ampl", 0)
         << QApplication::translate("hanle_measurement_worker", "off", 0)
        );
        label_29->setText(QApplication::translate("hanle_measurement_worker", "method", 0));
        pushButton->setText(QApplication::translate("hanle_measurement_worker", "start measurement", 0));
    } // retranslateUi

};

namespace Ui {
    class hanle_measurement_worker: public Ui_hanle_measurement_worker {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_HANLE_MEASUREMENT_WORKER_H
