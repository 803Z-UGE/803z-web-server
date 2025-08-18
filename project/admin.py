from datetime import datetime
from equipments.models import Reservation

def get_upcoming_reservations():
    upcoming_reservations = Reservation.objects.all()
    #.filter(start_date__gte=datetime.now()).order_by('start_date')

    table_data = {
        "headers": ["ID", "Start Date"],
        "rows": [
            [str(res.id), res.start_date.strftime("%Y-%m-%d %H:%M:%S")] for res in upcoming_reservations
        ]
    }

    return table_data

def dashboard_callback(request, context):
    upcoming_reservations = get_upcoming_reservations()

    context.update({
        "upcoming_reservations": upcoming_reservations,
    })

    return context

def environment_callback(request):
    """
    Callback has to return a list of two values represeting text value and the color
    type of the label displayed in top right corner.
    """
    return ["Development", "info"] # info, danger, warning, success