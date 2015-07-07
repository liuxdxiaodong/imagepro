#include "imgproc.h"
#include "common.h"

imgproc::imgproc(QWidget *parent, Qt::WFlags flags)
	: QMainWindow(parent, flags)
{
	ui.setupUi(this);
	connect(ui.OKButton,SIGNAL(clicked()),this,SLOT(accept()));
	connect(ui.OKButton,SIGNAL(clicked()),ui.dstImageView,SLOT(imageShow()));
}

imgproc::~imgproc()
{

}

void imgproc::on_imageLabel_imageShow()
{
	cv::Mat src = cv::imread("C:/Users/CGGI_006/Desktop/LXD/data/2.jpg");

}