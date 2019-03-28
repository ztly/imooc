import configparser


class ReadConfig:
    def __init__(self, filename=None, node=None):
        if filename is None:
            filename ='/Users/edz/Documents/VS_Code/SeleniumPython/config/LocalElement.ini'
        if node == None:
            self.node = 'element'
        else:
            self.node = node
        self.data = self.load_ini(filename)
        

    def load_ini(self, filename):
        parse = configparser.ConfigParser()
        parse.read(filename)
        return parse

    def get_data(self, key):
        element = self.data.get(self.node, key)
        return element


'''if __name__ == "__main__":
    filename = '/Users/edz/Documents/VS_Code/imooc/config/LocalElement.ini'
    paser = ReadConfig(filename)
    mail = paser.get_data('username')
    print(mail)'''

