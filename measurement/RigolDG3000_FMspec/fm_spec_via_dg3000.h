#ifndef FM_SPEC_VIA_DG3000_H
#define FM_SPEC_VIA_DG3000_H

#include <QMainWindow>

namespace Ui {
class FM_SPEC_via_DG3000;
}

class FM_SPEC_via_DG3000 : public QMainWindow
{
    Q_OBJECT

public:
    explicit FM_SPEC_via_DG3000(QWidget *parent = 0);
    ~FM_SPEC_via_DG3000();

private:
    Ui::FM_SPEC_via_DG3000 *ui;
};

#endif // FM_SPEC_VIA_DG3000_H
