1. Clonar el Repositorio
Cada integrante debe clonar el repositorio en su máquina local para poder trabajar en el código. Esto se hace con el comando: git clone https://github.com/NobelikoCL/calculo-subsidiosence-TD.git

2. Configurar Git (solo la primera vez o cuando sea necesario)
Es importante configurar Git con tu nombre de usuario y correo electrónico, especialmente si es la primera vez que usas Git:

3. Crear una Nueva Rama para la Característica o Corrección
Antes de comenzar a trabajar en una nueva característica o corrección, es importante crear una nueva rama (branch) basada en la última versión de la rama principal (usualmente main o master). Esto mantiene el trabajo organizado y separado de las demás características en desarrollo:

4. git checkout -b nombre-de-tu-rama
5. Realizar Cambios y Comprometerlos (Commit)
Una vez que hayas completado tu tarea o hecho un progreso significativo, debes "comprometer" tus cambios. Esto se hace en dos pasos: primero, añade los archivos modificados al área de preparación (staging area) con:

git add .
Luego, realiza el compromiso con un mensaje descriptivo de los cambios:

git commit -m "Descripción de los cambios realizados"
6. Subir la Rama a GitHub
Después de comprometer tus cambios, sube la rama a GitHub con:

git push origin nombre-de-tu-rama
7. Crear un Pull Request (PR)
Ve al repositorio en GitHub y haz clic en "New pull request". Selecciona tu rama como "compare" y la rama principal (usualmente main o master) como "base". Llena la descripción del PR, explicando los cambios y cualquier otra información relevante.

8. Revisión de Código y Fusión (Merge)
Otros miembros del equipo revisan el código, pueden dejar comentarios o solicitar cambios. Una vez que el PR es aprobado, se puede fusionar con la rama principal.

9. Mantener Tu Rama Actualizada
Es importante mantener tu rama local actualizada con los últimos cambios de la rama principal, especialmente antes de empezar a trabajar en algo nuevo. Esto se puede hacer con:

git checkout main
git pull origin main
git checkout nombre-de-tu-rama
git merge main
Siguiendo estos pasos, tu equipo puede colaborar eficientemente en el desarrollo de la app web
