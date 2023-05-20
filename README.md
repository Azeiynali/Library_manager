# Library manager
یک مدیر کتابخانه که به شما اجازه میدهد با استفاده از API کتاب ها را اضافه و حذف کنید، همچنین میتوانید لیستی از کتاب ها داشته باشید و همچنین با نام، اطلاعات آنها را بگیرید <br>
کتابخانه ها: Flask ----- Flask-SQLAlchemy

## Use
---
### URLs
/new --> ذخیره یک کتاب جدید، مقادیر موردنیاز:<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;name = (اجباری)نام کتاب
<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;wrr = (اجباری)نویسنده کتاب
<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;pass = (اجباری)رمز عبور
<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;sum = (اختیاری)خلاصه

/get --> گرفتن اطلاعات کتاب:
<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;name = نام کتاب- اجباری

/books --> تمام کتاب ها

/delet ---> حذف یک کتاب
<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;name = نام کتاب- اجباری
<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;pass = (اجباری)رمز عبور
