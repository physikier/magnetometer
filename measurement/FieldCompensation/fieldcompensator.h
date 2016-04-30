#ifndef FIELDCOMPENSATOR_H
#define FIELDCOMPENSATOR_H

#include <QMainWindow>

namespace Ui {
class fieldCompensator;
}

class fieldCompensator : public QMainWindow
{
    Q_OBJECT

public:
    explicit fieldCompensator(QWidget *parent = 0);
    ~fieldCompensator();

private:
    Ui::fieldCompensator *ui;
};

#endif // FIELDCOMPENSATOR_H
