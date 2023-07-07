import pywhatkit


#definitions
imagepath = "/Users/matthewlam/Documents/GitHub/cleaning-wheel-bot/178parkhillcleaning/wheel1.jpg"
caption= "Hello, here is cleaning wheel for this week! :)           This is an automated message from Matthew's Cleaning Bot"
group_id = "EgntfnQHwRYASbeQAzhpwL"

pywhatkit.sendwhats_image(group_id, imagepath, caption)
