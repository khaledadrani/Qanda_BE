Param (
    [string]$arg
)

../env/Scripts/activate 


if ($arg -eq '') {
    python manage.py runserver
}
Elseif ($arg -eq 'waitress') {
    python server.py
}
Elseif ($arg -eq 'notebook') {
    #https://stackoverflow.com/questions/35483328/how-do-i-set-up-jupyter-ipython-notebook-for-django
    python manage.py shell_plus --notebook
}
Else {
    python manage.py shell
}
