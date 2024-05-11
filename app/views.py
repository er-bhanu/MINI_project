from django.shortcuts import render
from . models import *
from datetime import datetime, timedelta
        # Get the current date
today = datetime.now()
# Calculate the date of Monday and Friday of the current week
monday = today - timedelta(days=today.weekday())
friday = monday + timedelta(days=4)
# Get the current year
current_year = today.year
# Format the dates
monday_formatted = monday.strftime('%Y-%m-%d')
friday_formatted = friday.strftime('%Y-%m-%d')


def index(request):
    # Fetch distinct programmes, semesters, and years of study from TimeTableMain model
    programmes = TimeTableMain.objects.values_list('Programme', flat=True).distinct()
    semesters = TimeTableMain.objects.values_list('Semister', flat=True).distinct()
    years_of_study = TimeTableMain.objects.values_list('YearOfStudy', flat=True).distinct()

    # Fetch selected Programme and its Department when a POST request is made
    if request.method == 'POST':
        programme = request.POST.get('programme')
        semester = request.POST.get('semester')
        year_of_study = request.POST.get('year_of_study')

        # Fetch the selected Programme and its Department from TimeTableMain model
        timetable_main_entry = TimeTableMain.objects.filter(Programme=programme).first()
        if timetable_main_entry:
            selected_programme = timetable_main_entry.Programme
            department = timetable_main_entry.Department
        else:
            selected_programme = None
            department = None

        # Fetch timetable entries for the selected programme, semester, and year of study
        timetable_entries = TimeTable.objects.filter(Programme__Programme=programme,
                                                     Programme__Semister=semester,
                                                     Programme__YearOfStudy=year_of_study)

        # Extract unique days from the fetched timetable entries
        days = set(entry.Day for entry in timetable_entries)

        timetable_data = {day: [] for day in days}

        for entry in timetable_entries:
            timetable_data[entry.Day].append(entry)


        # Initial rendering of the page without POST data
       

        context = {
            'programmes': programmes,
            'semesters': semesters,
            'years_of_study': years_of_study,
            'timetable_data': timetable_data,
            'selected_programme': selected_programme,
            'department': department,
            'monday': monday_formatted,
            'friday': friday_formatted,
            'current_year': current_year,
        }
        return render(request, 'pages/index.html', context)

   
    context = {
        'programmes': programmes,
        'semesters': semesters,
        'years_of_study': years_of_study,
        'selected_programme': None,
        'department': None,
        'monday': monday_formatted,
        'friday': friday_formatted,
        'current_year': current_year,
    }

    return render(request, 'pages/index.html', context)
     

    
def support(request):
    return render(request, 'pages/support.html')