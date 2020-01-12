from django.shortcuts import render

# Create your views here.
def website_test (request):
	context = {"msg":"Hello World!",
	"title": "django task 2",
    "header": "I thnink i finished Task 2!"}

	return render(request, "html_file.html", context)
