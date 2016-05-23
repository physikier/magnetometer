#include "fm_spec_via_dg3000.h"
#include <QApplication>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    FM_SPEC_via_DG3000 w;
    w.show();

    return a.exec();
}
