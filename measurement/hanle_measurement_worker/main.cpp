#include "hanle_measurement_worker.h"
#include <QApplication>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    hanle_measurement_worker w;
    w.show();

    return a.exec();
}
