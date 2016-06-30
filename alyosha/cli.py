from cmd import Cmd
from log import output

class CLI(Cmd):
    
    prompt = "alyosha>"   
    intro = "======== alyosha CLI ======="

    def __init__(self):

        Cmd.__init__(self)

    def do_alyosha(self, arg):
        output("alyosha1879")

    def do_test(self, arg):
        output("test")

    def do_quit(self, arg):
        return True;

    def do_sample(self, arg):
        # do sometihg 
        pass
