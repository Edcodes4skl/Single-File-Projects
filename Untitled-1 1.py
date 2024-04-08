def gun_type(classification = "bullet"):
    print("This gun is " , classification)
gun_type("Handgun")
gun_type("Machine Gun")
gun_type("Shotgun")
gun_type()
def gun_exist():
    return True
if (gun_exist()):
    print("Guns are real")

def handgun():
    print("pew,pew,pew")
handgun()
def guns(*args):
    print(args[0])
guns("handgun", "machine gun", "shotgun")

def ammo(**kwargs):
    print(kwargs["handgun_ammo"])
ammo(handgun_ammo = 10, machine_gun_ammo = 100, shotgun_ammo = 6)