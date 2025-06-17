import smtplib
try:
    server = smtplib.SMTP("smtp.gmail.com",port=587)
    server.starttls()

    ##receiver email
    receiver_mail = input("Enter the receiver email : ")

    ##mail credentials
    sender_email = "jaikrishan2001@gmail.com"
    password =  "wtar dlxx gwpn jfmx"

    ##login 
    server.login(sender_email,password)

    ##sending email
    subject = input("Enter the subject : ")
    body = input("Enter the body : ")
    message = f"Subject : {subject} \n\n {body}"
    server.sendmail(sender_email,receiver_mail,message)
    print("mail sent successfully")

    server.quit()
except Exception as e:
    print("An Error occured",e)