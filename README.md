# home-alarm
home-alarm project is just a home project which offers a basic home alarm system. This project runs in a raspberry pi 3 interconnected with some sensors using proper GPIO connector/adapter. 
## Main idea
The main idea is that we have a "master" device which enables/disables the alarm whenever its disconnected/connect in LAN respectively. So when "master" device is out, the system is armed and polls available sensors. Our main hypothesis behind this is that the master device takes constantly the same IP address. So in order to clarify whether device is connected or not we use <code>ping</code> command to this specific (leased) ip address which belongs to our local network (LAN). WARNING: this is completely insecure. Instead of that we have to implement a technique which checks at least the mac address of "master" device.
If any event is raised then it triggers alarm and sends email to the alarm owner with further information. In current version no siren is available so we just receive an email.

#### Language
* Python

#### Hardware used
* GPIO adapter (around 2-8EUR)
* pir sensor (around 2EUR per piece)
* magnetic swithces (around 4EUR for 5-6 pieces)
* simple cable (i used some old ones with efficient enough armor)

##### Execute
You have just to run switches.py with:
<code>py your/project/path/switches.py</code>
