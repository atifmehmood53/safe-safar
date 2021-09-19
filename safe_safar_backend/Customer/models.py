
from django.contrib.auth.models import User
from django.db import models


class Customer(User):
    community_score = models.FloatField(default=0.0)
    seats = models.ManyToManyField("RideFeedback.Seat", through="RideFeedback.Booking")

    def update_community_score(self, all_pfs):
        all_pfs_count = all_pfs.count()
        if all_pfs_count < 5:
            return
        self.community_score = sum(map(lambda x: float(x), all_pfs.values_list('vote', flat=True))) / all_pfs_count
        self.save(update_fields=['community_score'])
