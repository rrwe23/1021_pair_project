## 🎉1021 pair Project

***

![녹화_2022_10_23_21_57_11_327](https://user-images.githubusercontent.com/70432152/197394187-350cae49-c3ea-4483-b4cc-8040f19b5396.gif)

## 📗 실습 내용

***

- `CRUD` 구현

- 이미지 다루기

- Django Auth 활용 회원 관리

- 회원가입 기능,로그인, 로그아웃, 리뷰작성, 삭제

## 😢회고 및 고찰

- 잘하는 분과의 실력차를 헌저히 느낄 수 있었던 프로젝트였다... Articles 부분의 모델과 작성글 생성, 수정, 삭제 등의 기본적인 기능들은 무리없이 구현할 수 있었으나 이번 주에 학습한 기능들은 거의 혼자서 구현이 불가능했다...😢

- 계획에 없던 검색기능을 추가했다. 두 분이서 머리를 맞대고 고민하시더니 뚝딱 완성되었다. 제목 뿐만 아니라 글제목으로도 검색 할 수 있게 기능을 구현하는 모습을 보고 감탄했다. 

- 허나 시간이 많이 소요되어 디자인적인 부분을 구현하지 못했고 구상했던 리뷰 홈페이지 모습에서 댓글 기능을 미처 생각하지 못해 댓글 기능이 미구현 상태이다. 

- 미구현 상태로 프로젝트가 끝난 것이 어쩌면 기회 일 수 도 있다고 생각한다. 이후 시간이 나면 그 동안  해보고 싶었던 bootstrap 복습을 해 볼 예정이다.

## ✔Like ,Following기능 추가

***

![녹화_2022_10_25_22_25_40_435](https://user-images.githubusercontent.com/70432152/197785953-488ec28e-09a9-49b8-aabd-85d394774397.gif)



수업 시간에 배운 내용을 바탕으로 게시글에 좋아요와 팔로우 기능을 추가했다.

`Like`

- 먼저 models에 기능을 추가해준다.

```python
# articles/models.py에 한 줄 추가


like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_reviews')
```

`make migrations`, `migrate` 이후

```python
# articles/urls.py


path('<int:pk>/like/', views.like, name='like'),
```

```python
# views.py
@login_required
def like(request, pk):
    article = Article.objects.get(pk=pk)
    # 만약에 로그인한 유저가 이 글을 좋아요를 눌렀다면,
    # if article.like_users.filter(id=request.user.id).exists():
    if request.user in article.like_users.all(): 
        # 좋아요 삭제하고
        article.like_users.remove(request.user)
    else:
        # 좋아요 추가하고 
        article.like_users.add(request.user)
    # 상세 페이지로 redirect
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

- css 편집을 위해 링크 추가

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

- account 앱에서 작업해준다.

- model.py 에 추가 후 마이그레이션

```python
#accounts/models.py
class User(AbstractUser):

    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')


    @property
    def full_name(self):
        return f'{self.last_name}{self.first_name}'
```

- 경로 추가

```python
# urls.py

path('<int:pk>/follow/', views.follow, name='follow'),
```

- 함수 추가

```python
# views.py

def follow(request,pk):

    return redirect('accouontsd:detail',pk)
```

- detail 에 팔로우 버튼 추가

```python
# 팔로잉 숫자와 팔로워 숫자 표기
<p>{{ user.followings.count }}||{{ user.followers.count }}</p>
  <a href="{% url 'accounts:follow' user.pk %}">팔로우</a>
```

- 함수를 구현하자면

```python
@login_required
def follow(request, pk):
    # 프로필에 해당하는 유저를 로그인한 유저가!
    user = get_user_model().objects.get(pk=pk)
    if request.user == user:
        messages.warning(request, '스스로 팔로우 할 수 없습니다.')
        return redirect('accounts:detail', pk)
    if request.user in user.followers.all():
    # (이미) 팔로우 상태이면, '팔로우 취소'버튼을 누르면 삭제 (remove)
        user.followers.remove(request.user)
    else:
    # 팔로우 상태가 아니면, '팔로우'를 누르면 추가 (add)
        user.followers.add(request.user)
    return redirect('accounts:detail', pk)
```

```python
 # detail.html 팔로우 상태에 따라 글을 다르게 표
 <p>
    팔로우 :
    {{ user.followings.count }}
    || 팔로워 :
    {{ user.followers.count }}</p>
  {% if request.user != user %}# 로그인 한 사용자는 본인을 팔로워할 수 없음
    <a href="{% url 'accounts:follow' user.pk %}">
      {% if request.user in user.followers.all %}
        팔로우 취소
      {% else %}
        팔로우
      {% endif %}
    </a>
  {% endif %}
```


