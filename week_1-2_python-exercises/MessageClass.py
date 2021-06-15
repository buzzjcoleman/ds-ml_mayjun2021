# Create the Message class
class Message:

    customerName = ""
    helloMessage = "Hello and welcome,"
    byeMessage = "Thank you and goodbye,"

    def __init__(self, name):
        self.customerName = name
    
    def sayHello(self):
        print(self.helloMessage, self.customerName)

    def sayGoodbye(self):
        print(self.byeMessage, self.customerName)

# Instaniate the Message
newMessage = Message("John Doe")
newMessage.sayHello()
newMessage.sayGoodbye()