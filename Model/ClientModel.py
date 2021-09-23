
class Client:
    __computerName    = ""
    __ipAddress       = ""
    __macAddress      = ""
    __remark          = ""
    __windowsAccount  = ""
    __group           = ""
    __connectTime     = ""
    __status          = ""

    def __init__(self,computerName,ipAddress,macAddress,remark,windowsAccount,group,connectTime,status):
        self.__computerName = computerName
        self.__ipAddress = ipAddress
        self.__macAddress = macAddress
        self.__remark = remark
        self.__windowsAccount = windowsAccount
        self.__group = group
        self.__connectTime = connectTime
        self.__status = status
    
    def get_computerName(self):
        return self.__computerName
    def set_computerName(self,computerName):
        self.__computerName = computerName
    
    def get_ipAddress(self):
        return self.__ipAddress
    def set_ipAddress(self,ipAddress):
        self.__ipAddress = ipAddress
    
    def get_macAddress(self):
        return self.__macAddress
    def set_macAddress(self,macAddress):
        self.__macAddress = macAddress
    
    def get_remark(self):
        return self.__remark
    def set_remark(self,remark):
        self.__remark = remark

    def get_windowsAccount(self):
        return self.__windowsAccount
    def set_windowsAccount(self,windowsAccount):
        self.__windowsAccount = windowsAccount
    
    def get_group(self):
        return self.__group
    def set_group(self,group):
        self.__group = group
    
    def get_connectTime(self):
        return self.__connectTime
    def set_connectTime(self,connectTime):
        self.__connectTime = connectTime
    
    def get_status(self):
        return self.__status
    def set_status(self,stauts):
        self.__status = stauts

    
    