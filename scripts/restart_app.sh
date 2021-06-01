# For SQLITE
touch db.sqlite3
rm db.sqlite3

rm -rf crypto/migrations
python manage.py makemigrations crypto
python manage.py migrate
./scripts/create_superuser.sh
python manage.py runserver
