from django.shortcuts import render, get_object_or_404, redirect
from helent.models import Post

# from .models import Comment
from .forms import CommentForm


# Create your views here.

def post_comment(request, post_pk):
    # 先获取被评论的文章,评论和文章要关联
    # 函数get_object_or_404的作用是当获取的文章(Post)存在时获取,不存在时返回404页面
    post = get_object_or_404(Post, pk=post_pk)

    # 根据用户请求类型处理表单数据
    if request.method == 'POST':
        form = CommentForm(request.POST)
        # 检测参数是否符合表单要求
        if form.is_valid():
            # 根据表单数据生成comment实例,但是并不保存
            comment = form.save(commit=False)
            # 关联文章外键
            comment.post = post
            # 保存评论
            comment.save()
            # 重定向到详情页,显示评论
            return redirect(post)
        else:
            # 检测数据不合法,重新渲染详情页
            comment_list = post.comment_set.all()
            context = {'post': post,
                       'form': form,
                       'comment_list': comment_list
                       }
            return render(request, 'helent/detail.html', context=context)

    return redirect(post)
