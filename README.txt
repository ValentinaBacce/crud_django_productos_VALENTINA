CRUD Django – Gestión de Productos  
Autora: Valentina Baccellieri  

Proyecto desarrollado como parte de la Sumativa 2 de Programación V, implementando un CRUD monolítico con Django.  
El sistema permite gestionar productos mediante una interfaz web (HTML + Bootstrap 5) y una API mínima para pruebas en Postman

---

Instalación y ejecución del proyecto  
Requisitos:
- Python 3.10 o superior  
- Django 4.x  
- Git instalado  

Pasos: 
```bash
git clone https://github.com/ValentinaBacce/crud_django_productos_VALENTINA.git
cd crud_django_productos_VALENTINA
python -m venv venv
venv\Scripts\activate   # (Windows)
pip install django
python manage.py migrate
python manage.py runserver

Acceso al panel administrativo:

URL → http://127.0.0.1:8000/admin/

Usuario → admin

Contraseña → valen1234

Descripción del sistema

El sistema implementa las operaciones CRUD completas:

Create: crear productos mediante formulario.

Read: listar y detallar cada producto.

Update: editar registros existentes.

Delete: eliminar productos con confirmación.

Las vistas usan CBVs (Class Based Views) y las plantillas HTML están en templates/productos/:
producto_list.html, producto_detail.html, producto_form.html, producto_confirm_delete.html.

El diseño se realizó con Bootstrap 5, empleando tarjetas (cards), botones estilizados y disposición responsive.

El postman se probo y funciona tanto la modalidad Get como el Post.