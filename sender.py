import os
from dotenv import load_dotenv
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

load_dotenv()

SENDGRID_API_KEY = os.environ.get("SENDGRID_API_KEY", "OOPS, please set env var called 'SENDGRID_API_KEY'")
MY_ADDRESS = os.environ.get("MY_EMAIL_ADDRESS", "OOPS, please set env var called 'MY_EMAIL_ADDRESS'")

client = SendGridAPIClient(SENDGRID_API_KEY) #> <class 'sendgrid.sendgrid.SendGridAPIClient>
print("CLIENT:", type(client))

subject = "Your Receipt from the Green Grocery Store"

html_content = "Hello World"
#
# or maybe ...
#html_content = "Hello <strong>World</strong>"
#
# or maybe ...
#html_list_items = "<li>You ordered: Product 1</li>"
#html_list_items += "<li>You ordered: Product 2</li>"
#html_list_items += "<li>You ordered: Product 3</li>"
#html_content = f"""
#<h3>Hello this is your receipt</h3>
#<p>Date: ____________</p>
#<ol>
#    {html_list_items}
#</ol>
#"""
print("HTML:", html_content)

message = Mail(from_email=MY_ADDRESS, to_emails=MY_ADDRESS, subject=subject, html_content=html_content)

try:
    response = client.send(message)

    print("RESPONSE:", type(response)) #> <class 'python_http_client.client.Response'>
    print(response.status_code) #> 202 indicates SUCCESS
    print(response.body)
    print(response.headers)

except Exception as e:
    print("OOPS", e.message)