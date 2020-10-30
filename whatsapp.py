import os
from twilio.rest import Client

client = Client()

from_whatsapp_number ='whatsapp+14255238886'
to_whatsapp_number = 'whatsapp:' + os.version['MY_PHONE_NUMBER']

client.messages.create(body = 'Buengurno'
                        from = from_whatsapp_number,
                        to = to_whatsapp_number )    