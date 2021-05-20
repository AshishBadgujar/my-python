import time
from plyer import notification
import os

# os.chdir(r"D:\MY COADING\python tut\python projects\drinkWater.py")

if __name__=="__main__":
        notification.notify(
            title='Please drink water',
            message="hey ashish Please drink water its about 1 hour since you have drinked it",
            timeout=10
        )