from smarturls import surl as url
from views import index 

urlpatterns = [
	url(regex='/', view=index, name='portal_index')
]