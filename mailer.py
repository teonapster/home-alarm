#author teonapster@gmail.com

import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

#Mail sender class allows you to send custom messages from given account - Here i am using gmail account
class MailSender:

	mailFrom = "youremailhere@gmail.com"
	mailPassword = "yourveryVeryLongPasswordHere"
	
	def sendMail(self,mailTo,subject,body):
		msg = MIMEMultipart()
		msg['From'] = self.mailFrom
		msg['To'] = mailTo
		msg['Subject'] = subject
		msg.attach(MIMEText(body, 'plain'))
		server = smtplib.SMTP('smtp.gmail.com', 587)
		server.starttls()
		server.login(self.mailFrom,self.mailPassword)
		text = msg.as_string()
		server.sendmail(self.mailFrom, mailTo, text)
		server.quit()
