import numpy as np

def normalized_array(data):
    """
    change for checking
    מנרמלת מערך נתונים לטווח של [0, 1] לפי שיטת Min-Max Scaling.
    
    הנוסחה לביצוע:
    x_norm = (x - min) / (max - min)
    
    פרמטרים:
    data (list or np.array): מערך של מספרים.
    
    מחזירה:
    np.array: מערך מנורמל. אם כל הערכים במערך זהים, יש להחזיר מערך של אפסים.
    """
    # המרת הקלט ל-numpy array לצורך חישובים וקטוריים
    data = np.array(data)
    
    # --- כיתבו את הקוד שלכם כאן ---
    pass
    # חשוב לזכור להחליף את pass ב- return

if __name__ == "__main__":
    # כאן הסטודנטים יכולים להריץ בדיקה עצמית מהירה
    test_data = [10, 20, 30, 40, 50]
    print(f"Original: {test_data}")
    print(f"Normalized: {normalized_array(test_data)}")
