from .chromaconsole import enabled

class Text:
    @staticmethod
    def black():
        if enabled:
            return "\033[30m"
        else:
            return ""
        
    @staticmethod
    def red():
        if enabled:
            return "\033[31m"
        else:
            return ""
        
    @staticmethod
    def green():
        if enabled:
            return "\033[32m"
        else:
            return ""
        
    @staticmethod
    def yellow():
        if enabled:
            return "\033[33m"
        else:
            return ""
        
    @staticmethod
    def blue():
        if enabled:
            return "\033[34m"
        else:
            return ""
        
    @staticmethod
    def magenta():
        if enabled:
            return "\033[35m"
        else:
            return ""
        
    @staticmethod
    def cyan():
        if enabled:
            return "\033[36m"
        else:
            return ""
    
    @staticmethod
    def white():
        if enabled:
            return "\033[37m"
        else:
            return ""
    
    @staticmethod
    def br_black():
        if enabled:
            return "\033[90m"
        else:
            return ""
        
    @staticmethod
    def br_red():
        if enabled:
            return "\033[91m"
        else:
            return ""
        
    @staticmethod
    def br_green():
        if enabled:
            return "\033[92m"
        else:
            return ""
        
    @staticmethod
    def br_yellow():
        if enabled:
            return "\033[93m"
        else:
            return ""
        
    @staticmethod
    def br_blue():
        if enabled:
            return "\033[94m"
        else:
            return ""
        
    @staticmethod
    def br_magenta():
        if enabled:
            return "\033[95m"
        else:
            return ""
        
    @staticmethod
    def br_cyan():
        if enabled:
            return "\033[96m"
        else:
            return ""
    
    @staticmethod
    def br_white():
        if enabled:
            return "\033[97m"
        else:
            return ""