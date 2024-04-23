# This Python file uses the following encoding: utf-8
import sys
from pathlib import Path

from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine



import random
from PySide6.QtCore import QObject, Signal, Slot


import quoteGenerator as qg
import txtEncoder as te


qg.init() #Ideally, I should make this a class

aristocrat = te.AristocratEncoder()
kg = te.keyWordGenerator("storage/commonWordList.txt")


class CryptogramGenerator(QObject):
    def __init__(self):
        QObject.__init__(self)

    nextCryptogram = Signal(str, arguments=['cryptogram'])

    @Slot()
    def giveCryptogram(self):
        q = qg.getNextQuote()
        plaintext = q['q']
        author = q['a']
        del q

        key = kg.next()
        ciphertext = aristocrat.encrypt(plaintext)
        self.nextCryptogram.emit(ciphertext)







if __name__ == "__main__":
    app = QGuiApplication(sys.argv)
    engine = QQmlApplicationEngine()
    qml_file = Path(__file__).resolve().parent / "main.qml"

    cryptogram_generator = CryptogramGenerator()
    engine.rootContext().setContextProperty("cryptogramGenerator", cryptogram_generator)

    engine.load(qml_file)
    if not engine.rootObjects():
        sys.exit(-1)
    sys.exit(app.exec())






