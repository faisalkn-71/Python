class Phone:
    brand = "Samsung"
    color = 'Black'
    feature = ['camera', 'speaker', 'hammer']
    price = 19999
    
    def call(self):
        print("Call is calling someone")

    def send_sms(self, phone, sms):
        text = f"Sending SMS to:{phone} ans message is {sms}"
        return text



my_phone = Phone()
print(my_phone.feature)
my_phone.call()
result = my_phone.send_sms(12345, "Missy, I missed to miss you")
print(result)
