from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from django.core.paginator import Paginator
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login, logout
from django.contrib import messages
from django.core.mail import send_mail

from .models import News, Category
from .forms import NewsForm, UserRegisterForm, UserLoginForm, ContactForm
from .utils import MyMixin


def user_register(request):
    """Register new user in system and send all data in database."""
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()  # Save data in database.
            login(request, user)  # Connect user in system.
            messages.success(request, 'Вы успешно зарегестрированы')
            return redirect('home')
        else:
            messages.error(request, 'Ошибка регистрации')
    else:
        form = UserRegisterForm()
    return render(request, 'news/register.html', {'form': form})


def user_login(request):
    """Connect user in system."""
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()  # Get data about user.
            login(request, user)  # Connect user in system.
            return redirect('home')  # Back user on home page.
    else:
        form = UserLoginForm()
    return render(request, 'news/login.html', {'form': form})


def user_logout(request):
    """Disconnect user from system."""
    logout(request)
    return redirect('home')  # Back user on home page.


def send_message_to_email(request):
    """Send message on project-team e-mail address."""
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            mail = send_mail(form.cleaned_data['subject'], form.cleaned_data['content'],
                             '', [''], fail_silently=True)  # Send message on e-mail address and return 1 or 0.
            if mail:  # Check send.
                messages.success(request, 'Письмо отправлено')
                return redirect('contact')  # Back user on contact page.
            else:
                messages.error(request, 'Ошибка при отправке письма')
        else:
            messages.error(request, 'Ошибка ввода данных')
    else:
        form = ContactForm()
    return render(request, 'news/send_message.html', {'form': form})


def test(request):
    page_objs = News.objects.all()
    pag = Paginator(page_objs, 2)
    p_num = request.GET.get('page', 1)
    p_objects = pag.get_page(p_num)
    return render(request, 'news/test.html', {'page_obj': p_objects})


class HomeNews(ListView):
    """Get data on index.html and setting its."""
    model = News  # Connect model in class.
    template_name = 'news/index.html'
    context_object_name = 'news'
    paginate_by = 10  # Connect paginator on page with the step 10.
    # queryset = News.objects.select_related('category')

    def get_context_data(self, *, object_list=None, **kwargs):  # Update data, which get template.
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        return context

    def get_queryset(self):  # Check news on param is_published and return only publish news.
        return News.objects.filter(is_published=True).select_related('category')


class NewsByCategory(ListView):
    """Get data on category.html and setting its."""
    model = News  # Connect model in class.
    template_name = 'news/category.html'
    context_object_name = 'news'
    paginate_by = 10  # Connect paginator on page with the step 10.
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):  # Update data, which get template.
        context = super().get_context_data(**kwargs)
        context['title'] = News.objects.filter(category_id=self.kwargs['category_id'])
        return context

    def get_queryset(self):  # Check news on param category_id and return only news the same category.
        return News.objects.filter(category_id=self.kwargs['category_id'],
                                   is_published=True).select_related('category')


class ViewNews(DetailView):
    """Get data on view_news.html and view a new."""
    model = News  # Connect model in class.
    template_name = 'news/view_news.html'
    context_object_name = 'news_item'


class CreateNews(LoginRequiredMixin, CreateView):
    """Create page for create news.
    Only authorization users can use it.
    """
    form_class = NewsForm
    template_name = 'news/add_news.html'
    success_url = reverse_lazy('home')
    login_url = '/admin/'
    raise_exception = True


# def news(request):
#     all_news = News.objects.all()
#     return render(request, 'news/index.html', {
#         'all_news': all_news,
#     })
#
#
# def get_news_by_categories(request, category_id):
#     news = News.odjects.all().filter(category_id=category_id)
#     return render(request, 'news/index.html', {
#         'all_news': news,
#     })
#
#
# def get_category(request, category_id):
#     news = News.objects.filter(category_id=category_id)
#     category = Category.objects.get(pk=category_id)
#     return render(request, 'news/category.html', {
#         'news': news,
#         'category': category,
#     })
#
#
# def view_news(request, news_id):
#     # news_item = News.objects.get(pk=news_id)
#     news_item = get_object_or_404(News, pk=news_id)
#     return render(request, 'news/view_news.html', {
#         'news_item': news_item,
#     })
#
#
# def add_news(request):
#     if request.method == 'POST':
#         form = NewsForm(request.POST)
#         if form.is_valid():
#             news = form.save()
#             return redirect(news)
#     else:
#         form = NewsForm()
#     return render(request, 'news/add_news.html', {
#         'form': form,
#     })
