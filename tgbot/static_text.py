start_help = 'Этот бот помогает вести учет совместных расходов.\n' \
    'Для начала создайте несколько категорий, чтобы в отчете видеть траты по ним.\n' \
    'После добавьте расход и выберите категорию.\n' \
    'Отчет по тратам будет формироваться в зависимости от того, кто сколько потратил.\n\n' \
    'Команды:\n' \
    '/cat название — создать категорию\n' \
    '/add сумма — добавить расход\n' \
    '/rep — вывести отчет'

category_created = '<b>{name}</b> создана. Теперь ее можно выбрать при расходе.'
category_not_created = 'Категория не создана. Добавьте после команды название категории'

expense_added = '<b>{amount}</b> — без категории. Выберите нужную категорию:'
no_expense_added = 'Расход не добавлен. В команде нет числа.'
expese_cat = '<b>{amount}</b> — <u>{cat}</u>'
