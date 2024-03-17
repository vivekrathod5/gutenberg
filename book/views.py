from .models import Books, Format
from django.http import JsonResponse
from django.core.paginator import Paginator
from django.forms.models import model_to_dict




def book_list_api(request):
    try:
        # Initial queryset
        queryset = Books.objects.all()

        # Apply filters
        book_id = request.GET.get('book_id')
        if book_id:
            queryset = queryset.filter(gutenberg_id=book_id)

        language = request.GET.get('language')
        if language:
            queryset = queryset.filter(booklanguages__language__code=language)

        mime_type = request.GET.get('mime_type')
        if mime_type:
            queryset = queryset.filter(format__mime_type=mime_type)

        bookshelf = request.GET.get('bookshelf')
        if bookshelf:
            queryset = queryset.filter(bookshelves__bookshelf__name__icontains=bookshelf)

        topic = request.GET.get('topic')
        if topic:
            queryset = queryset.filter(subjects__name__icontains=topic)

        author = request.GET.get('author')
        if author:
            queryset = queryset.filter(bookauthors__author__name__icontains=author)

        title = request.GET.get('title')
        if title:
            queryset = queryset.filter(title__icontains=title)

        # Sort by download count in descending order
        queryset = queryset.order_by('-download_count')

        # Pagination
        paginator = Paginator(queryset, 20)
        page_number = request.GET.get('page', 1)
        page_obj = paginator.get_page(page_number)

        # Retrieve specific fields for each book
        books_data = []
        for book in page_obj:
            authors = [book_author.author.name for book_author in book.bookauthors_set.all()]
            subjects = [book_subject.subject.name for book_subject in book.booksubjects_set.all()]
            bookshelves = [book_bookshelf.bookshelf.name for book_bookshelf in book.bookshelves_set.all()]

            language_code = book.booklanguages_set.first().language.code if book.booklanguages_set.exists() else None

            # Retrieve formats for the book
            formats = Format.objects.filter(book=book)
            download_links = [{'mime_type': fmt.mime_type, 'url': fmt.url} for fmt in formats]

            book_data = {
                'book_id': book.gutenberg_id,
                'title': book.title,
                'authors': authors,
                'language': language_code,
                'subjects': subjects,
                'bookshelves': bookshelves,
                'download_count': book.download_count,
                'media_type': book.media_type,
                'download_links': download_links
            }
            books_data.append(book_data)
        return JsonResponse(books_data, safe=False)

    except Exception as error:
        return JsonResponse({"error" : repr(error)}, status=400)








"""

def csv_download(request):
    response = {}
    destination = 'media/'
    object_name = "pg_catalog.csv"
    file_path = os.path.join(destination, object_name)

    # Check if the file already exists
    if os.path.exists(file_path):
        response['error'] = "File already downloaded."
        return JsonResponse(response, status=400)

    # Check if the destination directory exists, if not create it
    if not os.path.exists(destination):
        try:
            os.makedirs(destination)
        except OSError as error:
            response['error'] = f"Failed to create directory: {error}"
            return JsonResponse(response, status=400)

    # Attempt to download the file
    try:
        with requests.get('https://www.gutenberg.org/cache/epub/feeds/pg_catalog.csv', stream=True) as r:
            r.raise_for_status()  # Raise an HTTPError if the response code is not ok

            with open(file_path, "wb") as file:
                for chunk in r.iter_content(chunk_size=8192):
                    file.write(chunk)
                file.flush()

    except RequestException as error:
        response["error"] = f"Failed to download file: {error}"
        return JsonResponse(response, status=400)

    # Check if the file exists after downloading
    if os.path.exists(file_path):
        response['msg'] = "File successfully downloaded."
        return JsonResponse(response, safe=False)
    else:
        response['error'] = "Something went wrong."
        return JsonResponse(response, status=400)
"""