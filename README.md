# 👨‍💻 Pair project(Signup-Login)
> 일시 : 2022-10-15
> 
> 목표 : git branch를 활용해 3명이서 회원가입, 로그인 페이지 구현
> 
> 인원 : 유순일, 김현중, 신윤식

## 🎯Objective
#### 1. 회원가입 기능 구현
![image](https://user-images.githubusercontent.com/97111793/195989549-deb3fb79-d393-426b-891e-eb24c0b94a90.png)
- Django의 내장폼인 UserCreationForm을 사용하여 회원가입 기능 구현
- `forms.py` 코드
```python
class CustomUserCreationForm(UserCreationForm):
  
  class Meta:
    model = get_user_model()
    fields = ('username', 'password1', 'password2', )
```
<br>

#### 2. 로그인 기능 구현
![image](https://user-images.githubusercontent.com/97111793/195989591-5b530855-3bc8-4db3-8d5f-f550b7291599.png)
![image](https://user-images.githubusercontent.com/97111793/195989641-d7395839-64f8-4e56-8add-71f9cbab8537.png)
- Django의 내장모듈인 authenticate를 사용하여 login 기능 구현
- `views.py` 코드
```python
def login(request):
  if request.method == 'POST':
    form = AuthenticationForm(request, data=request.POST)
    if form.is_valid():
      auth_login(request, form.get_user())
      return redirect(request.GET.get('next') or 'accounts:index')
  else:
    form = AuthenticationForm()
  context = {
    'form' : form,
  }
  return render(request, 'accounts/login.html', context)
```
## 📝Review
- 전직장에서의 협업이란 `문서를 작성하고 이메일로 주고받는 것`이었다. 하지만 개발자 세상에서의 협업은 `git branch`라는 것을 사용하는 것이었다. **main(master)라는 큰 줄기를 기준으로 branch라는 곁가지를 생성**하고, 작업물을 main(mater)에 병합한다는 기능은 하면 할수록, 효율적인 협업툴이라고 느껴졌다. 개발자로 하루 빨리 취업하여 현업에서 `git branch`를 사용하였으면 좋겠다.