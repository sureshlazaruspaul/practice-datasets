# libraries & dependencies
from send_email import notify_by_email
from list import contact_list

contact_list=contact_list()
print(contact_list)

subject = f"BUS622 grade has been posted."
print(subject)
message = f"Hello All,\n\n"
message += f"The final grade for our course has been posted.\n"
message += f"Have a nice break. Happy Holidays!\n\n"
message += f"PS: email sent for Prof. Suresh Paul, by Python Assistant.\n"
print(message)

notify_by_email(contact_list,subject,message)

logfile = "https://github.com/sureshlazaruspaul/practice-datasets/blob/main/mba-email-grades/notify.logfile"
print(f"logfile of the email program availbale at,\n{logfile}")