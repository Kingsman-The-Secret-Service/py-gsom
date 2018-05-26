import Gsom from gsom

class Migrate(Gsom):
    def __init__(self):
        super(Migrate, self).__init__()

class Database(Migrate):
    def __init__(self):
        super(Database, self).__init__()

    def create(self):
        pass
    
    def read(self):
        pass
    
    def update(self):
        pass
    
    def delete(self):
        pass

class Table(Migrate):
    def __init__(self):
        super(Table, self).__init__()

    def create(self):
        pass
    
    def read(self):
        pass
    
    def update(self):
        pass
    
    def delete(self):
        pass

class Schema(Table):
    def __init__(self):
        super(Schema, self).__init__()
    
    def create(self):
        pass
    
    def read(self):
        pass
    
    def update(self):
        pass
    
    def delete(self):
        pass
