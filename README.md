# STARWARS API

## Instalar y ejecutar la aplicación:

**1 - Instalar librerías:**
```
pip install -r requirements.txt
```

**2 - Ejecutar el servidor**
```
python manage.py runserver
```


## Probar los endpoints:

**1 - Swagger:**
```
http://localhost:8000
```

**2 - Obtener info del personaje:**
```
GET http://localhost:8000/api/character/1
```

**3 - Agregar puntuación a un personaje:**
```
POST http://localhost:8000/api/character/1/rating

Body (rating-puntuación):

{
    "rating": 2
}
```


## Ejecutar tests (test api, services y models)
```
python manage.py test
```


## Cógigo estándar (PEP8)
```
pycodestyle . --exclude=migration,settings.py,local_settings.py
```
