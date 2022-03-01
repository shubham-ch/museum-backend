from rest_framework.routers import SimpleRouter
from .views import GeneralFileViewSet

router = SimpleRouter()
router.register(r"", GeneralFileViewSet , basename="files")

urlpatterns = router.urls