import StudentCode

def test_countByKeyword1():
    filename = "interceptedMessages.txt"
    keyword = "stardust"
    assert StudentCode.countByKeyword(filename, keyword) == 245
    
def test_countByKeyword2():
    filename = "interceptedMessages.txt"
    keyword = "radio"
    assert StudentCode.countByKeyword(filename, keyword) == 29

def test_countByKeyword3():
    filename = "interceptedMessages.txt"
    keyword = "urgent"
    assert StudentCode.countByKeyword(filename, keyword) == 108
    
def test_countBySender1():
    filename = "interceptedMessages.txt"
    sender = "Stardust"
    assert StudentCode.countBySender(filename, sender) == 57

def test_countBySender2():
    filename = "interceptedMessages.txt"
    sender = "Krennic1"
    assert StudentCode.countBySender(filename, sender) == 60

def test_countBySender3():
    filename = "interceptedMessages.txt"
    sender = "Tarkin01"
    assert StudentCode.countBySender(filename, sender) == 57

def test_countByReceiver1():
    filename = "interceptedMessages.txt"
    receiver = "Stardust"
    assert StudentCode.countByReceiver(filename, receiver) == 39

def test_countByReceiver2():
    filename = "interceptedMessages.txt"
    receiver = "Krennic1"
    assert StudentCode.countByReceiver(filename, receiver) == 60

def test_countByReceiver3():
    filename = "interceptedMessages.txt"
    receiver = "Tarkin01"
    assert StudentCode.countByReceiver(filename, receiver) == 74

def test_getMessageByID1():
    filename = "interceptedMessages.txt"
    id = "70360314"
    assert StudentCode.getMessageByID(filename, id) == "Lighthearted note: The cafeteria droids are still terrible cooks."

def test_getMessageByID2():
    filename = "interceptedMessages.txt"
    id = "78920329"
    assert StudentCode.getMessageByID(filename, id) == "Encrypted directive: Resource allocation to Eadu confirmed."

def test_getMessageByID3():
    filename = "interceptedMessages.txt"
    id = "14170814"
    assert StudentCode.getMessageByID(filename, id) == "Encrypted update: Stardust nearing completion. Security is paramount."

def test_getIDByMessage():
    filename = "interceptedMessages.txt"
    message = "I have friends everywhere."
    assert StudentCode.getIDByMessage(filename, message) == "94031003"
