from django.shortcuts import render, HttpResponse

from authentication.models import MyUser
from ticket.models import Ticket

from .models import Comment
from .forms import CommentForm


def comment_form(request):
    ticketid = request.POST['t_id']
    commentform = CommentForm()
    return render(
        request,
        'comment_form.html',
        {
            'commentform': commentform,
            'ticketid': ticketid
        }
    )


def comment(request):
    if request.method == 'POST':
        print(request.POST)
        user = MyUser.objects.get(user_id=request.user.id)
        print(request.POST['is_internal_comment'])
        if request.POST['is_internal_comment']:
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

        if new_comment.is_internal_comment:
            comment_header = f'<h4>{new_comment.posted_by} -\
            { new_comment.date_posted } | Internal </h4>'

            comment_classes = 'internal-comment bg-warning'
        else:
            comment_header = f'<h4>{new_comment.posted_by} -\
            { new_comment.date_posted }'

            comment_classes = ''

        response = f'<div class="card comment border-primary">\
                        <div class="card-header">\
                            {comment_header}\
                        </div>\
                        <div class="card-body {comment_classes}">\
                            <p>{ new_comment.comment_content }</p>\
                        </div>\
                    </div>'
        return HttpResponse(content=response, status=200)
    return HttpResponse(status=403)
