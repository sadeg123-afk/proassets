# -*- coding: utf-8 -*-
"""
ProAssets - تطبيق Flask الرئيسي
Global Digital Assets Marketplace
"""

from flask import Flask, render_template, request, jsonify, redirect, url_for, session
from functools import wraps
import os
from config import config

def create_app(config_name=None):
    """إنشاء تطبيق Flask"""
    
    if config_name is None:
        config_name = os.environ.get('FLASK_ENV', 'development')
    
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    
    # ===== التشغيل الأساسي =====
    @app.before_request
    def before_request():
        """تشغيل قبل كل طلب"""
        pass
    
    # ===== الصفحات العامة =====
    @app.route('/')
    def home():
        """الصفحة الرئيسية"""
        return render_template('home.html', title='ProAssets - Global Digital Assets')
    
    @app.route('/about')
    def about():
        """صفحة من نحن"""
        return render_template('about.html', title='About ProAssets')
    
    @app.route('/contact', methods=['GET', 'POST'])
    def contact():
        """صفحة التواصل"""
        if request.method == 'POST':
            # سنكمل هذا لاحقاً
            return jsonify({'status': 'success', 'message': 'Message received'})
        return render_template('contact.html', title='Contact Us')
    
    # ===== تسجيل الدخول والتسجيل =====
    @app.route('/register', methods=['GET', 'POST'])
    def register():
        """تسجيل حساب جديد"""
        if request.method == 'POST':
            # سنكمل هذا لاحقاً
            return jsonify({'status': 'success'})
        return render_template('register.html', title='Create Account')
    
    @app.route('/login', methods=['GET', 'POST'])
    def login():
        """تسجيل الدخول"""
        if request.method == 'POST':
            # سنكمل هذا لاحقاً
            return jsonify({'status': 'success'})
        return render_template('login.html', title='Login')
    
    @app.route('/logout')
    def logout():
        """تسجيل الخروج"""
        session.clear()
        return redirect(url_for('home'))
    
    # ===== المنتجات والتصفح =====
    @app.route('/products')
    def products():
        """قائمة المنتجات"""
        category = request.args.get('category')
        search = request.args.get('search')
        # سنكمل هذا لاحقاً
        return render_template('products.html', title='Browse Products')
    
    @app.route('/product/<slug>')
    def product_detail(slug):
        """صفحة المنتج الواحد"""
        # سنكمل هذا لاحقاً
        return render_template('product_detail.html', title='Product Details')
    
    # ===== سلة التسوق =====
    @app.route('/cart')
    def cart():
        """عرض سلة التسوق"""
        return render_template('cart.html', title='Shopping Cart')
    
    @app.route('/cart/add/<int:product_id>', methods=['POST'])
    def add_to_cart(product_id):
        """إضافة منتج للسلة"""
        return jsonify({'status': 'success'})
    
    # ===== لوحة التحكم - العميل =====
    @app.route('/dashboard')
    def customer_dashboard():
        """لوحة تحكم العميل"""
        if 'user_id' not in session:
            return redirect(url_for('login'))
        return render_template('customer/dashboard.html', title='My Dashboard')
    
    @app.route('/library')
    def my_library():
        """مكتبتي (المنتجات المشتراة)"""
        if 'user_id' not in session:
            return redirect(url_for('login'))
        return render_template('customer/library.html', title='My Library')
    
    # ===== لوحة التحكم - المنشئ =====
    @app.route('/creator/dashboard')
    def creator_dashboard():
        """لوحة تحكم المنشئ"""
        if 'user_id' not in session:
            return redirect(url_for('login'))
        return render_template('creator/dashboard.html', title='Creator Dashboard')
    
    @app.route('/creator/products')
    def creator_products():
        """منتجات المنشئ"""
        if 'user_id' not in session:
            return redirect(url_for('login'))
        return render_template('creator/products.html', title='My Products')
    
    @app.route('/creator/upload', methods=['GET', 'POST'])
    def creator_upload():
        """رفع منتج جديد"""
        if 'user_id' not in session:
            return redirect(url_for('login'))
        if request.method == 'POST':
            # سنكمل هذا لاحقاً
            return jsonify({'status': 'success'})
        return render_template('creator/upload.html', title='Upload Product')
    
    @app.route('/creator/earnings')
    def creator_earnings():
        """الأرباح والمحفظة"""
        if 'user_id' not in session:
            return redirect(url_for('login'))
        return render_template('creator/earnings.html', title='My Earnings')
    
    # ===== لوحة التحكم - الإدارة =====
    @app.route('/admin')
    def admin_dashboard():
        """لوحة تحكم الإدارة"""
        if 'user_id' not in session or session.get('role') != 'admin':
            return redirect(url_for('login'))
        return render_template('admin/dashboard.html', title='Admin Dashboard')
    
    @app.route('/admin/users')
    def admin_users():
        """إدارة المستخدمين"""
        if session.get('role') != 'admin':
            return redirect(url_for('home'))
        return render_template('admin/users.html', title='Manage Users')
    
    @app.route('/admin/products')
    def admin_products():
        """مراجعة المنتجات"""
        if session.get('role') != 'admin':
            return redirect(url_for('home'))
        return render_template('admin/products.html', title='Review Products')
    
    # ===== معالجة الأخطاء =====
    @app.errorhandler(404)
    def not_found(error):
        """صفحة غير موجودة"""
        return render_template('errors/404.html'), 404
    
    @app.errorhandler(500)
    def server_error(error):
        """خطأ في الخادم"""
        return render_template('errors/500.html'), 500
    
    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, host='0.0.0.0', port=5000)
