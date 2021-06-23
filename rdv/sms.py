from twilio.rest import Client
#from rdv.models import form

"""  def __str__(self):
           return str(self.date_rdv)
     def save(self, *args, **kwarg):
        if self.date_rdv == {date_rdv -1}: """

def send_sms(): 
    account_sid ="ACbc0fdde455335f94a26c110a89ef1d5b"
    auth_token = "d71791a6a9b22f0cce673e571c7aa91a"

    client = Client(account_sid, auth_token)

    client.api.account.messages.create(
       #  to=f"form.cleaned_data['telephone']",
        to="+221775235100",
        from_="+19034800294",
        body='you are sucessfully register ')
        # return  super().save(*args, ** kwarg)
print('message send successfully')
