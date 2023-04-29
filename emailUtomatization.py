# Email Automation
# This code send emails to one or multiple contacts using the Python smtplib library.
#========================================================
"""
  args:
     - subject (str): The subject of the email.
     - html_body (str): The content of the email.
     - sender (str): The email address of the sender.
     - recipient (str): The email address of the recipient.
     - smtp_server (str): The SMTP server to be used to send the email.
     - smtp_port (int): The port number for the SMTP server.
     - username (str): The sender's username (can be the same as the email address).
     - password (str): The sender's password.
"""

# Dependencies
#========================================================
import os
import time
import smtplib
from email.message import EmailMessage
from email.mime.application import MIMEApplication


# This function send an emamil to mutiple contacts with attached files. If you don't want to send attached file just keep empty the posistion for the attached files when calling the send_email function
def send_email(subject, html_body, sender, recipient, smtp_server, smtp_port, username, password, file_paths=None):

    # Here we can validate the entry args
    #==========================================
    if not all ([subject, html_body, sender, recipient, smtp_server, smtp_port, username, password]):
        print('ERROR: Todos los argumentos son obligatorios')
        return False

    if not (isinstance(smtp_port, int) and smtp_port > 0):
        print('ERROR: El número de puerto SMTP debe ser un entero positivo')
        return False
    

    # Create an EmailMessage object with the email data
    #==========================================
    msg = EmailMessage()
    # Add sender and recipient
    msg['From'] = sender
    # 1 uncomment to send the email to ome contact
    # msg['To'] = recipient

    # 2 to send the email several contacts
    # msg['To'] = recipient.split(',')

    # 3 handel an array of contacts
    msg['To'] = ', '.join(recipient)

    # Add the subbject of the email
    msg['Subject'] = subject

    # Add body to email
    msg.add_alternative(html_body, subtype='html')

    # Add attachments files
    #==========================================
    if file_paths:
      for file_path in file_paths:
        try:
          with open(file_path, "rb") as attachment:
            part = MIMEApplication(
              attachment.read(),
                Name=os.path.basename(file_path)
            )
          # Add header to attachment part
          part['Content-Disposition'] = f'attachment; filename="{os.path.basename(file_path)}"'
          msg.attach(part)

        except FileNotFoundError:
          print(f'Archivo {file_path} no encontrado')
          print(f'ERROR: Attached file Error: {e}')
          return False
      

    # Create a secure connection to the SMTP server
    #==========================================
    with smtplib.SMTP(smtp_server, smtp_port) as server:
      try:
          # start a TLS connection
          server.starttls()

          # start session at the SMTP server
          server.login(username, password)

          # Send the email
          server.send_message(msg)

          print(f'Correo electrónico enviado a {recipient}')
          return True
      
      except Exception as e:
        print(f'ERROR: No se pudo enviar el correo electrónico: {e}')
        return False


# Execute after 2 minutes
# time.sleep(120)

# Define email parameters and send email
#==========================================
if __name__ == '__main__':
  subject = 'Test Email'

  # Create a html content for the email body
  #==========================================
  html_body = f"""\
  <html>
    <body>
      <div id="mi-elemento" style=" position: relativ; width: auto; height: auto; background: linear-gradient(90deg, rgba(15,3,209,7777) 20%, rgba(241,241,244, -.8888) 80%, rgba(247,0,0,7777) 100%), url('https://my-porfolio-khaki.vercel.app/assets/img-generic/me.png') no-repeat right fixed; color: white; padding: 15px; border-radius: 50px 0 50px 0;">

          <div style="display: flex; justify-content: space-between;"> 
              <div stytle="width: 30%"> 
                  <img style=" width: 50px; height: 60px; " src=" https://my-porfolio-khaki.vercel.app/assets/img-generic/elier.png"/>
                  <h2 style="padding: 0; margin-bottom: 0; font-style: italic; color:#6cca0e;">Elier Mercedes<h2/>
                  <p style="padding: 0; margin-top: 0; font-style: italic; color:#6cca0e; ">Software Developer<p/>
              <div/>

          <div/>
          <hr style="width:70%; margin-left:0;"/>
              <p style=" margin-buttom: 0; height: auto; width: 70%; border: 2px solid #ac55d4; border-radius: 10px; font-weight: 500; font-style: italic; padding: 10px; background: linear-gradient(to top right, rgba(222, 31, 37, 0.922) 50%,  rgba(222, 31, 37, 0.555) 70%); text-align: center;">
              
              Sehr geehrter Herr Michael Haslinger, 
            <br><br>
            Suchen Sie nach einem hochleistungsfähigen Full-Stack-Entwickler mit volle Motivation, um komplexe und hoch skalierbare Softwarelösungen zu erstellen? <span style="color: #ac55d4; text-decoration:underline;"> Elier Mercedes </span> ist die Antwort! Mit außergewöhnlichen Fähigkeiten in Analyse und logischem Denken sowie einem soliden Satz von Soft Skills ist Elier Experte in Technologien wie HTML, CSS, JavaScript, React, Python, PHP, Linux, Nodejs, Docker und anderen und vertraut mit Umgebungen wie DBA, CI/CD, TDD.
            <br><br>
            Darüber hinaus garantiert sein Fokus auf Softwareoptimierung und -sicherheit, dass Ihre Anwendungen immer auf dem neuesten Stand sind und gegen externe Bedrohungen geschützt sind.
            <br><br>
            Ob Sie eine Unternehmenswebsite, eine maßgeschneiderte Webanwendung oder ein komplettes E-Commerce-System benötigen, <span style="color: #ac55d4; text-decoration:underline;"> Elier Mercedes </span> hat alles, was Sie brauchen, um Ihr Projekt auf die nächste Stufe zu bringen.
            <br><br>
            Suchen Sie nicht, da ich zu Ihrer Verfügung stehe.
            <br><br>
            Mit freundlichen grüßen,
            <br><br>
            Elier Mercedes
              </p>
              
          <hr  style="width:70%; margin-left:0;"/>

          <div  style=" position: absolute; bottom: 0"> 

            <a href="https://my-porfolio-khaki.vercel.app/">

                <img style="width: 60px; margin-right:10px; height: 40px; border-radius: 15px;" src="https://camo.githubusercontent.com/61491d59e71fec5c794945fed916a4a682b6c0404fc31f30b08a0d919c558404/68747470733a2f2f696d616765732e73717561726573706163652d63646e2e636f6d2f636f6e74656e742f76312f3537363966633430316236333162616231616464623261622f313534313538303631313632342d5445363451474b524a4738535741495553374e532f6b6531375a77644742546f6464493870446d34386b506f73776c7a6a53564d4d2d53784f703743563539425a772d7a505067646e346a557756634a45315a7657515578776b6d794578676c4e714770304976544a5a616d574c49327a76595748384b332d735f3479737a63703272795449304871544f6161556f68724938504936465879386339505774426c7141566c555335697a7064634958445a71445976707252715a32395077306f2f636f64696e672d667265616b2e676966"/>
            </a>
              

                  <a href="https://my-porfolio-khaki.vercel.app/">
                  <img style="width: 30px; margin-right:10px; margin-right:10px; height: 30px; border-radius: 50%;" src="<img style="width: 100px; height: 70px;" src="https://d2gg9evh47fn9z.cloudfront.net/800px_COLOURBOX31029947.jpg"/>
                </a>

                  <a href="https://www.linkedin.com/in/elier-mercedes-7747a3256/">
                  <img style="width: 30px; margin-right:10px; height: 30px; border-radius: 50%;" src="<img style="width: 100px; height: 70px;" src="https://img.favpng.com/25/4/21/linkedin-facebook-social-media-font-awesome-icon-png-favpng-QRqmwk6cNZRQZwxSAJpYRt4Rf_t.jpg"/>
                </a>

                <a href="">
                  <img style="width: 30px; margin-right:10px; height: 30px; border-radius: 50%;" src="<img style="width: 100px; height: 70px;" src="https://e7.pngegg.com/pngimages/202/248/png-clipart-twitter-logo-computer-icons-encapsulated-postscript-tweeter-blue-logo-thumbnail.png"/>
                </a>

                <a href="https://www.facebook.com/ariel.mercedes1">
                  <img style="width: 30px; margin-right:10px; height: 30px; border-radius: 50%;" src="<img style="width: 100px; height: 70px;" src="https://img.freepik.com/free-psd/3d-rounded-square-with-glossy-facebook-logo_125540-1538.jpg?w=2000"/>
                </a>
              
                <a href="https://www.instagram.com/vitacora_web/?next=%2Fvitacora_web%2F">
                  <img style="width: 30px; margin-right:10px; height: 30px; border-radius: 50%;" src="<img style="width: 100px; height: 70px;" src="https://png.pngtree.com/png-clipart/20180626/ourmid/pngtree-instagram-icon-instagram-logo-png-image_3584853.png"/
                  >
                </a>

                <a href="https://www.facebook.com/ariel.mercedes1">
                  <img style="width: 30px; height: 30px; border-radius: 50%;" src="<img style="width: 100px; height: 70px;" src="https://w7.pngwing.com/pngs/914/758/png-transparent-github-social-media-computer-icons-logo-android-github-logo-computer-wallpaper-banner-thumbnail.png"/
                  >
                </a>
          <div/>
      <div/>
    </body>
  </html>
  """


  sender = 'example@gmail.com'
  # 1 for one contact
  # recipient = 'example@gmail.com'

  # 2 for several contacts
  # recipient = 'example@gmail.com, example@gmail.com, example@gmail.com'

  #3  send an array of contacts
  recipient = [ "example@gmail.com", 'example@gmail.com']
  smtp_server = 'smtp.gmail.com'
  smtp_port = 587
  username = 'example@gmail.com'
  password = os.getenv('GMAIL_PASSWORD')
  # password = os.environ.get('GMAIL_PASSWORD')

  # 1 Run the code without attached files
  send_email(subject, html_body, sender, recipient, smtp_server, smtp_port, username, password)
  
  # 2 Run the code with attached files
  # send_email(subject, html_body, sender, recipient, smtp_server, smtp_port, username, password, ['./assets/Resume-.pdf', './assets/emai_img.png'])


  

