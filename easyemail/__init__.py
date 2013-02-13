from email.mime.application import MIMEApplication
from email.mime.audio import MIMEAudio
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib

from mako.template import Template


class EasyEmail(object):
    """
    This class aims to abstract sending emails from templates, for now it
    covers only mako templating system but jinja2 is on its way.
    
    Constructor arguments:
    
    ``to``
    
       Defaults to empty list, can be list of emails or string.
    
    ``sender``
    
       Defaults to empty string - this should contain email of the sender (from)
    
    ``subject``
    
       Defaults to empty string - should contain subject of the message
    """
    def __init__(self, to=[], sender='', subject=''):
        self.message = MIMEMultipart('alternative')
        self.subject = subject
        self.to = to
        self.sender = sender

    def attach_image(self, image_content, subtype=None):
        self.message.attach(MIMEImage(image_content, _subtype=subtype))

    def attach_binary(self, binary_data, subtype=None):
        self.message.attach(MIMEApplication(binary_data, _subtype=subtype))

    def attach_text(self, text, subtype=None):
        self.message.attach(MIMEText(text, _subtype=subtype))

    def attach_audio(self, audio_data, subtype=None):
        self.message.attach(MIMEAudio(audio_data, _subtype=subtype))

    def load_template(self, template_file_path, context, data_type='html',
                      ttype='mako'):
        if ttype == 'mako':
            with open(template_file_path, 'r') as template_file:
                template = Template(template_file.read()).render(**context)
                self.attach_text(template, data_type)

    def send(self, connection_type='smtp', authentication=False, **smtp_params):
        self._compose()
        smtp_connection = self._connect(
            connection_type, authentication, **smtp_params
        )
        smtp_connection.sendmail(
            from_addr = self.sender,
            to_addrs = self.to,
            msg = self.message.as_string()
        )
        smtp_connection.quit()

    def _connect(self, connection_type, authentication, **smtp_params):
        if connection_type == 'smtp':
            smtp_connection = smtplib.SMTP(
                smtp_params.get('host', 'localhost'),
                smtp_params.get('port', 25),
                smtp_params.get('local_hostname'),
                smtp_params.get('timeout')
            )
        elif connection_type == 'ssl':
            smtp_connection = smtplib.SMTP_SSL(
                smtp_params.get('host'),
                smtp_params.get('port'),
                smtp_params.get('local_hostname'),
                smtp_params.get('keyfile'),
                smtp_params.get('certfile'),
                smtp_params.get('timeout')
            )
        elif connection_type == 'tls':
            smtp_connection = smtplib.SMTP(
                smtp_params.get('host'),
                smtp_params.get('port'),
                smtp_params.get('local_hostname'),
                smtp_params.get('timeout')
            )
            smtp_connection.starttls(
                smtp_params.get('keyfile'),
                smtp_params.get('certfile')
            )
        if authentication:
            smtp_connection.login(
                smtp_params.get('login'),
                smtp_params.get('password')
            )
        return smtp_connection

    def _compose(self):
        self.message['Subject'] = self.subject
        self.message['From'] = self.sender
        if isinstance(self.to, list):
            self.message['To'] = ', '.join(to)
        else:
            self.message['To'] = self.to