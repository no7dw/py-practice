class Displayer():
    def display(self, message):
        print(message)
class LoggerMixin():
    def log(self, message, filename='logfile.txt'):
        message ='\n' + message
        with open(filename, 'a') as fh:
            fh.write(message)
    def display(self, message):
        super().display(message)
        self.log(message)
class MySubClass(LoggerMixin, Displayer):
    def log(self, message):
        super().log(message, filename='subclasslog.txt')
class MySubClass2(Displayer, LoggerMixin):
    def log(self, message):
        super().log(message, filename='subclasslog.txt')
subclass = MySubClass()
subclass.display("This string will be shown and logged in subclasslog.txt")
subclass2 = MySubClass2()
subclass2.display("This string will be shown in stdout print")
