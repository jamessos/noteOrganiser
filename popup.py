from libaries import *
import data

class subject (QGroupBox):
    submit = Signal ()
    submitAndOpen = Signal ()
    cancel = Signal ()
    delete = Signal ()
    def __init__ (self, type):
        super().__init__ ()
        self.setStyleSheet ("QGroupBox{max-width: 800px; border-style: solid; border-width: 2px; border-color: #1c1c1c; min-width: 800px; max-height: 335px; min-height: 335px; background-color: #333333; border-radius: 20px} QPushButton {border-radius: 5px; min-height: 60px; max-height: 60px; min-width: 150px; max-width: 150px; font-size: 20px; background-color: #1c1c1c} color: #c1c1c1")
        popupLayout = QVBoxLayout ()
        popupLayout.setContentsMargins(0,25,0,25)
        
        self.titleEnter = QLineEdit ()
        self.titleEnter.setStyleSheet ("QLineEdit {padding-left: 10px;padding-right: 10px; font-size: 40px; background-color: #1c1c1c; max-height: 60px; min-height: 60px; max-width: 730px; min-width: 730px; border-radius: 5px}")
        self.titleEnter.setPlaceholderText("Name Of Course/Unit")
        popupLayout.addWidget (self.titleEnter, alignment=Qt.AlignmentFlag.AlignHCenter)

        self.flavourEnter = QLineEdit ()
        self.flavourEnter.setStyleSheet ("QLineEdit {padding-left: 5px;padding-right: 5px; font-size: 17px; background-color: #1c1c1c; max-height: 30px; min-height: 30px; max-width: 740px; min-width: 740px; border-radius: 5px}")
        self.flavourEnter.setPlaceholderText("Short Description")
        popupLayout.addWidget (self.flavourEnter, alignment=Qt.AlignmentFlag.AlignHCenter)

        self.overviewEnter = QPlainTextEdit ()
        self.overviewEnter.setStyleSheet ("QPlainTextEdit {padding-left: 5px;padding-right: 5px; font-size: 15px; background-color: #1c1c1c; max-height: 100px; min-height: 100px; max-width: 740px; min-width: 740px; border-radius: 5px}")
        self.overviewEnter.setPlaceholderText("Overview")
        popupLayout.addWidget (self.overviewEnter, alignment=Qt.AlignmentFlag.AlignHCenter)

        buttonGroup = popupButtonGroup (type)
        buttonGroup.cancel.connect (self.cancel.emit)
        buttonGroup.delete.connect (self.delete.emit)
        buttonGroup.submit.connect (self.submit.emit)
        buttonGroup.submitAndOpen.connect (self.submitAndOpen.emit)

        popupLayout.addWidget (buttonGroup, alignment=Qt.AlignmentFlag.AlignRight)


        self.setLayout (popupLayout)
        
    def getInfo (self):
        info = {}
        info["name"] = self.titleEnter.text()
        info["type"] = "subject"
        info["flavour"] = self.flavourEnter.text ()
        info["desc"] = self.overviewEnter.toPlainText ()
        return (info)
    def setText (self, subject):
        self.titleEnter.setText (subject.name)
        self.flavourEnter.setText (subject.flavour)
        self.overviewEnter.setPlainText (subject.desc)
    def focus (self):
        self.titleEnter.setFocus ()


class unit (QGroupBox):
    submit = Signal ()
    submitAndOpen = Signal ()
    cancel = Signal ()
    delete = Signal ()
    def __init__ (self, type):
        super().__init__ ()
        self.setStyleSheet ("QGroupBox{max-width: 800px; border-style: solid; border-width: 2px; border-color: #1c1c1c; min-width: 800px; max-height: 335px; min-height: 335px; background-color: #333333; border-radius: 20px} QPushButton {border-radius: 5px; min-height: 60px; max-height: 60px; min-width: 150px; max-width: 150px; font-size: 20px; background-color: #1c1c1c} color: #c1c1c1")
        popupLayout = QVBoxLayout ()
        popupLayout.setContentsMargins(0,25,0,25)
        
        self.titleEnter = QLineEdit ()
        self.titleEnter.setStyleSheet ("QLineEdit {padding-left: 10px;padding-right: 10px; font-size: 40px; background-color: #1c1c1c; max-height: 60px; min-height: 60px; max-width: 730px; min-width: 730px; border-radius: 5px}")
        self.titleEnter.setPlaceholderText("Name Of Unit/Category")
        popupLayout.addWidget (self.titleEnter, alignment=Qt.AlignmentFlag.AlignHCenter)

        self.flavourEnter = QLineEdit ()
        self.flavourEnter.setStyleSheet ("QLineEdit {padding-left: 5px;padding-right: 5px; font-size: 17px; background-color: #1c1c1c; max-height: 30px; min-height: 30px; max-width: 740px; min-width: 740px; border-radius: 5px}")
        self.flavourEnter.setPlaceholderText("Short Description")
        popupLayout.addWidget (self.flavourEnter, alignment=Qt.AlignmentFlag.AlignHCenter)

        self.overviewEnter = QPlainTextEdit ()
        self.overviewEnter.setStyleSheet ("QPlainTextEdit {padding-left: 5px;padding-right: 5px; font-size: 15px; background-color: #1c1c1c; max-height: 100px; min-height: 100px; max-width: 740px; min-width: 740px; border-radius: 5px}")
        self.overviewEnter.setPlaceholderText("Terms To Define")
        popupLayout.addWidget (self.overviewEnter, alignment=Qt.AlignmentFlag.AlignHCenter)

        buttonGroup = popupButtonGroup (type)
        buttonGroup.cancel.connect (self.cancel.emit)
        buttonGroup.delete.connect (self.delete.emit)
        buttonGroup.submit.connect (self.submit.emit)
        buttonGroup.submitAndOpen.connect (self.submitAndOpen.emit)

        popupLayout.addWidget (buttonGroup, alignment=Qt.AlignmentFlag.AlignRight)


        self.setLayout (popupLayout)
        
    def getInfo (self):
        info = {}
        info["name"] = self.titleEnter.text()
        info["type"] = "unit"
        info["flavour"] = self.flavourEnter.text ()
        info["desc"] = self.overviewEnter.toPlainText ()
        return (info)
    def setText (self, subject):
        self.titleEnter.setText (subject.name)
        self.flavourEnter.setText (subject.flavour)
        self.overviewEnter.setPlainText (subject.desc)
    def focus (self):
        self.titleEnter.setFocus ()


class element (QGroupBox):
    submit = Signal ()
    submitAndOpen = Signal ()
    cancel = Signal ()
    delete = Signal ()
    def __init__ (self, type):
        super().__init__ ()
        self.setStyleSheet ("QGroupBox{max-width: 800px; border-style: solid; border-width: 2px; border-color: #1c1c1c; min-width: 800px; max-height: 325px; min-height: 325px; background-color: #333333; border-radius: 20px} QPushButton {border-radius: 5px; min-height: 60px; max-height: 60px; min-width: 150px; max-width: 150px; font-size: 20px; background-color: #1c1c1c} color: #c1c1c1")
        popupLayout = QVBoxLayout ()
        popupLayout.setContentsMargins(0,25,0,25)
        
        rowOne = QGroupBox ()
        rowOneLayout = QHBoxLayout ()
        rowOne.setStyleSheet ("QGroupBox{background-color: #333333; max-height: 60px; min-height: 60px; max-width: 750px; min-width: 750px; border: 0; }")
        rowOneLayout.setContentsMargins(0,0,0,0)
        rowOneLayout.setSpacing (25)
        

        
        sizeBox = QGroupBox ()
        sizeBox.setStyleSheet ("QGroupBox{background-color: #1c1c1c; border: 0; max-height: 60px; min-height: 60px; min-width: 245px; max-width: 245px; border: 0;border-radius: 5px} font-size: 30px")
        sizeBoxLayout = QHBoxLayout ()
        sizeBox.setLayout (sizeBoxLayout)
        sizeBoxLayout.setContentsMargins(25,0,0,0)
        sizeBoxLayout.setSpacing (5)

        sizeText = QLabel ("Element Size: ")
        sizeText.setStyleSheet ("color: #c1c1c1; font-size: 25px; background-color: #1c1c1c; min-width: 0px; max-width: 200px; min-height: 60px; max-height: 60px;")

        self.sizeSelect = QComboBox ()
        self.sizeSelect.setStyleSheet ("QComboBox{padding-top: 0px; color: #c1c1c1 ;font-size: 25px; border: 0; background-color: rgba(0,0,0,0); min-width: 40px; max-width: 40px; max-height: 55px; min-height: 55px} QAbstractItemView{min-width: 100px} ")
        self.sizeSelect.addItem ("S")
        self.sizeSelect.addItem ("M")
        self.sizeSelect.addItem ("L")
        self.sizeSelect.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        sizeBoxLayout.addWidget (sizeText, alignment=Qt.AlignmentFlag.AlignVCenter)
        sizeBoxLayout.addWidget (self.sizeSelect, alignment=Qt.AlignmentFlag.AlignVCenter)
        sizeBoxLayout.addStretch ()




        self.titleEnter = QLineEdit ()
        self.titleEnter.setStyleSheet ("QLineEdit {padding-left: 10px;padding-right: 10px; font-size: 40px; background-color: #1c1c1c; max-height: 60px; min-height: 60px; max-width: 470px; min-width: 470px; border-radius: 5px}")
        self.titleEnter.setPlaceholderText("Title")

        rowOneLayout.addWidget (self.titleEnter)
        rowOneLayout.addWidget (sizeBox)

        rowOne.setLayout (rowOneLayout)

        popupLayout.addWidget (rowOne, alignment=Qt.AlignmentFlag.AlignHCenter)

        self.overviewEnter = QPlainTextEdit ()
        self.overviewEnter.setStyleSheet ("QPlainTextEdit {padding-left: 5px;padding-right: 5px; font-size: 15px; background-color: #1c1c1c; max-height: 100px; min-height: 100px; max-width: 740px; min-width: 740px; border-radius: 5px}")
        self.overviewEnter.setPlaceholderText("Description or definition")
        popupLayout.addWidget (self.overviewEnter, alignment=Qt.AlignmentFlag.AlignHCenter)

        buttonGroup = popupButtonGroup (type)
        buttonGroup.cancel.connect (self.cancel.emit)
        buttonGroup.delete.connect (self.delete.emit)
        buttonGroup.submit.connect (self.submit.emit)
        buttonGroup.submitAndOpen.connect (self.submitAndOpen.emit)


        popupLayout.addWidget (buttonGroup, alignment=Qt.AlignmentFlag.AlignRight)


        self.setLayout (popupLayout)
    def getInfo (self):
        info = {}
        info["name"] = self.titleEnter.text()
        info["type"] = "element"
        info["desc"] = self.overviewEnter.toPlainText ()
        info["size"] = self.sizeSelect.currentIndex() + 1
        return (info)
    def setText (self, element):
        self.titleEnter.setText (element.name)
        self.overviewEnter.setPlainText (element.desc)
        self.sizeSelect.setCurrentIndex(element.size - 1)
    def focus (self):
        self.titleEnter.setFocus ()

class group (QGroupBox):
    submit = Signal ()
    submitAndOpen = Signal ()
    cancel = Signal ()
    delete = Signal ()
    def __init__ (self, type):
        super().__init__ ()
        self.setStyleSheet ("QGroupBox{max-width: 800px; border-style: solid; border-width: 2px; border-color: #1c1c1c; min-width: 800px; max-height: 185px; min-height: 185px; background-color: #333333; border-radius: 20px} QPushButton {border-radius: 5px; min-height: 60px; max-height: 60px; min-width: 150px; max-width: 150px; font-size: 20px; background-color: #1c1c1c} color: #c1c1c1")
        popupLayout = QVBoxLayout ()
        popupLayout.setContentsMargins(0,25,0,25)
        
        self.titleEnter = QLineEdit ()
        self.titleEnter.setStyleSheet ("QLineEdit {padding-left: 10px;padding-right: 10px; font-size: 40px; background-color: #1c1c1c; max-height: 60px; min-height: 60px; max-width: 730px; min-width: 730px; border-radius: 5px}")
        self.titleEnter.setPlaceholderText("Title For Element Group")
        popupLayout.addWidget (self.titleEnter, alignment=Qt.AlignmentFlag.AlignHCenter)
        
        buttonGroup = groupButtonGroup (type)
        buttonGroup.cancel.connect (self.cancel.emit)
        buttonGroup.delete.connect (self.delete.emit)
        buttonGroup.submit.connect (self.submit.emit)
        buttonGroup.submitAndOpen.connect (self.submitAndOpen.emit)


        popupLayout.addWidget (buttonGroup, alignment=Qt.AlignmentFlag.AlignRight)

        self.setLayout (popupLayout)
    def getInfo (self):
        info = {}
        info["name"] = self.titleEnter.text()
        info["type"] = "group"
        info["size"] = 3
        return (info)
    def setText (self, element):
        self.titleEnter.setText (element.name)
    def focus (self):
        self.titleEnter.setFocus ()

class image (QGroupBox):
    submit = Signal ()
    submitAndOpen = Signal ()
    cancel = Signal ()
    delete = Signal ()

    image = "none"
    layoutType = "V"
    fitType = "HFit"
    imgPath = ""
    #either HFit, HFit, Scale or Original

    def __init__ (self, type):
        super().__init__ ()
        self.setStyleSheet ("QGroupBox{max-width: 1000px; border-style: solid; border-width: 2px; border-color: #1c1c1c; min-width: 1000px; max-height: 625px; min-height: 625px; background-color: #333333; border-radius: 20px} QPushButton {border-radius: 5px; min-height: 60px; max-height: 60px; min-width: 150px; max-width: 150px; font-size: 20px; background-color: #1c1c1c} color: #c1c1c1")
        popupLayout = QVBoxLayout ()
        popupLayout.setContentsMargins(0,25,0,25)
        
        rowOne = QGroupBox ()
        rowOneLayout = QHBoxLayout ()
        rowOne.setStyleSheet ("QGroupBox{background-color: #333333; max-height: 60px; min-height: 60px; max-width: 950px; min-width: 950px; border: 0; }")
        rowOneLayout.setContentsMargins(0,0,0,0)
        rowOneLayout.setSpacing (25)
        
        sizeBox = QGroupBox ()
        sizeBox.setStyleSheet ("QGroupBox{background-color: #1c1c1c; border: 0; max-height: 60px; min-height: 60px; min-width: 245px; max-width: 245px; border: 0;border-radius: 5px} font-size: 30px")
        sizeBoxLayout = QHBoxLayout ()
        sizeBox.setLayout (sizeBoxLayout)
        sizeBoxLayout.setContentsMargins(25,0,0,0)
        sizeBoxLayout.setSpacing (5)

        sizeText = QLabel ("Element Size: ")
        sizeText.setStyleSheet ("color: #c1c1c1; font-size: 25px; background-color: #1c1c1c; min-width: 0px; max-width: 200px; min-height: 60px; max-height: 60px;")

        self.sizeSelect = QComboBox ()
        self.sizeSelect.setStyleSheet ("QComboBox{padding-top: 0px; color: #c1c1c1 ;font-size: 25px; border: 0; background-color: rgba(0,0,0,0); min-width: 40px; max-width: 40px; max-height: 55px; min-height: 55px} QAbstractItemView{min-width: 100px} ")
        self.sizeSelect.addItem ("S")
        self.sizeSelect.addItem ("M")
        self.sizeSelect.addItem ("L")
        self.sizeSelect.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.sizeSelect.currentIndexChanged.connect (self.changeSize)

        sizeBoxLayout.addWidget (sizeText, alignment=Qt.AlignmentFlag.AlignVCenter)
        sizeBoxLayout.addWidget (self.sizeSelect, alignment=Qt.AlignmentFlag.AlignVCenter)
        sizeBoxLayout.addStretch ()

        self.titleEnter = QLineEdit ()
        self.titleEnter.setStyleSheet ("QLineEdit {padding-left: 10px;padding-right: 10px; font-size: 40px; background-color: #1c1c1c; max-height: 60px; min-height: 60px; max-width: 670px; min-width: 670px; border-radius: 5px}")
        self.titleEnter.setPlaceholderText("Title")
        self.titleEnter.textChanged.connect (self.reload)

        rowOneLayout.addWidget (self.titleEnter)
        rowOneLayout.addWidget (sizeBox)

        rowOne.setLayout (rowOneLayout)

        popupLayout.addWidget (rowOne, alignment=Qt.AlignmentFlag.AlignHCenter)

        self.overviewEnter = QPlainTextEdit ()
        self.overviewEnter.setStyleSheet ("QPlainTextEdit {padding-left: 5px;padding-right: 5px; font-size: 15px; background-color: #1c1c1c; max-height: 50px; min-height: 50px; max-width: 940px; min-width: 940px; border-radius: 5px}")
        self.overviewEnter.setPlaceholderText("Image Description")
        self.overviewEnter.textChanged.connect (self.reload)
        popupLayout.addWidget (self.overviewEnter, alignment=Qt.AlignmentFlag.AlignHCenter)

        self.upload = photoDropbox ()
        self.upload.photoUploaded.connect (self.uploadPhoto)
        popupLayout.addWidget (self.upload, alignment=Qt.AlignmentFlag.AlignHCenter)

        self.preview = photoPreview (**self.getInfo())
        popupLayout.addWidget (self.preview, alignment=Qt.AlignmentFlag.AlignHCenter)
        self.preview.deleteImage.connect(self.deletePhoto)
        self.preview.layoutChange.connect (self.changeLayout)
        self.preview.fitChange.connect (self.changeFit)

        self.buttonGroup = popupButtonGroup (type)
        self.buttonGroup.cancel.connect (self.cancel.emit)
        self.buttonGroup.delete.connect (self.delete.emit)
        self.buttonGroup.submit.connect (self.submit.emit)
        self.buttonGroup.submitAndOpen.connect (self.submitAndOpen.emit)
        
        popupLayout.addWidget (self.buttonGroup, alignment=Qt.AlignmentFlag.AlignRight)

        self.setLayout (popupLayout)
        self.reload()
        self.preview.changeLayout.setEnabled (False)

    def changeSize (self):
        if self.sizeSelect.currentIndex() + 1 == 1:
            self.layoutType = "V"
            self.preview.changeLayout.setEnabled (False)
        else:
            self.preview.changeLayout.setEnabled (True)
        self.reload()
    def changeLayout (self):
        match self.layoutType:
            case "V":
                self.layoutType = "H"
            case "H":
                self.layoutType = "V"
            
        self.reload ()
    def changeFit (self):
        match self.fitType:
            case "HFit":
                self.fitType = "VFit"
            case "VFit":
                self.fitType = "Scale"
            case "Scale":
                self.fitType = "Original"
            case "Original":
                self.fitType = "HFit"
        self.reload ()
    def focus (self):
        self.titleEnter.setFocus ()
    def reload (self):
        if self.image == "none":
            self.buttonGroup.submitButton.setEnabled (False)
            self.buttonGroup.submitOpenButton.setEnabled (False)
            self.buttonGroup.submitButton.setCursor(QCursor(Qt.CursorShape.ForbiddenCursor))
            self.buttonGroup.submitOpenButton.setCursor(QCursor(Qt.CursorShape.ForbiddenCursor))

            self.preview.hide()
            
            self.upload.show ()
        else:
            self.buttonGroup.submitButton.setEnabled (True)
            self.buttonGroup.submitOpenButton.setEnabled (True)
            self.buttonGroup.submitButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
            self.buttonGroup.submitOpenButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

            
            self.preview.show()
            self.preview.reload (**self.getInfo())
        
                

            self.upload.hide ()
    def setText (self, element):
        self.titleEnter.setText (element.name)
        self.overviewEnter.setPlainText (element.desc)
        self.sizeSelect.setCurrentIndex(element.size - 1)
        if element.type == "imageV":
            self.layoutType = "V"
        elif element.type == "imageH":
            self.layoutType = "H"
        self.fitType = element.fit
        self.image = QPixmap (data.filepath(element.img))
        self.imgPath = element.img
        self.reload()
        
    def uploadPhoto (self):
        self.image = self.upload.data
        self.reload()
    def deletePhoto (self):
        self.image = "none"
        self.reload()
    def getInfo (self):
        info = {}
        info["name"] = self.titleEnter.text()
        if self.layoutType == "V":
            info["type"] = "imageV"
        elif self.layoutType == "H":
            info["type"] = "imageH"
        info["desc"] = self.overviewEnter.toPlainText ()
        info["size"] = self.sizeSelect.currentIndex() + 1

        #image is the actual QPixmap variable containing the uploaded image, used for the preview, but not saved
        info["image"] = self.image

        #img is the filepath to the saved image used when the popup is submited, this value is saved in the notes object
        info["img"] = self.imgPath
        info["layout"] = self.layoutType
        info["fit"] = self.fitType
        return (info)
    def confirm (self):
        saveFound = False

        if self.titleEnter.text() != "":
            fileName = self.titleEnter.text()
        else:
            fileName = "untitled"

        saveLocation = "uploads/"+fileName+".png"
        
        suffix = 0

        if not os.path.exists (data.filepath (saveLocation)):
            saveFound = True
        while saveFound == False:
            suffix += 1
            saveLocation = "uploads/"+fileName + str(suffix) +".png"
            if not os.path.exists (data.filepath (saveLocation)):
                saveFound = True

        self.image.save (data.filepath(saveLocation))
        self.imgPath = saveLocation

class photoPreview (QGroupBox):
    deleteImage = Signal ()
    layoutChange = Signal ()
    fitChange = Signal ()
    def __init__(self, **kwargs):
        super().__init__()
        self.setStyleSheet('''
        QGroupBox {
            background-color: #1c1c1c;
            border: 0;
            border-radius: 5px;
            min-width: 950px;
            max-width: 950px;
            min-height: 325px;
            max-height: 325px
        }''')
        previewLayout = QVBoxLayout ()
        previewLayout.setContentsMargins(0,15,0,25)

        self.scrollV = QScrollArea ()
        self.scrollV.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollV.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollV.setWidgetResizable(True)
        self.scrollV.setBaseSize(QSize(950, 200))
        self.scrollV.setStyleSheet ("background-color: rgba(0,0,0,0)")
        self.scrollV.setAlignment (Qt.AlignmentFlag.AlignHCenter)

        self.previewV = photoMiniElementV (**kwargs)
        self.scrollV.setWidget (self.previewV)

        self.scrollH = QScrollArea ()
        self.scrollH.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollH.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollH.setWidgetResizable(True)
        self.scrollH.setBaseSize(QSize(950, 200))
        self.scrollH.setStyleSheet ("background-color: rgba(0,0,0,0)")
        self.scrollH.setAlignment (Qt.AlignmentFlag.AlignHCenter)

        self.previewH = photoMiniElementH (**kwargs)
        self.scrollH.setWidget (self.previewH)

        

        self.rowOne = QGroupBox()
        rowOneLayout = QHBoxLayout ()
        rowOneLayout.setContentsMargins(0,0,25,0)
        self.rowOne.setStyleSheet ("QGroupBox{min-width: 950px; max-width: 900px; min-height: 50px; max-height: 50px; background-color: #1c1c1c} QPushButton {min-height: 40px; max-height: 40px; min-width: 150px; max-width: 150px; background-color: #333333; font-size: 15px}")
        
        
        self.titlee = QLabel ("Preview: ")
        self.titlee.setStyleSheet ("padding-left: 15px; font-size: 35px; color: #c1c1c1; background-color: rgba(0,0,0,0)")
        rowOneLayout.addWidget (self.titlee, alignment=Qt.AlignmentFlag.AlignTop)
        rowOneLayout.addStretch ()

        self.changeFit = QPushButton ("Fit To Horizontal")
        self.changeFit.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        rowOneLayout.addWidget (self.changeFit, alignment=Qt.AlignmentFlag.AlignRight)
        self.changeFit.clicked.connect (self.fitChange.emit)

        self.changeLayout = QPushButton ("Layout: Vertical")
        self.changeLayout.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.changeLayout.clicked.connect(self.layoutChange.emit)
        rowOneLayout.addWidget (self.changeLayout, alignment=Qt.AlignmentFlag.AlignRight)
        

        self.changeImage = QPushButton ("Change Image")
        self.changeImage.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        rowOneLayout.addWidget (self.changeImage, alignment=Qt.AlignmentFlag.AlignRight)
        self.changeImage.clicked.connect (self.deleteImage.emit)




        self.rowOne.setLayout (rowOneLayout)
        
        previewLayout.addWidget (self.rowOne, alignment=Qt.AlignmentFlag.AlignLeft)

        previewLayout.addWidget (self.scrollV)
        previewLayout.addWidget (self.scrollH)
        self.setLayout (previewLayout) 
    def reload (self, **kwargs):
        match kwargs["layout"]:
            case "V":
                self.scrollV.show()
                self.scrollH.hide()
                self.previewV.setup (**kwargs)
                self.changeLayout.setText ("Layout: Vertical")
            case "H":
                self.scrollH.show()
                self.scrollV.hide()
                self.previewH.setup (**kwargs)
                self.changeLayout.setText ("Layout: Horizontal")

        match kwargs["fit"]:
            case "HFit":
                self.changeFit.setText ("Fit To Horizontal")
            case "VFit":
                self.changeFit.setText ("Fit To Vertical")
            case "Scale":
                self.changeFit.setText ("Scale To Fit")
            case "Original":
                self.changeFit.setText ("Original Size")
    

#these are ones with the description text
class photoMiniElementH (QGroupBox):
    def __init__(self,**kwargs):
        super().__init__()
        self.elementLayout = QHBoxLayout ()
        self.elementLayout.setContentsMargins(25,25,25,25)

        self.titlee = QLabel (kwargs["name"])
        self.titlee.setAlignment (Qt.AlignmentFlag.AlignTop)
        self.titlee.setWordWrap (True)
        self.titlee.setStyleSheet ("QLabel {background-color: #333333; max-width: 185px; min-width: 185px; min-height: 100px; max-height: 100px; font-size: 30px;}")

        self.desc = QLabel (kwargs["desc"])
        self.desc.setWordWrap (True)
        self.desc.setAlignment (Qt.AlignmentFlag.AlignTop)
        self.desc.setStyleSheet ("QLabel {background-color: #333333; max-width: 135px; min-width: 135px; min-height: 150px; max-height: 150px; font-size: 20px;}")

        self.imageScroll = QScrollArea ()
        self.imageScroll.setBaseSize (QSize(200, 150))
        self.image = QLabel ()
        self.imageScroll.setAlignment (Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignHCenter)
        self.image.setAlignment (Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignHCenter)
        self.imageScroll.setWidget (self.image)

        self.elementLayout.addWidget(self.titlee, alignment=Qt.AlignmentFlag.AlignTop)
        self.elementLayout.addWidget (self.desc, alignment=Qt.AlignmentFlag.AlignTop)
        self.elementLayout.addWidget (self.imageScroll)

        
        self.setup (**kwargs)
        self.setLayout(self.elementLayout)

    def setup (self, **kwargs):
        match kwargs["size"]:
            case 1:
                pass
            case 2:
                self.setStyleSheet ("QGroupBox {background-color: #333333; max-width: 590px; min-width: 590px; max-height: 200px; min-height: 200px; border-radius: 25px}")
            case 3:
                self.setStyleSheet ("QGroupBox {background-color: #333333; max-width: 900px; min-width: 900px; max-height: 350px; min-height: 350px; border-radius: 25px}")
        
        if kwargs["name"] == "":
            self.titlee.setText ("untitled")
        else:
            self.titlee.setText (kwargs["name"])
        if kwargs["desc"] == "":
            self.desc.setText ("no description was entered")
        else:
            self.desc.setText (kwargs["desc"])
        
        try:
            match kwargs["size"]:
                case 2:
                    self.titlee.setStyleSheet ("QLabel {background-color: #333333; max-width: 185px; min-width: 185px; min-height: 100px; max-height: 100px; font-size: 30px;}")
                    self.desc.setStyleSheet ("QLabel {background-color: #333333; max-width: 135px; min-width: 135px; min-height: 150px; max-height: 150px; font-size: 13px;}")
                    match kwargs["fit"]:
                        case "HFit":
                            scaledImage = kwargs["image"].scaledToWidth(200)
                        case "VFit":
                            scaledImage = kwargs["image"].scaledToHeight(150)
                        case "Scale":
                            scaledImage = kwargs["image"].scaled (QSize (200, 150))
                        case "Original":
                            scaledImage = kwargs["image"]
                case 3:
                    self.titlee.setStyleSheet ("QLabel {background-color: #333333; max-width: 185px; min-width: 185px; min-height: 250px; max-height: 250px; font-size: 30px;}")
                    self.desc.setStyleSheet ("QLabel {background-color: #333333; max-width: 135px; min-width: 135px; min-height: 300px; max-height: 300px; font-size: 13px;}")
                    match kwargs["fit"]:
                        case "HFit":
                            scaledImage = kwargs["image"].scaledToWidth(510)
                        case "VFit":
                            scaledImage = kwargs["image"].scaledToHeight(300)
                        case "Scale":
                            scaledImage = kwargs["image"].scaled (QSize (510, 300))
                        case "Original":
                            scaledImage = kwargs["image"]
                
            self.image.setPixmap (scaledImage)
            self.image.setFixedSize (scaledImage.size())
        except:
            pass

#no text
class photoMiniElementV (QGroupBox):
    def __init__(self, **kwargs):
        super().__init__()
        self.elementLayout = QVBoxLayout ()
        self.elementLayout.setContentsMargins(40,10,40,10)
        self.titlee = QLabel (kwargs["name"])
        #self.title.setStyleSheet ("max-height: 100px; min-height: 50px; min-width: 280px; max-width: 280px; background-color: #333333; color: #c1c1c1; font-size: 30px")
        self.imageScroll = QScrollArea ()
        self.image = QLabel ()
        self.image.setAlignment (Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignHCenter)
        self.imageScroll.setAlignment (Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignHCenter)
        try:
            scaledImage = kwargs["image"].scaledToWidth(200)
            self.image.setPixmap (scaledImage)
            self.image.setFixedSize (scaledImage.size())
        except:
            pass
        self.imageScroll.setWidget (self.image)
        self.imageScroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.imageScroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        
        self.elementLayout.addWidget (self.titlee)
        self.elementLayout.addWidget (self.imageScroll)
        
        self.setup(**kwargs)
        
        self.setLayout (self.elementLayout)
    def setup (self, **kwargs):
        match kwargs["size"]:
            case 1:
                self.setStyleSheet ("QGroupBox {background-color: #333333; max-width: 280px; min-width: 280px; max-height: 200px; min-height: 200px; border-radius: 25px}")
                self.imageScroll.setStyleSheet ("max-width: 200px; min-width: 200px; min-height: 150px; max-height: 150px")
                self.image.setStyleSheet ("QLabel {max-width: 20000px; min-width: 200px; min-height: 0px; max-height: 15000px}")
                self.titlee.setStyleSheet ("max-height: 20px; min-height: 20px; min-width: 200px; max-width: 200px; background-color: #333333; color: #c1c1c1; font-size: 20px")
            case 2:
                self.setStyleSheet ("QGroupBox {background-color: #333333; max-width: 590px; min-width: 590px; max-height: 200px; min-height: 200px; border-radius: 25px}")
                self.imageScroll.setStyleSheet ("max-width: 510px; min-width: 510px; min-height: 150px; max-height: 150px")
                self.image.setStyleSheet ("QLabel {max-width: 20000px; min-width: 510px; min-height: 0px; max-height: 15000px}")
                self.titlee.setStyleSheet ("max-height: 20px; min-height: 20px; min-width: 510px; max-width: 510px; background-color: #333333; color: #c1c1c1; font-size: 20px")
            case 3:
                self.setStyleSheet ("QGroupBox {background-color: #333333; max-width: 900px; min-width: 900px; max-height: 350px; min-height: 50px; border-radius: 25px}")
                self.imageScroll.setStyleSheet ("max-width: 820px; min-width: 820px; min-height: 150px; max-height: 300px")
                self.image.setStyleSheet ("QLabel {max-width: 20000px; min-width: 820px; min-height: 0px; max-height: 15000px}")
                self.titlee.setStyleSheet ("max-height: 20px; min-height: 20px; min-width: 820px; max-width: 820px; background-color: #333333; color: #c1c1c1; font-size: 20px")
        
        try:
            match kwargs["size"]:
                case 1:
                    match kwargs["fit"]:
                        case "HFit":
                            scaledImage = kwargs["image"].scaledToWidth(200)
                        case "VFit":
                            scaledImage = kwargs["image"].scaledToHeight(150)
                        case "Scale":
                            scaledImage = kwargs["image"].scaled (QSize (200, 150))
                        case "Original":
                            scaledImage = kwargs["image"]
                case 2:
                    match kwargs["fit"]:
                        case "HFit":
                            scaledImage = kwargs["image"].scaledToWidth(510)
                        case "VFit":
                            scaledImage = kwargs["image"].scaledToHeight(150)
                        case "Scale":
                            scaledImage = kwargs["image"].scaled (QSize (510, 150))
                        case "Original":
                            scaledImage = kwargs["image"]
                case 3:
                    match kwargs["fit"]:
                        case "HFit":
                            scaledImage = kwargs["image"].scaledToWidth(820)
                        case "VFit":
                            scaledImage = kwargs["image"].scaledToHeight(300)
                        case "Scale":
                            scaledImage = kwargs["image"].scaled (QSize (820, 300))
                        case "Original":
                            scaledImage = kwargs["image"]
            self.image.setPixmap (scaledImage)
            self.image.setFixedSize (scaledImage.size())
        except:
            pass
        if kwargs["name"] == "":
            self.titlee.setText ("untitled")
        else:
            self.titlee.setText (kwargs["name"])
        

class photoDropbox(QPushButton):
    photoUploaded = Signal ()
    data = "none"
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #self.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setText('\n\n Drop Image Here Or Click To Upload \n\n')
        self.setStyleSheet('''
        QPushButton {
            border: 5px dashed #aaa;
            min-width: 940px;
            max-width: 940px;
            min-height: 315px;
            max-height: 315px
        }''')

        self.clicked.connect(self.open_image)
        self.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        grid = QGridLayout(self)
        self.setAcceptDrops(True)

    

    def dragEnterEvent(self, event):
        if event.mimeData().hasImage:
            event.accept()
        else:
            event.ignore()

    def dragMoveEvent(self, event):
        if event.mimeData().hasImage:
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        if event.mimeData().hasImage:
            event.setDropAction(Qt.CopyAction)
            filename = event.mimeData().urls()[0].toLocalFile()
            event.accept()
            self.open_image(filename)
        else:
            event.ignore()

    def open_image(self, filename=None):
        if not filename:
            filename, _ = QFileDialog.getOpenFileName(self, 'Select Photo', 'Images (*.png *.jpg *.heic)')
            if not filename:
                return
        self.data = QPixmap(filename)
        self.photoUploaded.emit ()
        #QPixmap(filename).save (data.filepath("uploads/img.png"))

class photoDisplay (QGroupBox):
    back = Signal ()
    def __init__(self, image):
        super().__init__()
        if image.width()/image.height() > 2:
            scaledImage = image.scaledToWidth(1300)
        else:
            scaledImage = image.scaledToHeight(650)
        width = scaledImage.width()
        height = scaledImage.height()

        self.setStyleSheet ("QGroupBox{max-width: " + str(width+100) + "px; border-style: solid; border-width: 2px; border-color: #1c1c1c; min-width: " + str(width+100) + "px; max-height: " + str(height+100) + "px; min-height: " + str(height+100) + "px; background-color: #333333; border-radius: 20px} QPushButton {border-radius: 5px; min-height: 40px; max-height: 40px; min-width: 120px; max-width: 120px; font-size: 15px; background-color: #1c1c1c} color: #c1c1c1")
        self.image = QLabel ()
        self.image.setFixedSize (scaledImage.size())
        self.image.setPixmap (scaledImage)
        layout = QVBoxLayout ()
        layout.addWidget (self.image)
        
        self.cancelButton = QPushButton ("Return")
        self.cancelButton.setShortcut ("Esc")
        self.cancelButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.cancelButton.clicked.connect (self.back.emit)
        layout.addWidget (self.cancelButton, alignment=Qt.AlignmentFlag.AlignRight)

        layout.setContentsMargins (50, 20, 50, 20)
        self.setLayout (layout)
            

        

#for buttons group WITHOUT the "edit and open" option
class groupButtonGroup (QGroupBox):
    submit = Signal ()
    submitAndOpen = Signal ()
    cancel = Signal ()
    delete = Signal ()

    def __init__ (self, type):
        super().__init__ ()
        buttonLayout = QHBoxLayout ()
        buttonLayout.setContentsMargins(0,0,25,0)
        self.setStyleSheet ("QGroupBox {min-height: 60px; border: 0; max-height: 60px; min-width: 525px; max-width: 525px; font-size: 20px; background-color: #333333; border-radius: 0px} QPushButton {border-radius: 5px; min-height: 60px; max-height: 60px; min-width: 150px; max-width: 150px; font-size: 20px; background-color: #1c1c1c}")
        #buttonLayout.addStretch ()
        if type == "edit":
            submitButton = QPushButton ("Edit")
        else :
            submitButton = QPushButton ("Add")
        submitButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        submitButton.clicked.connect (self.submit.emit)
        submitButton.setShortcut ("Ctrl+Return")

        cancelButton = QPushButton ("Cancel")
        cancelButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        cancelButton.clicked.connect (self.cancel.emit)
        cancelButton.setShortcut ("Esc")
        if (type == "edit"):
            deleteButton = QPushButton ("Delete")
            deleteButton.setStyleSheet ("color: #ff0000")
            deleteButton.clicked.connect (self.delete.emit)
            deleteButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
            buttonLayout.addWidget (deleteButton, alignment=Qt.AlignmentFlag.AlignRight)
        else:
            self.setStyleSheet ("QGroupBox {min-height: 60px; border: 0; max-height: 60px; min-width: 375px; max-width: 375px; font-size: 20px; background-color: #333333; border-radius: 0px}")


        buttonLayout.addWidget (cancelButton, alignment=Qt.AlignmentFlag.AlignRight)
        buttonLayout.addWidget (submitButton, alignment=Qt.AlignmentFlag.AlignRight)

        self.setLayout (buttonLayout)
    

#for button group WITH the "edit and open" option
class popupButtonGroup (QGroupBox):
    submit = Signal ()
    submitAndOpen = Signal ()
    cancel = Signal ()
    delete = Signal ()

    def __init__ (self, type):
        super().__init__ ()
        buttonLayout = QHBoxLayout ()
        buttonLayout.setContentsMargins(0,0,25,0)
        self.setStyleSheet ("QGroupBox {min-height: 60px; border: 0; max-height: 60px; min-width: 720px; max-width: 720px; font-size: 20px; background-color: #333333; border-radius: 0px}")
        #buttonLayout.addStretch ()
        if type == "edit":
            self.submitButton = QPushButton ("Edit")
        else :
            self.submitButton = QPushButton ("Add")
        self.submitButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.submitButton.setShortcut ("Ctrl+Return")

        self.submitButton.clicked.connect (self.submit.emit)

        if type == "edit":
            self.submitOpenButton = QPushButton ("Edit && Open")
        else:
            self.submitOpenButton = QPushButton ("Add && Open")
            
        self.submitOpenButton.clicked.connect (self.submitAndOpen.emit)
        self.submitOpenButton.setShortcut ("Ctrl+Shift+Return")
        self.submitOpenButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))


        self.cancelButton = QPushButton ("Cancel")
        self.cancelButton.setShortcut ("Esc")
        self.cancelButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.cancelButton.clicked.connect (self.cancel.emit)

        if (type == "edit"):
            self.deleteButton = QPushButton ("Delete")
            self.deleteButton.setStyleSheet ("color: #ff0000")
            self.deleteButton.clicked.connect (self.delete.emit)
            self.deleteButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
            buttonLayout.addWidget (self.deleteButton, alignment=Qt.AlignmentFlag.AlignRight)
        else:
            self.setStyleSheet ("QGroupBox {min-height: 60px; border: 0; max-height: 60px; min-width: 550px; max-width: 550px; font-size: 20px; background-color: #333333; border-radius: 0px}")


        buttonLayout.addWidget (self.cancelButton, alignment=Qt.AlignmentFlag.AlignRight)
        buttonLayout.addWidget (self.submitButton, alignment=Qt.AlignmentFlag.AlignRight)
        buttonLayout.addWidget (self.submitOpenButton, alignment=Qt.AlignmentFlag.AlignRight)

        self.setLayout (buttonLayout)