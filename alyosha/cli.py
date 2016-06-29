from cmd import Cmd

class CLI(Cmd):
    
    prompt = "alyosha>"   

    def __init__(self):

        Cmd.__init__(self)
        self.run()

    def run(self):
        while True:        
            self.cmdloop()
