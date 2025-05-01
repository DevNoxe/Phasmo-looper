import ctypes
import time
import keyboard
import sys

# Configuración API Windows
user32 = ctypes.windll.user32

def move_click(x, y, delay=0.1):
    """Función mejorada para clicks confiables"""
    user32.SetCursorPos(x, y)
    time.sleep(0.05)
    user32.mouse_event(2, 0, 0, 0, 0)  # MOUSEEVENTF_LEFTDOWN
    time.sleep(delay)
    user32.mouse_event(4, 0, 0, 0, 0)  # MOUSEEVENTF_LEFTUP
    time.sleep(0.2)

def main_loop():
    print("Bot Phasmophobia iniciado (F8 para detener)")
    print("=== Secuencia ===")
    print("1. All Ready\n2. Continue (espera 15s)\n3. Skip\n4. Espera 1s\n5. Recompensa\n6. Next")

    # Estructura de acciones
    actions = [
        (583, 667, "All Ready"),
        (988, 665, "Continue", 18),  # Espera larga aquí
        (321, 694, "Skip"),
        (None, None, "Espera", 1),   # Espera 1s después de Skip
        (687, 536, "Recompensa"),
        (1047, 661, "Next")
    ]

    try:
        while not keyboard.is_pressed('f8'):
            for action in actions:
                if keyboard.is_pressed('f8'):
                    print("\nDeteniendo bot...")
                    return
                
                x, y, name = action[:3]
                
                if x is not None:  # Si no es una espera
                    print(f">> Acción: {name} ({x},{y})")
                    move_click(x, y)
                
                # Maneja tiempos de espera
                wait_time = action[3] if len(action) > 3 else 0.5
                if wait_time > 0:
                    print(f"Esperando {wait_time} segundos...")
                    end_time = time.time() + wait_time
                    while time.time() < end_time:
                        if keyboard.is_pressed('f8'):
                            print("\nDeteniendo bot...")
                            return
                        time.sleep(0.1)
    
    except KeyboardInterrupt:
        print("\nBot detenido manualmente")

if __name__ == "__main__":
    # Verificar admin
    try:
        if not ctypes.windll.shell32.IsUserAnAdmin():
            print("Advertencia: Ejecuta como administrador para mejor rendimiento")
            time.sleep(1)
    except:
        pass
    
    main_loop()
    print("Bot finalizado correctamente")