#include "fm_spec_via_dg3000.h"
#include "ui_fm_spec_via_dg3000.h"

FM_SPEC_via_DG3000::FM_SPEC_via_DG3000(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::FM_SPEC_via_DG3000)
{
    ui->setupUi(this);
}

FM_SPEC_via_DG3000::~FM_SPEC_via_DG3000()
{
    delete ui;
}
