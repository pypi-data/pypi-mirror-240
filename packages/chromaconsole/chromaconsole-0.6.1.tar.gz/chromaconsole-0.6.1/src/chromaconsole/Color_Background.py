from .chromaconsole import enabled

class Background:
    @staticmethod
    def black():
        if enabled:
            return "\033[40m"
        else:
            return ""
        
    @staticmethod
    def red():
        if enabled:
            return "\033[41m"
        else:
            return ""
        
    @staticmethod
    def green():
        if enabled:
            return "\033[42m"
        else:
            return ""
        
    @staticmethod
    def yellow():
        if enabled:
            return "\033[43m"
        else:
            return ""
        
    @staticmethod
    def blue():
        if enabled:
            return "\033[44m"
        else:
            return ""
        
    @staticmethod
    def magenta():
        if enabled:
            return "\033[45m"
        else:
            return ""
        
    @staticmethod
    def cyan():
        if enabled:
            return "\033[46m"
        else:
            return ""
    
    @staticmethod
    def white():
        if enabled:
            return "\033[47m"
        else:
            return ""
        
    @staticmethod
    def br_black():
        if enabled:
            return "\033[100m"
        else:
            return ""
        
    @staticmethod
    def br_red():
        if enabled:
            return "\033[101m"
        else:
            return ""
        
    @staticmethod
    def br_green():
        if enabled:
            return "\033[102m"
        else:
            return ""
        
    @staticmethod
    def br_yellow():
        if enabled:
            return "\033[103m"
        else:
            return ""
        
    @staticmethod
    def br_blue():
        if enabled:
            return "\033[104m"
        else:
            return ""
        
    @staticmethod
    def br_magenta():
        if enabled:
            return "\033[105m"
        else:
            return ""
        
    @staticmethod
    def br_cyan():
        if enabled:
            return "\033[106m"
        else:
            return ""
    
    @staticmethod
    def br_white():
        if enabled:
            return "\033[107m"
        else:
            return ""