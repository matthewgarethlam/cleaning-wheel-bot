import pywhatkit


#definitions
imagepath = "/Users/matthewlam/Documents/GitHub/cleaning-wheel-bot/178parkhillcleaning/wheel4.jpg"
caption= "*Hello, here is the cleaning wheel for this week! Happy Cleaning! :)*                                                    _This is an automated message from Matthew's Cleaning Bot_"
group_id = "EgntfnQHwRYASbeQAzhpwL"

pywhatkit.sendwhats_image(group_id, imagepath, caption)
