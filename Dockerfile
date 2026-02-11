# استخدم صورة Node.js رسمية
FROM node:18-alpine

# تعيين مجلد العمل
WORKDIR /app

# نسخ package.json و package-lock.json
COPY package*.json ./

# تثبيت المتعلقات
RUN npm install --omit=dev

# نسخ باقي الكود
COPY . .

# تعريض المنفذ (تعديل حسب احتياجاتك)
EXPOSE 3000

# أمر البدء
CMD ["npm", "start"]
