from django.shortcuts import render , redirect , get_object_or_404
from .models import *
from .forms  import BokForm , CategoryForm
from django.views.generic.edit import UpdateView

# Create your views here.


def index(request):
    if request.method == 'POST':
            add_book=  BokForm(request.POST , request.FILES)
            if add_book.is_valid():
                    add_book.save()
    
    
    
    if request.method == 'POST':
            add_cat=  CategoryForm(request.POST)
            if add_cat.is_valid():
                    add_cat.save()                
                    
                 
        
        
    books  =  Book.objects.all()
    cat = Category.objects.all()
    form = BokForm()
    forms= CategoryForm()
    allbooks = Book.objects.filter(active= True).count()
    soldbooks = Book.objects.filter(status= 'sold').count()
    rentalbooks = Book.objects.filter(status= 'rental').count()
    avialblebooks = Book.objects.filter(status= 'avialble').count()


    return  render(request, 'pages/index.html', {'books': books , 'cat' :cat , 'form':form , 'forms': forms , 'allbooks':allbooks , 'soldbook':soldbooks, 'rentalbooks': rentalbooks, 'avialblebooks':avialblebooks})




def books(request):
        search = Book.objects.all()
        title = None
        if 'search_name' in request.GET :
                title = request.GET['search_name']
                if title :
                        search = search.filter(title__icontains= title)
                
        
        if request.method == 'POST':
            add_cat=  CategoryForm(request.POST)
            if add_cat.is_valid():
                    add_cat.save()        
        context = {

                                
       'books'  : search,
       'cat' : Category.objects.all() , 
       'forms':CategoryForm()
        }
        
        return  render(request, 'pages/books.html', context)
    
    
def update(request , id):
        book_id = Book.objects.get(id= id)
        if request.method == 'POST':
                book_save = BokForm(request.POST , request.FILES , instance=book_id)
                if book_save.is_valid():
                        book_save.save()
                        return redirect('index')
                        
        else :
                book_save =BokForm(instance=book_id)
                
        context = {
                'from' :book_save,
        }        
        return  render(request, 'pages/update.html', context)
    
     

    

def delete(request , id):
        book_delete = get_object_or_404(Book , id=id)
        if request.method == 'POST':
                book_delete.delete()
                return redirect('index')
        return  render(request, 'pages/delete.html')

        
        