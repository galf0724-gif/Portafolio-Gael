# Portafolio – Gael

Sitio de portafolio técnico para **Gael** (Python/Django, HTML/CSS/JS, Git/GitHub, SQL).  
El sitio se publica con **GitHub Pages** desde la carpeta `docs/`.

## Cómo publicar en GitHub Pages
1. Crea un repositorio público en tu cuenta llamado **portafolio-gael**.
2. Sube el contenido de este directorio.
3. Ve a **Settings → Pages** y selecciona:
   - *Build and deployment*: **Deploy from a branch**
   - *Branch*: `main`  |  *Folder*: `/docs`
4. Abre la URL: `https://<USUARIO_GITHUB>.github.io/portafolio-gael/` (reemplaza `<USUARIO_GITHUB>`).

> Alternativa: usa **GitHub Actions** (ya incluimos `.github/workflows/pages.yml`). Si eliges *Source: GitHub Actions*, se publicará automáticamente desde `docs/`.

## Estructura
```
portafolio-gael/
 ├─ docs/
 │   ├─ index.md
 │   ├─ proyecto-x.md
 │   ├─ img/
 │   └─ demo/
 ├─ snippets/
 │   ├─ auth_view.py
 │   └─ query_optimization.sql
 ├─ .github/workflows/pages.yml
 ├─ README.md
 └─ LICENSE
```

## Aviso
Este repositorio **no** contiene código propietario. Los fragmentos son ejemplos mínimos y seguros.
El código real del proyecto privado puede mostrarse **solo bajo solicitud** mediante acceso temporal a un repo privado.
