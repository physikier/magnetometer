#include "fieldcompensator.h"
#include "ui_fieldcompensator.h"

fieldCompensator::fieldCompensator(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::fieldCompensator)
{
    ui->setupUi(this);
}

fieldCompensator::~fieldCompensator()
{
    delete ui;
}
