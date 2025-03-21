# funciones/funciones_backup.py
import shutil
import os
from datetime import datetime

def realizar_backup(db_name='corner_analysis.db', backup_dir='backups'):
    """
    Realiza una copia de seguridad de la base de datos.
    """
    try:
        if not os.path.exists(backup_dir):
            os.makedirs(backup_dir)
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_file = os.path.join(backup_dir, f"{db_name}_backup_{timestamp}.db")
        
        shutil.copy2(db_name, backup_file)
        print(f"Backup realizado correctamente en: {backup_file}")
        return backup_file
    except Exception as e:
        print(f"Error al realizar el backup: {e}")
        return None

def restaurar_backup(backup_file, db_name='corner_analysis.db'):
    """
    Restaura la base de datos desde un backup.
    """
    try:
        if not os.path.exists(backup_file):
            print(f"El archivo de backup {backup_file} no existe.")
            return False
        
        shutil.copy2(backup_file, db_name)
        print(f"Base de datos restaurada correctamente desde: {backup_file}")
        return True
    except Exception as e:
        print(f"Error al restaurar el backup: {e}")
        return False