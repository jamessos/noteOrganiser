from libaries import *
import data


class subject (QPushButton):
    #define all the signals that the widget could send
    edit = Signal (str, list)
    enter = Signal (list)
    rearrange = Signal (int, list)
    changeSize = Signal (int, list)
    def __init__(self, subject):
        super().__init__()
        #set up path of self
        self.path = []
        for i in data.path:
            self.path.append (i)
        self.path.append (data.currentDisplay.subelement.index(subject))

        #set stylesheet of self
        self.setStyleSheet ("QPushButton {background-color: #333333; max-width: 420px; min-width: 420px; max-height: 175px; min-height: 175px; border-radius: 25px}")
        self.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        
        #define the layout and set the spacing
        self.subjectLayout = QVBoxLayout ()
        self.subjectLayout.setContentsMargins(30,15,30,15)

        #set up the top row containing the title and buttons
        self.topRow = QGroupBox ()
        self.topRow.setStyleSheet ("QGroupBox {max-height: 50px; min-height: 50px; min-width: 360px; max-width: 360px; background-color: #333333} background-color: #333333")
        self.topRowLayout = QHBoxLayout ()
        self.topRowLayout.setContentsMargins(0,0,0,0)
        self.topRowLayout.setSpacing (15)

        #widget for the title of the element
        self.title = QLabel (subject.name)
        self.title.setStyleSheet ("max-height: 50px; min-height: 50px; min-width: 280px; max-width: 280px; background-color: #333333; color: #c1c1c1; font-size: 45px")

        #buttons for moving the element
        self.arrange = moveButton ()
        self.arrange.moved.connect (lambda d: self.rearrange.emit(d, self.path))

        self.editButton = editButton ()
        self.editButton.edit.connect (lambda: self.edit.emit("subject", self.path))

        #add the title to the top row
        self.topRowLayout.addWidget (self.title)
        self.topRowLayout.addWidget (self.editButton)
        self.topRowLayout.addWidget (self.arrange)

        #set the layout of the top row
        self.topRow.setLayout(self.topRowLayout)

        #display and set style of the the description of the element
        self.desc = QLabel (subject.flavour)
        self.desc.setWordWrap(True)
        self.desc.setAlignment (Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)
        self.desc.setStyleSheet ("max-height: 70px; min-height: 70px; min-width: 360px; max-width: 360px; background-color: #333333; color: #c1c1c1; font-size: 25px")
        
        #add the widgets to the layout
        self.subjectLayout.addWidget (self.topRow)
        self.subjectLayout.addWidget (self.desc)

        #set the layout of self
        self.setLayout (self.subjectLayout)

        #define the index that will be used in the signal
        
        #send the signal when the widget is clicked on
        self.clicked.connect (lambda: self.enter.emit(self.path))


class element (QPushButton):
    edit = Signal (str, list)
    enter = Signal (list)
    rearrange = Signal (int, list)
    changeSize = Signal (int, list)
    def __init__(self, element):
        super().__init__()

        #this is nessessary as it is something that can be in an element group
        try:
            self.index = data.currentDisplay.subelement.index(element)
        except:
            self.index = -1

        self.path = []
        for i in data.path:
            self.path.append (i)
        self.path.append (self.index)

        #set stylesheet of self
        self.setStyleSheet ("QPushButton {background-color: #333333; max-width: 420px; min-width: 420px; max-height: 300px; min-height: 300px; border-radius: 25px}")
        self.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        
        #define the layout and set the spacing
        self.elementLayout = QVBoxLayout ()
        self.elementLayout.setContentsMargins(30,15,30,15)

        #set up the top row containing the title and buttons
        self.topRow = QGroupBox ()
        self.topRow.setStyleSheet ("QGroupBox {max-height: 80px; min-height: 50px; min-width: 360px; max-width: 360px; background-color: #333333} background-color: #333333")
        self.topRowLayout = QHBoxLayout ()
        self.topRowLayout.setContentsMargins(0,0,0,0)
        self.topRowLayout.setSpacing (15)

        #widget for the title of the element
        self.title = QLabel (element.name)
        self.title.setStyleSheet ("max-height: 100px; min-height: 50px; min-width: 280px; max-width: 280px; background-color: #333333; color: #c1c1c1; font-size: 30px")
        self.title.setWordWrap (True)
        #buttons for moving the element
        self.arrange = moveButton ()
        self.arrange.moved.connect (lambda d: self.rearrange.emit(d, self.path))

        self.editButton = editButton ()
        self.editButton.edit.connect (lambda: self.edit.emit("element", self.path))

        self.sizeButton = sizeButton ()
        self.sizeButton.sizeChange.connect (lambda d:self.changeSize.emit (d, self.path))

        #add the title to the top row
        self.topRowLayout.addWidget (self.title)
        self.topRowLayout.addWidget (self.editButton)
        self.topRowLayout.addWidget (self.arrange)
        self.topRowLayout.addWidget (self.sizeButton)

        #set the layout of the top row
        self.topRow.setLayout(self.topRowLayout)

        #display and set style of the the description of the element
        self.desc = QLabel (element.desc)
        self.desc.setWordWrap(True)
        self.desc.setAlignment (Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)
        self.desc.setStyleSheet ("max-height: 195px; min-height: 145px; min-width: 360px; max-width: 360px; background-color: #333333; color: #c1c1c1; font-size: 20px")
        
        #add the widgets to the layout
        self.elementLayout.addWidget (self.topRow)
        self.elementLayout.addWidget (self.desc)
        self.elementLayout.addStretch()
        #set the layout of self
        self.setLayout (self.elementLayout)

        #define the index that will be used in the signal
        
        #send the signal when the widget is clicked on
        self.clicked.connect (lambda: self.enter.emit(self.path))

        self.sizeChange (element.size)
    def sizeChange (self, size):
        if size == 1:
            self.setStyleSheet ("QPushButton {background-color: #333333; max-width: 420px; min-width: 420px; max-height: 300px; min-height: 300px; border-radius: 25px}")
            self.topRow.setStyleSheet ("QGroupBox {max-height: 80px; min-height: 50px; min-width: 360px; max-width: 360px; background-color: #333333} background-color: rgba(0,0,0,0)")
            self.title.setStyleSheet ("max-height: 100px; min-height: 50px; min-width: 255px; max-width: 255px; background-color: #333333; color: #c1c1c1; font-size: 30px")
            self.desc.setStyleSheet ("max-height: 195px; min-height: 145px; min-width: 360px; max-width: 360px; background-color: #333333; color: #c1c1c1; font-size: 20px")
        elif size == 2:
            self.setStyleSheet ("QPushButton {background-color: #333333; max-width: 885px; min-width: 885px; max-height: 300px; min-height: 300px; border-radius: 25px}")
            self.topRow.setStyleSheet ("QGroupBox {max-height: 80px; min-height: 50px; min-width: 825px; max-width: 825px; background-color: #333333} background-color: #333333")
            self.title.setStyleSheet ("max-height: 100px; min-height: 50px; min-width: 745px; max-width: 745px; background-color: #333333; color: #c1c1c1; font-size: 30px")
            self.desc.setStyleSheet ("max-height: 195px; min-height: 145px; min-width: 825px; max-width: 825px; background-color: #333333; color: #c1c1c1; font-size: 20px")
        elif size == 3:
            self.setStyleSheet ("QPushButton {background-color: #333333; max-width: 1350px; min-width: 1350px; max-height: 500px; min-height: 50px; border-radius: 25px}")
            self.topRow.setStyleSheet ("QGroupBox {max-height: 80px; min-height: 50px; min-width: 1290px; max-width: 1290px; background-color: #333333} background-color: #333333")
            self.title.setStyleSheet ("max-height: 100px; min-height: 50px; min-width: 1210px; max-width: 1210px; background-color: #333333; color: #c1c1c1; font-size: 30px")
            self.desc.setStyleSheet ("max-height: 195px; min-height: 0px; min-width: 1290px; max-width: 1290px; background-color: #333333; color: #c1c1c1; font-size: 20px")
        self.update()


class unit (QPushButton):
    #define all the signals that the widget could send
    edit = Signal (str, list)
    enter = Signal (list)
    rearrange = Signal (int, list)
    changeSize = Signal (int, list)
    def __init__(self, subject):
        super().__init__()
        #set up path of self
        try:
            self.index = data.currentDisplay.subelement.index(subject)
        except:
            self.index = -1

        self.path = []
        for i in data.path:
            self.path.append (i)
        self.path.append (self.index)

        #set stylesheet of self
        self.setStyleSheet ("QPushButton {background-color: #333333; max-width: 420px; min-width: 420px; max-height: 175px; min-height: 0px; border-radius: 25px}")
        self.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        
        #define the layout and set the spacing
        self.subjectLayout = QVBoxLayout ()
        self.subjectLayout.setContentsMargins(30,15,30,15)

        #set up the top row containing the title and buttons
        #set up the top row containing the title and buttons
        self.topRow = QGroupBox ()
        self.topRow.setStyleSheet ("QGroupBox {max-height: 80px; min-height: 50px; min-width: 360px; max-width: 360px; background-color: #333333} background-color: #333333")
        self.topRowLayout = QHBoxLayout ()
        self.topRowLayout.setContentsMargins(0,0,0,0)
        self.topRowLayout.setSpacing (15)

        #widget for the title of the element
        self.title = QLabel (subject.name)
        self.title.setStyleSheet ("max-height: 100px; min-height: 50px; min-width: 275px; max-width: 275px; background-color: #333333; color: #c1c1c1; font-size: 30px")
        self.title.setWordWrap (True)
        #buttons for moving the element
        self.arrange = moveButton ()
        self.arrange.moved.connect (lambda d: self.rearrange.emit(d, self.path))

        self.editButton = editButton ()
        self.editButton.edit.connect (lambda: self.edit.emit("unit", self.path))

        #add the title to the top row
        self.topRowLayout.addWidget (self.title)
        self.topRowLayout.addWidget (self.editButton, alignment=Qt.AlignmentFlag.AlignRight)
        self.topRowLayout.addWidget (self.arrange, alignment=Qt.AlignmentFlag.AlignRight)

        #set the layout of the top row
        self.topRow.setLayout(self.topRowLayout)

        #display and set style of the the description of the element
        self.desc = QLabel (subject.flavour)
        self.desc.setWordWrap(True)
        self.desc.setAlignment (Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)
        self.desc.setStyleSheet ("min-width: 360px; max-width: 360px; max-height:70px; min-height:0px; background-color: #333333; color: #c1c1c1; font-size: 20px")
        
        if subject.flavour == "":
            self.setStyleSheet ("QPushButton {background-color: #333333; max-width: 420px; min-width: 420px; max-height: 110px; min-height: 80px; border-radius: 25px}")
            self.subjectLayout.addWidget (self.topRow)
        else:
            self.subjectLayout.addWidget (self.topRow)
            self.subjectLayout.addWidget (self.desc)
        
        #add the widgets to the layout
        
        

        #set the layout of self
        self.setLayout (self.subjectLayout)
        #self.desc.setFixedSize(self.desc.sizeHint())
        self.adjustSize()
        #define the index that will be used in the signal
        
        

        #self.setFixedSize (self.size())
        #send the signal when the widget is clicked on
        self.clicked.connect (lambda: self.enter.emit(self.path))


class group (QGroupBox):
    edit = Signal (str, list)
    enter = Signal (list)
    rearrange = Signal (int, list)
    changeSize = Signal (int, list)
    enlargeImage = Signal (QPixmap)
    addItem = Signal (str, list)
    #str is the type and list is for the path
    def __init__(self, element):
        super().__init__()
        
        self.path = []
        for i in data.path:
            self.path.append (i)
        self.path.append (data.currentDisplay.subelement.index(element))

        #set stylesheet of self
        self.setStyleSheet ("QGroupBox {background-color: #1c1c1c; max-width: 1350px; min-width: 1350px; max-height: 50000px; min-height: 0px}")

        self.groupLayout = QVBoxLayout ()
        #self.groupLayout.setContentsMargins(30,15,30,15)
        self.groupLayout.setContentsMargins(0,0,0,0)
        self.groupLayout.setSpacing (25)

        topBorder = groupBorder ()


        #set up the top row containing the title and buttons
        self.topRow = QGroupBox ()
        
        self.topRow.setStyleSheet ("QGroupBox {max-height: 80px; min-height: 50px; min-width: 1350px; max-width: 1350px; background-color: #1c1c1c} QPushButton {border: 0; background-color: #333333; max-width: 100px; min-width: 100px; min-height: 60px; max-height: 60px; border-radius: 15px} background-color: #333333; ")
        self.topRowLayout = QHBoxLayout ()
        self.topRowLayout.setContentsMargins(30,0,30,0)
        self.topRowLayout.setSpacing (15)

        #widget for the title of the element
        self.title = QLabel (element.name)
        self.title.setStyleSheet ("max-height: 100px; min-height: 50px; min-width: 875px; max-width: 875px; background-color: #1c1c1c; color: #c1c1c1; font-size: 45px")
        #buttons for moving the element

        self.add = QPushButton ()
        
        self.add.setIcon (QPixmap(data.filepath ("img/add.png")))
        self.add.setIconSize (QSize(20, 20))
        self.add.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.add.clicked.connect (lambda: self.addItem.emit ("element", self.path))

        self.img = QPushButton ()
        self.img.setIcon (QPixmap(data.filepath ("img/image.png")))
        self.img.setIconSize (QSize(50, 22))
        self.img.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.img.clicked.connect (lambda: self.addItem.emit ("image", self.path))

        self.txt = QPushButton ()
        self.txt.setIcon (QPixmap(data.filepath ("img/text.png")))
        self.txt.setIconSize (QSize(32, 23))
        self.txt.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.txt.clicked.connect (lambda: self.addItem.emit ("unit", self.path))


        self.arrange = moveButton ()
        self.arrange.setStyleSheet ("QGroupBox {max-width: 20px; min-width: 20px; max-height: 50px; min-height: 50px; background-color: #1c1c1c} QPushButton { background-color: #1c1c1c; max-width: 20px; min-width: 20px; max-height: 25px; min-height: 25px;} background-color: #1c1c1c")
        self.arrange.moved.connect (lambda d: self.rearrange.emit(d, self.path))

        self.editButton = editButton ()
        self.editButton.setStyleSheet ("QPushButton {max-width: 30px; min-width: 30px; max-height: 50px; min-height: 50px; background-color: #1c1c1c}")
        self.editButton.edit.connect (lambda: self.edit.emit("group", self.path))

        #add the title to the top row
        self.topRowLayout.addWidget (self.title)

        self.topRowLayout.addWidget (self.add)
        self.topRowLayout.addWidget (self.img)
        self.topRowLayout.addWidget (self.txt)

        self.topRowLayout.addWidget (self.editButton)
        self.topRowLayout.addWidget (self.arrange)

        #set the layout of the top row
        self.topRow.setLayout(self.topRowLayout)


        self.subelements = groupElementList (element.subelement, self.path)
        self.subelements.openItem.connect(self.enter)
        self.subelements.editItem.connect(self.edit)
        self.subelements.moveItem.connect(self.rearrange)
        self.subelements.sizeItem.connect(self.changeSize)
        self.subelements.enlargeImage.connect (self.enlargeImage)
        self.subelements.setStyleSheet ("QGroupBox{background-color: #1c1c1c; max-width: 1440px; min-width: 1440px; min-height: 0px; max-height: 50000px}")
        bottomBorder = groupBorder ()

        self.groupLayout.addWidget (topBorder)
        self.groupLayout.addWidget (self.topRow)
        self.groupLayout.addWidget (self.subelements)
        self.groupLayout.addWidget (bottomBorder)

        self.setLayout (self.groupLayout)

class groupBorder (QGroupBox):
    def __init__(self):
        super().__init__()
        self.setStyleSheet ("QGroupBox {background-color: #333333; max-width: 1350px; min-width: 1350px; max-height: 15px; min-height: 15px; border-radius: 25px}")


class groupElementList (QGroupBox):
    openItem = Signal (list)
    editItem = Signal (str, list)
    moveItem = Signal (int, list)
    sizeItem = Signal (int, list)
    enlargeImage = Signal (QPixmap)
    def __init__(self, elements, path):
        super().__init__()
        #define the base layout of the list and remove the margins
        self.elementLayout = QVBoxLayout ()
        self.elementLayout.setContentsMargins(0,15,0,15)
        self.elementLayout.setSpacing (45)

        #self.setStyleSheet ("QGroupBox{background-color: #ff0000; max-width: 1440px; min-width: 1440px}")
        
        self.load (elements, path)
    def load (self, elements, path):
        #defile a list of elements
        list = []
        #each row hold 3 sizes worth of elements
        sizeVar = 0
        
        #set up a for loop to display every subelement
        for index, thing in enumerate(elements):
            #add the element to the list
            list.append (thing)
            #add the size of the widget to sizevar
            sizeVar += thing.size

            #if the sum of the size of all the elements in the list adds up to 3, create a row of these elements and add it to the layout
            if sizeVar == 3 or index == len(elements) - 1 or sizeVar + elements[index+1].size > 3:
                
                #set up the widget containing the row
                rowOfSubject = QGroupBox ()
                rowOfSubject.setStyleSheet ("max-width: 1440px; min-width: 1440px;min-height: 175px; max-width: 175px; background-color: #1c1c1c")
                #set up the layout for the row
                rowLayout = QHBoxLayout ()
                #set up the spacing between elements
                rowLayout.setSpacing (45)
                rowLayout.setContentsMargins(0,0,0,0)

                #for every element in the list, add it to the layout of the row, depending on the type
                for item in list:
                    match item.type:
                        case "element":
                            itemToAdd = element(item)
                        case "imageV":
                            itemToAdd = imageV(item)
                        case "imageH":
                            itemToAdd = imageH(item)
                        case "unit":
                            itemToAdd = unit(item)
                            #add the widget
                    
                    self.connectItem (item, elements, itemToAdd, path)

                    rowLayout.addWidget (itemToAdd)

                #if the row of the item is the last row, add stretch to the row
                if index == len(elements) - 1 or sizeVar + elements[index+1].size > 3:
                    rowLayout.addStretch ()
                #set the layout of the row
                rowOfSubject.setLayout (rowLayout)

                #reset the list and the size
                list = []
                sizeVar = 0

                #add the row to the main widget
                self.elementLayout.addWidget (rowOfSubject)

        #set the layout of the widget
        self.setLayout (self.elementLayout)
        #add stretch to the layout
        #self.elementLayout.addStretch ()
    def connectItem (self, item, elements, itemToAdd, path):
        currentPath = []
        for i in path:
            currentPath.append (i)
        currentPath.append(elements.index(item))

        itemToAdd.enter.connect (lambda: self.openItem.emit(currentPath))
        itemToAdd.edit.connect (lambda type, x: self.editItem.emit(type, currentPath))
        itemToAdd.rearrange.connect (lambda direction, x: self.moveItem.emit(direction, currentPath))
        itemToAdd.changeSize.connect (lambda size, x: self.sizeItem.emit(size, currentPath))
        try:
            itemToAdd.enlargeImage.connect(self.enlargeImage.emit)
        except:
            pass
    def reload (self):
        for i in reversed(range(self.elementLayout.count())): 
            if self.elementLayout.itemAt(i).__class__.__name__ != "QSpacerItem":
                self.elementLayout.itemAt(i).widget().setParent(None) 
            else:
                #QSpacerItem.changeS
                self.elementLayout.itemAt(i).changeSize (0,0)
        self.load ()
        self.update ()
   

class imageH (QPushButton):
    edit = Signal (str, list)
    enter = Signal (list)
    rearrange = Signal (int, list)
    changeSize = Signal (int, list)
    enlargeImage = Signal (QPixmap)
    def __init__(self, element):
        super().__init__()
        try:
            self.index = data.currentDisplay.subelement.index(element)
        except:
            self.index = -1

        self.path = []
        for i in data.path:
            self.path.append (i)
        self.path.append (self.index)

        self.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.elementLayout = QHBoxLayout ()
        self.elementLayout.setContentsMargins(25,25,25,25)

        self.firstColumn = QGroupBox ()
        self.firstColumnLayout = QVBoxLayout ()
        self.firstColumnLayout.setContentsMargins(0,0,0,0)

        self.titlee = QLabel (element.name)
        self.titlee.setAlignment (Qt.AlignmentFlag.AlignTop)
        self.titlee.setWordWrap (True)

        #set up the top row containing the title and buttons
        self.topRow = QGroupBox ()
        self.topRow.setStyleSheet ("QGroupBox {border-radius: 0px; max-height: 50px; min-height: 50px; min-width: 250px; max-width: 250px; background-color: #333333} QPushButton {background-color: #333333} background-color: #333333")
        self.topRowLayout = QHBoxLayout ()
        self.topRowLayout.setContentsMargins(0,0,0,0)
        self.topRowLayout.setSpacing (15)

       
        #buttons for moving the element
        self.arrange = moveButton ()
        self.arrange.moved.connect (lambda d: self.rearrange.emit(d, self.path))

        self.editButton = editButton ()
        self.editButton.edit.connect (lambda: self.edit.emit("image", self.path))

        self.topRowLayout.addWidget (self.editButton)
        self.topRowLayout.addWidget (self.arrange)
        self.topRow.setLayout (self.topRowLayout)

        self.desc = QLabel (element.desc)
        self.desc.setWordWrap (True)
        self.desc.setAlignment (Qt.AlignmentFlag.AlignTop)

        self.firstColumnLayout.addWidget (self.titlee)
        self.firstColumnLayout.addWidget (self.topRow)
        self.firstColumnLayout.addStretch ()
        self.firstColumn.setLayout (self.firstColumnLayout)


        self.imageScroll = QScrollArea ()

        self.imageButton = QPushButton ()
        imageButtonLayout = QHBoxLayout ()
        imageButtonLayout.setContentsMargins(0,0,0,0)

        self.image = QLabel ()
        self.image.setAlignment (Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignHCenter)
        self.imageScroll.setAlignment (Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignHCenter)
        imageButtonLayout.setAlignment (Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignHCenter)
        
        imageButtonLayout.addWidget (self.image)
        self.imageButton.setLayout (imageButtonLayout)
        self.imageButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.imageScroll.setWidget (self.imageButton)
        self.imageScroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.imageScroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.imageButton.clicked.connect (lambda: self.enlargeImage.emit(QPixmap(data.filepath(element.img))))

        self.elementLayout.addWidget(self.firstColumn, alignment=Qt.AlignmentFlag.AlignTop)
        self.elementLayout.addSpacerItem (QSpacerItem(25, 10))
        self.elementLayout.addWidget (self.desc, alignment=Qt.AlignmentFlag.AlignTop)
        self.elementLayout.addSpacerItem (QSpacerItem(25, 10))
        self.elementLayout.addWidget (self.imageScroll)

         #send the signal when the widget is clicked on
        self.clicked.connect (lambda: self.enter.emit(self.path))

        self.setup (element)
        self.setLayout(self.elementLayout)

    def setup (self, element):
        originalImage = QPixmap(data.filepath(element.img))  
        if element.name == "":
            self.titlee.setText ("untitled")
        else:
            self.titlee.setText (element.name)
        if element.desc == "":
            self.desc.setText ("no description was entered")
        else:
            self.desc.setText (element.desc)
        
        match element.size:
            case 2:
                self.setStyleSheet ("QPushButton {background-color: #333333; max-width: 885px; min-width: 885px; max-height: 300px; min-height: 300px; border-radius: 25px}")
                self.titlee.setStyleSheet ("QLabel {background-color: #333333; max-width: 200px; min-width: 200px; min-height: 0px; max-height: 175px; font-size: 40px;}")
                self.firstColumn.setStyleSheet ("QGroupBox {background-color: #333333; max-width: 200px; min-width: 200px; min-height: 225px; max-height: 225px}")
                self.desc.setStyleSheet ("QLabel {background-color: #333333; max-width: 225px; min-width: 225px; min-height: 225px; max-height: 225px; font-size: 20px;}")
                self.image.setStyleSheet ("QLabel {background-color: #1c1c1c; max-width: 20000px; min-width: 300px; min-height: 0px; max-height: 15000px}")
                self.imageButton.setStyleSheet ("QPushButton {background-color: #1c1c1c; max-width: 20000px; min-width: 300px; min-height: 0px; max-height: 15000px}")
                self.imageScroll.setStyleSheet ("background-color: #1c1c1c; max-width: 300px; min-width: 300px; min-height: 225px; max-height: 225px")
                match element.fit:
                    case "HFit":
                        scaledImage = originalImage.scaledToWidth(300)
                    case "VFit":
                        scaledImage = originalImage.scaledToHeight(225)
                    case "Scale":
                        scaledImage = originalImage.scaled (QSize (300, 225))
                    case "Original":
                        scaledImage = originalImage
            case 3:
                self.setStyleSheet ("QPushButton {background-color: #333333; max-width: 1350px; min-width: 1350px; max-height: 300px; min-height: 300px; border-radius: 25px}")
                self.titlee.setStyleSheet ("QLabel {background-color: #333333; max-width: 250px; min-width: 250px; min-height: 0px; max-height: 175px; font-size: 40px;}")
                self.firstColumn.setStyleSheet ("QGroupBox {background-color: #333333; max-width: 250px; min-width: 250px; min-height: 225px; max-height: 225px}")
                self.desc.setStyleSheet ("QLabel {background-color: #333333; max-width: 490px; min-width: 490px; min-height: 225px; max-height: 225px; font-size: 20px;}")
                self.imageScroll.setStyleSheet ("background-color: #1c1c1c; max-width: 450px; min-width: 450px; min-height: 225px; max-height: 225px")
                self.image.setStyleSheet ("QLabel {max-width: 20000px; min-width: 450px; min-height: 0px; max-height: 15000px}")
                self.imageButton.setStyleSheet ("QPushButton {max-width: 20000px; min-width: 450px; min-height: 0px; max-height: 15000px}")
                match element.fit:
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


class imageV (QPushButton):
    edit = Signal (str, list)
    enter = Signal (list)
    rearrange = Signal (int, list)
    changeSize = Signal (int, list)
    enlargeImage = Signal (QPixmap)
    def __init__(self, element):
        super().__init__()
        try:
            self.index = data.currentDisplay.subelement.index(element)
        except:
            self.index = -1

        self.path = []
        for i in data.path:
            self.path.append (i)
        self.path.append (self.index)
        self.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.elementLayout = QVBoxLayout ()
        self.elementLayout.setContentsMargins(60,15,60,15)


        self.topRow = QGroupBox ()
        self.topRow.setStyleSheet ("QGroupBox {max-height: 80px; min-height: 50px; min-width: 360px; max-width: 360px; background-color: #333333} background-color: #333333")
        self.topRowLayout = QHBoxLayout ()
        self.topRowLayout.setContentsMargins(0,0,0,0)
        self.topRowLayout.setSpacing (15)

        #widget for the title of the element
        self.titlee = QLabel (element.name)
        #buttons for moving the element
        self.arrange = miniMoveButton ()
        self.arrange.moved.connect (lambda d: self.rearrange.emit(d, self.path))

        self.editButton = miniEditButton ()
        self.editButton.edit.connect (lambda: self.edit.emit("image", self.path))

        #add the title to the top row
        self.topRowLayout.addWidget (self.titlee)
        self.topRowLayout.addWidget (self.editButton)
        self.topRowLayout.addWidget (self.arrange)

        self.topRow.setLayout (self.topRowLayout)
        
        #self.title.setStyleSheet ("max-height: 100px; min-height: 50px; min-width: 280px; max-width: 280px; background-color: #333333; color: #c1c1c1; font-size: 30px")
        self.imageScroll = QScrollArea ()

        self.imageButton = QPushButton ()
        imageButtonLayout = QHBoxLayout ()
        imageButtonLayout.setContentsMargins(0,0,0,0)

        self.image = QLabel ()
        self.image.setAlignment (Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignHCenter)
        self.imageScroll.setAlignment (Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignHCenter)
        imageButtonLayout.setAlignment (Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignHCenter)
        
        imageButtonLayout.addWidget (self.image)
        self.imageButton.setLayout (imageButtonLayout)
        self.imageButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
    
        self.imageButton.clicked.connect (lambda: self.enlargeImage.emit(QPixmap(data.filepath(element.img))))

        self.imageScroll.setWidget (self.imageButton)
        self.imageScroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.imageScroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        
        self.elementLayout.addWidget (self.topRow)
        self.elementLayout.addWidget (self.imageScroll)
        self.clicked.connect (lambda: self.enter.emit(self.path))
        self.setup(element)
        
        self.setLayout (self.elementLayout)
    def setup (self, element):
        
        
        originalImage = QPixmap(data.filepath(element.img))
        match element.size:
            case 1:
                self.setStyleSheet ("QPushButton {background-color: #333333; max-width: 420px; min-width: 420px; max-height: 300px; min-height: 300px; border-radius: 25px}")
                self.imageScroll.setStyleSheet ("background-color: #1c1c1c; max-width: 300px; min-width: 300px; min-height: 225px; max-height: 225px")
                self.image.setStyleSheet ("QLabel {max-width: 20000px; min-width: 300px; min-height: 0px; max-height: 15000px}")
                self.imageButton.setStyleSheet ("QPushButton {max-width: 20000px; min-width: 300px; min-height: 0px; max-height: 15000px}")
                self.topRow.setStyleSheet ("max-height: 30px; min-height: 30px; min-width: 300px; max-width: 300px; background-color: #333333; color: #c1c1c1; font-size: 30px")
                self.titlee.setStyleSheet ("max-height: 30px; min-height: 30px; min-width: 225px; max-width: 225px; background-color: #333333; color: #c1c1c1; font-size: 25px")
                
                match element.fit:
                    case "HFit":
                        scaledImage =originalImage.scaledToWidth(300)
                    case "VFit":
                        scaledImage = originalImage.scaledToHeight(225)
                    case "Scale":
                        scaledImage = originalImage.scaled (QSize (300, 225))
                    case "Original":
                        scaledImage = originalImage
            case 2:
                self.setStyleSheet ("QPushButton {background-color: #333333; max-width: 885px; min-width: 885px; max-height: 300px; min-height: 300px; border-radius: 25px}")
                self.imageScroll.setStyleSheet ("background-color: #1c1c1c; max-width: 765px; min-width: 765px; min-height: 225px; max-height: 225px")
                self.image.setStyleSheet ("QLabel {max-width: 20000px; min-width: 765px; min-height: 0px; max-height: 15000px}")
                self.imageButton.setStyleSheet ("QPushButton {max-width: 20000px; min-width: 765px; min-height: 0px; max-height: 15000px}")
                self.topRow.setStyleSheet ("max-height: 30px; min-height: 30px; min-width: 765px; max-width: 765px; background-color: #333333; color: #c1c1c1; font-size: 25px")
                self.titlee.setStyleSheet ("max-height: 30px; min-height: 30px; min-width: 690px; max-width: 690px; background-color: #333333; color: #c1c1c1; font-size: 25px")
                match element.fit:
                    case "HFit":
                        scaledImage = originalImage.scaledToWidth(765)
                    case "VFit":
                        scaledImage = originalImage.scaledToHeight(225)
                    case "Scale":
                        scaledImage = originalImage.scaled (QSize (765, 225))
                    case "Original":
                        scaledImage = originalImage
            case 3:
                self.setStyleSheet ("QPushButton {background-color: #333333; max-width: 1350px; min-width: 1350px; max-height: 525px; min-height: 525px; border-radius: 25px}")
                self.imageScroll.setStyleSheet ("background-color: #1c1c1c; max-width: 1230px; min-width: 1230px; min-height: 450px; max-height: 450px")
                self.image.setStyleSheet ("QLabel {max-width: 20000px; min-width: 1230px; min-height: 0px; max-height: 15000px}")
                self.imageButton.setStyleSheet ("QPushButton {max-width: 20000px; min-width: 1230px; min-height: 0px; max-height: 15000px}")
                self.topRow.setStyleSheet ("max-height: 30px; min-height: 30px; min-width: 1230px; max-width: 1230px; background-color: #333333; color: #c1c1c1; font-size: 25px")
                self.topRow.setStyleSheet ("max-height: 30px; min-height: 30px; min-width: 1155px; max-width: 1155px; background-color: #333333; color: #c1c1c1; font-size: 25px")
                
                match element.fit:
                    case "HFit":
                        scaledImage = originalImage.scaledToWidth(1230)
                    case "VFit":
                        scaledImage = originalImage.scaledToHeight(450)
                    case "Scale":
                        scaledImage = originalImage.scaled (QSize (1230, 450))
                    case "Original":
                        scaledImage = originalImage
        self.image.setPixmap (scaledImage)
        self.imageButton.setFixedSize (scaledImage.size())
        self.image.setFixedSize (scaledImage.size())
        


class editButton (QPushButton):
    edit = Signal ()
    def __init__(self):
        super().__init__()
        self.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.setStyleSheet ("QPushButton {max-width: 30px; min-width: 30px; max-height: 50px; min-height: 50px;}")
        self.setIcon (QPixmap(data.filepath ("img/edit.png")))
        self.setIconSize ((QSize(20, 20)))
        self.clicked.connect (self.edit.emit)


class miniEditButton (QPushButton):
    edit = Signal ()
    def __init__(self):
        super().__init__()
        self.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.setStyleSheet ("QPushButton {max-width: 30px; min-width: 30px; max-height: 30px; min-height: 30px;}")
        self.setIcon (QPixmap(data.filepath ("img/edit.png")))
        self.setIconSize ((QSize(15, 15)))
        self.clicked.connect (self.edit.emit)


class miniMoveButton (QGroupBox):
    moved = Signal (int)
    def __init__(self):
        super().__init__()
        self.setStyleSheet ("QGroupBox {max-width: 12px; min-width: 12px; max-height: 30px; min-height: 30px;} QPushButton { max-width: 12px; min-width: 12px; max-height: 15px; min-height: 15px;}")
        self.moveButtonLayout = QVBoxLayout ()
        self.moveButtonLayout.setContentsMargins(0,0,0,0)
        self.moveButtonLayout.setSpacing(0)
        self.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))


        self.moveUp = QPushButton ()
        self.moveUp.setIcon (QPixmap(data.filepath ("img/up.png")))
        self.moveUp.setIconSize ((QSize(7, 7)))
        self.moveUp.clicked.connect (lambda: self.moved.emit(-1))


        self.moveDown = QPushButton ()
        self.moveDown.setIcon (QPixmap(data.filepath ("img/down.png")))
        self.moveDown.setIconSize ((QSize(7, 7)))
        self.moveDown.clicked.connect (lambda: self.moved.emit(1))

        self.moveButtonLayout.addWidget (self.moveUp)
        self.moveButtonLayout.addWidget (self.moveDown)
        self.setLayout (self.moveButtonLayout)

class moveButton (QGroupBox):
    moved = Signal (int)
    def __init__(self):
        super().__init__()
        self.setStyleSheet ("QGroupBox {max-width: 20px; min-width: 20px; max-height: 50px; min-height: 50px;} QPushButton {max-width: 20px; min-width: 20px; max-height: 25px; min-height: 25px;}")
        self.moveButtonLayout = QVBoxLayout ()
        self.moveButtonLayout.setContentsMargins(0,0,0,0)
        self.moveButtonLayout.setSpacing(0)
        self.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))


        self.moveUp = QPushButton ()
        self.moveUp.setIcon (QPixmap(data.filepath ("img/up.png")))
        self.moveUp.setIconSize ((QSize(12, 12)))
        self.moveUp.clicked.connect (lambda: self.moved.emit(-1))


        self.moveDown = QPushButton ()
        self.moveDown.setIcon (QPixmap(data.filepath ("img/down.png")))
        self.moveDown.setIconSize ((QSize(12, 12)))
        self.moveDown.clicked.connect (lambda: self.moved.emit(1))

        self.moveButtonLayout.addWidget (self.moveUp)
        self.moveButtonLayout.addWidget (self.moveDown)
        self.setLayout (self.moveButtonLayout)



class sizeButton (QGroupBox):
    sizeChange = Signal (int)
    def __init__(self):
        super().__init__()
        self.setStyleSheet ("QGroupBox {max-width: 20px; min-width: 20px; max-height: 50px; min-height: 50px;} QPushButton {max-width: 20px; min-width: 20px; max-height: 25px; min-height: 25px;}")
        self.sizeButtonLayout = QVBoxLayout ()
        self.sizeButtonLayout.setContentsMargins(0,0,0,0)
        self.sizeButtonLayout.setSpacing(0)
        self.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.bigger = QPushButton ()
        self.bigger.setIcon (QPixmap(data.filepath ("img/plus.png")))
        self.bigger.setIconSize ((QSize(12, 12)))
        self.bigger.clicked.connect (lambda: self.sizeChange.emit(1))


        self.smaller = QPushButton ()
        self.smaller.setIcon (QPixmap(data.filepath ("img/minus.png")))
        self.smaller.setIconSize ((QSize(12, 2)))
        self.smaller.clicked.connect (lambda: self.sizeChange.emit(-1))

        self.sizeButtonLayout.addWidget (self.bigger)
        self.sizeButtonLayout.addWidget (self.smaller)
        self.setLayout (self.sizeButtonLayout)