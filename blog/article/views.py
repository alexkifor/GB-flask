from flask import Blueprint, render_template,redirect
from flask_login import login_required


article = Blueprint('article', __name__, url_prefix='/articles', static_folder='../static')

ARTICLES = {
    1: {'title': 'Article_1',
        'text': 'Hello Article_1!',
        'author': {
            'login': 'John_S',
            'id': 1
        }
    },
    2: {'title': 'Article_2',
        'text': 'Hello Article_2!',
        'author': {
            'login': 'Michael_B',
            'id': 2
        }
    },
    3: {'title': 'Article_3',
        'text': 'Hello Article_3!',
        'author': {
            'login': 'Anna_F',
            'id': 3
        }
    },
}

@article.route('/')
@login_required
def article_list():
    return render_template(
        'articles/list.html',
        articles=ARTICLES,
        )

@article.route('/<int:pk>')
@login_required
def get_article(pk: int):
    try:
        article_name = ARTICLES[pk]['title']
    except KeyError:
        return redirect('/articles/')
    article_name = ARTICLES[pk]['title']
    article_text = ARTICLES[pk]['text']
    article_author = ARTICLES[pk]['author']['login']
    article_author_id = ARTICLES[pk]['author']['id']
    return render_template(
        'articles/details.html',
        article_name=article_name,
        article_text=article_text,
        article_author=article_author,
        article_author_id=article_author_id
        )
