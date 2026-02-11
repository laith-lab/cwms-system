# نشر سريع على Render.com

## الطريقة الأولى: النشر المباشر (الأسهل)

1. اذهب إلى: https://render.com
2. اضغط **New** → **Web Service**
3. اختر **Deploy from Git Repository**
4. ربط حسابك على GitHub واختر `cwms-system`
5. اضغط **Create Web Service**
6. انتظر 5-10 دقائق للنشر
7. ستحصل على URL مثل: `https://cwms-system-xxxx.onrender.com`

## الطريقة الثانية: استخدام Railway.app

1. اذهب إلى: https://railway.app
2. اضغط **Start New Project**
3. اختر **Deploy from GitHub**
4. اختر المستودع `cwms-system`
5. Railway سيكتشف Dockerfile تلقائياً
6. اضغط **Deploy**
7. ستحصل على URL عام

## الطريقة الثالثة: استخدام Heroku (مجاني - Eco Dyno)

```bash
# تثبيت Heroku CLI
# ثم:
heroku login
heroku create cwms-system
git push heroku main
```

## اختبار التطبيق بعد النشر

بعد النشر، ستحصل على URL يشبه:
```
https://cwms-system-xxxx.onrender.com/
```

اختبر هذه الروابط:
```
GET https://cwms-system-xxxx.onrender.com/
GET https://cwms-system-xxxx.onrender.com/health
```
