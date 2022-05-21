from django.db import models


class Community(models.Model):
    custom_id = models.CharField(max_length=30, unique=True, null=True, verbose_name='Custom id')
    name = models.CharField(max_length=100, unique=True, verbose_name='Name')
    description = models.TextField(null=True, verbose_name='Description')
    creating_date = models.DateField(auto_now_add=True, blank=True, verbose_name='Creating date')
    creator = models.ForeignKey(
        to='users.User',
        on_delete=models.SET_NULL,
        null=True,
        related_name='created_communities',
        verbose_name='Creator',
    )
    participants = models.ManyToManyField(
        to='users.User',
        through='communities.CommunityParticipant',
        through_fields=('community', 'participant'),
        related_name='communities',
        verbose_name='Participants',
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Community'
        verbose_name_plural = 'Communities'


class CommunityParticipant(models.Model):
    community = models.ForeignKey(to='communities.Community', on_delete=models.CASCADE, verbose_name='Community')
    participant = models.ForeignKey(to='users.User', on_delete=models.CASCADE, verbose_name='Participant')
    entry_date = models.DateField(auto_now_add=True, blank=True, verbose_name='Entry date')

    def __str__(self):
        return f'{self.participant} in {self.community}'

    class Meta:
        verbose_name = 'Community participant'
        verbose_name_plural = 'Communities participants'
        unique_together = ['community', 'participant']
