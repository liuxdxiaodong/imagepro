#include "imgproc.h"
#include "common.h"

imgproc::imgproc(QWidget *parent, Qt::WFlags flags)
	: QMainWindow(parent, flags)
{
	ui.setupUi(this);
	imgproc::connect()
}

imgproc::~imgproc()
{

}

void imgshow()
{
	cv::Mat src = cv::imread("../../data_and_commonh/2.jpg");
	cv::imshow("sourceimg", src);
}

void on_OKButton_clicked()
{
	
}