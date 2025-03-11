class Config:
    empty_dict = {}

    @staticmethod
    def set_setting(key,value):
        Config.empty_dict[key] = value
    
    @staticmethod
    def get_setting(key):
        return Config.empty_dict[key]
    
    def show_settings():
        print(Config.empty_dict)
    
Config.set_setting("theme", "dark")
Config.set_setting("volume", 75)
print(Config.get_setting("theme")) # Output: dark
Config.show_settings()