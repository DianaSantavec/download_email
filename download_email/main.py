import imaplib
import base64
import os
import email

email_address = "diana.santavec@gmail.com"
password = "dianamail2"
smtp_server = "imap.gmail.com"
smtp_port = 993

try:
    mail = imaplib.IMAP4_SSL(smtp_server,smtp_port)
    mail.login(email_address,password)


#select inbox
    mail.select('inbox',True)
    type, data = mail.search(None, '(FROM "noreply@discordapp.com")')
    mail_ids = data[0]
    id_list = mail_ids.split()
    
    for num in data[0].split():
        typ, data = mail.fetch(num, '(RFC822)' )
        raw_email = data[0][1]
        raw_email_string = raw_email.decode('utf-8')
        email_message = email.message_from_string(raw_email_string)

        print (email_message)
        

    # ids = data[0] # data is a list.
    # id_list = ids.split() # ids is a space separated string
    
    # latest_email_id = id_list[-1] # get the latest

    # result, data = mail.fetch(latest_email_id, "(RFC822)") # fetch the email body (RFC822)             for the given ID

    # raw_email = data[0][1]
    #print (raw_email)

except Exception as e:
    print (str(e))

#mail_ids = data[0]
#id_list = mail_ids.split()
#first_email_id = int(id_list[0])
#latest_email_id = int(id_list[-1])

#for i in range(latest_email_id,first_email_id, -1):
#            typ, data = mail.fetch(i, '(RFC822)' )

            #for response_part in data:
             #   if isinstance(response_part, tuple):
              #      msg = email.message_from_string(response_part[1])
               #     email_subject = msg['subject']
                #    email_from = msg['from']
                 #   print ('From : ' + email_from + '\n')
                  #  print ('Subject : ' + email_subject + '\n')
#
#def read_email():
 #   print ("bla")