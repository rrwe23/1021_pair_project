## ๐1021 pair Project

***

![๋นํ_2022_10_23_21_57_11_327](https://user-images.githubusercontent.com/70432152/197394187-350cae49-c3ea-4483-b4cc-8040f19b5396.gif)

## ๐ ์ค์ต ๋ด์ฉ

***

- `CRUD` ๊ตฌํ

- ์ด๋ฏธ์ง ๋ค๋ฃจ๊ธฐ

- Django Auth ํ์ฉ ํ์ ๊ด๋ฆฌ

- ํ์๊ฐ์ ๊ธฐ๋ฅ,๋ก๊ทธ์ธ, ๋ก๊ทธ์์, ๋ฆฌ๋ทฐ์์ฑ, ์ญ์ 

## ๐ขํ๊ณ  ๋ฐ ๊ณ ์ฐฐ

- ์ํ๋ ๋ถ๊ณผ์ ์ค๋ ฅ์ฐจ๋ฅผ ํ์ ํ ๋๋ ์ ์์๋ ํ๋ก์ ํธ์๋ค... Articles ๋ถ๋ถ์ ๋ชจ๋ธ๊ณผ ์์ฑ๊ธ ์์ฑ, ์์ , ์ญ์  ๋ฑ์ ๊ธฐ๋ณธ์ ์ธ ๊ธฐ๋ฅ๋ค์ ๋ฌด๋ฆฌ์์ด ๊ตฌํํ  ์ ์์์ผ๋ ์ด๋ฒ ์ฃผ์ ํ์ตํ ๊ธฐ๋ฅ๋ค์ ๊ฑฐ์ ํผ์์ ๊ตฌํ์ด ๋ถ๊ฐ๋ฅํ๋ค...๐ข

- ๊ณํ์ ์๋ ๊ฒ์๊ธฐ๋ฅ์ ์ถ๊ฐํ๋ค. ๋ ๋ถ์ด์ ๋จธ๋ฆฌ๋ฅผ ๋ง๋๊ณ  ๊ณ ๋ฏผํ์๋๋ ๋๋ฑ ์์ฑ๋์๋ค. ์ ๋ชฉ ๋ฟ๋ง ์๋๋ผ ๊ธ์ ๋ชฉ์ผ๋ก๋ ๊ฒ์ ํ  ์ ์๊ฒ ๊ธฐ๋ฅ์ ๊ตฌํํ๋ ๋ชจ์ต์ ๋ณด๊ณ  ๊ฐํํ๋ค. 

- ํ๋ ์๊ฐ์ด ๋ง์ด ์์๋์ด ๋์์ธ์ ์ธ ๋ถ๋ถ์ ๊ตฌํํ์ง ๋ชปํ๊ณ  ๊ตฌ์ํ๋ ๋ฆฌ๋ทฐ ํํ์ด์ง ๋ชจ์ต์์ ๋๊ธ ๊ธฐ๋ฅ์ ๋ฏธ์ฒ ์๊ฐํ์ง ๋ชปํด ๋๊ธ ๊ธฐ๋ฅ์ด ๋ฏธ๊ตฌํ ์ํ์ด๋ค. 

- ๋ฏธ๊ตฌํ ์ํ๋ก ํ๋ก์ ํธ๊ฐ ๋๋ ๊ฒ์ด ์ด์ฉ๋ฉด ๊ธฐํ ์ผ ์ ๋ ์๋ค๊ณ  ์๊ฐํ๋ค. ์ดํ ์๊ฐ์ด ๋๋ฉด ๊ทธ ๋์  ํด๋ณด๊ณ  ์ถ์๋ bootstrap ๋ณต์ต์ ํด ๋ณผ ์์ ์ด๋ค.

## โLike ,Following๊ธฐ๋ฅ ์ถ๊ฐ

***

![๋นํ_2022_10_25_22_25_40_435](https://user-images.githubusercontent.com/70432152/197785953-488ec28e-09a9-49b8-aabd-85d394774397.gif)



์์ ์๊ฐ์ ๋ฐฐ์ด ๋ด์ฉ์ ๋ฐํ์ผ๋ก ๊ฒ์๊ธ์ ์ข์์์ ํ๋ก์ฐ ๊ธฐ๋ฅ์ ์ถ๊ฐํ๋ค.

`Like`

- ๋จผ์  models์ ๊ธฐ๋ฅ์ ์ถ๊ฐํด์ค๋ค.

```python
# articles/models.py์ ํ ์ค ์ถ๊ฐ


like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_reviews')
```

`make migrations`, `migrate` ์ดํ

```python
# articles/urls.py


path('<int:pk>/like/', views.like, name='like'),
```

```python
# views.py
@login_required
def like(request, pk):
    article = Article.objects.get(pk=pk)
    # ๋ง์ฝ์ ๋ก๊ทธ์ธํ ์ ์ ๊ฐ ์ด ๊ธ์ ์ข์์๋ฅผ ๋๋ ๋ค๋ฉด,
    # if article.like_users.filter(id=request.user.id).exists():
    if request.user in article.like_users.all(): 
        # ์ข์์ ์ญ์ ํ๊ณ 
        article.like_users.remove(request.user)
    else:
        # ์ข์์ ์ถ๊ฐํ๊ณ  
        article.like_users.add(request.user)
    # ์์ธ ํ์ด์ง๋ก redirect
    return redirect('articles:detail', pk)
```

```html
# detail.html


<span>
    <a class="like-heart" href="{% url 'articles:like' review.pk %}">
      {% if request.user in review.like_users.all %}
        <i class="bi bi-heart-fill"></i>
      {% else %}
        <i class="bi bi-heart"></i>
      {% endif %}
    </a>{{ review.like_users.count }}</span>
```

- css ํธ์ง์ ์ํด ๋งํฌ ์ถ๊ฐ

```html
# base.html <head>
{% load django_bootstrap5 %}
{% load static %}


<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.9.1/font/bootstrap-icons.css">
<link rel="stylesheet" href="{% static 'css/style.css' %}">
```

```css
# static/css/style.css


.header {
    height: 20rem;
    background-image: url('/static/images/bg.jpg');
    background-size: cover;
    background-position: center;
    filter: blur(5);
}

.like-heart {
    text-decoration: none !important;
}
```

`Follow`

- account ์ฑ์์ ์์ํด์ค๋ค.

- model.py ์ ์ถ๊ฐ ํ ๋ง์ด๊ทธ๋ ์ด์

```python
#accounts/models.py
class User(AbstractUser):

    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')


    @property
    def full_name(self):
        return f'{self.last_name}{self.first_name}'
```

- ๊ฒฝ๋ก ์ถ๊ฐ

```python
# urls.py

path('<int:pk>/follow/', views.follow, name='follow'),
```

- ํจ์ ์ถ๊ฐ

```python
# views.py

def follow(request,pk):

    return redirect('accouontsd:detail',pk)
```

- detail ์ ํ๋ก์ฐ ๋ฒํผ ์ถ๊ฐ

```python
# ํ๋ก์ ์ซ์์ ํ๋ก์ ์ซ์ ํ๊ธฐ
<p>{{ user.followings.count }}||{{ user.followers.count }}</p>
  <a href="{% url 'accounts:follow' user.pk %}">ํ๋ก์ฐ</a>
```

- ํจ์๋ฅผ ๊ตฌํํ์๋ฉด

```python
@login_required
def follow(request, pk):
    # ํ๋กํ์ ํด๋นํ๋ ์ ์ ๋ฅผ ๋ก๊ทธ์ธํ ์ ์ ๊ฐ!
    user = get_user_model().objects.get(pk=pk)
    if request.user == user:
        messages.warning(request, '์ค์ค๋ก ํ๋ก์ฐ ํ  ์ ์์ต๋๋ค.')
        return redirect('accounts:detail', pk)
    if request.user in user.followers.all():
    # (์ด๋ฏธ) ํ๋ก์ฐ ์ํ์ด๋ฉด, 'ํ๋ก์ฐ ์ทจ์'๋ฒํผ์ ๋๋ฅด๋ฉด ์ญ์  (remove)
        user.followers.remove(request.user)
    else:
    # ํ๋ก์ฐ ์ํ๊ฐ ์๋๋ฉด, 'ํ๋ก์ฐ'๋ฅผ ๋๋ฅด๋ฉด ์ถ๊ฐ (add)
        user.followers.add(request.user)
    return redirect('accounts:detail', pk)
```

```python
 # detail.html ํ๋ก์ฐ ์ํ์ ๋ฐ๋ผ ๊ธ์ ๋ค๋ฅด๊ฒ ํ
 <p>
    ํ๋ก์ฐ :
    {{ user.followings.count }}
    || ํ๋ก์ :
    {{ user.followers.count }}</p>
  {% if request.user != user %}# ๋ก๊ทธ์ธ ํ ์ฌ์ฉ์๋ ๋ณธ์ธ์ ํ๋ก์ํ  ์ ์์
    <a href="{% url 'accounts:follow' user.pk %}">
      {% if request.user in user.followers.all %}
        ํ๋ก์ฐ ์ทจ์
      {% else %}
        ํ๋ก์ฐ
      {% endif %}
    </a>
  {% endif %}
```


