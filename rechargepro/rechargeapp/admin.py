from django.contrib import admin
from .models import Contact
from .models import Recharge
from .models import Subscribe
from .models import CardDetails
from .models import HeroUnlimited
from .models import Recommended
from .models import OtherPacks

# Register your models here.

admin.site.register(Contact)
admin.site.register(Recharge)
admin.site.register(Subscribe)
admin.site.register(CardDetails)
admin.site.register(HeroUnlimited)
admin.site.register(Recommended)
admin.site.register(OtherPacks)
