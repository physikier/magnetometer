#ifndef HANLE_MEASUREMENT_WORKER_H
#define HANLE_MEASUREMENT_WORKER_H

#include <QMainWindow>

namespace Ui {
class hanle_measurement_worker;
}

class hanle_measurement_worker : public QMainWindow
{
    Q_OBJECT

public:
    explicit hanle_measurement_worker(QWidget *parent = 0);
    ~hanle_measurement_worker();

private:
    Ui::hanle_measurement_worker *ui;
};

#endif // HANLE_MEASUREMENT_WORKER_H
