#include "hanle_measurement_worker.h"
#include "ui_hanle_measurement_worker.h"

hanle_measurement_worker::hanle_measurement_worker(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::hanle_measurement_worker)
{
    ui->setupUi(this);
}

hanle_measurement_worker::~hanle_measurement_worker()
{
    delete ui;
}
