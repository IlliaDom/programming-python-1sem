class Expense:
    def __init__(self, date: str, category: str, amount: float):
        self.date = date
        self.category = category
        self.amount = amount

    def monthly_cost(self) -> float:
        """Проста разова/щомісячна витрата - сума як є."""
        return self.amount

    def describe(self) -> str:
        return (
            f"{self.date} {self.category}: {self.amount:.2f} UAH "
            f"-> {self.monthly_cost():.2f} UAH/міс ({type(self).__name__})"
        )


class RecurringExpense(Expense):
    """Регулярна витрата, що повторюється кілька разів на місяць."""

    def __init__(self, date: str, category: str, amount: float, times_per_month: int):
        super().__init__(date, category, amount)
        self.times_per_month = times_per_month

    def monthly_cost(self) -> float:
        return self.amount * self.times_per_month


class SharedExpense(Expense):
    """Спільна витрата, що ділиться між кількома людьми."""

    def __init__(self, date: str, category: str, amount: float, people: int):
        super().__init__(date, category, amount)
        self.people = people

    def monthly_cost(self) -> float:
        return self.amount / self.people
