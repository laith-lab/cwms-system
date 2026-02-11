# CWMS System - Centralized Warehouse Management System

![Build Status](https://img.shields.io/badge/build-passing-brightgreen)
![Version](https://img.shields.io/badge/version-1.0.0-blue)
![License](https://img.shields.io/badge/license-MIT-green)

نظام إدارة مركز توزيع مركزي متكامل يوفر حلولاً شاملة لإدارة المستودعات والمخزون والشحنات.

## المميزات

- 🚀 API RESTful حديثة
- 🐳 دعم Docker للنشر السهل
- 📦 إدارة المخزون الذكية
- 📊 تقارير وإحصائيات متقدمة
- 🔒 نظام أمان قوي
- 🌍 دعم العمليات متعددة اللغات

## المتطلبات

- Node.js >= 18.0.0
- npm أو yarn
- Docker & Docker Compose (اختياري)

## التثبيت السريع

### محلياً (بدون Docker)

```bash
# استنساخ المستودع
git clone https://github.com/laith-lab/cwms-system.git
cd cwms-system

# تثبيت المتعلقات
npm install

# نسخ متغيرات البيئة
cp .env.example .env

# تشغيل التطبيق
npm start

# تشغيل في وضع التطوير (مع nodemon)
npm run dev
```

التطبيق سيعمل على `http://localhost:3000`

### مع Docker

```bash
# بناء وتشغيل الحاوية
docker-compose up --build

# أو استخدام docker مباشرة
docker build -t cwms-system:latest .
docker run -p 3000:3000 cwms-system:latest
```

## الاختبار

```bash
# تشغيل الاختبارات
npm test

# فحص الكود
npm run lint
```

## النشر على Docker Hub

تم تكوين GitHub Actions لبناء ودفع صورة Docker تلقائياً عند كل push إلى main.

**خطوات إضافية:**

1. أضف secrets إلى GitHub Repository:
   - `DOCKER_HUB_USERNAME`: اسم المستخدم على Docker Hub
   - `DOCKER_HUB_TOKEN`: رمز الوصول على Docker Hub

2. عند كل push على `main`، سيتم:
   - بناء صورة Docker
   - دفعها إلى Docker Hub
   - وسمها بـ `latest` و رقم commit

### سحب الصورة من Docker Hub

```bash
docker pull YOUR_DOCKER_HUB_USERNAME/cwms-system:latest
docker run -p 3000:3000 YOUR_DOCKER_HUB_USERNAME/cwms-system:latest
```

## API Endpoints

### Health Check
```
GET /health
```

### Status
```
GET /
```

## المساهمة

نرحب بكل المساهمات! يرجى:

1. عمل fork للمستودع
2. إنشاء فرع للميزة الجديدة (`git checkout -b feature/amazing-feature`)
3. الالتزام بالتغييرات (`git commit -m 'Add some amazing feature'`)
4. الدفع إلى الفرع (`git push origin feature/amazing-feature`)
5. فتح Pull Request

## الترخيص

هذا المشروع مرخص تحت رخصة MIT - انظر ملف [LICENSE](LICENSE) للتفاصيل.

## التواصل

- **الإيميل**: contact@laithlab.com
- **GitHub**: [@laith-lab](https://github.com/laith-lab)

---

**آخر تحديث**: 2026-02-11