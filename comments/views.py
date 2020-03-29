'''
Comment module Views file
'''
from django.shortcuts import HttpResponse, render

from authentication.models import MyUser
from ticket.models import Ticket

from .forms import AgentCommentForm, UserCommentForm
from .models import Comment


def comment_form(request):
    '''
    Return the comment form, taking into account
    the logged in user's role
    '''
    user_profile = MyUser.objects.get(user_id=request.user.id)
    ticketid = request.POST['t_id']
    if user_profile.role == 'AGN':
        commentform = AgentCommentForm()
    else:
        commentform = UserCommentForm()
    return render(
        request,
        'comment_form.html',
        {
            'commentform': commentform,
            'ticketid': ticketid
        }
    )


def comment(request):
    '''
    Save the comment to the database
    '''
    if request.method == 'POST':
        user = MyUser.objects.get(user_id=request.user.id)
        is_internal = request.POST['is_internal_comment']
        if is_internal == 'true':
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
            { new_comment.date_posted } |\
            <span class="badge badge-warning">INTERNAL</span> </h4>'

            comment_classes = 'internal-comment border-warning'
        else:
            comment_header = f'<h4>{new_comment.posted_by} -\
            { new_comment.date_posted }'

            comment_classes = 'border-primary'

        response = f'<div class="card comment {comment_classes}">\
                        <div class="card-header">\
                            {comment_header}\
                        </div>\
                        <div class="card-body {comment_classes}">\
                            <p>{ new_comment.comment_content }</p>\
                        </div>\
                    </div>'
        return HttpResponse(content=response, status=200)
    return HttpResponse(status=403)
