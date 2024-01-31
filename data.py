from libaries import *

t = os.path.dirname(__file__)
def filepath (path):
    return (os.path.join(t, path))



mode = "normal"

path = []


def getPathString ():

    returnVar = ["", ""]
    parentPath = []
    for number in path:
        parentPath.append (number)
    
    
    if path.__len__() >= 2:
        parentPath.pop ()
        if getElement (parentPath).type == "group" or getElement (parentPath).type == "timeline":
            parentPath.pop ()
        targetPath = [getElement (parentPath), getElement (path)]
        returnVar[0] = "... " + targetPath[0].name
        returnVar[1] = " > " + targetPath[1].name
        
    elif path.__len__() == 1:
        parentPath.pop ()
        targetPath = [getElement (parentPath), getElement (path)]
        returnVar[0] = targetPath[0].name
        returnVar[1] = " > " + targetPath[1].name
    else:
        returnVar[0] = notes.name
 
    return (returnVar)
    

def getCurrentPath (item, elements, path):
    returnVar = []
    for i in path:
        returnVar.append (i)
    returnVar.append(elements.index(item))
    return (returnVar)


def getElement (path):
    returnVar = notes
    for i in path:
        returnVar = returnVar.subelement[i]
    return (returnVar)

def getElementType (path):
    thing = getElement (path)
    match thing.type:
        case "element":
            return ("element")
        case "title":
            return ("title")
        case "imageH":
            return ("image")
        case "subject":
            return ("subject")
        case "unit":
            return ("unit")
        case "imageV":
            return ("image")

class data:
    def __init__(self, **kwargs):
        try:
            self.name = kwargs["name"]
        except:
            self.name = "untitled"
        if self.name == "":
            self.name = "untitled"

        try:
            self.flavour = kwargs["flavour"]
        except:
            self.flavour = ""

        try:
            self.desc = kwargs["desc"]
        except:
            self.desc = ""

        try:
            self.type = kwargs["type"]
        except:
            self.type = "element"
        
        try:
            self.size = kwargs["size"]
        except:
            self.size = 1

        try:
            self.img = kwargs["img"]
        except:
            self.img = "none"
        
        try:
            self.layout = kwargs["layout"]
        except:
            self.layout = "none"

        try:
            self.fit = kwargs["fit"]
        except:
            self.fit = "none"

        self.subelement = []
        
    def edit (self, **kwargs):
        try:
            
            self.name = kwargs["name"]
        except:
            pass

        try:
            
            self.flavour = kwargs["flavour"]
        except:
            pass

        try:
            
            self.desc = kwargs["desc"]
        except:
            pass
        
        try:
            self.size = kwargs["size"]
        except:
            pass
            
        try:
            self.img = kwargs["img"]
        except:
            pass
        
        try:
            self.layout = kwargs["layout"]
        except:
            pass

        try:
            self.fit = kwargs["fit"]
        except:
            pass

        try:
            self.type = kwargs["type"]
        except:
            pass


def save ():
    file = open(filepath("data.pkl"), 'wb')
    pickle.dump (notes, file)
    file.close ()
    print ("saved")

#save ()

def loadData ():
    global notes
    try:
        file = open(filepath("data.pkl"), 'rb')
        savedFile = pickle.load (file)
        notes = savedFile
        file.close ()
    except:
        notes = data(type = "home", name = "The Note Taker", desc = "Na", size = 1, subelement = [])


loadData()

def blankFunction ():
    return (0)

currentDisplay = notes

def updateCurrentDisplay ():
    global currentDisplay
    newDisplay = notes
    
    for index in path:
        #print ("pathed")
        newDisplay = newDisplay.subelement[index]
    currentDisplay = newDisplay


    
def changeElementSize (size, index):
    target = notes
    for i in index:
        target = target.subelement[i]
    target.size += size
    if target.size > 3:
        target.size = 1
    elif target.size < 1:
        target.size = 3
    updateCurrentDisplay ()

def moveElement (direction, index):

    targetParent = notes

    parentIndex = index
    targetIndex = index[-1]

    parentIndex.pop()

    #print (targetIndex+direction)

    for i in parentIndex:
        targetParent = targetParent.subelement[i]

    if targetIndex+direction >= 0 and targetIndex+direction < targetParent.subelement.__len__():

        targetParent.subelement.insert(targetIndex+direction, targetParent.subelement.pop(targetIndex))

    updateCurrentDisplay ()
    
def deleteElement (index):
    print (index)
    targetParent = notes

    parentIndex = index
    targetIndex = index[-1]

    parentIndex.pop()
    
    for i in parentIndex:
        targetParent = targetParent.subelement[i]
    print (targetParent.subelement[targetIndex].subelement)

    maxI = targetParent.subelement[targetIndex].subelement.__len__()-1
    i = 0
    while i<maxI+1:
        newIndex = []
        for j in parentIndex:
            newIndex.append (j)
        newIndex.append (targetIndex)
        newIndex.append (maxI-i)
        deleteElement (newIndex)
        i+= 1

    if targetParent.subelement[targetIndex].img != "none":
        try:
            if os.path.exists (filepath (targetParent.subelement[targetIndex].img)):
                os.remove (filepath (targetParent.subelement[targetIndex].img))
            else:
                pass
        except:
            pass

    del targetParent.subelement[targetIndex]
    
    updateCurrentDisplay ()

def editElement (index, info):
    target = notes
    for i in index:
        target = target.subelement[i]
    target.edit (**info)
    updateCurrentDisplay ()

def addElement (index, info):
    #print ("add")
    target = notes
    for i in index:
        target = target.subelement[i]
    #print (target.subelement)
    target.subelement.append (data(**info))
    #print (target.subelement)
    updateCurrentDisplay ()


#testing
#save ()
#loadData ()