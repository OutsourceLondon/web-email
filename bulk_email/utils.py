import pandas as pd
import smtplib
from email.mime.text import MIMEText

def read_file(file):
    df = pd.read_csv(file)
    return df

def send_mail(file, subject, message):
    df = read_file(file)
    for index, row in df.iterrows():
        to_email = row['Email']
        if pd.notna(to_email):
            str_email = str(to_email)
            try:
                s = smtplib.SMTP('smtp.gmail.com', 587)
                s.starttls()
                s.login('theblacklion2223@gmail.com', 'ygbk puij that cgxh')
                msg = MIMEText(message)
                msg['Subject'] = subject
                msg['From'] = 'theblacklion2223@gmail.com'
                msg['To'] = str_email
                s.sendmail('theblacklion2223@gmail.com', str_email, msg.as_string())
            except Exception as e:
                print("error", e)
            finally:
                s.quit()
        else:
            pass
