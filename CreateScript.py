import dxIndex

class CreateScript:
    def __init__(self):
        #path and env vars won't change so constants here
        self.PATH = 'PATH=$PATH:  \nexport PATH' #Paths for essential index files
        self.TERM = 'TERMDIR= ' #term dir
        self.LIBSTRING = 'LIBSTRING= ' #enter lib string
        self.EXPORTS = 'export TERMDIR LIBSTRING'
        self.cd = 'cd ' #file path here
        self.run = 'run ' #run path here


    def get_create_script(self,dxroute):
        if dxroute in dxIndex.DXPATHS:
            self.run += dxroute.lower()
            try:
                with open(dxroute + ".sh",'w') as script_file:
                    script_file.write(self.PATH + '\n')
                    script_file.write(self.TERM + '\n')
                    script_file.write(self.LIBSTRING + '\n')
                    script_file.write(self.EXPORTS + '\n')
                    script_file.write(self.cd + '\n')
                    script_file.write(self.run + '\n')
            except:
                print('Script created failed')
            return script_file
        else:
            return 'Script create fail'