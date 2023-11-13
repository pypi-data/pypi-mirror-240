from .chromaconsole import enabled

class Color:
    @staticmethod
    def text(*args): #38;2;r;g;bm
        '''
        changes the color of the text\n
        Color.text(r, g, b)\n
        Color.text("#rrggbb")
        '''
        if enabled:
            if len(args) == 1:
                color = args[0].lstrip("#")
                if len(color) == 3:
                    r, g, b = (int(c * 2, 16) for c in color)
                elif len(color) == 6:
                    r, g, b = (int(color[i:i+2], 16) for i in range(0, 6, 2))
                else:
                    raise ValueError("Invalid color format")
            elif len(args) == 3:
                r, g, b = args
            else:
                raise ValueError("Invalid number of arguments")

            return f"\033[38;2;{r};{g};{b}m"
        else:
            return ""
        
    @staticmethod
    def text_gradient(text, start_color, end_color):
        '''
        this can be used to make text gradient\n
        text_gradient(str, (r,g,b) or "#rrggbb" , (r,g,b) or "#rrggbb")
        '''
        gradient_text = ""

        def interpolate_color(start_color, end_color, factor):
            interpolated_color = tuple(
                int(start + (end - start) * factor)
                for start, end in zip(start_color, end_color)
            )
            return interpolated_color

        def parse_color(color):
            if isinstance(color, str):
                if color.startswith("#"):
                    color = color.lstrip("#")
                if len(color) == 3:
                    color = ''.join(c * 2 for c in color)
                if len(color) != 6:
                    raise ValueError("Invalid color format")
                return (
                    int(color[0:2], 16),
                    int(color[2:4], 16),
                    int(color[4:6], 16)
                )
            return color

        start_color = parse_color(start_color)
        end_color = parse_color(end_color)

        # Compute interpolation steps
        interpolation_step = 1 / (len(text) - 1)
        for i, char in enumerate(text):
            factor = i * interpolation_step
            interpolated_color = interpolate_color(start_color, end_color, factor)
            gradient_text += Color.text(*interpolated_color) + char

        return gradient_text + "\033[39m"
        
    @staticmethod
    def default_text(): #39m
        '''
        Default foreground color\n
        Implementation defined (according to standard)
        '''
        if enabled:
            return "\033[39m"
        else:
            return ""
    
    @staticmethod
    def background(*args): #48;2;r;g;bm
        '''
        changes the color of the text background\n
        Color.background(r, g, b)\n
        Color.background("#rrggbb")
        '''
        if enabled:
            if len(args) == 1:
                color = args[0].lstrip("#")
                if len(color) == 3:
                    r, g, b = (int(c * 2, 16) for c in color)
                elif len(color) == 6:
                    r, g, b = (int(color[i:i+2], 16) for i in range(0, 6, 2))
                else:
                    raise ValueError("Invalid color format")
            elif len(args) == 3:
                r, g, b = args
            else:
                raise ValueError("Invalid number of arguments")

            return f"\033[48;2;{r};{g};{b}m"
        else:
            return ""
        
    @staticmethod
    def background_gradient(text, start_color, end_color):
        '''
        this can be used to make background gradient\n
        background_gradient(str, (r,g,b) or "#rrggbb" , (r,g,b) or "#rrggbb")
        '''
        gradient_text = ""

        def interpolate_color(start_color, end_color, factor):
            interpolated_color = tuple(
                int(start + (end - start) * factor)
                for start, end in zip(start_color, end_color)
            )
            return interpolated_color

        def parse_color(color):
            if isinstance(color, str):
                if color.startswith("#"):
                    color = color.lstrip("#")
                if len(color) == 3:
                    color = ''.join(c * 2 for c in color)
                if len(color) != 6:
                    raise ValueError("Invalid color format")
                return (
                    int(color[0:2], 16),
                    int(color[2:4], 16),
                    int(color[4:6], 16)
                )
            return color

        start_color = parse_color(start_color)
        end_color = parse_color(end_color)

        # Compute interpolation steps
        interpolation_step = 1 / (len(text) - 1)
        for i, char in enumerate(text):
            factor = i * interpolation_step
            interpolated_color = interpolate_color(start_color, end_color, factor)
            gradient_text += Color.background(*interpolated_color) + char

        return gradient_text + "\033[49m"
    
    @staticmethod
    def default_background(): #49m
        '''
        Default background color\n
        Implementation defined (according to standard)
        '''
        if enabled:
            return "\033[49m"
        else:
            return ""
    
    @staticmethod
    def text_black():
        if enabled:
            return "\033[30m"
        else:
            return ""
        
    @staticmethod
    def text_red():
        if enabled:
            return "\033[31m"
        else:
            return ""
        
    @staticmethod
    def text_green():
        if enabled:
            return "\033[32m"
        else:
            return ""
        
    @staticmethod
    def text_yellow():
        if enabled:
            return "\033[33m"
        else:
            return ""
        
    @staticmethod
    def text_blue():
        if enabled:
            return "\033[34m"
        else:
            return ""
        
    @staticmethod
    def text_magenta():
        if enabled:
            return "\033[35m"
        else:
            return ""
        
    @staticmethod
    def text_cyan():
        if enabled:
            return "\033[36m"
        else:
            return ""
    
    @staticmethod
    def text_white():
        if enabled:
            return "\033[37m"
        else:
            return ""
        
    @staticmethod
    def bg_black():
        if enabled:
            return "\033[40m"
        else:
            return ""
        
    @staticmethod
    def bg_red():
        if enabled:
            return "\033[41m"
        else:
            return ""
        
    @staticmethod
    def bg_green():
        if enabled:
            return "\033[42m"
        else:
            return ""
        
    @staticmethod
    def bg_yellow():
        if enabled:
            return "\033[43m"
        else:
            return ""
        
    @staticmethod
    def bg_blue():
        if enabled:
            return "\033[44m"
        else:
            return ""
        
    @staticmethod
    def bg_magenta():
        if enabled:
            return "\033[45m"
        else:
            return ""
        
    @staticmethod
    def bg_cyan():
        if enabled:
            return "\033[46m"
        else:
            return ""
    
    @staticmethod
    def bg_white():
        if enabled:
            return "\033[47m"
        else:
            return ""
