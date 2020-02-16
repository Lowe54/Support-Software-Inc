from django.shortcuts import HttpResponse
from authentication.models import MyUser

from ticket.models import Ticket
from .models import Comment


def comment(request):
    if request.method == 'POST':
        print(request.POST)
        user = MyUser.objects.get(user_id=request.user.id)
        print(request.POST['is_internal_comment'])
        if request.POST['is_internal_comment'] == 'on':
            internal_comment = True
        else:
            internal_comment = False
        new_comment = Comment(
            comment_content=request.POST['comment_content'],
            posted_by=user,
            related_ticket=Ticket.objects.get(id=request.POST['rel_ticket']),
            is_internal_comment=internal_comment
        )
        new_comment.save()
        response = '<div class="comment"><p class="comment-title">{} posted on {}</p><p>{}</p>\
            </div>'.format(
            new_comment.posted_by,
            new_comment.date_posted,
            new_comment.comment_content,
            )
        return HttpResponse(content=response, status=200)
    return HttpResponse(status=403)