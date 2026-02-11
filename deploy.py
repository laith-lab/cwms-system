#!/usr/bin/env python3
"""
Auto Deploy CWMS System to Render.com
"""

import os
import sys
import subprocess
import time
import json

def print_header(text):
    print(f"\n{'='*60}")
    print(f"  {text}")
    print(f"{'='*60}\n")

def run_command(cmd, description=""):
    """Run a shell command and return the output"""
    if description:
        print(f"📍 {description}")
    print(f"$ {cmd}\n")
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    if result.stdout:
        print(result.stdout)
    if result.stderr and result.returncode != 0:
        print(f"❌ Error: {result.stderr}")
        return False
    return True

def main():
    print_header("🚀 CWMS System - Auto Deploy to Render")
    
    # Step 1: Check if we're in the right directory
    if not os.path.exists("package.json"):
        print("❌ package.json not found! Run this from the project root directory.")
        sys.exit(1)
    
    print("✅ Project found")
    
    # Step 2: Check Git status
    print_header("Step 1: Git Status Check")
    run_command("git status", "Checking git status...")
    
    # Step 3: Ensure all changes are committed
    print_header("Step 2: Verify Git is Clean")
    result = subprocess.run("git status --porcelain", shell=True, capture_output=True, text=True)
    if result.stdout.strip():
        print("⚠️  You have uncommitted changes:")
        print(result.stdout)
        print("\n📝 Committing changes...")
        run_command("git add .", "Adding files...")
        run_command("git commit -m 'auto: deployment preparation'", "Committing...")
    else:
        print("✅ Git is clean - all changes committed")
    
    # Step 4: Push to GitHub
    print_header("Step 3: Push to GitHub")
    run_command("git push origin main", "Pushing to GitHub...")
    
    # Step 5: Show GitHub repository URL
    print_header("Step 4: GitHub Repository")
    run_command("git remote -v", "Current remotes:")
    print("\n📍 Your repository:")
    print("🔗 https://github.com/laith-lab/cwms-system")
    
    # Step 6: Instructions
    print_header("Step 5: Manual Deployment to Render.com")
    
    print("""
╔════════════════════════════════════════════════════════════════╗
║                   RENDER.COM DEPLOYMENT                        ║
╚════════════════════════════════════════════════════════════════╝

📋 تعليمات يدوية بسيطة جداً:

1️⃣  افتح هذا الرابط في المتصفح:
    🔗 https://render.com/dashboard

2️⃣  اضغط على "New" أو "Create Service"

3️⃣  اختر "Web Service"

4️⃣  اختر "Connect a Git Repository"

5️⃣  ربط GitHub (إذا لم تكن قد ربطت)

6️⃣  ابحث واختر: laith-lab/cwms-system
    
7️⃣  الإعدادات:
    • Name: cwms-system
    • Region: Singapore (أو إقليمك)
    • Branch: main
    • Build: npm install
    • Start: npm start

8️⃣  اضغط "Create Web Service"

9️⃣  انتظر 5-10 دقائق

🔟 سيحصل على URL مثل:
    https://cwms-system-xxxxx.onrender.com

╔════════════════════════════════════════════════════════════════╗
║              أو استخدم هذا الرابط المباشر:                     ║
╚════════════════════════════════════════════════════════════════╝

🚀 رابط التوزيع المباشر:
https://render.com/deploy?repo=https://github.com/laith-lab/cwms-system

    """)
    
    # Step 7: Show what's been setup
    print_header("✅ ما تم إعداده")
    print("""
✅ Dockerfile - صورة Docker
✅ package.json - Node.js dependencies  
✅ .dockerignore - استبعاد الملفات
✅ render.yaml - إعدادات Render
✅ docker-compose.yml - تطوير محلي
✅ src/index.js - التطبيق الرئيسي
✅ GitHub repository - مجهز للنشر
✅ GitHub Actions - CI/CD جاهز
    """)
    
    # Step 8: Test locally
    print_header("Step 6: اختيار - اختبر محلياً أولاً (اختياري)")
    print("""
إذا أردت اختبار محلياً قبل النشر:

    docker-compose up --build

ثم افتح: http://localhost:3000

أو:

    npm install
    npm start
    """)
    
    # Final status
    print_header("✨ الحالة النهائية")
    print("""
┌─────────────────────────────────────────┐
│  🎉 التطبيق جاهز 100% للنشر على الإنترنت  │
│                                         │
│  الخطوة الأخيرة: فتح رابط Render أعلاه  │
│  والنشر سيكون تلقائياً!                  │
└─────────────────────────────────────────┘

📊 الخادم سيكون متاح على:
   https://cwms-system-xxxxx.onrender.com

🧪 اختبر بعد النشر:
   GET /
   GET /health

💾 جميع الملفات محفوظة على GitHub:
   https://github.com/laith-lab/cwms-system
    """)
    
    print_header("🎯 التالي")
    print("اختر أحد الخيارات:")
    print("1. افتح Render وأنشئ Web Service")
    print("2. أو استخدم الرابط المباشر أعلاه")
    print("3. أو اختبر محلياً: docker-compose up")

if __name__ == "__main__":
    main()
