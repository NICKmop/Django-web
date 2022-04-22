from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from .models import Bookmark

class BookmarkListView(ListView):
    # 어떤 모델에 대한 제네릭 뷰인지 지정
    model = Bookmark  # db에 등록된 Bookmark 데이터 전체 반환

class BookmarkCreateView(CreateView):
    model = Bookmark
    fields = ['site_name', 'url']
    success_url = reverse_lazy('list')  # 성공 후 redirect url 지정
    template_name_suffix = '_create'  # create와 update는 모델명_form.html을 불러오기 때문에 suffix 변경하여 사용

class BookmarkDetailView(DetailView):
    model = Bookmark

class BookmarkUpdateView(UpdateView):
    model = Bookmark
    fields = ['site_name', 'url']
    template_name_suffix = '_update'