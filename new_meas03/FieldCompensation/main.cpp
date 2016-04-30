#include "fieldcompensator.h"
#include <QApplication>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    fieldCompensator w;
    w.show();

    return a.exec();
}
