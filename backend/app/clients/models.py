from django.db import models
from datetime import date, datetime
from transliterate import translit
from django.utils.text import slugify


class Client(models.Model):
  name = models.CharField(max_length=40, verbose_name='Имя')
  last_name = models.CharField(max_length=40, verbose_name='Фамилия')
  second_name = models.CharField(max_length=40, verbose_name='Отчество', blank=True)
  phone = models.CharField(max_length=30, verbose_name='телефон')
  email = models.EmailField(max_length=155, verbose_name='Email')
  slug = models.SlugField(max_length=255, verbose_name='слаг')
  
  class Meta:
    verbose_name = 'Клиент'
    verbose_name_plural = 'Клиенты'
    indexes = [
      models.Index(fields=('email', 'last_name', 'phone'))
    ]
  
  
  @classmethod
  def create_client(cls, **kwargs):
    
  
  
  def __str__(self):
    return f'{self.last_name} {self.name} {self.phone}'




class ClientProfile(models.Model):
  CLIENT_STATUS_CHOICE = (
    ('NW', 'новый'),
    ('RG', 'постоянный')
  )
  shirt_size = models.CharField(max_length=4, verbose_name='размер футболки', blank=True)
  status = models.CharField(max_length=2, verbose_name='статус клиента')
  nutrition_features = models.CharField(max_length=400, verbose_name='питание', blank=True)
  comment = models.CharField(max_length=600, verbose_name='коммент', blank=True)
  city = models.CharField(max_length=150, verbose_name='город', blank=True)
  date_of_birth = models.DateField(verbose_name='дата рождения', blank=True, null=True)
  
  client = models.OneToOneField(Client, related_name='client_profile', on_delete=models.CASCADE, verbose_name='клиент')
  
  class Meta:
    verbose_name = 'Профиль клиента'
    verbose_name_plural = 'Профили клиентов'
  
  def __str__(self):
    return f'{self.status} {self.city} '




class ClientDocument(models.Model):
  DOC_TYPE_CHOICE = (
    ('PS', 'Паспорт'),
    ('CR', 'свидетельство')
  )
  doc_type = models.CharField(max_length=2, choices=DOC_TYPE_CHOICE, verbose_name='Тип документа')
  series = models.CharField(max_length=20, verbose_name='Серия документа')
  number = models.CharField(max_length=20, verbose_name='Номер документа')
  date_of_issue = models.DateField(verbose_name='Дата выдачи')
  issued_by = models.CharField(max_length=400, verbose_name='Кем выдан')
  
  client = models.OneToOneField(Client, related_name='client_document', on_delete=models.CASCADE, verbose_name='клиент')
  
  class Meta:
    verbose_name='Документ клиента'
    verbose_name_plural='Документы клиентов'
  
  
  def __str__(self):
    return super().__str__()
  
  
  def check_client_age(self, client_id: int):
    client: Client = Client.objects.select_related('client_profile').get(pk=client_id)
    client_birth = client.client_profile.date_of_birth
    client_year = datetime.strptime(client_birth, '%Y-%m-%d')
    today = date.today()
    age = datetime.now().year - client_year.year - ((datetime.now().month, datetime.now().day) < (client_year.month, client_year.day))
    self.doc_type = 'CR' if age < 14 else 'PS'


