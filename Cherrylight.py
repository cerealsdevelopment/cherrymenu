import sys
import os
# Main Routine
def menua():
    print("\n  ========_________________________!!!!!!!!!!!!!!!__________________========\n")
    print("\n	                     _=! Cherry Trail Menu !=_\n")
    print("                        Happily brought to you by the cereals_development")
    print("                        https://github.com/cerealsdevelopment")
    print("\n ------ Set the Correct Brightness: ------\n")
    print("1. Set the Screen Brightness")
    print("\n ------ DNF Commands: ------ \n")
    print("2. Update System without Kernel")
    print("\n ------ System Features: ------\n")
    print("3. Reboot")
    print("4. Force shutdown")
    print("5. Exit the app")
    print("\n----------------------------------------------------------------------\n")

def menubrightness():
    print("\n ------ Input the Brightness------\n")
    print("1. Set at 10%")
    print("2. Set at 25%")
    print("3. Set at 50%")
    print("4. Set at 75%")
    print("5. Set at 100%")
    print("6. Go back Main Menu\n")

def backlightfunction():
    os.system('sudo sh -c "echo 10 >/sys/class/backlight/intel_backlight/brightness"')
def backlightfunction1():
    os.system('sudo sh -c "echo 25 >/sys/class/backlight/intel_backlight/brightness"')
def backlightfunction2():
    os.system('sudo sh -c "echo 50 >/sys/class/backlight/intel_backlight/brightness"')
def backlightfunction3():
    os.system('sudo sh -c "echo 75 >/sys/class/backlight/intel_backlight/brightness"')
def backlightfunction4():
    os.system('sudo sh -c "echo 100 >/sys/class/backlight/intel_backlight/brightness"')

def rebootsystem():
    os.system('reboot')

def dnfupdatenokernel():
    os.system('sudo dnf update --exclude kernel*')

def hellshutdown():
    os.system('shutdown -h now')

## Text menu in Python

menua()
loop = True

while loop:  ## main loop
    choice = input("Enter your choice [1-5]: ")
    choice = int(choice)

    if choice == 1:
        print("\n--- Set Brightness: ---\n")
        menubrightness()
        loop1 = True

        while loop1:  ## While loop for the submenu of Brightness

            choice1 = input("Enter your choice [1-6]: ")
            choice1 = int(choice1)
            if choice1 == 1:
                print("\n- 10% Brightness -\n")
                backlightfunction()
                menubrightness()
            if choice1 == 2:
                print("\n- 25% Brightness -\n")
                backlightfunction1()
                menubrightness()
            if choice1 == 3:
                print("\n- 50% Brightness -\n")
                backlightfunction2()
                menubrightness()
            if choice1 == 4:
                print("\n- 75% Brightness -\n")
                backlightfunction3()
                menubrightness()
            if choice1 == 5:
                print("\n- 100% Brightness -\n")
                backlightfunction4()
                menubrightness()
            if choice1 == 6:
                print("\nLet's go back to the previous menu%\n")
                menua()
                break
        else:
            break


    elif choice == 2:
        print("\n- @@ Let's Update the system without updating kernel @@ -\n")
        dnfupdatenokernel()

    elif choice == 3:
        print("\n- # Hey Oh! Let's Reboot # -\n")
        rebootsystem()

    elif choice == 4:
        print("\n- !!!Your system is going down!!! -\n")
        hellshutdown()

    elif choice == 5:
        print("\n- Bye bye Cherry friend -\n")
        exit()

loop = false

