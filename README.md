Sends a dad joke whenever you want

Pulls from an API and uses most carrier's feature where an email to number@domain will text your phone.

I use windows task scheduler to run dadjoke.bat every day at noon, which will in turn run Dadjoke_oneshot. I recommend making a gmail account (it is important to turn access for less secure apps ON). Give the script your username and password, and also give it the emails associate with MMS servicing for your phone (you can google this, it will be your phone number + some domain specific to your carrier).

DadJoke.py can be used if you want the script to run constantly and send at a certain time instead of using task scheduler.