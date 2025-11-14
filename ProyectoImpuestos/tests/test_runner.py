import os, subprocess, sys

# Rutas base del proyecto y carpetas de pruebas
THIS_FILE   = os.path.abspath(__file__)
TESTS_DIR   = os.path.dirname(THIS_FILE)
ROOT_DIR    = os.path.abspath(os.path.join(TESTS_DIR, ".."))
VALID_DIR   = os.path.join(TESTS_DIR, "valid")
INVALID_DIR = os.path.join(TESTS_DIR, "invalid")
MAIN_PY     = os.path.join(ROOT_DIR, "main.py")

# 1) Asegurar carpetas (no borra nada si ya existen)
os.makedirs(VALID_DIR, exist_ok=True)
os.makedirs(INVALID_DIR, exist_ok=True)

def debug_ls(path: str):
    """
    Imprime el listado real de una carpeta para depuración.
    Útil para confirmar que el runner "ve" los archivos .txt de pruebas.
    """
    try:
        items = sorted(os.listdir(path))
        print(f"[DEBUG] ls {path} -> {items}")
    except Exception as e:
        print(f"[DEBUG] No se pudo listar {path}: {e}")

def run_folder(folder_abs_path: str, label: str) -> tuple[int, int]:
    """
    Ejecuta todas las pruebas .txt dentro de una carpeta dada.
    Llama a main.py con cada archivo y cuenta OK/FAIL según el returncode.
    :return: (ok, fail)
    """
    if not os.path.isdir(folder_abs_path):
        print(f"❌ No existe la carpeta {label}: {folder_abs_path}")
        return (0, 0)

    # Solo archivos .txt ordenados por nombre (para resultados reproducibles)
    files = sorted(f for f in os.listdir(folder_abs_path) if f.endswith(".txt"))
    if not files:
        print(f"⚠️  No hay .txt en {folder_abs_path}")
        return (0, 0)

    print(f"\n== Ejecutando pruebas ({label}) en {folder_abs_path} ==")
    ok, fail = 0, 0
    for name in files:
        print(f"\n--- {name} ---")
        file_path = os.path.join(folder_abs_path, name)

        # Ejecuta main.py con el archivo de prueba; captura el código de salida
        result = subprocess.run(["python", MAIN_PY, file_path], cwd=ROOT_DIR)

        # Convención: 0 = éxito (válido), !=0 = fallo (inválido o error)
        if result.returncode == 0:
            ok += 1
        else:
            fail += 1
    return (ok, fail)

if __name__ == "__main__":
    # Información de depuración: rutas que usará el runner
    print("[DEBUG] ROOT_DIR   :", ROOT_DIR)
    print("[DEBUG] TESTS_DIR  :", TESTS_DIR)
    print("[DEBUG] VALID_DIR  :", VALID_DIR)
    print("[DEBUG] INVALID_DIR:", INVALID_DIR)
    print("[DEBUG] MAIN_PY    :", MAIN_PY)

    # Listado real para verificar que el runner "ve" tus archivos
    debug_ls(TESTS_DIR)
    debug_ls(VALID_DIR)
    debug_ls(INVALID_DIR)

    # Ejecutar carpetas de pruebas: valid e invalid
    ok_v, fail_v = run_folder(VALID_DIR, "valid")
    ok_i, fail_i = run_folder(INVALID_DIR, "invalid")

    # Resumen final
    total_ok   = ok_v + ok_i
    total_fail = fail_v + fail_i
    total_run  = total_ok + total_fail

    print("\n==== RESUMEN ====")
    print(f"Valid   -> OK: {ok_v} | FAIL: {fail_v}")
    print(f"Invalid -> OK: {ok_i} | FAIL: {fail_i}")
    print(f"Total   -> OK: {total_ok} | FAIL: {total_fail} | RUN: {total_run}")

    # Salida 0 si todo ok, 1 si hubo fallos (útil para CI/automatización)
    sys.exit(0 if total_fail == 0 else 1)
