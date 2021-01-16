import pandas as p
import smtplib as sm
from email.mime.multipart import MIMEMultipart
from email.mime.text import  MIMEText


data = p.read_excel("bro.xlsx")
#print(type(data))
email_col = data.get("email")
list_of_email = list(email_col)
print(list_of_email)


try:
    server = sm.SMTP("smtp.hostinger.in", 587)
    server.starttls()
    server.login("ashutosh@bunkinfotech.in","Abcd@1234")
    from_ = "ashutosh@bunkinfotech.in"
    to_ = list_of_email
    message = MIMEMultipart("alternative")
    message['Subject']="@ashutosh working ststus"
    message["from"]="ashutosh@bunkinfotech.in"

    html = '''

        <html>

        <head>
        </head>

            <body>
                <h4>12/01/2021</h4>
                <h1>my working status of 12/01/2021</h1>
                <h2>start learning of web API creations</h2>
                <h3>
                <ul>
                    <li>introduction of API</li>
                    <li>types of Api</li>
                    <li>how to use API</li>
                    <li>What is web API</li>
                    <li>how to use web API</li>
                    <li>what is REST API</li>
                    <li>how to use REST API</li>

                </ul>
            </h3>
            <br>
            <br>
            <h1>my working status of 13/01/2021</h1>
            <h3>
                <ul>
                    <li>what is CRUD operation (REST API)</li>
                    <li>take a example of student API resource</li>
                    <li>how request and response work</li>
                    <li>how to use GET REQUESTSE and RESPONSE </li>
                    <li>how to use POST REQUESTSE and RESPONSE </li>
                    <li>how to use PUT REQUESTSE and RESPONSE </li>
                    <li>how to use DELETE REQUESTSE and RESPONSE </li>
                    <br>
                    <li>intro of REST API SERIALIZER </li>
                    <li>REST API SERIALIZER DUMPS AND LOADS methods</li>
                    <li>intro of REST API SERIALIZER CLASS </li>

                    <br>
                    <br>
                </ul>
            </h3>
            <h3>by the evining of the day i make a automation bulk email sending app by PYTHON  </h3>
            <h2>thank you</h2>
            <h2>your reliable</h2>
            <h2>ASHUTOSH KUAMR</h2>
            



            </body>

            </html>
            ''' 

    text = MIMEText(html,"html")
    message.attach(text)

    server.sendmail(from_, to_, message.as_string())
    print("successfully send")
except Exception as e:
    print(e)