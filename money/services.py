from django.db.models import Sum


def get_report_chat(chat):
    """
    Структура ответа:
    {
        'total': 0,
        'categories': [
            {'name': '', 'total': 0},
        ],
        'no_cat_total': 0,
        'members': [
            {'username': '', 'total': 0, 'debt': 0}
        ]
    }
    """
    data = dict()
    members_count = chat.members.count()
    data['total'] = chat.expenses.aggregate(Sum('amount')).get('amount__sum', 0)

    data['categories'] = list()
    for cat in chat.categories.all():
        total = cat.expenses.aggregate(Sum('amount')).get('amount__sum', 0)
        data['categories'].append({
            'name': cat.name,
            'total': total if total else 0
        })
    data['no_cat_total'] = chat.expenses.filter(category=None).aggregate(Sum('amount')).get('amount__sum', 0)

    data['members'] = list()
    for u in chat.members.all():
        total = chat.expenses.filter(user=u).aggregate(Sum('amount')).get('amount__sum', 0)
        debt = data['total'] / members_count - total
        data['members'].append({
            'username': u.username,
            'total': total,
            'debt': round(debt)
        })
    return data
