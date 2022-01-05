from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.urls import reverse


def home(request):
    html = f"<html><body><h1>Welcome to my course notes!</h1><p> <a href={reverse('sections')}>Check the list of sections</a></p></body></html>"
    return HttpResponse(html)


def create_html(string):
    html = f"<html><body><h2>Browse my notes by section</h2><ol><li><a href={reverse('notes', args=['Web Frameworks'])}>Web Frameworks</a></li><li><a href={reverse('notes', args=['Setting up Django'])}>Setting up Django</a></li><li><a href={reverse('notes', args=['URL Mapping'])}>URL Mapping</a></ol><p><a href={reverse('home')}>Back to home</a></p></body></html>"


def sections(request):
    html = f"<html><body><h2>Browse my notes by section</h2><ol><li><a href={reverse('notes', args=['Web Frameworks'])}>Web Frameworks</a></li><li><a href={reverse('notes', args=['Setting up Django'])}>Setting up Django</a></li><li><a href={reverse('notes', args=['URL Mapping'])}>URL Mapping</a></ol><p><a href={reverse('home')}>Back to home</a></p></body></html>"
    return HttpResponse(html)


def notes(request, text):

    html1 = f"<html><body><h2>Notes about {text}</h2><ol><li>As the design of the World Wide Web was not inherently dynamic, early hypertext consisted of hand-coded HTML text files that were published on web servers. Any modifications to published pages needed to be performed by the pages' author. In 1993, the Common Gateway Interface (CGI) standard was introduced for interfacing external applications with web servers, to provide a dynamic web page that reflected user inputs</li><li>In 1995, fully integrated server/language development environments first emerged and new web-specific languages were introduced, such as ColdFusion, PHP, and Active Server Pages.</li><li>Although the vast majority of languages for creating dynamic web pages have libraries to help with common tasks, web applications often require specific libraries for particular tasks, such as creating HTML (for example, JavaServer Faces).</li></ol><p><a href={reverse('sections')}>Back to sections</a></p></body></html>"
    html2 = f"<html><body><h2>Notes about {text}</h2><ol><li>Before you can start to build the individual functionality of a new Django web application, you always need to complete a couple of setup steps. This tutorial gives you a reference for the necessary steps to set up a Django project.</li><li>Use this tutorial as your go-to reference until you have built so many projects that the necessary commands become second nature. Until then, follow the steps outlined below. There are also a few exercises throughout the tutorial to help reinforce what you have learned.'</li><li>'If the activation was successful, then you will see the name of your virtual environment, (env), at the beginning of your command prompt. This means that your environment setup is complete.</li></ol><p><a href={reverse('sections')}>Back to sections</a></p></body></html>"
    html3 = (
        html
    ) = f"<html><body><h2>Notes about {text}</h2><ol><li>Serves as the identifier the host web server uses to direct an HTTP request to a specific HTTP method VI or static file. Each HTTP method VI and static file has one URL mapping.</li><li>Identifies and assigns values to input parameters on the connector pane of the HTTP method VI. You can append input parameters to the end of a URL mapping by appending a question mark, a control label, an equals sign, and the value to assign the control.</li><li>A client can omit any input parameters from the query string. If a client omits an input parameter value, the Web service uses the default value for the input terminal stored in the VI</li></ol><p><a href={reverse('sections')}>Back to sections</a></p></body></html>"

    if text == "Web Frameworks":
        return HttpResponse(html1)
    elif text == "Setting up Django":
        return HttpResponse(html2)
    elif text == "URL Mapping":
        return HttpResponse(html3)
