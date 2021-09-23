class Request:
    type = ""
    user = ""
    ipAddress = ""
    content = ""

    def __init__(self,type,user,ipAddress,content):
        self.type = type
        self.user = user
        self.ipAddress = ipAddress
        self.content = content
    
    def get_type(self):
        return self.type
    def set_type(self,type):
        self.type = type

    def get_user(self):
        return self.user
    def set_user(self,user):
        self.user = user

    def get_ipAddress(self):
        return self.ipAddress
    def set_ipAddress(self,ipAddress):
        self.ipAddress = ipAddress

    def get_content(self):
        return self.content
    def set_content(self,content):
        self.content = content