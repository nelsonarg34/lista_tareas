from rest_framework import routers

from list.views import *

router = routers.DefaultRouter()

router.register(r'lists',ListViewSet,basename = 'lists')
router.register(r'tasks',TaskViewSet,basename = 'tasks')

urlpatterns = router.urls