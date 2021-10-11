from django.db import models
from django.utils.translation import ugettext as _
# Create your models here.




class Apply(models.Model):
    id = models.AutoField(_('id'),primary_key=True,db_index=True,unique=True)
    email = models.EmailField(_('email address'),max_length=120)
    create_timestamp = models.DateTimeField(auto_now=True)

    @property
    def status(self):
        if hasattr(self,'status_of'):
            return 'Approche' if self.status_of.status=='A' else 'Eejected'
        return 'None'


    def __str__(self) -> str:
        return f'{self.id}: {self.email}'

    class Meta:
        verbose_name = "apply"
        verbose_name_plural = 'applications'


class ApplyStatus(models.Model):
    APPROCHE  = 'A'
    REJECT = 'R'
    STATUS_OF_APPLY =[
        (APPROCHE, 'Approche'),
        (REJECT, 'Regect')
    ]
    id = models.AutoField(_('id'),primary_key=True,unique=True,db_index=True)
    apply = models.OneToOneField('apply.Apply', verbose_name=_('apply'),on_delete=models.CASCADE,
                                    related_name='status_of')
    status = models.CharField(max_length=1,choices=STATUS_OF_APPLY,null=True)

    def __str__(self) -> str:
        return f'status of Apply-{self.apply.id}: {self.status}'
    
    class Meta:
        verbose_name= 'apply status'
        verbose_name_plural = 'applications status'


    
