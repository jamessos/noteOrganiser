import data
from libaries import *
import element

class main (QGroupBox):

    addElement = Signal (str, list)
    editElement = Signal (str, list)
    moveElement = Signal (int, list)
    openElement = Signal (list)
    sizeElement = Signal (int, list)
    
    showImage = Signal (QPixmap)

    back = Signal ()

    def __init__(self):
        super().__init__()
        #set style of the base widget
        #self.setContentsMargins(0,0,0,0)
        self.setStyleSheet ("background-color: #1c1c1c; min-height: 2000px; min-width: 1440px; max-width: 1440px;")

        #set up the layout
        self.mainLayout = QVBoxLayout ()
        self.mainLayout.setContentsMargins(0,40,0,0)
        self.mainLayout.setSpacing (50)
        self.mainLayout.setAlignment (Qt.AlignmentFlag.AlignHCenter)

        #the top bar of the widget
        self.top = topbar ()
        #set up the signal to add a subelement
        self.top.addElement.connect (self.addElement.emit)
        self.top.back.connect (self.back.emit)
        #add the top bar to the widget
        self.mainLayout.addWidget (self.top, alignment=Qt.AlignmentFlag.AlignHCenter)

        #add the widget that show the definition and name of an element/subject
        self.titlebar = titlebar ()
        self.titleImagebar = titleImagebar()
        self.titlebar.editItem.connect (self.editElement.emit)
        self.titleImagebar.editItem.connect (self.editElement.emit)
        self.titleImagebar.enlargeImage.connect (self.showImage.emit)
        self.mainLayout.addWidget (self.titlebar, alignment=Qt.AlignmentFlag.AlignHCenter)
        self.mainLayout.addWidget (self.titleImagebar, alignment=Qt.AlignmentFlag.AlignHCenter)
        if data.currentDisplay.type == "home":
            self.titlebar.hide()
            self.titleImagebar.hide()
        
        self.list = elementList ()
        self.list.openItem.connect (self.openElement.emit)
        self.list.editItem.connect (self.editElement.emit)
        self.list.moveItem.connect (self.moveElement.emit)
        self.list.sizeItem.connect (self.sizeElement.emit)
        self.list.addItem.connect (self.addElement.emit)
        self.list.showImage.connect (self.showImage.emit)

        self.mainLayout.addWidget (self.list, alignment=Qt.AlignmentFlag.AlignHCenter)
        
        self.setLayout (self.mainLayout)
    def displayChange (self):
        if data.currentDisplay.type == "home":
            self.titlebar.hide()
            #self.titleImagebar.hide()
        else:
            try:
                if data.currentDisplay.img == "none":
                    self.titlebar.show()
                    self.titleImagebar.hide()
                else:
                    self.titleImagebar.show()
                    self.titlebar.hide()
                    #self.titlebar.show() #to be commented out
            except:
                self.titlebar.show()
        self.titlebar.updateText()
        try:
            self.titleImagebar.updateText()
        except:
            pass
    def reload (self):
        self.list.reload ()
        self.top.reload ()
        self.titlebar.updateText()
        try:
            self.titleImagebar.updateText()
        except:
            pass
        self.update ()
        
        pass



class topbar (QGroupBox):
    back = Signal ()
    addElement = Signal (str, list)
    def __init__(self):
        super().__init__()
        #self.setContentsMargins(50,0,0,0)
        self.setStyleSheet ("QGroupBox {max-height: 60px; min-height: 60px; min-width: 1440px; max-width: 1440px; background-color: #1c1c1c} QPushButton {border: 0; background-color: #333333; max-width: 100px; min-width: 100px; min-height: 60px; max-height: 60px; border-radius: 15px}")
        self.topbarLayout = QHBoxLayout ()
        self.topbarLayout.setContentsMargins(45,0,45,0)
        
        self.load()
        self.setLayout (self.topbarLayout)
    def load (self):
        self.topbarLayout.setContentsMargins(45,0,45,0)
        
        self.titlee = primaryTitle ()        
        
        self.titlee.back.connect (self.back.emit)
        

        self.addItem = QPushButton ()
        self.addItem.setIcon (QPixmap(data.filepath ("img/add.png")))
        self.addItem.setIconSize (QSize(20, 20))
        self.addItem.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.addItem.setShortcut ("Ctrl+T")

        self.addGroup = QPushButton ()
        self.addGroup.setIcon (QPixmap(data.filepath ("img/elementGroup.png")))
        self.addGroup.setIconSize (QSize(64, 18))
        self.addGroup.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.addGroup.setShortcut ("Ctrl+G")

        self.addUnit = QPushButton ()
        self.addUnit.setIcon (QPixmap(data.filepath ("img/text.png")))
        self.addUnit.setIconSize (QSize(32, 23))
        self.addUnit.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.addUnit.setShortcut ("Ctrl+N")

        self.addTimeline = QPushButton ()
        self.addTimeline.setIcon (QPixmap(data.filepath ("img/timeline.png")))
        self.addTimeline.setIconSize (QSize(57, 17))
        self.addTimeline.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        
        self.addQuestion = QPushButton ()
        self.addQuestion.setIcon (QPixmap(data.filepath ("img/question.png")))
        self.addQuestion.setIconSize (QSize(48, 24))
        self.addQuestion.setCursor(QCursor(Qt.CursorShape.ForbiddenCursor))

        self.addImage = QPushButton ()
        self.addImage.setIcon (QPixmap(data.filepath ("img/image.png")))
        self.addImage.setIconSize (QSize(50, 22))
        self.addImage.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.addImage.setShortcut ("Ctrl+I")

        self.addItem.clicked.connect (lambda: self.addElement.emit("subject", data.path) if data.currentDisplay.type == "home" else self.addElement.emit("element", data.path))
        self.addUnit.clicked.connect (lambda: self.addElement.emit("unit", data.path) if data.currentDisplay.type == "home" else self.addElement.emit("unit", data.path))
        self.addGroup.clicked.connect (lambda: self.addElement.emit("group", data.path) if data.currentDisplay.type != "home" else data.blankFunction)
        self.addImage.clicked.connect (lambda: self.addElement.emit("image", data.path) if data.currentDisplay.type != "home" else data.blankFunction)

        self.topbarLayout.addWidget (self.titlee)
        self.topbarLayout.addWidget (self.addItem)
        self.topbarLayout.addWidget (self.addGroup)
        self.topbarLayout.addWidget (self.addUnit)
        self.topbarLayout.addWidget (self.addTimeline)
        self.topbarLayout.addWidget (self.addQuestion)
        self.topbarLayout.addWidget (self.addImage)



        #self.topbarLayout.addStretch ()
    def reload (self):
        data.save()
        for i in reversed(range(self.topbarLayout.count())): 
            #self.topbarLayout.itemAt(i).widget().setParent(None) 
            pass
            #self.topbarLayout.itemAt(i).changeSize (0,0)
        self.titlee.refresh()
        self.update()


class primaryTitle (QGroupBox):
    back = Signal ()
    def __init__(self):
        super().__init__()
        self.path = data.getPathString ()
        self.titleLayout = QHBoxLayout ()
        self.titleLayout.setContentsMargins(0,0,0,0)
        self.titleLayout.setSpacing (0)
        self.setStyleSheet ("max-height: 60px; min-height: 60px; min-width: 650px; max-width: 650px; background-color: #1c1c1c; color: #c1c1c1; font-size: 40px")


        self.backButton = QPushButton ()
        
        if self.path[1] != "":
            self.backButton.setText (self.path[0])
            self.backButton.setStyleSheet ("min-width: 0px; max-width: 650px")
        else:
            self.backButton.setText ("")
            self.backButton.setStyleSheet ("min-width: 0px; max-width: 0px")
        
        self.backButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.backButton.clicked.connect (self.back.emit)
        

        #self.backButton.adjustSize()

        self.currentWindow = QLabel ()
        if self.path[1] != "":
            self.currentWindow.setText (self.path[1])
        else:
            self.currentWindow.setText (self.path[0])
        
        self.currentWindow.setStyleSheet ("min-width: 0px; max-width: 650px")

        self.titleLayout.addWidget (self.backButton)
        self.titleLayout.addWidget (self.currentWindow)
        self.titleLayout.addStretch ()
        self.backButton.setShortcut ("Ctrl+[")
        self.setLayout (self.titleLayout)
    def refresh (self):
        self.path = data.getPathString ()
        #print (self.path)
        if self.path[1] != "":
            self.backButton.setText (self.path[0])
            self.backButton.setStyleSheet ("min-width: 0px; max-width: 650px")
        else:
            self.backButton.setText ("")
            self.backButton.setStyleSheet ("min-width: 0px; max-width: 0px; background-color: #ff0000")

        if self.path[1] != "":
            self.currentWindow.setText (self.path[1])
        else:
            self.currentWindow.setText (self.path[0])

        self.backButton.setShortcut ("Ctrl+[")
        self.update()

class titleImagebar (QGroupBox):
    editItem = Signal (str, list)
    enlargeImage = Signal (QPixmap)
    def __init__(self):
        super().__init__()
        self.setStyleSheet ("QGroupBox {border-radius: 25px; max-height: 300px; min-height: 50px; min-width: 1350px; max-width: 1350px; background-color: #333333} QLabel {max-width: 1250px; min-width: 1250px; background-color: #333333}")
        imagebarLayout = QHBoxLayout ()
        imagebarLayout.setContentsMargins(0,0,0,0)
        imagebarLayout.setSpacing (25)
        self.textWindow = titlebar ()
        self.textWindow.editItem.connect (self.editItem.emit)

        self.imageWindow = QScrollArea ()
        self.imageButton = QPushButton ()
        imageButtonLayout = QHBoxLayout ()
        imageButtonLayout.setContentsMargins(0,0,0,0)

        self.image = QLabel ()
        self.image.setAlignment (Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignHCenter)
        self.imageWindow.setAlignment (Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignHCenter)
        imageButtonLayout.setAlignment (Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignHCenter)
        
        imageButtonLayout.addWidget (self.image)
        self.imageButton.setLayout (imageButtonLayout)
        self.imageButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.imageWindow.setWidget (self.imageButton)
        self.imageWindow.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.imageWindow.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.imageButton.clicked.connect (lambda: self.enlargeImage.emit(QPixmap(data.filepath(data.currentDisplay.img))))

        imagebarLayout.addWidget (self.textWindow, alignment=Qt.AlignmentFlag.AlignLeft)
        imagebarLayout.addWidget (self.imageWindow, alignment=Qt.AlignmentFlag.AlignLeft)
        self.setLayout (imagebarLayout)
    def updateText (self):
        self.textWindow.updateText ()
        self.textWindow.titlebarLayout.addStretch ()
        self.textWindow.setStyleSheet ("QGroupBox {border-radius: 25px; max-height: 500px; min-height: 50px; min-width: 825px; max-width: 825px; background-color: #333333} QLabel {max-width: 725px; min-width: 725px; background-color: #333333}")
        self.textWindow.topRow.setStyleSheet ("background-color: #333333; max-height: 45px; min-height: 45px; min-width: 725px; max-width: 725px;")
        
        self.image.setStyleSheet ("QLabel {background-color: #1c1c1c; max-width: 20000px; min-width: 300px; min-height: 0px; max-height: 15000px}")
        self.imageButton.setStyleSheet ("QPushButton {background-color: #1c1c1c; max-width: 20000px; min-width: 300px; min-height: 0px; max-height: 15000px}")
        self.imageWindow.setStyleSheet ("background-color: #1c1c1c; max-width: 450px; min-width: 450px; min-height: 225px; max-height: 225px")
        originalImage = QPixmap(data.filepath(data.currentDisplay.img))        
        
        match data.currentDisplay.fit:
            case "HFit":
                scaledImage = originalImage.scaledToWidth(450)
            case "VFit":
                scaledImage = originalImage.scaledToHeight(225)
            case "Scale":
                scaledImage = originalImage.scaled (QSize (450, 225))
            case "Original":
                scaledImage = originalImage

        self.image.setPixmap (scaledImage)
        self.image.setFixedSize (scaledImage.size())
        self.imageButton.setFixedSize (scaledImage.size())

class titlebar (QGroupBox):
    editItem = Signal (str, list)
    def __init__(self):
        super().__init__()
        self.setStyleSheet ("QGroupBox {border-radius: 25px; max-height: 500px; min-height: 50px; min-width: 1350px; max-width: 1350px; background-color: #333333} QLabel {max-width: 1250px; min-width: 1250px; background-color: #333333}")
        self.titlebarLayout = QVBoxLayout ()
        self.titlebarLayout.setSpacing (5)
        self.titlebarLayout.setContentsMargins(50,15,50,25)

        self.topRow = QGroupBox ()
        self.topRow.setStyleSheet ("background-color: #333333; max-height: 45px; min-height: 45px; min-width: 1250px; max-width: 1250px;")
        self.topRowLayout = QHBoxLayout ()
        self.topRowLayout.setContentsMargins(0,0,0,0)

        self.elementTitle = QLabel ("")
        self.elementTitle.setText (data.currentDisplay.name)
        self.elementTitle.setStyleSheet ("background-color: #333333; font-size: 40px; max-height: 45px; min-height: 0px; min-width: 1000px; max-width: 1000px")

        self.edit = QPushButton ()

        self.edit.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.edit.setStyleSheet ("QPushButton {background-color: #333333; max-width: 30px; min-width: 30px; max-height: 50px; min-height: 50px;}")
        self.edit.setIcon (QPixmap(data.filepath ("img/edit.png")))
        self.edit.setIconSize ((QSize(20, 20)))

        self.edit.clicked.connect (lambda: self.editItem.emit(data.getElementType(data.path), data.path))

        
        
       
        self.topRowLayout.addWidget (self.elementTitle, alignment=Qt.AlignmentFlag.AlignLeft)
        self.topRowLayout.addWidget (self.edit, alignment=Qt.AlignmentFlag.AlignRight)

        self.topRow.setLayout (self.topRowLayout)

        self.elementFlavour = QLabel ("")
        self.elementFlavour.setText (data.currentDisplay.flavour)

        if data.currentDisplay.flavour == "":
            self.elementFlavour.setStyleSheet ("font-size: 40px; max-height: 0px; min-height: 0px")
        else:
            self.elementFlavour.setStyleSheet ("font-size: 15px; max-height: 30px; min-height: 0px")

        #self.elementFlavour.setStyleSheet ("font-size: 15px; max-height: 30px; min-height: 0px")
        
        self.elementDesc = QLabel ("")
        self.elementDesc.setText (data.currentDisplay.desc)
        self.elementDesc.setWordWrap(True)
        #self.elementDesc.setStyleSheet ("font-size: 20px; min-height: 0px; max-height: 410px")

        if data.currentDisplay.desc == "":
            self.elementDesc.setStyleSheet ("font-size: 0px; max-height: 0px; min-height: 0px")
        else:
            self.elementDesc.setStyleSheet ("font-size: 20px; max-height: 410px; min-height: 0px")


        self.titlebarLayout.addWidget (self.topRow, alignment=Qt.AlignmentFlag.AlignTop)
        self.titlebarLayout.addWidget (self.elementFlavour, alignment=Qt.AlignmentFlag.AlignTop)
        self.titlebarLayout.addSpacerItem (QSpacerItem(100, 10))
        self.titlebarLayout.addWidget (self.elementDesc, alignment=Qt.AlignmentFlag.AlignTop)
        self.setLayout (self.titlebarLayout)

    def updateText (self):
        self.elementTitle.setText (data.currentDisplay.name)
        self.elementFlavour.setText (data.currentDisplay.flavour)
        self.elementDesc.setText (data.currentDisplay.desc)

        if data.currentDisplay.desc == "":
            self.elementDesc.setStyleSheet ("font-size: 0px; max-height: 0px; min-height: 0px")
        else:
            self.elementDesc.setStyleSheet ("font-size: 20px; max-height: 410px; min-height: 0px")
        if data.currentDisplay.flavour == "":
            self.elementFlavour.setStyleSheet ("font-size: 40px; max-height: 0px; min-height: 0px")
        else:
            self.elementFlavour.setStyleSheet ("font-size: 15px; max-height: 30px; min-height: 0px")
        self.update()


class elementList (QGroupBox):
    openItem = Signal (list)
    editItem = Signal (str, list)
    moveItem = Signal (int, list)
    sizeItem = Signal (int, list)

    
    addItem = Signal (str, list)

    showImage = Signal (QPixmap)


    def __init__(self):
        super().__init__()
        #define the base layout of the list and remove the margins
        self.elementLayout = QVBoxLayout ()
        self.elementLayout.setContentsMargins(0,0,0,0)
        self.elementLayout.setSpacing (45)

        self.setStyleSheet ("background-color: #1c1c1c; max-width: 1440px; min-width: 1440px; min-height: 700px")
        self.load ()
    def load (self):
        #defile a list of elements
        list = []
        #each row hold 3 sizes worth of elements
        sizeVar = 0
        
        #set up a for loop to display every subelement
        for index, thing in enumerate(data.currentDisplay.subelement):
            #add the element to the list
            list.append (thing)
            #add the size of the widget to sizevar
            sizeVar += thing.size

            #if the sum of the size of all the elements in the list adds up to 3, create a row of these elements and add it to the layout
            if sizeVar == 3 or index == len(data.currentDisplay.subelement) - 1 or sizeVar + data.currentDisplay.subelement[index+1].size > 3:
                
                #set up the widget containing the row
                rowOfSubject = QGroupBox ()
                rowOfSubject.setStyleSheet ("max-width: 1440px; min-width: 1440px;min-height: 75px; max-width: 175px; background-color: #1c1c1c")
                #set up the layout for the row
                rowLayout = QHBoxLayout ()
                #set up the spacing between elements
                rowLayout.setSpacing (45)
                rowLayout.setContentsMargins(45,0,45,0)

                #for every element in the list, add it to the layout of the row, depending on the type
                for item in list:
                    if item.type == "image":
                        item.type = "imageV"
                        data.save()
                    #print (item.type)
                    match item.type:
                        #when the subelement is a subject
                        case "subject":
                            
                            #set up the widget
                            itemToAdd = element.subject(item)
                            #print ("added subject")
                            #set up the signal connection
                            
                        case "element":
                            itemToAdd = element.element(item)
                            #add the widget
                        case "group":
                            itemToAdd = element.group(item)
                            #add the widget
                        case "imageV":
                            itemToAdd = element.imageV(item)
                        case "imageH":
                            itemToAdd = element.imageH(item)
                        case "unit":
                            itemToAdd = element.unit(item)
                        
                    itemToAdd.enter.connect (self.openItem.emit)
                    itemToAdd.edit.connect (self.editItem.emit)
                    itemToAdd.rearrange.connect (self.moveItem.emit)
                    itemToAdd.changeSize.connect (self.sizeItem.emit)
                    try:
                        itemToAdd.enlargeImage.connect (self.showImage.emit)
                    except:
                        pass

                    if item.type == "group" or item.type == "timeline" or item.type == "list":
                        itemToAdd.addItem.connect (self.addItem.emit)

                    rowLayout.addWidget (itemToAdd)


                #if the row of the item is the last row, add stretch to the row
                if index == len(data.currentDisplay.subelement) - 1 or sizeVar + data.currentDisplay.subelement[index+1].size > 3:
                    rowLayout.addStretch ()
                #set the layout of the row
                rowOfSubject.setLayout (rowLayout)
                
                #rowOfSubject.setFixedSize(rowLayout.sizeHint())


                #reset the list and the size
                list = []
                sizeVar = 0

                #add the row to the main widget
                self.elementLayout.addWidget (rowOfSubject)

        #set the layout of the widget
        self.setLayout (self.elementLayout)
        #add stretch to the layout
        self.elementLayout.addStretch ()
    def reload (self):
        for i in reversed(range(self.elementLayout.count())): 
            if self.elementLayout.itemAt(i).__class__.__name__ != "QSpacerItem":
                self.elementLayout.itemAt(i).widget().setParent(None) 
            else:
                #QSpacerItem.changeS
                self.elementLayout.itemAt(i).changeSize (0,0)
        self.load ()
        self.update ()
   