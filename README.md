# ๐จโ๐ป Pair project(Signup-Login)
> ์ผ์ : 2022-10-15
> 
> ๋ชฉํ : git branch๋ฅผ ํ์ฉํด 3๋ช์ด์ ํ์๊ฐ์, ๋ก๊ทธ์ธ ํ์ด์ง ๊ตฌํ
> 
> ์ธ์ : ์ ์์ผ, ๊นํ์ค, ์ ์ค์

## ๐ฏObjective
#### 1. ํ์๊ฐ์ ๊ธฐ๋ฅ ๊ตฌํ
![image](https://user-images.githubusercontent.com/97111793/195989549-deb3fb79-d393-426b-891e-eb24c0b94a90.png)
- Django์ ๋ด์ฅํผ์ธ UserCreationForm์ ์ฌ์ฉํ์ฌ ํ์๊ฐ์ ๊ธฐ๋ฅ ๊ตฌํ
- `forms.py` ์ฝ๋
```python
class CustomUserCreationForm(UserCreationForm):
  
  class Meta:
    model = get_user_model()
    fields = ('username', 'password1', 'password2', )
```
<br>

#### 2. ๋ก๊ทธ์ธ ๊ธฐ๋ฅ ๊ตฌํ
![image](https://user-images.githubusercontent.com/97111793/195989591-5b530855-3bc8-4db3-8d5f-f550b7291599.png)
![image](https://user-images.githubusercontent.com/97111793/195989641-d7395839-64f8-4e56-8add-71f9cbab8537.png)
- Django์ ๋ด์ฅ๋ชจ๋์ธ authenticate๋ฅผ ์ฌ์ฉํ์ฌ login ๊ธฐ๋ฅ ๊ตฌํ
- `views.py` ์ฝ๋
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

<hr>

## ๐Review
- ์ ์ง์ฅ์์์ ํ์์ด๋ `๋ฌธ์๋ฅผ ์์ฑํ๊ณ  ์ด๋ฉ์ผ๋ก ์ฃผ๊ณ ๋ฐ๋ ๊ฒ`์ด์๋ค. ํ์ง๋ง ๊ฐ๋ฐ์ ์ธ์์์์ ํ์์ `git branch`๋ผ๋ ๊ฒ์ ์ฌ์ฉํ๋ ๊ฒ์ด์๋ค. **main(master)๋ผ๋ ํฐ ์ค๊ธฐ๋ฅผ ๊ธฐ์ค์ผ๋ก branch๋ผ๋ ๊ณ๊ฐ์ง๋ฅผ ์์ฑ**ํ๊ณ , ์์๋ฌผ์ main(mater)์ ๋ณํฉํ๋ค๋ ๊ธฐ๋ฅ์ ํ๋ฉด ํ ์๋ก, ํจ์จ์ ์ธ ํ์ํด์ด๋ผ๊ณ  ๋๊ปด์ก๋ค. ๊ฐ๋ฐ์๋ก ํ๋ฃจ ๋นจ๋ฆฌ ์ทจ์ํ์ฌ ํ์์์ `git branch`๋ฅผ ์ฌ์ฉํ์์ผ๋ฉด ์ข๊ฒ ๋ค.