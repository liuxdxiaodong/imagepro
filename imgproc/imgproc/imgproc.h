#ifndef IMGPROC_H
#define IMGPROC_H

#include <QtGui/QMainWindow>
#include "ui_imgproc.h"

class imgproc : public QMainWindow
{
	Q_OBJECT

public:
	imgproc(QWidget *parent = 0, Qt::WFlags flags = 0);
	~imgproc();
	QListView *srcImageView;
private:
	Ui::imgprocClass ui;
private slots:
	void imgshow();	
};

#endif // IMGPROC_H
