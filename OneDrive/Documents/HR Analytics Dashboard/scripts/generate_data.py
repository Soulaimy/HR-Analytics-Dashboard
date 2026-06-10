import pandas as pd
import random
from faker import Faker
from datetime import datetime, timedelta

fake = Faker("fr_FR")

# -------------------
# EMPLOYEES
# -------------------

departments = [
    "IT",
    "RH",
    "Finance",
    "Marketing",
    "Sales",
    "Operations"
]

positions = {
    "IT": ["Technicien Support", "Administrateur Système", "Data Analyst"],
    "RH": ["Chargé RH", "Responsable RH"],
    "Finance": ["Comptable", "Contrôleur de Gestion"],
    "Marketing": ["Chef de Projet", "Marketing Analyst"],
    "Sales": ["Commercial", "Account Manager"],
    "Operations": ["Coordinateur", "Manager Opérationnel"]
}

employees = []

for i in range(1, 501):

    dept = random.choice(departments)

    employees.append({
        "EmployeeID": i,
        "Nom": fake.name(),
        "Département": dept,
        "Poste": random.choice(positions[dept]),
        "Salaire": random.randint(28000, 70000),
        "DateEmbauche": fake.date_between(
            start_date="-8y",
            end_date="today"
        )
    })

employees_df = pd.DataFrame(employees)

# -------------------
# ATTENDANCE
# -------------------

attendance = []

start_date = datetime(2025, 1, 1)
end_date = datetime(2026, 12, 31)

current = start_date

while current <= end_date:

    for emp in employees_df["EmployeeID"]:

        status = random.choices(
            ["Présent", "Absent"],
            weights=[95, 5]
        )[0]

        attendance.append({
            "EmployeeID": emp,
            "Date": current.date(),
            "Status": status
        })

    current += timedelta(days=1)

attendance_df = pd.DataFrame(attendance)

# -------------------
# PERFORMANCE
# -------------------

performance = []

for emp in employees_df["EmployeeID"]:

    for year in [2025, 2026]:

        performance.append({
            "EmployeeID": emp,
            "Année": year,
            "Score": random.randint(60, 100)
        })

performance_df = pd.DataFrame(performance)

# -------------------
# PROMOTIONS
# -------------------

promotions = []

for emp in employees_df["EmployeeID"]:

    if random.random() < 0.20:

        promotions.append({
            "EmployeeID": emp,
            "DatePromotion": fake.date_between(
                start_date="-3y",
                end_date="today"
            )
        })

promotions_df = pd.DataFrame(promotions)

# -------------------
# EXPORT
# -------------------

employees_df.to_csv("../data/employees.csv", index=False)
attendance_df.to_csv("../data/attendance.csv", index=False)
performance_df.to_csv("../data/performance.csv", index=False)
promotions_df.to_csv("../data/promotions.csv", index=False)

print("Datasets générés avec succès.")