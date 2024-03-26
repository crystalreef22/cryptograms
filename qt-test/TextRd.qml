import QtQuick


Column {/*
        width: 24; height: 32
        color: "lightsteelblue"
        border.color: "gray"

        property alias text: input.text
        property alias input: input

        TextInput {
            id: input
            anchors.fill: parent
            anchors.margins: 4
            focus: true
            font.pointSize: 20
            verticalAlignment: Text.AlignVCenter
            horizontalAlignment: Text.AlignHCenter
            validator: RegExpValidator{regExp: /^[0-9,/]+$/}
        }*/

    //TextField qt controls
    Rectangle{
        width: ti.width
        height: ti.height
        color: "lightsteelblue"
        TextInput {
            id: ti
            width:24; height:32
            font.pointSize: 20
            verticalAlignment: TextInput.AlignVCenter
            horizontalAlignment: TextInput.AlignHCenter
            padding: 0
            focus: true
            onTextChanged: {
                if (length > 1)
                    remove(0, length - 1)

                text = text.toUpperCase()

            }

        }
    }
    Rectangle{
        width: ti.width
        height: ti.height
        color: "lightsteelblue"
        Text {
            anchors.horizontalCenter: parent.horizontalCenter
            horizontalAlignment: TextInput.AlignHCenter
            text: "*"
            font.pointSize: 15
        }
    }
}
