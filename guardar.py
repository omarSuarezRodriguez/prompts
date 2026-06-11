import subprocess
import sys

# Si no proporciona mensaje, usa uno por defecto
if len(sys.argv) < 2:
    mensaje = "Actualización"
else:
    # Une todos los argumentos en un solo mensaje
    mensaje = " ".join(sys.argv[1:])

try:
    # git add .
    subprocess.run(["git", "add", "."], check=True)
    print("✓ git add . completado")
    
    # git commit -m "mensaje"
    subprocess.run(["git", "commit", "-m", mensaje], check=True)
    print(f"✓ git commit -m '{mensaje}' completado")
    
    # git push -u origin main
    subprocess.run(["git", "push", "-u", "origin", "main"], check=True)
    print("✓ git push -u origin main completado")
    
    print("\n✓ Todos los comandos se ejecutaron exitosamente")
except subprocess.CalledProcessError as e:
    print(f"Error al ejecutar comando git: {e}")
    sys.exit(1)
