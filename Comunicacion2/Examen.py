import pikepdf
from itertools import product

# --- CONFIGURACIÓN ---
# Pon aquí el nombre exacto de TU archivo (incluyendo .pdf)
nombre_archivo = "EXAMEN_24_224211952.pdf" 

patrones = ["80211", "8023", "80215", "80216"]
hex_chars = "0123456789ABCDEF"

def crackear():
    print(f"Buscando contraseña para {nombre_archivo}...")
    
    for p in patrones:
        faltantes = 7 - len(p)
        print(f"Probando variaciones del estándar IEEE {p}...")
        
        # Generamos todas las combinaciones de los caracteres que faltan
        for combo in product(hex_chars, repeat=faltantes):
            extra = "".join(combo)
            
            # Probamos 3 posiciones comunes: al final, al inicio y "rodeando"
            # Ejemplo con 80211: 80211XX, XX80211, X80211X
            intentos = [
                p + extra,           # Al final
                extra + p,           # Al inicio
            ]
            
            # Si faltan 2 caracteres (como en 80211), probamos uno a cada lado
            if faltantes == 2:
                intentos.append(extra[0] + p + extra[1])

            for password in intentos:
                try:
                    # Intentamos abrir el PDF con la contraseña
                    with pikepdf.open(nombre_archivo, password=password):
                        print("-" * 30)
                        print(f"¡LOGRADO! Contraseña: {password}")
                        print("-" * 30)
                        return
                except pikepdf.PasswordError:
                    continue
                except FileNotFoundError:
                    print(f"Error: No encontré el archivo '{nombre_archivo}' en esta carpeta.")
                    return

    print("No se encontró la contraseña. Revisa si el patrón es distinto.")

if __name__ == "__main__":
    crackear()