class TVClass:  # Base class TVClass 
    def __init__(self, brand):   # Constructor method to set the objects
        self.brand = brand
        self.channel = 1 
        self.price = 0  
        self.inches = 0
        self.on_off = False
        self.volume = 50

    def increase_volume(self): # Increase volume function method
        if self.volume < 100:
            self.volume += 1
        else:
            self.display("Volume is already at maximum.")

    def decrease_volume(self):  # Decrease volume function method
        if self.volume > 0:
            self.volume -= 1
        else:
            self.display("Volume is already at minimum.")

    def set_channel(self, channel):  # Set chanel(0 - 50) function method 
        if 1 <= channel <= 50:
            self.channel = channel
        else:
            self.display("Invalid channel. The TV has only 50 channels.") 

    def reset_tv(self):    # Method to reset TV Channel 1 and Volume 50
        self.channel = 1
        self.volume = 50

    def get_status(self):   #Getting the status of the TV Brand at Channel ?, volume at ?
        return f"{self.brand} at channel {self.channel}, volume {self.volume}"

    def display(self, message):
        print(message)


class LedTV(TVClass):  # Sub class LedTV function inheritance of TVClass
    def __init__(self, brand, screen_thickness, energy_usage, lifespan, refresh_rate):  # Adding TV details in Part - B
        super().__init__(brand)
        self.screen_thickness = screen_thickness
        self.energy_usage = energy_usage
        self.lifespan = lifespan
        self.refresh_rate = refresh_rate
        self.viewing_angle = 0  
        self.backlight = False

    def display_details(self):
        details = f"{self.brand} LED TV - Screen Thickness: {self.screen_thickness} inches, " \
                  f"Energy Usage: {self.energy_usage}, Lifespan: {self.lifespan} years, " \
                  f"Refresh Rate: {self.refresh_rate} Hz, Viewing Angle: {self.viewing_angle}, " \
                  f"Backlight: {'On' if self.backlight else 'Off'}"
        self.display(details)


class PlasmaTV(TVClass): # Sub class Plasma TV function inheritance of TVClass
    def __init__(self, brand, screen_thickness, energy_usage, lifespan, refresh_rate):
        super().__init__(brand)
        self.screen_thickness = screen_thickness
        self.energy_usage = energy_usage
        self.lifespan = lifespan
        self.refresh_rate = refresh_rate
        self.viewing_angle = 0  
        self.backlight = False  

    def display_details(self):
        details = f"{self.brand} Plasma TV - Screen Thickness: {self.screen_thickness} inches, " \
                  f"Energy Usage: {self.energy_usage}, Lifespan: {self.lifespan} years, " \
                  f"Refresh Rate: {self.refresh_rate} Hz, Viewing Angle: {self.viewing_angle}, " \
                  f"Backlight: {'On' if self.backlight else 'Off'}"
        self.display(details)


# Example Usage:
led_tv = LedTV("Panasonic", 3, "Low", 5, 120,)
led_tv.display(led_tv.get_status())  # Output: "Panasonic at channel 1, volume 50"
led_tv.increase_volume()    # adding 1 volume
led_tv.set_channel(8)       # Set the channel at 8
led_tv.display(led_tv.get_status())  # Output: "Panasonic at channel 8, volume 51"
led_tv.display_details()  # Output: Details of the LED TV

plasma_tv = PlasmaTV("Samsung", 1.5, "Medium", 6, 90)
plasma_tv.display(plasma_tv.get_status())  # Output: "Samsung at channel 1, volume 50"
plasma_tv.decrease_volume()  # Decrease 1 volume
plasma_tv.set_channel(60)    # Set the channel at 60
plasma_tv.display(plasma_tv.get_status())  # Output: "Samsung at channel 1, volume 49"
plasma_tv.display_details()  # Output: Details of the Plasma TV
