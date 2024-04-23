import QtQuick
import QtQuick.Window
import QtQuick.Controls

Window {
    width: 640
    height: 480
    visible: true
    title: qsTr("Hello World")
    // https://www.qt.io/product/qt6/qml-book/ch19-python-build-app
    Column {
        width: parent.width // Adjust the width of the label to fit within the parent
        Button {
            text: qsTr("Give me a cryptogram!")
            onClicked: cryptogramGenerator.giveCryptogram()
        }
        Label {
            id: cryptogramLabel
            text: qsTr("...")
            wrapMode: Text.Wrap
            width: parent.width // Adjust the width of the label to fit within the parent
        }
        Button {
            text: qsTr("Show answer!")
            onClicked: cryptogramGenerator.showAnswer()
        }

        Label {
            id: plaintextLabel
            text: qsTr("WIP")
            wrapMode: Text.Wrap
            width: parent.width // Adjust the width of the label to fit within the parent
        }
    }

    Connections {
        target: cryptogramGenerator
        function onNextCryptogram(Cryptogram) {
            cryptogramLabel.text = Cryptogram
        }
    }
}
