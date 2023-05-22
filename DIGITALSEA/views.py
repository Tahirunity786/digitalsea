from django.http import Http404
from django.shortcuts import render, redirect,get_object_or_404
from django.core.paginator import Paginator
from core.models import Post, Category, Contact,Tag,Post_comment
from core.templatetags import extras

# MAIN API
def main(request):
    recommended_posts = Post.objects.filter(section='Recommended').order_by('-id')[:4]
    popular_posts = Post.objects.filter(section='Popular').order_by('-id')[:10]
    recent_posts = Post.objects.filter(section='Recent').order_by('-id')[:4]
    main_post = Post.objects.filter(Main_Post=True).order_by('-id')[:1]
    Latest_post = Post.objects.filter(section='Latest_Post').order_by('-id')[:10]
    Inspire_posts = Post.objects.filter(section='Inspirations').order_by('-id')[:5]
    
    # Filter Trending posts by Publish status
    trending_posts = Post.objects.filter(section='Trending', Publish=True).order_by('-id')[:10]

    # Category fetcher
    category_area= Category.objects.all()
    
    # ALL TAGs HOME
    universal_tag = Tag.objects.all()
    
    context = {
        'recommended_posts': recommended_posts,
        'Popular_posts': popular_posts,
        'trending_posts': trending_posts,
        'Inspire_post':Inspire_posts,
        'recent_posts': recent_posts,
        'Latest_Post':Latest_post,
        'Main_post': main_post,
        # Category data delivery
        'Category_data':category_area,
        # All tag delivery
        'universal_tag':universal_tag
    }
    return render(request, 'Home.html', context)


# GENERAL URL ROUTING

def postcate(request, slug):
    try:
        post_slug = get_object_or_404(Post, new_slug=slug)
        unique_post = Post.objects.filter(new_slug=slug)
        unique_popular_posts = Post.objects.filter(section='Popular').order_by('-id')[:3]
        unique_post_category = Category.objects.all()   
        unique_post_comment = Post_comment.objects.filter(post=post_slug, parent=None)[:10]
        unique_post_comment_parent = Post_comment.objects.filter(post=post_slug).exclude(parent=None)
        # Logic for getting replies
        replyDict = {}
        for reply in unique_post_comment_parent:
            parent_sno = reply.parent_id
            if parent_sno not in replyDict:
                replyDict[parent_sno] = [reply]
            else:
                replyDict[parent_sno].append(reply)
        # Logic end
        unique_post_comment_numver = Post_comment.objects.filter(post=post_slug).count()
        # Category for header
        category_area= Category.objects.all()
        post_rel_tags = Tag.objects.filter(post=unique_post.first())  # Retrieve the first Post instance from     the queryset
    
        universal_tag = Tag.objects.all()
        context = {
            'post_slug':post_slug,
            'unique_post':unique_post,
            'unique_post_category':unique_post_category,
            'unique_puppular_posts':unique_popular_posts,
            'unique_post_comment': unique_post_comment,
            'unique_post_comment_number':unique_post_comment_numver,
            'Category_data':category_area,
            'unique_post_comment':unique_post_comment,
            'post_rel_tags':post_rel_tags,
            'universal_tag':universal_tag,
            'replyDict':replyDict,
        }
        return render(request, 'blog-single.html', context)
    except:
        pass
    try:
        category_area= get_object_or_404(Category, slug = slug)
        posts_related_to_category = Post.objects.filter(category = category_area).order_by('-id')
        unique_category = Category.objects.get(slug=slug)
        uniquecat_popular_posts = Post.objects.filter(section='Popular').order_by('-id')[:3]
        category_flash = Category.objects.all()
        universal_tag = Tag.objects.all()
        # Pagination implementation
        
        pagination = Paginator(posts_related_to_category, 5)
        page_counter = request.GET.get('page')
        pagination_obj = pagination.get_page(page_counter)
        print('Page number are', pagination_obj)
        # Pagination implementation
        context = {
            'posts_related_to_category': posts_related_to_category,
            'uniquecat_popular_posts': uniquecat_popular_posts,
            'category_data': unique_category,
            'Category_data': category_flash,
            'universal_tag': universal_tag,
            'pagination_obj': pagination_obj,
        }
        return render(request, 'category.html', context)

    except:
        pass


# Contact API
def contact(request):
    if request.method == "POST":
        Name = request.POST['InputName']
        Emails = request.POST['InputEmail']
        Subject = request.POST['InputSubject']
        Message = request.POST['InputMessage']
        contact = Contact(Username = Name, Email = Emails, User_Subject=Subject, Comment = Message )
        contact.save()
        return redirect('Contact')
    else:
        pass
    return render(request, "Contact.html")



# SEARCH API
def search(request):
    search_popular_posts = Post.objects.filter(section='Popular').order_by('-id')[:12]
    search_recent_posts = Post.objects.filter(section='Recent').order_by('-id')[:4]
    query = request.GET['query']
    if len(query) > 78 :
        all_post = Post.objects.none()
    else:
        all_post_Title= Post.objects.filter(Title__icontains=query)
        all_post_content= Post.objects.filter(content__icontains=query)
        all_post= all_post_Title.union(all_post_content)
        
        # All category 
        category_area= Category.objects.all()
        #
    context={
        'unique_search_data':all_post,
        'Popular_posts': search_popular_posts,
        'recent_posts': search_recent_posts,
        'Category_data':category_area,
        'query':query,
    }
    return render(request,"search.html", context)


# USER post comment API
def postcomment(request):
    if request.method == "POST":
        Message = request.POST.get('InputComment')
        # user = request.user
        F_name = request.POST.get('InputName')
        Emails = request.POST.get('InputEmail')
        user_web = request.POST.get('InputWeb')
        
        post_sno = request.POST.get('PostSno',None)
        
        parent_Sno = request.POST.get('mysano', None)
        
        print("This is post sno : ", post_sno)
        post = Post.objects.get(id=post_sno)
        
        # User restriction only two user can message on this post
        same_post_obj = Post_comment.objects.filter(email=Emails, user=F_name, Website=user_web).count()
        if same_post_obj >= 2:
            return redirect(f'/core/{post.new_slug}')
        
        # Reply handling
        if parent_Sno == "":
            user_comment = Post_comment(user=F_name, email=Emails, Website=user_web, User_Message = Message, post = post)
            user_comment.save()
        else:
            parent = Post_comment.objects.get(id=parent_Sno)
            user_comment = Post_comment(user=F_name, email=Emails, Website=user_web, User_Message = Message, post = post, parent = parent,)
            user_comment.save()
        
        return redirect(f'/core/{post.new_slug}')
    else:
        pass
    return render(request, "blog-single.html")



# ABOUT FUNCTION
def about(request):
    universal_tag = Tag.objects.all()
    uniquecat_popular_posts = Post.objects.filter(section='Popular').order_by('-id')[:3]

    category_area= Category.objects.all()
    context = {
        'Category_data':category_area,
        'universal_tag': universal_tag,
        'uniquecat_popular_posts':uniquecat_popular_posts,
        
    }
    return render(request, 'about.html', context)


def privacy_policy(request):
    return render(request, 'privacy_policy.html')



def Disclaimers(request):
    return render(request, 'Disclaimer.html')

def filtered_tag(request):
    # Get the tag name from the request, assuming it is passed as a query parameter named 'tag'
    tag_name = request.GET.get('tag')
    
    # Filter the posts based on the tag name
    related_posts = Post.objects.filter(tags__Name=tag_name)
    # Category DATA
    category_area= Category.objects.all()
    # Render the template and pass the related posts as context
    
    context = {
        'tag_post': related_posts,
        'Category_data':category_area,

    }
    return render(request, 'tags.html' , context)