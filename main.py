import sys
from design import *
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog
from PyQt5.QtGui import QPixmap


class Main(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)
        self.btnEscolherArquivo.clicked.connect(self.abrir_imagem)
        self.btnRedimensionar.clicked.connect(self.redimensionar)
        self.btnSalvar.clicked.connect(self.salvar)

    def abrir_imagem(self):
        imagem, _ = QFileDialog.getOpenFileName(
            self.centralwidget,
            'Abrir imagem',
            r'COLOCAR O CAMINHO PARA AS IMAGENS AQUI',
            #options=QFileDialog.DontUseNativeDialog
        )
        self.inputAbrirArquivo.setText(imagem)
        self.original_img = QPixmap(imagem)
        self.labelImg.setPixmap(self.original_img)
        self.inputLargura.setText(str(self.original_img.width()))
        self.inputAltura.setText(str(self.original_img.height()))

    def redimensionar(self):
        largura = int(self.inputLargura.text())
        self.nova_imagem = self.original_img.scaledToWidth(largura)
        self.labelImg.setPixmap(self.nova_imagem)
        self.inputLargura.setText(str(self.nova_imagem.width()))
        self.inputAltura.setText(str(self.nova_imagem.height()))

    def salvar(self):
        imagem, _ = QFileDialog.getSaveFileName(
            self.centralwidget,
            'Salvar imagem',
            r'COLOCAR O CAMINHO PARA ONDE AS IMAGENS SERÃO CRIADAS',
            #options=QFileDialog.DontUseNativeDialog
        )
        self.nova_imagem.save(imagem, 'PNG')


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    main = Main()
    main.show()
    qt.exec_()