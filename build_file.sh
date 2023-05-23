echo "Build Start"

python -m pip install -r requirment.txt
python manage.py collectstatic --noinput --clear

echo "BUILD END"