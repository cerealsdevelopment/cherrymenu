import sys
import os
## Menu
print("\n  ========_________________________!!!!!!!!!!!!!!!__________________========\n")
print("\n	                     _=! Cherry Trail Menu !=_\n")
print("                        Happily brought to you by the Cereals Development\n")
print("\n ------ Set the Correct Brightness: ------\n")
print("1. Set at 10%")
print("2. Set at 25%")
print("3. Set at 50%")
print("4. Set at 75%")
print("5. Set at 100%")
print("\n ------ DNF Commands: ------ \n")
print("6. Update System without Kernel")
print("\n ------ System Features: ------\n")
print("7. Reboot")
print("8. Force shutdown")
print("9. Exit the app")
print("\n----------------------------------------------------------------------\n")

## I developed it for Fedora. 

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

## Sometimes I have freezing or slowing issues and cannot access the Gnome buttons correctly
def rebootsystem():
    os.system('reboot')

## Most of the times a kernel gets an update Cherry Trail devices behave differently. 
def dnfupdatenokernel():
    os.system('sudo dnf update --exclude kernel*')
    
## Sometimes I have freezing or slowing issues and cannot access the Gnome buttons correctly
def hellshutdown():
    os.system('shutdown -h now')


loop = True

while loop:  ## While loop which will keep going until loop = False
      ## Displays choice
    choice = input("Enter your choice [1-9]: ")
    choice = int(choice)
    
    if choice == 1:
        print("\nBacklight at 10%\n")
        backlightfunction()
        ## You can add your code or functions here
    elif choice == 2:
        print("\nBacklight at 25%\n")
        backlightfunction1()
        ## You can add your code or functions here
    elif choice == 3:
        print("\nBacklight at 50%\n")
        backlightfunction2()
        ## You can add your code or functions here
    elif choice == 4:
        print("\nBacklight to 75%\n")
        backlightfunction3()
        ## You can add your code or functions here
    elif choice == 5:
        print("\nBacklight to 100%\n")
        backlightfunction4()
    elif choice == 6:
        print("\nYou have chosen to update! It's a good choice not to upgrade kernel if it works for you :)\n")
        dnfupdatenokernel()
    elif choice == 7:
        print("\nYou have chosen to reboot! keep the RAM fresh!\n")
        rebootsystem()
    elif choice == 8:
        print("\nAngry User trying to shutdown the system\n")
        dnfupdatenokernel()
    elif choice == 9:
        print("\nBye bye Cherry friend\n")
        exit()

        loop = false

    else:
        # Any integer inputs other than values 1-9 we print an error message
        raw_input("Wrong option selection. Enter any key to try again..")
